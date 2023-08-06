from __future__ import annotations

import decimal
from typing import Union

import yaml

import zinc.openapi_schema_pydantic as opi
from zinc.api import codegen_api


def load_spec(path: str) -> opi.Components:
    with open(path, "r") as f:
        load = yaml.full_load(f)
        return opi.Components(**load["components"])


def to_class_specs(components: dict[str, opi.Components]) -> list[codegen_api.ClassSpec]:
    specs: list[codegen_api.ClassSpec] = []
    for path, component in components.items():
        if component.schemas:
            local_components = {"": component, **components}
            for name, schema in component.schemas.items():
                specs.append(
                    to_class_spec(
                        codegen_api.ObjectTypeName(name),
                        schema,
                        local_components,
                    )
                )
    return specs


def to_class_spec(
    name: codegen_api.ObjectTypeName, schema: opi.Schema, components: dict[str, opi.Components]
) -> codegen_api.ClassSpec:
    required_fields = schema.required if schema.required is not None else []
    if schema.allOf is not None:
        fields = {}
        for inner_schemaish in schema.allOf:
            inner_schema = resolve_schema(inner_schemaish, components)
            inner_required_fields = required_fields + (
                inner_schema.required if inner_schema.required is not None else []
            )
            properties = inner_schema.properties if inner_schema.properties is not None else {}
            fields.update(
                {
                    key: to_field_spec(value, required=key in inner_required_fields)
                    for key, value in properties.items()
                }
            )
        return codegen_api.ObjectSpec(name=name, fields=fields)

    if schema.oneOf is not None:
        if schema.discriminator is None:
            raise Exception("Invalid oneOf definition. Expecting 'discriminator' to exist")
        union = {}
        discriminator_field = schema.discriminator.propertyName
        for inner_schemaish in schema.oneOf:
            field = resolve_field(inner_schemaish, discriminator_field, components)
            if field is None or field.enum is None or len(field.enum) != 1:
                raise Exception(f"Union variant {inner_schemaish} is missing valid discriminator")
            union[field.enum[0]] = to_object_name(inner_schemaish)

        return codegen_api.UnionSpec(
            name=name,
            discriminator_field=discriminator_field,
            union=union,
        )

    if schema.type is not None:
        if schema.type == "object" and schema.additionalProperties is None:
            properties = schema.properties if schema.properties is not None else {}
            return codegen_api.ObjectSpec(
                name=name,
                fields={
                    key: to_field_spec(value, required=key in required_fields)
                    for key, value in properties.items()
                },
                description=schema.description,
            )
        elif schema.type == "string" and schema.enum is not None:
            return codegen_api.EnumSpec(
                name=name,
                values=schema.enum,
                description=schema.description,
            )
        else:
            return codegen_api.AliasSpec(
                name=name,
                field=to_field_spec(schema, required=True),
                description=schema.description,
            )

    raise Exception(f"Encountered unexpected schema. type: {schema.type}")


