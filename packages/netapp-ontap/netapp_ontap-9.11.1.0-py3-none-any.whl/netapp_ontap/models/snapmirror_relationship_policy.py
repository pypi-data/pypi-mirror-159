r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRelationshipPolicy", "SnapmirrorRelationshipPolicySchema"]
__pdoc__ = {
    "SnapmirrorRelationshipPolicySchema.resource": False,
    "SnapmirrorRelationshipPolicySchema.opts": False,
    "SnapmirrorRelationshipPolicy": False,
}


class SnapmirrorRelationshipPolicySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRelationshipPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the snapmirror_relationship_policy. """

    name = fields.Str(data_key="name")
    r""" The name field of the snapmirror_relationship_policy.

Example: Asynchronous """

    transfer_schedule = fields.Nested("netapp_ontap.models.snapmirror_relationship_policy_transfer_schedule.SnapmirrorRelationshipPolicyTransferScheduleSchema", unknown=EXCLUDE, data_key="transfer_schedule")
    r""" The transfer_schedule field of the snapmirror_relationship_policy. """

    type = fields.Str(data_key="type")
    r""" The type field of the snapmirror_relationship_policy.

Valid choices:

* async
* sync
* continuous """

    uuid = fields.Str(data_key="uuid")
    r""" The uuid field of the snapmirror_relationship_policy.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return SnapmirrorRelationshipPolicy

    gettable_fields = [
        "links",
        "name",
        "transfer_schedule",
        "type",
        "uuid",
    ]
    """links,name,transfer_schedule,type,uuid,"""

    patchable_fields = [
        "name",
        "transfer_schedule",
        "uuid",
    ]
    """name,transfer_schedule,uuid,"""

    postable_fields = [
        "name",
        "transfer_schedule",
        "uuid",
    ]
    """name,transfer_schedule,uuid,"""


class SnapmirrorRelationshipPolicy(Resource):

    _schema = SnapmirrorRelationshipPolicySchema
