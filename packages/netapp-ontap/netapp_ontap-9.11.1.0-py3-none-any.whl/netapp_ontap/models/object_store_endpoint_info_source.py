r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStoreEndpointInfoSource", "ObjectStoreEndpointInfoSourceSchema"]
__pdoc__ = {
    "ObjectStoreEndpointInfoSourceSchema.resource": False,
    "ObjectStoreEndpointInfoSourceSchema.opts": False,
    "ObjectStoreEndpointInfoSource": False,
}


class ObjectStoreEndpointInfoSourceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpointInfoSource object"""

    endpoint = fields.Nested("netapp_ontap.models.object_store_endpoint_info_source_endpoint.ObjectStoreEndpointInfoSourceEndpointSchema", unknown=EXCLUDE, data_key="endpoint")
    r""" The endpoint field of the object_store_endpoint_info_source. """

    physical_size = Size(data_key="physical_size")
    r""" Physical used size of the source endpoint.

Example: 421888 """

    type = fields.Str(data_key="type")
    r""" Set to rw for read/write, and dp for a data protection endpoint.

Valid choices:

* rw
* dp """

    @property
    def resource(self):
        return ObjectStoreEndpointInfoSource

    gettable_fields = [
        "endpoint",
        "physical_size",
        "type",
    ]
    """endpoint,physical_size,type,"""

    patchable_fields = [
        "endpoint",
    ]
    """endpoint,"""

    postable_fields = [
        "endpoint",
    ]
    """endpoint,"""


class ObjectStoreEndpointInfoSource(Resource):

    _schema = ObjectStoreEndpointInfoSourceSchema
