r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRelationshipRestore", "SnapmirrorRelationshipRestoreSchema"]
__pdoc__ = {
    "SnapmirrorRelationshipRestoreSchema.resource": False,
    "SnapmirrorRelationshipRestoreSchema.opts": False,
    "SnapmirrorRelationshipRestore": False,
}


class SnapmirrorRelationshipRestoreSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRelationshipRestore object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the snapmirror_relationship_restore. """

    archive_retrieval_priority = fields.Str(data_key="archive_retrieval_priority")
    r""" Priority level at which the objects are restored from the archival storage. The value can be high, standard or low. The cloud provider's lowest priority will be used as the default. It is only supported for object store SnapMirror relationships. If the objects were not archived, the property will be ignored.

Valid choices:

* standard
* high
* low """

    create_destination = fields.Nested("netapp_ontap.models.snapmirror_restore_destination.SnapmirrorRestoreDestinationSchema", unknown=EXCLUDE, data_key="create_destination")
    r""" The create_destination field of the snapmirror_relationship_restore. """

    destination = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", unknown=EXCLUDE, data_key="destination")
    r""" This property is the destination endpoint of the restore relationship. The destination endpoint can be a FlexVol volume or a FlexGroup volume. For the POST request, the destination endpoint must be of type "DP" for full volume restore, "RW" for incremental volume restore and restore of files or LUNs. The destination endpoint path name must be specified in the "destination.path" property. """

    files = fields.List(fields.Nested("netapp_ontap.models.snapmirror_relationship_restore_files.SnapmirrorRelationshipRestoreFilesSchema", unknown=EXCLUDE), data_key="files")
    r""" This specifies the list of files or LUNs to be restored. Can contain up to eight files or LUNs. """

    source = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", unknown=EXCLUDE, data_key="source")
    r""" This property is the source endpoint of the restore relationship. The source endpoint can be a FlexVol volume or a FlexGroup volume. """

    source_snapshot = fields.Str(data_key="source_snapshot")
    r""" Specifies the Snapshot copy on the source to be transferred to the destination. """

    storage_efficiency_enabled = fields.Boolean(data_key="storage_efficiency_enabled")
    r""" Set this property to "false" to turn off storage efficiency for data transferred over the wire and written to the destination. """

    throttle = Size(data_key="throttle")
    r""" Throttle, in KBs per seconds. Defaults to unlimited. """

    @property
    def resource(self):
        return SnapmirrorRelationshipRestore

    gettable_fields = [
    ]
    """"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "archive_retrieval_priority",
        "create_destination",
        "destination",
        "files",
        "source",
        "source_snapshot",
        "storage_efficiency_enabled",
        "throttle",
        "uuid",
    ]
    """archive_retrieval_priority,create_destination,destination,files,source,source_snapshot,storage_efficiency_enabled,throttle,uuid,"""


class SnapmirrorRelationshipRestore(Resource):

    _schema = SnapmirrorRelationshipRestoreSchema
