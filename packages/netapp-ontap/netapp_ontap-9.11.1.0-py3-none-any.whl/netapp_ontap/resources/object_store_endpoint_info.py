r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
When a SnapMirror relationship created by a SnapMirror POST API with an object store destination endpoint is populated, a UUID is created to reference the data that is stored in the object store for this endpoint. This API allows these endpoints, using the object store's UUID and endpoint UUID to identify the endpoint to be manipulated.
If a SnapMirror relationship with an object store endpoint path, in the form of <objstore name>:/objstore/<endpoint name>, is deleted, that same object store endpoint path can be reused in a subsequent SnapMirror relationship. This means that an object store endpoint path can be associated with different relationship UUIDs and different object store UUIDs. The user is expected to maintain a mapping of object store endpoint paths and UUIDs manually, so as to be able to provide the correct UUID to this API.
An object store is created using a /cloud/target API. Object store entities are referred to here as 'object store', 'object-store' or 'object_store' below, depending on context.
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


__all__ = ["ObjectStoreEndpointInfo", "ObjectStoreEndpointInfoSchema"]
__pdoc__ = {
    "ObjectStoreEndpointInfoSchema.resource": False,
    "ObjectStoreEndpointInfoSchema.opts": False,
    "ObjectStoreEndpointInfo.object_store_endpoint_info_show": False,
    "ObjectStoreEndpointInfo.object_store_endpoint_info_create": False,
    "ObjectStoreEndpointInfo.object_store_endpoint_info_modify": False,
    "ObjectStoreEndpointInfo.object_store_endpoint_info_delete": False,
}


class ObjectStoreEndpointInfoSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ObjectStoreEndpointInfo object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the object_store_endpoint_info. """

    archived_objects = fields.Boolean(
        data_key="archived_objects",
    )
    r""" Indicates whether or not the endpoint has objects in the archival storage. """

    destination = fields.Nested("netapp_ontap.models.object_store_endpoint_info_destination.ObjectStoreEndpointInfoDestinationSchema", data_key="destination", unknown=EXCLUDE)
    r""" The destination field of the object_store_endpoint_info. """

    object_store = fields.Nested("netapp_ontap.models.object_store_endpoint_info_object_store.ObjectStoreEndpointInfoObjectStoreSchema", data_key="object_store", unknown=EXCLUDE)
    r""" The object_store field of the object_store_endpoint_info. """

    source = fields.Nested("netapp_ontap.models.object_store_endpoint_info_source.ObjectStoreEndpointInfoSourceSchema", data_key="source", unknown=EXCLUDE)
    r""" The source field of the object_store_endpoint_info. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Destination endpoint UUID.

Example: 21c3abec-ee22-11ea-8048-00505682f04b """

    @property
    def resource(self):
        return ObjectStoreEndpointInfo

    gettable_fields = [
        "links",
        "archived_objects",
        "destination",
        "object_store",
        "source",
        "uuid",
    ]
    """links,archived_objects,destination,object_store,source,uuid,"""

    patchable_fields = [
        "destination",
        "object_store",
        "source",
        "uuid",
    ]
    """destination,object_store,source,uuid,"""

    postable_fields = [
        "destination",
        "object_store",
        "source",
        "uuid",
    ]
    """destination,object_store,source,uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in ObjectStoreEndpointInfo.get_collection(fields=field)]
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
            raise NetAppRestError("ObjectStoreEndpointInfo modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class ObjectStoreEndpointInfo(Resource):
    """Allows interaction with ObjectStoreEndpointInfo objects on the host"""

    _schema = ObjectStoreEndpointInfoSchema
    _path = "/api/snapmirror/object-stores/{object_store[uuid]}/endpoints"
    _keys = ["object_store.uuid", "uuid"]





    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["ObjectStoreEndpointInfo"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""This API deletes all the data of a specific endpoint within an object store that was populated by SnapMirror. The object store UUID, together with the endpoint's UUID will be used to specify the data to be processed by this API.
### Related ONTAP commands
* `snapmirror object-store endpoint delete`
### Examples
  DELETE "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{uuid}`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{uuid})"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)


    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information for the specified object store, endpoint.
### Related ONTAP commands
* `snapmirror object-store endpoint show`
### Example
  GET "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{uuid}`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{uuid})"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="object store endpoint info show")
        def object_store_endpoint_info_show(
            object_store_uuid,
            archived_objects: Choices.define(_get_field_list("archived_objects"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single ObjectStoreEndpointInfo resource

            Args:
                archived_objects: Indicates whether or not the endpoint has objects in the archival storage.
                uuid: Destination endpoint UUID.
            """

            kwargs = {}
            if archived_objects is not None:
                kwargs["archived_objects"] = archived_objects
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = ObjectStoreEndpointInfo(
                object_store_uuid,
                **kwargs
            )
            resource.get()
            return [resource]



    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""This API deletes all the data of a specific endpoint within an object store that was populated by SnapMirror. The object store UUID, together with the endpoint's UUID will be used to specify the data to be processed by this API.
### Related ONTAP commands
* `snapmirror object-store endpoint delete`
### Examples
  DELETE "/api/snapmirror/object-stores/cd9563a0-2e59-11ea-a778-00505682bd8f/endpoints/af86c94c-bcb2-4b4e-b8cc-c294793a310a/"

### Learn more
* [`DOC /snapmirror/object-stores/{object_store.uuid}/endpoints/{uuid}`](#docs-snapmirror-snapmirror_object-stores_{object_store.uuid}_endpoints_{uuid})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="object store endpoint info delete")
        async def object_store_endpoint_info_delete(
            object_store_uuid,
            archived_objects: bool = None,
            uuid: str = None,
        ) -> None:
            """Delete an instance of a ObjectStoreEndpointInfo resource

            Args:
                archived_objects: Indicates whether or not the endpoint has objects in the archival storage.
                uuid: Destination endpoint UUID.
            """

            kwargs = {}
            if archived_objects is not None:
                kwargs["archived_objects"] = archived_objects
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(ObjectStoreEndpointInfo, "find"):
                resource = ObjectStoreEndpointInfo.find(
                    object_store_uuid,
                    **kwargs
                )
            else:
                resource = ObjectStoreEndpointInfo(object_store_uuid,)
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete ObjectStoreEndpointInfo: %s" % err)


