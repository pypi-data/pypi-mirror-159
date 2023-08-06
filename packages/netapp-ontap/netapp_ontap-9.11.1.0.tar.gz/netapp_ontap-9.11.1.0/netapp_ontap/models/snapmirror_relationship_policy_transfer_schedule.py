r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRelationshipPolicyTransferSchedule", "SnapmirrorRelationshipPolicyTransferScheduleSchema"]
__pdoc__ = {
    "SnapmirrorRelationshipPolicyTransferScheduleSchema.resource": False,
    "SnapmirrorRelationshipPolicyTransferScheduleSchema.opts": False,
    "SnapmirrorRelationshipPolicyTransferSchedule": False,
}


class SnapmirrorRelationshipPolicyTransferScheduleSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRelationshipPolicyTransferSchedule object"""

    name = fields.Str(data_key="name")
    r""" The name field of the snapmirror_relationship_policy_transfer_schedule.

Example: hourly """

    @property
    def resource(self):
        return SnapmirrorRelationshipPolicyTransferSchedule

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


class SnapmirrorRelationshipPolicyTransferSchedule(Resource):

    _schema = SnapmirrorRelationshipPolicyTransferScheduleSchema
