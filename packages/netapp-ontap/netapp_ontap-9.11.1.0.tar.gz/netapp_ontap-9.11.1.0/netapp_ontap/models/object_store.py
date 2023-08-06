r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ObjectStore", "ObjectStoreSchema"]
__pdoc__ = {
    "ObjectStoreSchema.resource": False,
    "ObjectStoreSchema.opts": False,
    "ObjectStore": False,
}


class ObjectStoreSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStore object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the object_store. """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the object_store.

Example: cd9563a0-2e59-11ea-a778-00505682bd8f """

    @property
    def resource(self):
        return ObjectStore

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


class ObjectStore(Resource):

    _schema = ObjectStoreSchema
