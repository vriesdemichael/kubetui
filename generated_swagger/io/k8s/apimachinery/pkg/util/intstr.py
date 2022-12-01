# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-01T16:01:27+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class IntOrString(BaseModel):
    __root__: str = Field(
        ...,
        description='IntOrString is a type that can hold an int32 or a string.  When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type.  This allows you to have, for example, a JSON field that can accept a name or number.',
    )