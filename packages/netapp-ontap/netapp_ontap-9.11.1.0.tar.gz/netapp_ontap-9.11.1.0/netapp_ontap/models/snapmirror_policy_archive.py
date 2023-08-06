r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorPolicyArchive", "SnapmirrorPolicyArchiveSchema"]
__pdoc__ = {
    "SnapmirrorPolicyArchiveSchema.resource": False,
    "SnapmirrorPolicyArchiveSchema.opts": False,
    "SnapmirrorPolicyArchive": False,
}


class SnapmirrorPolicyArchiveSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorPolicyArchive object"""

    after_days = Size(data_key="after_days")
    r""" Number of days after which the objects are archived. This is only applicable when "archive.enabled" is "true". If this property is not set when "archive.enabled" is "true", the default value is "0" and therefore archiving will be triggered instantly. The value range is 0..999. If the value is set to "0", the latest snapshot copy will be archived. The value of after_days cannot be changed from "0" if any FlexVol SnapMirror relationship is associated with the policy. """

    enabled = fields.Boolean(data_key="enabled")
    r""" When set to "true", the objects are archived. When set to "false", the objects are not archived. """

    @property
    def resource(self):
        return SnapmirrorPolicyArchive

    gettable_fields = [
        "after_days",
        "enabled",
    ]
    """after_days,enabled,"""

    patchable_fields = [
        "after_days",
        "enabled",
    ]
    """after_days,enabled,"""

    postable_fields = [
        "after_days",
        "enabled",
    ]
    """after_days,enabled,"""


class SnapmirrorPolicyArchive(Resource):

    _schema = SnapmirrorPolicyArchiveSchema
