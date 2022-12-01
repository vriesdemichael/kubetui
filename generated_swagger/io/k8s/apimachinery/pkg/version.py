# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-01T16:01:27+00:00

from __future__ import annotations

from pydantic import BaseModel


class Info(BaseModel):
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str