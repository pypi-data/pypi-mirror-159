r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["XcEmsEventResponseRecordsParameters", "XcEmsEventResponseRecordsParametersSchema"]
__pdoc__ = {
    "XcEmsEventResponseRecordsParametersSchema.resource": False,
    "XcEmsEventResponseRecordsParametersSchema.opts": False,
    "XcEmsEventResponseRecordsParameters": False,
}


class XcEmsEventResponseRecordsParametersSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcEmsEventResponseRecordsParameters object"""

    name = fields.Str(data_key="name")
    r""" Name of parameter

Example: numOps """

    value = fields.Str(data_key="value")
    r""" Value of parameter

Example: 123 """

    @property
    def resource(self):
        return XcEmsEventResponseRecordsParameters

    gettable_fields = [
        "name",
        "value",
    ]
    """name,value,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class XcEmsEventResponseRecordsParameters(Resource):

    _schema = XcEmsEventResponseRecordsParametersSchema
