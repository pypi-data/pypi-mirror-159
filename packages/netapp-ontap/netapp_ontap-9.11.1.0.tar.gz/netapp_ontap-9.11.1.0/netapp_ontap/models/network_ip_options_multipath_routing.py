r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["NetworkIpOptionsMultipathRouting", "NetworkIpOptionsMultipathRoutingSchema"]
__pdoc__ = {
    "NetworkIpOptionsMultipathRoutingSchema.resource": False,
    "NetworkIpOptionsMultipathRoutingSchema.opts": False,
    "NetworkIpOptionsMultipathRouting": False,
}


class NetworkIpOptionsMultipathRoutingSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the NetworkIpOptionsMultipathRouting object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" When set to "true", multipath routing is enabled. When set to "false", multipath routing is disabled. """

    @property
    def resource(self):
        return NetworkIpOptionsMultipathRouting

    gettable_fields = [
        "enabled",
    ]
    """enabled,"""

    patchable_fields = [
        "enabled",
    ]
    """enabled,"""

    postable_fields = [
        "enabled",
    ]
    """enabled,"""


class NetworkIpOptionsMultipathRouting(Resource):

    _schema = NetworkIpOptionsMultipathRoutingSchema
