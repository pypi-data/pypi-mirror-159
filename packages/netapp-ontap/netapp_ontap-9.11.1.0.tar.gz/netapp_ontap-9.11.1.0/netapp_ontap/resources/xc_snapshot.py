r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

try:
    RECLINE_INSTALLED = False
    import recline
    from recline.arg_types.choices import Choices
    from recline.commands import ReclineCommandError
    from netapp_ontap.resource_table import ResourceTable
    RECLINE_INSTALLED = True
except ImportError:
    pass

from marshmallow import fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["XcSnapshot", "XcSnapshotSchema"]
__pdoc__ = {
    "XcSnapshotSchema.resource": False,
    "XcSnapshotSchema.opts": False,
    "XcSnapshot.xc_snapshot_show": False,
    "XcSnapshot.xc_snapshot_create": False,
    "XcSnapshot.xc_snapshot_modify": False,
    "XcSnapshot.xc_snapshot_delete": False,
}


class XcSnapshotSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSnapshot object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_snapshot. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" A comment associated with the Snapshot copy. This is an optional attribute for POST or PATCH. """

    create_time = ImpreciseDateTime(
        data_key="create_time",
    )
    r""" Creation time of the Snapshot copy. It is the volume access time when the Snapshot copy was created.

Example: 2019-02-04T19:00:00Z """

    expiry_time = ImpreciseDateTime(
        data_key="expiry_time",
    )
    r""" The expiry time for the Snapshot copy. This is an optional attribute for POST or PATCH. Snapshot copies with an expiry time set are not allowed to be deleted until the retention time is reached.

Example: 2019-02-04T19:00:00Z """

    name = fields.Str(
        data_key="name",
    )
    r""" Snapshot copy. Valid in POST or PATCH.

Example: this_snapshot """

    owners = fields.List(fields.Str, data_key="owners")
    r""" The owners field of the xc_snapshot. """

    provenance_volume = fields.Nested("netapp_ontap.models.snapshot_provenance_volume.SnapshotProvenanceVolumeSchema", data_key="provenance_volume", unknown=EXCLUDE)
    r""" The provenance_volume field of the xc_snapshot. """

    reclaimable_space = Size(
        data_key="reclaimable_space",
    )
    r""" Space reclaimed when the Snapshot copy is deleted, in bytes. """

    size = Size(
        data_key="size",
    )
    r""" Size of the active file system at the time the Snapshot copy is captured. The actual size of the Snapshot copy also includes those blocks trapped by other Snapshot copies. On a Snapshot copy deletion, the "size" amount of blocks is the maximum number of blocks available. On a Snapshot copy restore, the "afs-used size" value will match the Snapshot copy "size" value.

Example: 122880 """

    snaplock_expiry_time = ImpreciseDateTime(
        data_key="snaplock_expiry_time",
    )
    r""" SnapLock expiry time for the Snapshot copy, if the Snapshot copy is taken on a SnapLock volume. A Snapshot copy is not allowed to be deleted or renamed until the SnapLock ComplianceClock time goes beyond this retention time.

Example: 2019-02-04T19:00:00Z """

    snapmirror_label = fields.Str(
        data_key="snapmirror_label",
    )
    r""" Label for SnapMirror operations """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['valid', 'invalid', 'partial']),
    )
    r""" State of the Snapshot copy. There are cases where some Snapshot copies are not complete. In the "partial" state, the Snapshot copy is consistent but exists only on the subset of the constituents that existed prior to the FlexGroup's expansion. Partial Snapshot copies cannot be used for a Snapshot copy restore operation. A Snapshot copy is in an "invalid" state when it is present in some FlexGroup constituents but not in others. At all other times, a Snapshot copy is valid.

Valid choices:

* valid
* invalid
* partial """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_snapshot. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID of the Snapshot copy in the volume that uniquely identifies the Snapshot copy in that volume.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    version_uuid = fields.Str(
        data_key="version_uuid",
    )
    r""" The 128 bit identifier that uniquely identifies a snapshot and its logical data layout.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the xc_snapshot. """

    @property
    def resource(self):
        return XcSnapshot

    gettable_fields = [
        "links",
        "comment",
        "create_time",
        "expiry_time",
        "name",
        "owners",
        "provenance_volume",
        "reclaimable_space",
        "size",
        "snaplock_expiry_time",
        "snapmirror_label",
        "state",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
        "version_uuid",
        "volume.links",
        "volume.name",
        "volume.uuid",
    ]
    """links,comment,create_time,expiry_time,name,owners,provenance_volume,reclaimable_space,size,snaplock_expiry_time,snapmirror_label,state,svm.links,svm.name,svm.uuid,uuid,version_uuid,volume.links,volume.name,volume.uuid,"""

    patchable_fields = [
        "comment",
        "expiry_time",
        "name",
        "provenance_volume",
        "reclaimable_space",
        "snapmirror_label",
        "svm.name",
        "svm.uuid",
        "volume.name",
        "volume.uuid",
    ]
    """comment,expiry_time,name,provenance_volume,reclaimable_space,snapmirror_label,svm.name,svm.uuid,volume.name,volume.uuid,"""

    postable_fields = [
        "comment",
        "expiry_time",
        "name",
        "provenance_volume",
        "reclaimable_space",
        "snapmirror_label",
        "svm.name",
        "svm.uuid",
        "volume.name",
        "volume.uuid",
    ]
    """comment,expiry_time,name,provenance_volume,reclaimable_space,snapmirror_label,svm.name,svm.uuid,volume.name,volume.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSnapshot.get_collection(fields=field)]
    return getter

async def _wait_for_job(response: NetAppResponse) -> None:
    """Examine the given response. If it is a job, asynchronously wait for it to
    complete. While polling, prints the current status message of the job.
    """

    if not response.is_job:
        return
    from netapp_ontap.resources import Job
    job = Job(**response.http_response.json()["job"])
    while True:
        job.get(fields="state,message")
        if hasattr(job, "message"):
            print("[%s]: %s" % (job.state, job.message))
        if job.state == "failure":
            raise NetAppRestError("XcSnapshot modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSnapshot(Resource):
    r""" snapshot clone for cluster peer. """

    _schema = XcSnapshotSchema
    _path = "/api/svm/peers/{peer[uuid]}/storage/volumes/{volume[uuid]}/snapshots"
    _keys = ["peer.uuid", "volume.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET snapshots"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc snapshot show")
        def xc_snapshot_show(
            volume_uuid,
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            create_time: Choices.define(_get_field_list("create_time"), cache_choices=True, inexact=True)=None,
            expiry_time: Choices.define(_get_field_list("expiry_time"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            owners: Choices.define(_get_field_list("owners"), cache_choices=True, inexact=True)=None,
            reclaimable_space: Choices.define(_get_field_list("reclaimable_space"), cache_choices=True, inexact=True)=None,
            size: Choices.define(_get_field_list("size"), cache_choices=True, inexact=True)=None,
            snaplock_expiry_time: Choices.define(_get_field_list("snaplock_expiry_time"), cache_choices=True, inexact=True)=None,
            snapmirror_label: Choices.define(_get_field_list("snapmirror_label"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            version_uuid: Choices.define(_get_field_list("version_uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "create_time", "expiry_time", "name", "owners", "reclaimable_space", "size", "snaplock_expiry_time", "snapmirror_label", "state", "uuid", "version_uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSnapshot resources

            Args:
                comment: A comment associated with the Snapshot copy. This is an optional attribute for POST or PATCH.
                create_time: Creation time of the Snapshot copy. It is the volume access time when the Snapshot copy was created.
                expiry_time: The expiry time for the Snapshot copy. This is an optional attribute for POST or PATCH. Snapshot copies with an expiry time set are not allowed to be deleted until the retention time is reached.
                name: Snapshot copy. Valid in POST or PATCH.
                owners: 
                reclaimable_space: Space reclaimed when the Snapshot copy is deleted, in bytes.
                size: Size of the active file system at the time the Snapshot copy is captured. The actual size of the Snapshot copy also includes those blocks trapped by other Snapshot copies. On a Snapshot copy deletion, the \"size\" amount of blocks is the maximum number of blocks available. On a Snapshot copy restore, the \"afs-used size\" value will match the Snapshot copy \"size\" value.
                snaplock_expiry_time: SnapLock expiry time for the Snapshot copy, if the Snapshot copy is taken on a SnapLock volume. A Snapshot copy is not allowed to be deleted or renamed until the SnapLock ComplianceClock time goes beyond this retention time.
                snapmirror_label: Label for SnapMirror operations
                state: State of the Snapshot copy. There are cases where some Snapshot copies are not complete. In the \"partial\" state, the Snapshot copy is consistent but exists only on the subset of the constituents that existed prior to the FlexGroup's expansion. Partial Snapshot copies cannot be used for a Snapshot copy restore operation. A Snapshot copy is in an \"invalid\" state when it is present in some FlexGroup constituents but not in others. At all other times, a Snapshot copy is valid.
                uuid: The UUID of the Snapshot copy in the volume that uniquely identifies the Snapshot copy in that volume.
                version_uuid: The 128 bit identifier that uniquely identifies a snapshot and its logical data layout.
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if create_time is not None:
                kwargs["create_time"] = create_time
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if name is not None:
                kwargs["name"] = name
            if owners is not None:
                kwargs["owners"] = owners
            if reclaimable_space is not None:
                kwargs["reclaimable_space"] = reclaimable_space
            if size is not None:
                kwargs["size"] = size
            if snaplock_expiry_time is not None:
                kwargs["snaplock_expiry_time"] = snaplock_expiry_time
            if snapmirror_label is not None:
                kwargs["snapmirror_label"] = snapmirror_label
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if version_uuid is not None:
                kwargs["version_uuid"] = version_uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSnapshot.get_collection(
                volume_uuid,
                peer_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all XcSnapshot resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET snapshots"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






