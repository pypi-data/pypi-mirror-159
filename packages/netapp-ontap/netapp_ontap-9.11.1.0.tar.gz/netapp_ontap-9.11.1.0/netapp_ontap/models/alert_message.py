r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["AlertMessage", "AlertMessageSchema"]
__pdoc__ = {
    "AlertMessageSchema.resource": False,
    "AlertMessageSchema.opts": False,
    "AlertMessage": False,
}


class AlertMessageSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AlertMessage object"""

    message = fields.Str(data_key="message")
    r""" The message field of the alert_message. """

    @property
    def resource(self):
        return AlertMessage

    gettable_fields = [
        "message",
    ]
    """message,"""

    patchable_fields = [
        "message",
    ]
    """message,"""

    postable_fields = [
        "message",
    ]
    """message,"""


class AlertMessage(Resource):

    _schema = AlertMessageSchema
