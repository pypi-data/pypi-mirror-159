r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRestoreDestinationStorageService", "SnapmirrorRestoreDestinationStorageServiceSchema"]
__pdoc__ = {
    "SnapmirrorRestoreDestinationStorageServiceSchema.resource": False,
    "SnapmirrorRestoreDestinationStorageServiceSchema.opts": False,
    "SnapmirrorRestoreDestinationStorageService": False,
}


class SnapmirrorRestoreDestinationStorageServiceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRestoreDestinationStorageService object"""

    enabled = fields.Boolean(data_key="enabled")
    r""" This property indicates whether to create the destination endpoint using storage service. """

    enforce_performance = fields.Boolean(data_key="enforce_performance")
    r""" Optional property to enforce storage service performance on the destination endpoint when the destination endpoint is used for read-write operations. This property is applicable to FlexVol volume and FlexGroup volume endpoints. """

    name = fields.Str(data_key="name")
    r""" Optional property to specify the storage service name for the destination endpoint. This property is considered when the property "create_destination.storage_service.enabled" is set to "true". When the property "create_destination.storage_service.enabled" is set to "true" and the "create_destination.storage_service.name" for the endpoint is not specified, then ONTAP selects the highest storage service available on the cluster to provision the destination endpoint. This property is applicable to FlexVol volume, and FlexGroup volume endpoints.

Valid choices:

* extreme
* performance
* value """

    @property
    def resource(self):
        return SnapmirrorRestoreDestinationStorageService

    gettable_fields = [
        "enabled",
        "enforce_performance",
        "name",
    ]
    """enabled,enforce_performance,name,"""

    patchable_fields = [
        "enabled",
        "enforce_performance",
        "name",
    ]
    """enabled,enforce_performance,name,"""

    postable_fields = [
        "enabled",
        "enforce_performance",
        "name",
    ]
    """enabled,enforce_performance,name,"""


class SnapmirrorRestoreDestinationStorageService(Resource):

    _schema = SnapmirrorRestoreDestinationStorageServiceSchema
