r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsEventResponseRecordsActionPossibleActionsParameters", "EmsEventResponseRecordsActionPossibleActionsParametersSchema"]
__pdoc__ = {
    "EmsEventResponseRecordsActionPossibleActionsParametersSchema.resource": False,
    "EmsEventResponseRecordsActionPossibleActionsParametersSchema.opts": False,
    "EmsEventResponseRecordsActionPossibleActionsParameters": False,
}


class EmsEventResponseRecordsActionPossibleActionsParametersSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsEventResponseRecordsActionPossibleActionsParameters object"""

    format = fields.Str(data_key="format")
    r""" Indicates the contents and format of the string.

Example: date-time """

    name = fields.Str(data_key="name")
    r""" Parameter name.

Example: schedule-at """

    type = fields.Str(data_key="type")
    r""" Parameter type.

Valid choices:

* string
* integer """

    @property
    def resource(self):
        return EmsEventResponseRecordsActionPossibleActionsParameters

    gettable_fields = [
        "format",
        "name",
        "type",
    ]
    """format,name,type,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class EmsEventResponseRecordsActionPossibleActionsParameters(Resource):

    _schema = EmsEventResponseRecordsActionPossibleActionsParametersSchema
