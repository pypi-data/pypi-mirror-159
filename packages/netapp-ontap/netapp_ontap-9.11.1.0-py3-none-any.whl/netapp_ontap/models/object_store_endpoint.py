r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStoreEndpoint", "ObjectStoreEndpointSchema"]
__pdoc__ = {
    "ObjectStoreEndpointSchema.resource": False,
    "ObjectStoreEndpointSchema.opts": False,
    "ObjectStoreEndpoint": False,
}


class ObjectStoreEndpointSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpoint object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the object_store_endpoint. """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the object_store_endpoint.

Example: af86c94c-bcb2-4b4e-b8cc-c294793a310a """

    @property
    def resource(self):
        return ObjectStoreEndpoint

    gettable_fields = [
        "links",
        "uuid",
    ]
    """links,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class ObjectStoreEndpoint(Resource):

    _schema = ObjectStoreEndpointSchema
