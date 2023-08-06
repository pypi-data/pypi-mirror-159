r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API manages Snapshot copies associated with object store endpoints.
For SnapMirror relationship's with an object store endpoint path one or more Snapshot copies are transferred to the object store endpoint on successful SnapMirror transfer. Each Snapshot copy has a unique identifier.
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


__all__ = ["SnapmirrorObjectStoreEndpointSnapshot", "SnapmirrorObjectStoreEndpointSnapshotSchema"]
__pdoc__ = {
    "SnapmirrorObjectStoreEndpointSnapshotSchema.resource": False,
    "SnapmirrorObjectStoreEndpointSnapshotSchema.opts": False,
    "SnapmirrorObjectStoreEndpointSnapshot.snapmirror_object_store_endpoint_snapshot_show": False,
    "SnapmirrorObjectStoreEndpointSnapshot.snapmirror_object_store_endpoint_snapshot_create": False,
    "SnapmirrorObjectStoreEndpointSnapshot.snapmirror_object_store_endpoint_snapshot_modify": False,
    "SnapmirrorObjectStoreEndpointSnapshot.snapmirror_object_store_endpoint_snapshot_delete": False,
}


class SnapmirrorObjectStoreEndpointSnapshotSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SnapmirrorObjectStoreEndpointSnapshot object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the snapmirror_object_store_endpoint_snapshot. """

    archived_objects = fields.Boolean(
        data_key="archived_objects",
    )
    r""" Indicates whether or not the Snapshot copy has objects in the archival storage. """

    create_time = ImpreciseDateTime(
        data_key="create_time",
    )
    r""" Creation time of the Snapshot copy in date-time format.

Example: 2020-04-17T19:00:00Z """

    endpoint = fields.Nested("netapp_ontap.models.object_store_endpoint.ObjectStoreEndpointSchema", data_key="endpoint", unknown=EXCLUDE)
    r""" The object store endpoint associated with the Snapshot copy. """

    logical_size = Size(
        data_key="logical_size",
    )
    r""" Logical size of the Snapshot copy in bytes.

Example: 10156769280 """

    name = fields.Str(
        data_key="name",
    )
    r""" Snapshot copy name.

Example: snap1 """

    object_store = fields.Nested("netapp_ontap.models.object_store.ObjectStoreSchema", data_key="object_store", unknown=EXCLUDE)
    r""" The object store associated with the Snapshot copy. """

    snapmirror_label = fields.Str(
        data_key="snapmirror_label",
    )
    r""" SnapMirror label.

Example: daily """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Snapshot copy UUID.

Example: 04fb1ddb-2947-4eb0-af09-3eb6dc538926 """

    @property
    def resource(self):
        return SnapmirrorObjectStoreEndpointSnapshot

    gettable_fields = [
        "links",
        "archived_objects",
        "create_time",
        "endpoint",
        "logical_size",
        "name",
        "object_store",
        "snapmirror_label",
        "uuid",
    ]
    """links,archived_objects,create_time,endpoint,logical_size,name,object_store,snapmirror_label,uuid,"""

    patchable_fields = [
        "endpoint",
        "object_store",
        "uuid",
    ]
    """endpoint,object_store,uuid,"""

    postable_fields = [
        "endpoint",
        "object_store",
        "uuid",
    ]
    """endpoint,object_store,uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SnapmirrorObjectStoreEndpointSnapshot.get_collection(fields=field)]
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
            raise NetAppRestError("SnapmirrorObjectStoreEndpointSnapshot modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SnapmirrorObjectStoreEndpointSnapshot(Resource):
    r""" Snapshot copy information associated with an object store endpoint. """

    _schema = SnapmirrorObjectStoreEndpointSnapshotSchema
    _path = "/api/snapmirror/object-stores/{object_store[uuid]}/endpoints/{endpoint[uuid]}/snapshots"
    _keys = ["object_store.uuid", "endpoint.uuid", "uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves Snapshot copy information associated with an object store endpoint. The object store UUID, together with the endpoint UUID is used to list the Snapshot copies and their information.
### Related ONTAP commands
* `snapmirror object-store endpoint snapshot show`
### Examples
GET "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/snapshots"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{endpoint.uuid}/snapshots`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{endpoint.uuid}_snapshots)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snapmirror object store endpoint snapshot show")
        def snapmirror_object_store_endpoint_snapshot_show(
            endpoint_uuid,
            object_store_uuid,
            archived_objects: Choices.define(_get_field_list("archived_objects"), cache_choices=True, inexact=True)=None,
            create_time: Choices.define(_get_field_list("create_time"), cache_choices=True, inexact=True)=None,
            logical_size: Choices.define(_get_field_list("logical_size"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            snapmirror_label: Choices.define(_get_field_list("snapmirror_label"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["archived_objects", "create_time", "logical_size", "name", "snapmirror_label", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SnapmirrorObjectStoreEndpointSnapshot resources

            Args:
                archived_objects: Indicates whether or not the Snapshot copy has objects in the archival storage.
                create_time: Creation time of the Snapshot copy in date-time format.
                logical_size: Logical size of the Snapshot copy in bytes.
                name: Snapshot copy name.
                snapmirror_label: SnapMirror label.
                uuid: Snapshot copy UUID.
            """

            kwargs = {}
            if archived_objects is not None:
                kwargs["archived_objects"] = archived_objects
            if create_time is not None:
                kwargs["create_time"] = create_time
            if logical_size is not None:
                kwargs["logical_size"] = logical_size
            if name is not None:
                kwargs["name"] = name
            if snapmirror_label is not None:
                kwargs["snapmirror_label"] = snapmirror_label
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SnapmirrorObjectStoreEndpointSnapshot.get_collection(
                endpoint_uuid,
                object_store_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SnapmirrorObjectStoreEndpointSnapshot resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)



    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SnapmirrorObjectStoreEndpointSnapshot"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a Snapshot copy from the object store endpoint. The object store UUID, object store endpoint UUID together with the Snapshot copy UUID will be used to specify the Snapshot copy to be deleted.
