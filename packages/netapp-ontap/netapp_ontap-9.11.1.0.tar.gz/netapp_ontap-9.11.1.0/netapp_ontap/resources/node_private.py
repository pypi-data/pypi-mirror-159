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


__all__ = ["NodePrivate", "NodePrivateSchema"]
__pdoc__ = {
    "NodePrivateSchema.resource": False,
    "NodePrivateSchema.opts": False,
    "NodePrivate.node_private_show": False,
    "NodePrivate.node_private_create": False,
    "NodePrivate.node_private_modify": False,
    "NodePrivate.node_private_delete": False,
}


class NodePrivateSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the NodePrivate object"""

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the node_private.

Example: 90121081160018809713 """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the node_private.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return NodePrivate

    gettable_fields = [
        "serial_number",
        "uuid",
    ]
    """serial_number,uuid,"""

    patchable_fields = [
        "serial_number",
    ]
    """serial_number,"""

    postable_fields = [
        "serial_number",
    ]
    """serial_number,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in NodePrivate.get_collection(fields=field)]
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
            raise NetAppRestError("NodePrivate modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class NodePrivate(Resource):
    r""" Node information for the private API. """

    _schema = NodePrivateSchema
    _path = "/api/private/cluster/nodes"
    _keys = ["uuid"]



    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["NodePrivate"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the node information.
### Related ONTAP commands
* `system node modify`
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)




    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information for the node.
### Related ONTAP commands
* `system node virtual-machine instance show`
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="node private show")
        def node_private_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single NodePrivate resource

            Args:
                serial_number: 
                uuid: 
            """

            kwargs = {}
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = NodePrivate(
                **kwargs
            )
            resource.get()
            return [resource]


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the node information.
### Related ONTAP commands
* `system node modify`
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="node private modify")
        async def node_private_modify(
        ) -> ResourceTable:
            """Modify an instance of a NodePrivate resource

            Args:
                serial_number: 
                query_serial_number: 
                uuid: 
                query_uuid: 
            """

            kwargs = {}
            changes = {}
            if query_serial_number is not None:
                kwargs["serial_number"] = query_serial_number
            if query_uuid is not None:
                kwargs["uuid"] = query_uuid

            if serial_number is not None:
                changes["serial_number"] = serial_number
            if uuid is not None:
                changes["uuid"] = uuid

            if hasattr(NodePrivate, "find"):
                resource = NodePrivate.find(
                    **kwargs
                )
            else:
                resource = NodePrivate()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify NodePrivate: %s" % err)



