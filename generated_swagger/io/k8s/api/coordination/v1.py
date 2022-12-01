# generated by datamodel-codegen:
#   filename:  https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json
#   timestamp: 2022-12-01T16:01:27+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from ...apimachinery.pkg.apis.meta import v1


class LeaseSpec(BaseModel):
    acquireTime: Optional[v1.MicroTime] = Field(
        None, description='acquireTime is a time when the current lease was acquired.'
    )
    holderIdentity: Optional[str] = Field(
        None,
        description='holderIdentity contains the identity of the holder of a current lease.',
    )
    leaseDurationSeconds: Optional[int] = Field(
        None,
        description='leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measure against time of last observed RenewTime.',
    )
    leaseTransitions: Optional[int] = Field(
        None,
        description='leaseTransitions is the number of transitions of a lease between holders.',
    )
    renewTime: Optional[v1.MicroTime] = Field(
        None,
        description='renewTime is a time when the current holder of a lease has last updated the lease.',
    )


class Lease(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMeta] = Field(
        None,
        description='More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )
    spec: Optional[LeaseSpec] = Field(
        None,
        description='Specification of the Lease. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status',
    )


class LeaseList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[Lease] = Field(..., description='Items is a list of schema objects.')
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata',
    )
