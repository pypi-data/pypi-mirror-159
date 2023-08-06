r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

SnapDiff is an ONTAP engine that efficiently identifies the file and directory differences between two Snapshot copies of a volume. The POST API is used to establish a SnapDiff session. The API returns a session UUID and a session handle. A backup application can subsequently use the session UUID and handle to communicate with SnapDiff through Remote Procedure Calls (RPC).
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


__all__ = ["SnapdiffSession", "SnapdiffSessionSchema"]
__pdoc__ = {
    "SnapdiffSessionSchema.resource": False,
    "SnapdiffSessionSchema.opts": False,
    "SnapdiffSession.snapdiff_session_show": False,
    "SnapdiffSession.snapdiff_session_create": False,
    "SnapdiffSession.snapdiff_session_modify": False,
    "SnapdiffSession.snapdiff_session_delete": False,
}


class SnapdiffSessionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapdiffSession object"""

    access_time = fields.Boolean(
        data_key="access_time",
    )
    r""" Set to true to report files which have access time changes. """

    application = fields.Nested("netapp_ontap.models.snapdiff_application.SnapdiffApplicationSchema", data_key="application", unknown=EXCLUDE)
    r""" Application using the session. """

    base_snapshot = fields.Nested("netapp_ontap.resources.snapshot.SnapshotSchema", data_key="base_snapshot", unknown=EXCLUDE)
    r""" The base_snapshot field of the snapdiff_session. """

    checkpoint_enabled = fields.Boolean(
        data_key="checkpoint_enabled",
    )
    r""" Set to true to enable checkpointing for the session. A checkpoint cookie for restart will be returned when a sd_rpc_next RPC request is called. """

    diff_snapshot = fields.Nested("netapp_ontap.resources.snapshot.SnapshotSchema", data_key="diff_snapshot", unknown=EXCLUDE)
    r""" The diff_snapshot field of the snapdiff_session. """

    file_access_protocol = fields.Str(
        data_key="file_access_protocol",
        validate=enum_validation(['nfs', 'nfsv4', 'cifs']),
    )
    r""" This specifies the file access protocol for the filenames to be returned by each sd_rpc_next RPC call. This facilitates clients to use the filenames to access the changed files from the system.

Valid choices:

* nfs
* nfsv4
* cifs """

    handle = fields.Str(
        data_key="handle",
    )
    r""" Handle of the session. This is generated when the session is created and is to be used by SnapDiff RPC requests throughout the entire session.

Example: 0x00000414-00 """

    max_diffs = Size(
        data_key="max_diffs",
        validate=integer_validation(minimum=256, maximum=4096),
    )
    r""" This specifies the maximum number of changes to be returned by each sd_rpc_next RPC call. """

    report_file_attributes = fields.Boolean(
        data_key="report_file_attributes",
    )
    r""" Set to true to report the attributes of files. If this property is set to false, then only the inode number, change-type, filename, and file type are reported. """

    restart_cookie = fields.Str(
        data_key="restart_cookie",
    )
    r""" This is the cookie to start a session from the associated checkpoint. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" UUID of the session. This is generated when the session is created and is to be used by SnapDiff RPC requests throughout the entire session.

