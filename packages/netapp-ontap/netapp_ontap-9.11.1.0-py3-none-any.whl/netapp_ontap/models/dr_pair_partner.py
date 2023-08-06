r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["DrPairPartner", "DrPairPartnerSchema"]
__pdoc__ = {
    "DrPairPartnerSchema.resource": False,
    "DrPairPartnerSchema.opts": False,
    "DrPairPartner": False,
}


class DrPairPartnerSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the DrPairPartner object"""

    name = fields.Str(data_key="name")
    r""" Name of the node.

Example: nodeB """

    @property
    def resource(self):
        return DrPairPartner

    gettable_fields = [
        "name",
    ]
    """name,"""

    patchable_fields = [
        "name",
    ]
    """name,"""

    postable_fields = [
        "name",
    ]
    """name,"""


class DrPairPartner(Resource):

    _schema = DrPairPartnerSchema
