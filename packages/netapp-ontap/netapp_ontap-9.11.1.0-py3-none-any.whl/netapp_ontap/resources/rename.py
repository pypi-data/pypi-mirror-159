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


__all__ = ["Rename", "RenameSchema"]
__pdoc__ = {
    "RenameSchema.resource": False,
    "RenameSchema.opts": False,
    "Rename.rename_show": False,
    "Rename.rename_create": False,
    "Rename.rename_modify": False,
    "Rename.rename_delete": False,
}


class RenameSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Rename object"""

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the rename.

Example: exchange """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the rename.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return Rename

    gettable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Rename.get_collection(fields=field)]
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
            raise NetAppRestError("Rename modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Rename(Resource):
    """Allows interaction with Rename objects on the host"""

    _schema = RenameSchema
    _path = "/api/renames"
    _keys = ["rename.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves xxxx.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter.
* `xxx`
* `xxx.*`
* `xxx.xxx`
### Related ONTAP commands
* `xxx`
* `xxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="rename show")
        def rename_show(
            fields: List[Choices.define(["name", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Rename resources

            Args:
                name: 
                uuid: 
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Rename.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Rename resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Rename"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a xxxx.
### Related ONTAP commands
* `xxx xxx xxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["Rename"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Rename"], NetAppResponse]:
        r"""Creates a xxx.
### Required properties
* `xxx` or `xxx` - Description.
* `xxx`, `xxx.xxx.xxx`, or `xxx.xxx.xxx` - Description.
* `xxx` or `xxx.xxx` - Description.
### Recommended optional properties
* `xxx` - Description.
* `xxx` or `xxx` - Description.
### Default property values
If not specified in POST, the following default property values are assigned:
* `xxx` - _value_
* `xxx` - _value_
### Related ONTAP commands
* `xxxxx`
* `xxxxx`
* `xxxxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["Rename"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a xxxx.
### Related ONTAP commands
* `network interface delete`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves xxxx.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter.
* `xxx`
* `xxx.*`
* `xxx.xxx`
### Related ONTAP commands
* `xxx`
* `xxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves xxxx.
### Expensive properties
There is an added cost to retrieving values for these properties. They are not included by default in GET results and must be explicitly requested using the `fields` query parameter.
* `xxx`
* `xxx.*`
* `xxx.xxx`
### Related ONTAP commands
* `xxx`
* `xxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a xxx.
### Required properties
* `xxx` or `xxx` - Description.
* `xxx`, `xxx.xxx.xxx`, or `xxx.xxx.xxx` - Description.
* `xxx` or `xxx.xxx` - Description.
### Recommended optional properties
* `xxx` - Description.
* `xxx` or `xxx` - Description.
### Default property values
If not specified in POST, the following default property values are assigned:
* `xxx` - _value_
* `xxx` - _value_
### Related ONTAP commands
* `xxxxx`
* `xxxxx`
* `xxxxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="rename create")
        async def rename_create(
        ) -> ResourceTable:
            """Create an instance of a Rename resource

            Args:
                name: 
                uuid: 
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = Rename(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create Rename: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a xxxx.
### Related ONTAP commands
* `xxx xxx xxx`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="rename modify")
        async def rename_modify(
        ) -> ResourceTable:
            """Modify an instance of a Rename resource

            Args:
                name: 
                query_name: 
                uuid: 
                query_uuid: 
            """

            kwargs = {}
            changes = {}
            if query_name is not None:
                kwargs["name"] = query_name
            if query_uuid is not None:
                kwargs["uuid"] = query_uuid

            if name is not None:
                changes["name"] = name
            if uuid is not None:
                changes["uuid"] = uuid

            if hasattr(Rename, "find"):
                resource = Rename.find(
                    **kwargs
                )
            else:
                resource = Rename()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Rename: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a xxxx.
### Related ONTAP commands
* `network interface delete`
### Learn more
* [`DOC /xxx/xxx`](#docs-xxx-xxx_xxx)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="rename delete")
        async def rename_delete(
        ) -> None:
            """Delete an instance of a Rename resource

            Args:
                name: 
                uuid: 
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(Rename, "find"):
                resource = Rename.find(
                    **kwargs
                )
            else:
                resource = Rename()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete Rename: %s" % err)