Example: c868a31d-a3d7-4b33-b555-a5bec402e41a """

    @property
    def resource(self):
        return SnapdiffSession

    gettable_fields = [
        "access_time",
        "application",
        "base_snapshot.links",
        "base_snapshot.name",
        "base_snapshot.uuid",
        "checkpoint_enabled",
        "diff_snapshot.links",
        "diff_snapshot.name",
        "diff_snapshot.uuid",
        "file_access_protocol",
        "handle",
        "max_diffs",
        "report_file_attributes",
        "restart_cookie",
        "uuid",
    ]
    """access_time,application,base_snapshot.links,base_snapshot.name,base_snapshot.uuid,checkpoint_enabled,diff_snapshot.links,diff_snapshot.name,diff_snapshot.uuid,file_access_protocol,handle,max_diffs,report_file_attributes,restart_cookie,uuid,"""

    patchable_fields = [
        "application",
    ]
    """application,"""

    postable_fields = [
        "access_time",
        "application",
        "base_snapshot.name",
        "base_snapshot.uuid",
        "checkpoint_enabled",
        "diff_snapshot.name",
        "diff_snapshot.uuid",
        "file_access_protocol",
        "max_diffs",
        "report_file_attributes",
        "restart_cookie",
    ]
    """access_time,application,base_snapshot.name,base_snapshot.uuid,checkpoint_enabled,diff_snapshot.name,diff_snapshot.uuid,file_access_protocol,max_diffs,report_file_attributes,restart_cookie,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SnapdiffSession.get_collection(fields=field)]
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
            raise NetAppRestError("SnapdiffSession modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SnapdiffSession(Resource):
    r""" SnapDiff session """

    _schema = SnapdiffSessionSchema
    _path = "/api/storage/volumes/{volume[uuid]}/snapdiff/sessions"
    _keys = ["volume.uuid"]




    @classmethod
    def post_collection(
        cls,
        records: Iterable["SnapdiffSession"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SnapdiffSession"], NetAppResponse]:
        r"""Creates a SnapDiff session.
### Required properties
* `application.name` - Name of the application.
* `application.type` - Type of the application.
* `diff_snapshot.name` or `diff_snapshot.uuid` - Name or UUID of the Snapshot copy corresponding to the end time of the difference operation.
### Recommended optional properties
* `base_snapshot.name` or `base_snapshot.uuid` - Name or UUID of the Snapshot copy corresponding to the beginning time of the difference operation.
* `restart_cookie` - Cookie to start a session from the associated checkpoint.
### Default property values
* `access_time` - _true_
* `report_file_attributes` - _true_
* `checkpoint_enabled` - _true_
* `file_access_protocol` - _nfs_
* `max_diffs` - _256_
### Example
Creating a SnapDiff session:
<br/>
```
POST "/api/storage/volumes/{volume.uuid}/snapdiff/sessions/" '{ "application":{"name": "BackupApp", "type": "backup"}, "base_snapshot":{"name": "snap1"}, "diff_snapshot":{"name": "snap2"} }'
```
<br/>

### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapdiff/sessions`](#docs-snapdiff-storage_volumes_{volume.uuid}_snapdiff_sessions)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)




    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a SnapDiff session.
### Required properties
* `application.name` - Name of the application.
* `application.type` - Type of the application.
* `diff_snapshot.name` or `diff_snapshot.uuid` - Name or UUID of the Snapshot copy corresponding to the end time of the difference operation.
### Recommended optional properties
* `base_snapshot.name` or `base_snapshot.uuid` - Name or UUID of the Snapshot copy corresponding to the beginning time of the difference operation.
* `restart_cookie` - Cookie to start a session from the associated checkpoint.
### Default property values
* `access_time` - _true_
* `report_file_attributes` - _true_
* `checkpoint_enabled` - _true_
* `file_access_protocol` - _nfs_
* `max_diffs` - _256_
### Example
Creating a SnapDiff session:
<br/>
```
POST "/api/storage/volumes/{volume.uuid}/snapdiff/sessions/" '{ "application":{"name": "BackupApp", "type": "backup"}, "base_snapshot":{"name": "snap1"}, "diff_snapshot":{"name": "snap2"} }'
```
<br/>

### Learn more
* [`DOC /storage/volumes/{volume.uuid}/snapdiff/sessions`](#docs-snapdiff-storage_volumes_{volume.uuid}_snapdiff_sessions)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snapdiff session create")
        async def snapdiff_session_create(
            volume_uuid,
            access_time: bool = None,
            application: dict = None,
            base_snapshot: dict = None,
            checkpoint_enabled: bool = None,
            diff_snapshot: dict = None,
            file_access_protocol: str = None,
            handle: str = None,
            max_diffs: Size = None,
            report_file_attributes: bool = None,
            restart_cookie: str = None,
            uuid: str = None,
        ) -> ResourceTable:
            """Create an instance of a SnapdiffSession resource

            Args:
                access_time: Set to true to report files which have access time changes.
                application: Application using the session.
                base_snapshot: 
                checkpoint_enabled: Set to true to enable checkpointing for the session. A checkpoint cookie for restart will be returned when a sd_rpc_next RPC request is called.
                diff_snapshot: 
                file_access_protocol: This specifies the file access protocol for the filenames to be returned by each sd_rpc_next RPC call. This facilitates clients to use the filenames to access the changed files from the system.
                handle: Handle of the session. This is generated when the session is created and is to be used by SnapDiff RPC requests throughout the entire session.
                max_diffs: This specifies the maximum number of changes to be returned by each sd_rpc_next RPC call.
                report_file_attributes: Set to true to report the attributes of files. If this property is set to false, then only the inode number, change-type, filename, and file type are reported.
                restart_cookie: This is the cookie to start a session from the associated checkpoint.
                uuid: UUID of the session. This is generated when the session is created and is to be used by SnapDiff RPC requests throughout the entire session.
            """

            kwargs = {}
            if access_time is not None:
                kwargs["access_time"] = access_time
            if application is not None:
                kwargs["application"] = application
            if base_snapshot is not None:
                kwargs["base_snapshot"] = base_snapshot
            if checkpoint_enabled is not None:
                kwargs["checkpoint_enabled"] = checkpoint_enabled
            if diff_snapshot is not None:
                kwargs["diff_snapshot"] = diff_snapshot
            if file_access_protocol is not None:
                kwargs["file_access_protocol"] = file_access_protocol
            if handle is not None:
                kwargs["handle"] = handle
            if max_diffs is not None:
                kwargs["max_diffs"] = max_diffs
            if report_file_attributes is not None:
                kwargs["report_file_attributes"] = report_file_attributes
            if restart_cookie is not None:
                kwargs["restart_cookie"] = restart_cookie
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = SnapdiffSession(
                volume_uuid,
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SnapdiffSession: %s" % err)
            return [resource]




