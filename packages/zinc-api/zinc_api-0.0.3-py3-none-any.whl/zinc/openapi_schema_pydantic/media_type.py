from typing import Any, Optional, Union

from pydantic import BaseModel
from pydantic import Extra
from pydantic import Field

from .example import Example
from .reference import Reference
from .schema import Schema


class MediaType(BaseModel):
    """Each Media Type Object provides schema and examples for the media type identified by its key."""

    media_type_schema: Optional[Union[Reference, Schema]] = Field(default=None, alias="schema")
    """
    The schema defining the content of the request, response, or parameter.
    """

    example: Optional[Any] = None
    """
    Example of the media type.
    
    The example object SHOULD be in the correct format as specified by the media type.
    
    The `example` field is mutually exclusive of the `examples` field.
    
    Furthermore, if referencing a `schema` which contains an example,
    the `example` value SHALL _override_ the example provided by the schema.
    """

    examples: Optional[dict[str, Union[Example, Reference]]] = None
    """
    Examples of the media type.
    
    Each example object SHOULD match the media type and specified schema if present.
    
    The `examples` field is mutually exclusive of the `example` field.
    
    Furthermore, if referencing a `schema` which contains an example,
    the `examples` value SHALL _override_ the example provided by the schema.
    """

    class Config:
        extra = Extra.ignore
        allow_population_by_field_name = True
        schema_extra = {
            "examples": [
                {
                    "schema": {"$ref": "#/components/schemas/Pet"},
                    "examples": {
                        "cat": {
                            "summary": "An example of a cat",
                            "value": {
                                "name": "Fluffy",
                                "petType": "Cat",
                                "color": "White",
                                "gender": "male",
                                "breed": "Persian",
                            },
                        },
                        "dog": {
                            "summary": "An example of a dog with a cat's name",
                            "value": {
                                "name": "Puma",
                                "petType": "Dog",
                                "color": "Black",
                                "gender": "Female",
                                "breed": "Mixed",
                            },
                        },
                        "frog": {"$ref": "#/components/examples/frog-example"},
                    },
                }
            ]
        }
