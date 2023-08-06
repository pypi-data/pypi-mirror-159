r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["MaxdataOnSanMetadata", "MaxdataOnSanMetadataSchema"]
__pdoc__ = {
    "MaxdataOnSanMetadataSchema.resource": False,
    "MaxdataOnSanMetadataSchema.opts": False,
    "MaxdataOnSanMetadata": False,
}


class MaxdataOnSanMetadataSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the MaxdataOnSanMetadata object"""

    key = fields.Str(data_key="key")
    r""" Key to look up metadata associated with an application. """

    value = fields.Str(data_key="value")
    r""" Value associated with the key. """

    @property
    def resource(self):
        return MaxdataOnSanMetadata

    gettable_fields = [
        "key",
        "value",
    ]
    """key,value,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "key",
        "value",
    ]
    """key,value,"""


class MaxdataOnSanMetadata(Resource):

    _schema = MaxdataOnSanMetadataSchema
