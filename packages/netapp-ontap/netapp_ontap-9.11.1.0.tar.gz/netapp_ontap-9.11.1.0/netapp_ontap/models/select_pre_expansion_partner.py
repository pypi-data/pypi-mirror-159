r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SelectPreExpansionPartner", "SelectPreExpansionPartnerSchema"]
__pdoc__ = {
    "SelectPreExpansionPartnerSchema.resource": False,
    "SelectPreExpansionPartnerSchema.opts": False,
    "SelectPreExpansionPartner": False,
}


class SelectPreExpansionPartnerSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SelectPreExpansionPartner object"""

    mac = fields.Str(data_key="mac")
    r""" MAC address of partner node.

Example: 00:16:3e:48:c9:6d """

    name = fields.Str(data_key="name")
    r""" Name of partner node. """

    @property
    def resource(self):
        return SelectPreExpansionPartner

    gettable_fields = [
        "mac",
        "name",
    ]
    """mac,name,"""

    patchable_fields = [
        "mac",
        "name",
    ]
    """mac,name,"""

    postable_fields = [
        "mac",
        "name",
    ]
    """mac,name,"""


class SelectPreExpansionPartner(Resource):

    _schema = SelectPreExpansionPartnerSchema
