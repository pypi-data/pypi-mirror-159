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


__all__ = ["Note", "NoteSchema"]
__pdoc__ = {
    "NoteSchema.resource": False,
    "NoteSchema.opts": False,
    "Note.note_show": False,
    "Note.note_create": False,
    "Note.note_modify": False,
    "Note.note_delete": False,
}


class NoteSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Note object"""

    client_secret = fields.Str(
        data_key="client_secret",
    )
    r""" Encrypted value that is only visible to user that created it. """

    modified_from = fields.Str(
        data_key="modified_from",
    )
    r""" The modified_from field of the note.

Example: 172.120.10.1 """

    modified_time = ImpreciseDateTime(
        data_key="modified_time",
    )
    r""" The modified_time field of the note.

Example: 2008-09-15T15:53:00 """

    name = fields.Str(
        data_key="name",
    )
    r""" Name or key identifying the note.

Example: com.netapp.ocum.address """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the note. """

    scope = fields.Str(
        data_key="scope",
    )
    r""" The scope field of the note. """

    user = fields.Str(
        data_key="user",
    )
    r""" User that created the entry.

Example: joe """

    value = fields.Str(
        data_key="value",
    )
    r""" Opaque data associated with the note.

Example: 172.120.10.1 """

    @property
    def resource(self):
        return Note

    gettable_fields = [
        "client_secret",
        "modified_from",
        "modified_time",
        "name",
        "owner.links",
        "owner.name",
        "owner.uuid",
        "scope",
        "user",
        "value",
    ]
    """client_secret,modified_from,modified_time,name,owner.links,owner.name,owner.uuid,scope,user,value,"""

    patchable_fields = [
        "client_secret",
        "owner.name",
        "owner.uuid",
        "scope",
        "value",
    ]
    """client_secret,owner.name,owner.uuid,scope,value,"""

    postable_fields = [
        "client_secret",
        "name",
        "owner.name",
        "owner.uuid",
        "scope",
        "value",
    ]
    """client_secret,name,owner.name,owner.uuid,scope,value,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Note.get_collection(fields=field)]
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
            raise NetAppRestError("Note modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Note(Resource):
    """Allows interaction with Note objects on the host"""

    _schema = NoteSchema
    _path = "/api/private/cluster/notes"
    _keys = ["owner.uuid", "name"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the notes associated with the cluster. Notes are small
opaque pieces of meta-data used by administrators or
management applications for capturing hints or preferences.
An example is: curl -k -u admin -X GET https://10.234.45.17/api/private/cluster/notes
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="note show")
        def note_show(
            fields: List[Choices.define(["client_secret", "modified_from", "modified_time", "name", "scope", "user", "value", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Note resources

            Args:
                client_secret: Encrypted value that is only visible to user that created it.
                modified_from: 
                modified_time: 
                name: Name or key identifying the note.
                scope: 
                user: User that created the entry.
                value: Opaque data associated with the note.
            """

            kwargs = {}
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if modified_from is not None:
                kwargs["modified_from"] = modified_from
            if modified_time is not None:
                kwargs["modified_time"] = modified_time
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if user is not None:
                kwargs["user"] = user
            if value is not None:
                kwargs["value"] = value
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Note.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Note resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Note"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a cluster note.
Example of a PATCH request:
curl -k -u admin -X PATCH https://10.234.45.17/api/private/cluster/notes/342a6fae-02dc-11e9-8b27-005056a78833/ta -d '{"value":"172.120.10.1"}'
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["Note"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Note"], NetAppResponse]:
        r"""Creates a note associated with the cluster.
An example of creating a row:
curl -v -k -u admin -X POST https://10.234.45.17/api/private/cluster/notes -d '{"name":"ta","value":"argh"}'
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
        records: Iterable["Note"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a cluter note.
Example of deleting a row:
curl -k -u admin -X DELETE https://10.234.45.17/api/private/cluster/notes/342a6fae-02dc-11e9-8b27-00505678833/ta
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the notes associated with the cluster. Notes are small
opaque pieces of meta-data used by administrators or
management applications for capturing hints or preferences.
An example is: curl -k -u admin -X GET https://10.234.45.17/api/private/cluster/notes
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific cluster note.
An example request: curl -k -u admin -X GET https://10.234.45.17/api/private/cluster/notes/342a6fae-02dc-11e9-8b27-005056a7833/ta
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
        r"""Creates a note associated with the cluster.
An example of creating a row:
curl -v -k -u admin -X POST https://10.234.45.17/api/private/cluster/notes -d '{"name":"ta","value":"argh"}'
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="note create")
        async def note_create(
        ) -> ResourceTable:
            """Create an instance of a Note resource

            Args:
                client_secret: Encrypted value that is only visible to user that created it.
                modified_from: 
                modified_time: 
                name: Name or key identifying the note.
                owner: 
                scope: 
                user: User that created the entry.
                value: Opaque data associated with the note.
            """

            kwargs = {}
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if modified_from is not None:
                kwargs["modified_from"] = modified_from
            if modified_time is not None:
                kwargs["modified_time"] = modified_time
            if name is not None:
                kwargs["name"] = name
            if owner is not None:
                kwargs["owner"] = owner
            if scope is not None:
                kwargs["scope"] = scope
            if user is not None:
                kwargs["user"] = user
            if value is not None:
                kwargs["value"] = value

            resource = Note(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create Note: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a cluster note.
Example of a PATCH request:
curl -k -u admin -X PATCH https://10.234.45.17/api/private/cluster/notes/342a6fae-02dc-11e9-8b27-005056a78833/ta -d '{"value":"172.120.10.1"}'
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="note modify")
        async def note_modify(
        ) -> ResourceTable:
            """Modify an instance of a Note resource

            Args:
                client_secret: Encrypted value that is only visible to user that created it.
                query_client_secret: Encrypted value that is only visible to user that created it.
                modified_from: 
                query_modified_from: 
                modified_time: 
                query_modified_time: 
                name: Name or key identifying the note.
                query_name: Name or key identifying the note.
                scope: 
                query_scope: 
                user: User that created the entry.
                query_user: User that created the entry.
                value: Opaque data associated with the note.
                query_value: Opaque data associated with the note.
            """

            kwargs = {}
            changes = {}
            if query_client_secret is not None:
                kwargs["client_secret"] = query_client_secret
            if query_modified_from is not None:
                kwargs["modified_from"] = query_modified_from
            if query_modified_time is not None:
                kwargs["modified_time"] = query_modified_time
            if query_name is not None:
                kwargs["name"] = query_name
            if query_scope is not None:
                kwargs["scope"] = query_scope
            if query_user is not None:
                kwargs["user"] = query_user
            if query_value is not None:
                kwargs["value"] = query_value

            if client_secret is not None:
                changes["client_secret"] = client_secret
            if modified_from is not None:
                changes["modified_from"] = modified_from
            if modified_time is not None:
                changes["modified_time"] = modified_time
            if name is not None:
                changes["name"] = name
            if scope is not None:
                changes["scope"] = scope
            if user is not None:
                changes["user"] = user
            if value is not None:
                changes["value"] = value

            if hasattr(Note, "find"):
                resource = Note.find(
                    **kwargs
                )
            else:
                resource = Note()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Note: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a cluter note.
Example of deleting a row:
curl -k -u admin -X DELETE https://10.234.45.17/api/private/cluster/notes/342a6fae-02dc-11e9-8b27-00505678833/ta
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="note delete")
        async def note_delete(
        ) -> None:
            """Delete an instance of a Note resource

            Args:
                client_secret: Encrypted value that is only visible to user that created it.
                modified_from: 
                modified_time: 
                name: Name or key identifying the note.
                scope: 
                user: User that created the entry.
                value: Opaque data associated with the note.
            """

            kwargs = {}
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if modified_from is not None:
                kwargs["modified_from"] = modified_from
            if modified_time is not None:
                kwargs["modified_time"] = modified_time
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if user is not None:
                kwargs["user"] = user
            if value is not None:
                kwargs["value"] = value

            if hasattr(Note, "find"):
                resource = Note.find(
                    **kwargs
                )
            else:
                resource = Note()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete Note: %s" % err)


