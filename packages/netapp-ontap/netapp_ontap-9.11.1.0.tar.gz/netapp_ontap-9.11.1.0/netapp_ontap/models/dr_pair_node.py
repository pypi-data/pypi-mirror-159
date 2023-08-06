r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["DrPairNode", "DrPairNodeSchema"]
__pdoc__ = {
    "DrPairNodeSchema.resource": False,
    "DrPairNodeSchema.opts": False,
    "DrPairNode": False,
}


class DrPairNodeSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the DrPairNode object"""

    name = fields.Str(data_key="name")
    r""" Name of the node.

Example: nodeA """

    @property
    def resource(self):
        return DrPairNode

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


class DrPairNode(Resource):

    _schema = DrPairNodeSchema
