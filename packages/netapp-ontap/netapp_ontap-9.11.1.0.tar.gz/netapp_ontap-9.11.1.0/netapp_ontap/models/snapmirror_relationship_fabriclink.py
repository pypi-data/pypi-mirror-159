r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SnapmirrorRelationshipFabriclink", "SnapmirrorRelationshipFabriclinkSchema"]
__pdoc__ = {
    "SnapmirrorRelationshipFabriclinkSchema.resource": False,
    "SnapmirrorRelationshipFabriclinkSchema.opts": False,
    "SnapmirrorRelationshipFabriclink": False,
}


class SnapmirrorRelationshipFabriclinkSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorRelationshipFabriclink object"""

    destination_bucket = fields.Str(data_key="destination_bucket")
    r""" Specifies the name of the destination bucket of the FabricLink SnapMirror relationship. This parameter is supported for FabricLink SnapMirror relationships with ONTAP or external object store vendor endpoints. This parameter is only available on ONTAP 9.10.1 or later. """

    destination_role = fields.Str(data_key="destination_role")
    r""" This field represents the destination bucket's role within FabricLink. Possible values for this field are "active_mirror" and "backup". In a bi-directional ONTAP to ONTAP mirroring relationship, both FabricLink SnapMirror records will contain "active_mirror" in both the source-role and destination-role fields. This field conveys that both mirrors are capable of performing an active role at any time. In an ONTAP to Non-ONTAP FabricLink replication relationship, the source-role is "active_mirror" and the destination-role is "backup". This parameter is supported for FabricLink SnapMirror relationships with ONTAP or external object store vendor endpoints. This parameter is only available in ONTAP 9.10.1 or later.

Valid choices:

* active_mirror
* backup """

    pending_work_task_count = Size(data_key="pending_work_task_count")
    r""" Conveys how many discrete tasks the bucket in this unidirectional FabricLink SnapMirror relationship knows it will eventually have to perform to fully update the destination to reflect the source's state. Each work item might represent the need to push a newly created object from the source to the destination mirror, or perhaps to advise the destination mirror that an existing object has been modified or deleted. If the link is configured with an RPO of one hour and the user creates an object on the source bucket, that bucket will immediately show that it now has a pending work item to send that new object to the destination; FabricLink intentionally will not act on that work item until the hour has elapsed. This parameter is only available in ONTAP 9.10.1 or later. """

    pull_byte_count = Size(data_key="pull_byte_count")
    r""" Represents the approximate number of bytes of data that the destination bucket anticipates reading from the source bucket for the FabricLink SnapMirror relationship. This parameter is only available in ONTAP 9.10.1 or later. """

    push_byte_count = Size(data_key="push_byte_count")
    r""" Represents the approximate number of bytes of data that must be pushed from the source bucket to the destination bucket for the FabricLink SnapMirror relationship. This parameter is only available in ONTAP 9.10.1 or later. """

    source_bucket = fields.Str(data_key="source_bucket")
    r""" Specifies the name of the source bucket of the FabricLink SnapMirror relationship. This parameter is supported only for FabricLink SnapMirror relationships with ONTAP endpoints. This parameter is only available in ONTAP 9.10.1 or later. """

    source_role = fields.Str(data_key="source_role")
    r""" This field represents the source bucket's role within FabricLink. One possible value for this field is "active_mirror". In a bi-directional ONTAP to ONTAP mirroring relationship, both FabricLink SnapMirror records will contain "active_mirror" in both the source-role and destination-role fields. This field conveys that both mirrors are capable of performing an active role at any time. In an ONTAP to Non-ONTAP FabricLink replication relationship, the source-role is "active_mirror" and the destination-role is "backup". This parameter is supported only for FabricLink SnapMirror relationships with an ONTAP endpoint. This parameter is only available in ONTAP 9.10.1 or later.

Valid choices:

* active_mirror """

    status = fields.Str(data_key="status")
    r""" Specifies the status of the FabricLink SnapMirror relationship. This parameter is only available in ONTAP 9.10.1 or later. """

    topology_uuid = fields.Str(data_key="topology_uuid")
    r""" Topology UUID is used to refer to a unique data set. All the links that connect the same data set share the same topology UUID. Thus, in a fan-out topology, all links fanning from the same source bucket will carry the same topology-uuid value. Similarly, in a cascading mirror arrangement, all links in the cascade will carry the same topology-uuid value. This parameter is only available in ONTAP 9.10.1 or later. """

    @property
    def resource(self):
        return SnapmirrorRelationshipFabriclink

    gettable_fields = [
        "destination_bucket",
        "destination_role",
        "pending_work_task_count",
        "pull_byte_count",
        "push_byte_count",
        "source_bucket",
        "source_role",
        "status",
        "topology_uuid",
    ]
    """destination_bucket,destination_role,pending_work_task_count,pull_byte_count,push_byte_count,source_bucket,source_role,status,topology_uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class SnapmirrorRelationshipFabriclink(Resource):

    _schema = SnapmirrorRelationshipFabriclinkSchema
