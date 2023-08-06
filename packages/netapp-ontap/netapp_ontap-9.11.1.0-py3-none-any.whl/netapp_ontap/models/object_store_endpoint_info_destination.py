r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStoreEndpointInfoDestination", "ObjectStoreEndpointInfoDestinationSchema"]
__pdoc__ = {
    "ObjectStoreEndpointInfoDestinationSchema.resource": False,
    "ObjectStoreEndpointInfoDestinationSchema.opts": False,
    "ObjectStoreEndpointInfoDestination": False,
}


class ObjectStoreEndpointInfoDestinationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpointInfoDestination object"""

    logical_size = Size(data_key="logical_size")
    r""" Logical size of the destination endpoint.

Example: 262144 """

    @property
    def resource(self):
        return ObjectStoreEndpointInfoDestination

    gettable_fields = [
        "logical_size",
    ]
    """logical_size,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class ObjectStoreEndpointInfoDestination(Resource):

    _schema = ObjectStoreEndpointInfoDestinationSchema
