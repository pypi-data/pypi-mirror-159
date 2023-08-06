r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["FileHole", "FileHoleSchema"]
__pdoc__ = {
    "FileHoleSchema.resource": False,
    "FileHoleSchema.opts": False,
    "FileHole": False,
}


class FileHoleSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the FileHole object"""

    size = Size(data_key="size")
    r""" Size of the hole, in bytes. """

    start = Size(data_key="start")
    r""" Starting offset of the hole. """

    @property
    def resource(self):
        return FileHole

    gettable_fields = [
        "size",
        "start",
    ]
    """size,start,"""

    patchable_fields = [
        "size",
        "start",
    ]
    """size,start,"""

    postable_fields = [
        "size",
        "start",
    ]
    """size,start,"""


class FileHole(Resource):

    _schema = FileHoleSchema