def to_field_spec(
    property: Union[opi.Reference, opi.Schema], required: bool
) -> codegen_api.FieldSpec:
    if isinstance(property, opi.Reference):
        return codegen_api.ObjectFieldSpec(
            object_type=to_object_name(property),
            required=required,
            description=property.description,
        )
    if property.type == "string":
        if property.enum:
            if len(property.enum) != 1:
                raise Exception(
                    "Unexpected definition. Inline enum fields can only have a single value"
                )
            return codegen_api.StringLiteralFieldSpec(
                value=property.enum[0],
                required=required,
                description=property.description,
            )
        if property.schema_format == "date":
            return codegen_api.DateFieldSpec(required=required, description=property.description)
        elif property.schema_format == "datetime":
            return codegen_api.DatetimeFieldSpec(
                required=required, description=property.description
            )
        elif property.schema_format == "uuid":
            return codegen_api.UUIDFieldSpec(required=required, description=property.description)
        return codegen_api.StringFieldSpec(
            required=required,
            description=property.description,
        )
    elif property.type == "array":
        if property.items is None:
            raise Exception("Invalid array definition. Expecting 'items' to exist")

        return codegen_api.ListFieldSpec(
            element_type=to_field_spec(property.items, True),
            min_count=property.minItems,
            max_count=property.maxItems,
            allow_single_value_as_array=property.allow_single_value_as_array,
            required=True,
            description=property.description,
        )
    elif property.type == "number" or property.type == "integer":
        minimum: float | None = None
        exclusive_min = False
        if property.minimum is not None:
            minimum = property.minimum
        if property.exclusiveMinimum is not None:
            minimum = property.minimum
            exclusive_min = True

        maximum: float | None = None
        exclusive_max = False
        if property.maximum is not None:
            maximum = property.maximum
        if property.exclusiveMaximum is not None:
            maximum = property.maximum
            exclusive_max = True

        if property.type == "number":
            if (
                property.schema_format == "float"
                or property.schema_format == "double"
                or property.schema_format is None
            ):
                return codegen_api.NumberFieldSpec(
                    minimum=decimal.Decimal(minimum) if minimum is not None else minimum,
                    exclusive_min=exclusive_min,
                    maximum=decimal.Decimal(maximum) if maximum is not None else maximum,
                    exclusive_max=exclusive_max,
                    required=required,
                    description=property.description,
                )
            else:
                raise Exception(
                    f"Property with type number has invalid format='{property.schema_format}'"
                    " (valid formats are 'float', 'double' and absent)"
                )
        elif property.type == "integer":
            if property.schema_format == "int32" or property.schema_format is None:
                return codegen_api.IntFieldSpec(
                    minimum=int(minimum) if minimum is not None else minimum,
                    exclusive_min=exclusive_min,
                    maximum=int(maximum) if maximum is not None else maximum,
                    exclusive_max=exclusive_max,
                    allow_number=property.allow_number_as_int,
                    required=required,
                    description=property.description,
                )
            else:
                raise Exception(
                    f"Property with type integer has invalid format='{property.schema_format}'"
                    " (valid formats are 'int32' and absent)"
                )
    elif property.type == "boolean":
        return codegen_api.BooleanFieldSpec(
            required=required,
            description=property.description,
        )
    elif property.type == "object":
        if property.additionalProperties is not None:
            if isinstance(property.additionalProperties, bool):
                raise Exception("Invalid map definition")
            return codegen_api.DictFieldSpec(
                value_type=to_field_spec(property.additionalProperties, True),
                min_count=property.minProperties,
                max_count=property.maxProperties,
                required=True,
                description=property.description,
            )
    raise Exception(f"Encountered unexpected property: {property}")


def to_object_name(schemaish: Union[opi.Reference, opi.Schema]) -> codegen_api.ObjectTypeName:
    if isinstance(schemaish, opi.Reference):
        return codegen_api.ObjectTypeName(schemaish.ref[schemaish.ref.rindex("/") + 1 :])
    raise Exception()


def resolve_field(
    schemaish: Union[opi.Reference, opi.Schema], field: str, components: dict[str, opi.Components]
) -> opi.Schema | None:
    if isinstance(schemaish, opi.Reference):
        schema = resolve_schema(schemaish, components)
    else:
        schema = schemaish

    if schema.type and schema.properties is not None and schema.type == "object":
        if inner_schema := schema.properties.get(field):
            return resolve_schema(inner_schema, components)

    if schema.allOf:
        for inner_schema in schema.allOf:
            if current_field := resolve_field(inner_schema, field, components):
                return current_field
    return None


def resolve_schema(
    schemaish: Union[opi.Reference, opi.Schema], components: dict[str, opi.Components]
) -> opi.Schema:
    if isinstance(schemaish, opi.Reference):
        file, json_path = schemaish.ref.split("#")
        reference_type = json_path[json_path.rindex("/") + 1 :]
        component = components.get(file)
        if component is None or component.schemas is None:
            raise Exception(f"Missing definition for reference {schemaish}")
        return component.schemas[reference_type]
    return schemaish
