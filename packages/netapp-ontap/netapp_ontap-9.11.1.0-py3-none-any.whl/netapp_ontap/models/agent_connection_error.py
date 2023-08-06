r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["AgentConnectionError", "AgentConnectionErrorSchema"]
__pdoc__ = {
    "AgentConnectionErrorSchema.resource": False,
    "AgentConnectionErrorSchema.opts": False,
    "AgentConnectionError": False,
}


class AgentConnectionErrorSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AgentConnectionError object"""

    code = Size(data_key="code")
    r""" Error code associated with the last error. """

    message = fields.Str(data_key="message")
    r""" Error message associated with the last error. """

    time = ImpreciseDateTime(data_key="time")
    r""" ISO-8601 time of the last error. """

    @property
    def resource(self):
        return AgentConnectionError

    gettable_fields = [
        "code",
        "message",
        "time",
    ]
    """code,message,time,"""

    patchable_fields = [
        "code",
        "message",
        "time",
    ]
    """code,message,time,"""

    postable_fields = [
        "code",
        "message",
        "time",
    ]
    """code,message,time,"""


class AgentConnectionError(Resource):

    _schema = AgentConnectionErrorSchema
