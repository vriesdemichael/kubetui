# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/v3/api__v1_openapi.json
#   timestamp: 2022-12-01T15:55:56+00:00

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, Field


class IntOrString(BaseModel):
    __root__: Union[int, str] = Field(
        ...,
        description='IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.',
    )
