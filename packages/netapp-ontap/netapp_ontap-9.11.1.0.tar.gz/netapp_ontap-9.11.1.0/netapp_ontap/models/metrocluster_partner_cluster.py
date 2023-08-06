r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["MetroclusterPartnerCluster", "MetroclusterPartnerClusterSchema"]
__pdoc__ = {
    "MetroclusterPartnerClusterSchema.resource": False,
    "MetroclusterPartnerClusterSchema.opts": False,
    "MetroclusterPartnerCluster": False,
}


class MetroclusterPartnerClusterSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the MetroclusterPartnerCluster object"""

    name = fields.Str(data_key="name")
    r""" Name of the partner cluster.

Example: cluster2 """

    @property
    def resource(self):
        return MetroclusterPartnerCluster

    gettable_fields = [
    ]
    """"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "name",
    ]
    """name,"""


class MetroclusterPartnerCluster(Resource):

    _schema = MetroclusterPartnerClusterSchema
