from __future__ import annotations

import dataclasses
import decimal
from typing import Literal, NewType, Union

PrimitiveTypeName = Literal["boolean", "int", "number", "date", "enum", "string", "list", "dict"]
ObjectTypeName = NewType("ObjectTypeName", str)
FieldType = Union[PrimitiveTypeName, Literal["object"]]
TypeName = Union[ObjectTypeName, PrimitiveTypeName]


@dataclasses.dataclass(frozen=True)
class BooleanFieldSpec:
    required: bool = True
    description: str | None = None
    field_type: Literal["boolean"] = "boolean"


@dataclasses.dataclass(frozen=True)
class IntFieldSpec:
    required: bool = True
    minimum: int | None = None
    maximum: int | None = None
    exclusive_min: bool = False
    exclusive_max: bool = False
    allow_number: bool = False
    description: str | None = None
    field_type: Literal["int"] = "int"


@dataclasses.dataclass(frozen=True)
class NumberFieldSpec:
    required: bool = True
    minimum: decimal.Decimal | None = None
    maximum: decimal.Decimal | None = None
    exclusive_min: bool = False
    exclusive_max: bool = False
    description: str | None = None
    field_type: Literal["number"] = "number"


@dataclasses.dataclass(frozen=True)
class DateFieldSpec:
    required: bool = True
    description: str | None = None
    field_type: Literal["date"] = "date"


@dataclasses.dataclass(frozen=True)
class DatetimeFieldSpec:
    required: bool = True
    description: str | None = None
    field_type: Literal["datetime"] = "datetime"


@dataclasses.dataclass(frozen=True)
class StringFieldSpec:
    required: bool = True
    description: str | None = None
    field_type: Literal["string"] = "string"


@dataclasses.dataclass(frozen=True)
class UUIDFieldSpec:
    required: bool = True
    description: str | None = None
    field_type: Literal["uuid"] = "uuid"


@dataclasses.dataclass
class StringLiteralFieldSpec:
    value: str
    required: bool = True
    description: str | None = None
    field_type: Literal["literal"] = "literal"


@dataclasses.dataclass(frozen=True)
class ListFieldSpec:
    element_type: FieldSpec
    min_count: int | None = None
    max_count: int | None = None
    allow_single_value_as_array: bool = False
    required: bool = True
    description: str | None = None
    field_type: Literal["list"] = "list"


@dataclasses.dataclass(frozen=True)
class DictFieldSpec:
    # keys have to be strings
    value_type: FieldSpec
    min_count: int | None = None
    max_count: int | None = None
    required: bool = True
    description: str | None = None
    field_type: Literal["dict"] = "dict"


@dataclasses.dataclass(frozen=True)
class ObjectFieldSpec:
    object_type: ObjectTypeName
    required: bool = True
    description: str | None = None
    field_type: Literal["object"] = "object"


FieldSpec = Union[
    BooleanFieldSpec,
    DateFieldSpec,
    DatetimeFieldSpec,
    DictFieldSpec,
    IntFieldSpec,
    ListFieldSpec,
    NumberFieldSpec,
    ObjectFieldSpec,
    StringFieldSpec,
    StringLiteralFieldSpec,
    UUIDFieldSpec,
]


@dataclasses.dataclass(frozen=True)
class ObjectSpec:
    name: ObjectTypeName
    fields: dict[str, FieldSpec]
    description: str | None = None
    type: Literal["object"] = "object"


@dataclasses.dataclass(frozen=True)
class EnumSpec:
    name: ObjectTypeName
    values: list[str]
    description: str | None = None
    type: Literal["enum"] = "enum"


@dataclasses.dataclass(frozen=True)
class UnionSpec:
    name: ObjectTypeName
    discriminator_field: str
    union: dict[str, ObjectTypeName]
    description: str | None = None
    type: Literal["union"] = "union"


@dataclasses.dataclass(frozen=True)
class AliasSpec:
    name: ObjectTypeName
    field: FieldSpec
    description: str | None = None
    type: Literal["alias"] = "alias"


ClassSpec = Union[ObjectSpec, EnumSpec, UnionSpec, AliasSpec]
