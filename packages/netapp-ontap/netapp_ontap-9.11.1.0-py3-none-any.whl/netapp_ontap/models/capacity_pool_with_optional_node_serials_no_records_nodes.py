r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["CapacityPoolWithOptionalNodeSerialsNoRecordsNodes", "CapacityPoolWithOptionalNodeSerialsNoRecordsNodesSchema"]
__pdoc__ = {
    "CapacityPoolWithOptionalNodeSerialsNoRecordsNodesSchema.resource": False,
    "CapacityPoolWithOptionalNodeSerialsNoRecordsNodesSchema.opts": False,
    "CapacityPoolWithOptionalNodeSerialsNoRecordsNodes": False,
}


class CapacityPoolWithOptionalNodeSerialsNoRecordsNodesSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CapacityPoolWithOptionalNodeSerialsNoRecordsNodes object"""

    new_node_serial_number = fields.Str(data_key="new_node_serial_number")
    r""" New node serial number to assign to this node.
This is not required when reassigning an existing node that is using capacity pools licensing to another capacity pool license.
It is required when converting a node that is using capacity tiers (node-locked) licensing to using capacity pools licensing. In this case, a new serial number must be generated from the license manager that has the capacity pool license installed.


Example: 99939000010000000011 """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the capacity_pool_with_optional_node_serials_no_records_nodes. """

    @property
    def resource(self):
        return CapacityPoolWithOptionalNodeSerialsNoRecordsNodes

    gettable_fields = [
        "node.links",
        "node.name",
        "node.uuid",
    ]
    """node.links,node.name,node.uuid,"""

    patchable_fields = [
        "new_node_serial_number",
        "node.name",
        "node.uuid",
    ]
    """new_node_serial_number,node.name,node.uuid,"""

    postable_fields = [
        "new_node_serial_number",
        "node.name",
        "node.uuid",
    ]
    """new_node_serial_number,node.name,node.uuid,"""


class CapacityPoolWithOptionalNodeSerialsNoRecordsNodes(Resource):

    _schema = CapacityPoolWithOptionalNodeSerialsNoRecordsNodesSchema
