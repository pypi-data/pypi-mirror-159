r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapdiffApplication", "SnapdiffApplicationSchema"]
__pdoc__ = {
    "SnapdiffApplicationSchema.resource": False,
    "SnapdiffApplicationSchema.opts": False,
    "SnapdiffApplication": False,
}


class SnapdiffApplicationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapdiffApplication object"""

    name = fields.Str(data_key="name")
    r""" Name of the application using SnapDiff.

Example: BackupApp """

    type = fields.Str(data_key="type")
    r""" Type of the application using SnapDiff.

Example: backup """

    @property
    def resource(self):
        return SnapdiffApplication

    gettable_fields = [
        "name",
        "type",
    ]
    """name,type,"""

    patchable_fields = [
        "name",
        "type",
    ]
    """name,type,"""

    postable_fields = [
        "name",
        "type",
    ]
    """name,type,"""


class SnapdiffApplication(Resource):

    _schema = SnapdiffApplicationSchema
