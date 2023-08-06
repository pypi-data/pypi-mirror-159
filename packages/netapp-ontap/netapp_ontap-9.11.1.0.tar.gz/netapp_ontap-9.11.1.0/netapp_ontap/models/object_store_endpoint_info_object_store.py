r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStoreEndpointInfoObjectStore", "ObjectStoreEndpointInfoObjectStoreSchema"]
__pdoc__ = {
    "ObjectStoreEndpointInfoObjectStoreSchema.resource": False,
    "ObjectStoreEndpointInfoObjectStoreSchema.opts": False,
    "ObjectStoreEndpointInfoObjectStore": False,
}


class ObjectStoreEndpointInfoObjectStoreSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpointInfoObjectStore object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the object_store_endpoint_info_object_store. """

    container = fields.Str(data_key="container")
    r""" Name of the object store container hosting the endpoint.

Example: bucket1 """

    name = fields.Str(data_key="name")
    r""" The object store configuration name.

Example: sw_object_store """

    provider_type = fields.Str(data_key="provider_type")
    r""" Type of object store provider hosting the endpoint.

Valid choices:

* aws_s3
* sgws
* azure_cloud
* s3_compatible
* ibm_cos
* alicloud
* googlecloud
* ontap_s3 """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the object_store_endpoint_info_object_store.

Example: cd9563a0-2e59-11ea-a778-00505682bd8f """

    @property
    def resource(self):
        return ObjectStoreEndpointInfoObjectStore

    gettable_fields = [
        "links",
        "container",
        "name",
        "provider_type",
        "uuid",
    ]
    """links,container,name,provider_type,uuid,"""

    patchable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""

    postable_fields = [
        "container",
        "name",
        "provider_type",
        "uuid",
    ]
    """container,name,provider_type,uuid,"""


class ObjectStoreEndpointInfoObjectStore(Resource):

    _schema = ObjectStoreEndpointInfoObjectStoreSchema
