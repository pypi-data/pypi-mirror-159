r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStoreEndpointInfoSourceEndpoint", "ObjectStoreEndpointInfoSourceEndpointSchema"]
__pdoc__ = {
    "ObjectStoreEndpointInfoSourceEndpointSchema.resource": False,
    "ObjectStoreEndpointInfoSourceEndpointSchema.opts": False,
    "ObjectStoreEndpointInfoSourceEndpoint": False,
}


class ObjectStoreEndpointInfoSourceEndpointSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpointInfoSourceEndpoint object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the object_store_endpoint_info_source_endpoint. """

    name = fields.Str(data_key="name")
    r""" Source name.

Example: src1 """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", unknown=EXCLUDE, data_key="svm")
    r""" The svm field of the object_store_endpoint_info_source_endpoint. """

    type = fields.Str(data_key="type")
    r""" Type of the source endpoint. Supported value is volume.

Valid choices:

* volume """

    uuid = fields.Str(data_key="uuid")
    r""" Source UUID.

Example: f1c68b66-2e59-11ea-a778-00505682bd8f """

    @property
    def resource(self):
        return ObjectStoreEndpointInfoSourceEndpoint

    gettable_fields = [
        "links",
        "name",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "type",
        "uuid",
    ]
    """links,name,svm.links,svm.name,svm.uuid,type,uuid,"""

    patchable_fields = [
        "svm.name",
        "svm.uuid",
    ]
    """svm.name,svm.uuid,"""

    postable_fields = [
        "svm.name",
        "svm.uuid",
    ]
    """svm.name,svm.uuid,"""


class ObjectStoreEndpointInfoSourceEndpoint(Resource):

    _schema = ObjectStoreEndpointInfoSourceEndpointSchema