### Related ONTAP commands
* `snapmirror object-store endpoint snapshot delete`
### Examples
  DELETE "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/snapshots/04fb1ddb-2947-4eb0-af09-3eb6dc538926"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{endpoint.uuid}/snapshots`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{endpoint.uuid}_snapshots)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves Snapshot copy information associated with an object store endpoint. The object store UUID, together with the endpoint UUID is used to list the Snapshot copies and their information.
### Related ONTAP commands
* `snapmirror object-store endpoint snapshot show`
### Examples
GET "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/snapshots"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{endpoint.uuid}/snapshots`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{endpoint.uuid}_snapshots)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves specific Snapshot copy information given its UUID. The object store UUID, endpoint UUID together with the Snapshot copy UUID is used to list the information for the specific Snapshot copy.
### Related ONTAP commands
* `snapmirror object-store endpoint snapshot show`
### Example
<br/>
```
GET "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/snapshots/04fb1ddb-2947-4eb0-af09-3eb6dc538926"
```
<br/>
### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{endpoint.uuid}/snapshots`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{endpoint.uuid}_snapshots)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)



    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a Snapshot copy from the object store endpoint. The object store UUID, object store endpoint UUID together with the Snapshot copy UUID will be used to specify the Snapshot copy to be deleted.
### Related ONTAP commands
* `snapmirror object-store endpoint snapshot delete`
### Examples
  DELETE "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/snapshots/04fb1ddb-2947-4eb0-af09-3eb6dc538926"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{endpoint.uuid}/snapshots`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{endpoint.uuid}_snapshots)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="snapmirror object store endpoint snapshot delete")
        async def snapmirror_object_store_endpoint_snapshot_delete(
            endpoint_uuid,
            object_store_uuid,
            archived_objects: bool = None,
            create_time: datetime = None,
            logical_size: Size = None,
            name: str = None,
            snapmirror_label: str = None,
            uuid: str = None,
        ) -> None:
            """Delete an instance of a SnapmirrorObjectStoreEndpointSnapshot resource

            Args:
                archived_objects: Indicates whether or not the Snapshot copy has objects in the archival storage.
                create_time: Creation time of the Snapshot copy in date-time format.
                logical_size: Logical size of the Snapshot copy in bytes.
                name: Snapshot copy name.
                snapmirror_label: SnapMirror label.
                uuid: Snapshot copy UUID.
            """

            kwargs = {}
            if archived_objects is not None:
                kwargs["archived_objects"] = archived_objects
            if create_time is not None:
                kwargs["create_time"] = create_time
            if logical_size is not None:
                kwargs["logical_size"] = logical_size
            if name is not None:
                kwargs["name"] = name
            if snapmirror_label is not None:
                kwargs["snapmirror_label"] = snapmirror_label
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(SnapmirrorObjectStoreEndpointSnapshot, "find"):
                resource = SnapmirrorObjectStoreEndpointSnapshot.find(
                    endpoint_uuid,
                    object_store_uuid,
                    **kwargs
                )
            else:
                resource = SnapmirrorObjectStoreEndpointSnapshot(endpoint_uuid,object_store_uuid,)
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SnapmirrorObjectStoreEndpointSnapshot: %s" % err)


