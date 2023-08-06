r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["VolumeRebalancing1FailureReason", "VolumeRebalancing1FailureReasonSchema"]
__pdoc__ = {
    "VolumeRebalancing1FailureReasonSchema.resource": False,
    "VolumeRebalancing1FailureReasonSchema.opts": False,
    "VolumeRebalancing1FailureReason": False,
}


class VolumeRebalancing1FailureReasonSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the VolumeRebalancing1FailureReason object"""

    code = fields.Str(data_key="code")
    r""" Error code of volume capacity rebalancing operation. """

    message = fields.Str(data_key="message")
    r""" Details why the volume capacity rebalancing operation failed. """

    @property
    def resource(self):
        return VolumeRebalancing1FailureReason

    gettable_fields = [
        "code",
        "message",
    ]
    """code,message,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class VolumeRebalancing1FailureReason(Resource):

    _schema = VolumeRebalancing1FailureReasonSchema
