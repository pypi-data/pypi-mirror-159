r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["XcNodeResponseRecordsHa", "XcNodeResponseRecordsHaSchema"]
__pdoc__ = {
    "XcNodeResponseRecordsHaSchema.resource": False,
    "XcNodeResponseRecordsHaSchema.opts": False,
    "XcNodeResponseRecordsHa": False,
}


class XcNodeResponseRecordsHaSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcNodeResponseRecordsHa object"""

    auto_giveback = fields.Boolean(data_key="auto_giveback")
    r""" Specifies whether giveback is automatically initiated when the node that owns the storage is ready. """

    enabled = fields.Boolean(data_key="enabled")
    r""" Specifies whether or not storage failover is enabled. """

    giveback = fields.Nested("netapp_ontap.models.xc_node_response_records_ha_giveback.XcNodeResponseRecordsHaGivebackSchema", unknown=EXCLUDE, data_key="giveback")
    r""" The giveback field of the xc_node_response_records_ha. """

    interconnect = fields.Nested("netapp_ontap.models.cluster_nodes_ha_interconnect.ClusterNodesHaInterconnectSchema", unknown=EXCLUDE, data_key="interconnect")
    r""" The interconnect field of the xc_node_response_records_ha. """

    partners = fields.List(fields.Nested("netapp_ontap.models.xc_node_ha_partners.XcNodeHaPartnersSchema", unknown=EXCLUDE), data_key="partners")
    r""" Nodes in this node's High Availability (HA) group. """

    ports = fields.List(fields.Nested("netapp_ontap.models.cluster_nodes_ha_ports.ClusterNodesHaPortsSchema", unknown=EXCLUDE), data_key="ports")
    r""" The ports field of the xc_node_response_records_ha. """

    takeover = fields.Nested("netapp_ontap.models.cluster_nodes_ha_takeover.ClusterNodesHaTakeoverSchema", unknown=EXCLUDE, data_key="takeover")
    r""" The takeover field of the xc_node_response_records_ha. """

    @property
    def resource(self):
        return XcNodeResponseRecordsHa

    gettable_fields = [
        "auto_giveback",
        "enabled",
        "giveback",
        "interconnect",
        "partners.links",
        "partners.name",
        "partners.uuid",
        "ports",
        "takeover",
    ]
    """auto_giveback,enabled,giveback,interconnect,partners.links,partners.name,partners.uuid,ports,takeover,"""

    patchable_fields = [
        "giveback",
        "interconnect",
        "takeover",
    ]
    """giveback,interconnect,takeover,"""

    postable_fields = [
        "giveback",
        "interconnect",
        "takeover",
    ]
    """giveback,interconnect,takeover,"""


class XcNodeResponseRecordsHa(Resource):

    _schema = XcNodeResponseRecordsHaSchema
