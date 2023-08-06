r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["Usage", "UsageSchema"]
__pdoc__ = {
    "UsageSchema.resource": False,
    "UsageSchema.opts": False,
    "Usage": False,
}


class UsageSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Usage object"""

    count = Size(data_key="count")
    r""" Number of times the inspection point has been triggered.
On POST, this specifies the incremental number of uses.


Example: 12 """

    milliseconds = Size(data_key="milliseconds")
    r""" Cumulative elapsed time, in milliseconds, spent at this
inspection point. On POST, this specifies the incremental
time.


Example: 3029 """

    name = fields.Str(data_key="name")
    r""" Identifier for the inspection point that is being measured.
Use a dotted-string representation for keys, where the first
portion of the key specifies the source or application
that generated the record.


Example: ocsm.volumes.inventory """

    @property
    def resource(self):
        return Usage

    gettable_fields = [
        "count",
        "milliseconds",
        "name",
    ]
    """count,milliseconds,name,"""

    patchable_fields = [
        "count",
        "milliseconds",
        "name",
    ]
    """count,milliseconds,name,"""

    postable_fields = [
        "count",
        "milliseconds",
        "name",
    ]
    """count,milliseconds,name,"""


class Usage(Resource):

    _schema = UsageSchema
