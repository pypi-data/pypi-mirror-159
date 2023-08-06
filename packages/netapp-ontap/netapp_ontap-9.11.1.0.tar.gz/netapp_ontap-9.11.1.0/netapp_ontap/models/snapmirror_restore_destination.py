r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRestoreDestination", "SnapmirrorRestoreDestinationSchema"]
__pdoc__ = {
    "SnapmirrorRestoreDestinationSchema.resource": False,
    "SnapmirrorRestoreDestinationSchema.opts": False,
    "SnapmirrorRestoreDestination": False,
}


class SnapmirrorRestoreDestinationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRestoreDestination object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" Optional property to create the destination endpoint when establishing a SnapMirror restore relationship. It is assumed to be "false" if no other property is set and assumed to be "true" if any other property is set. """

    storage_service = fields.Nested("netapp_ontap.models.snapmirror_restore_destination_storage_service.SnapmirrorRestoreDestinationStorageServiceSchema", unknown=EXCLUDE, data_key="storage_service")
    r""" The storage_service field of the snapmirror_restore_destination. """

    @property
    def resource(self):
        return SnapmirrorRestoreDestination

    gettable_fields = [
    ]
    """"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "enabled",
        "storage_service",
    ]
    """enabled,storage_service,"""


class SnapmirrorRestoreDestination(Resource):

    _schema = SnapmirrorRestoreDestinationSchema
