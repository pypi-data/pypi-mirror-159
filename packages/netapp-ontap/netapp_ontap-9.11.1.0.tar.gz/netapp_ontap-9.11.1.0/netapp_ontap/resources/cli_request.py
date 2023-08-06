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


__all__ = ["CliRequest", "CliRequestSchema"]
__pdoc__ = {
    "CliRequestSchema.resource": False,
    "CliRequestSchema.opts": False,
    "CliRequest.cli_request_show": False,
    "CliRequest.cli_request_create": False,
    "CliRequest.cli_request_modify": False,
    "CliRequest.cli_request_delete": False,
}


class CliRequestSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CliRequest object"""

    error = fields.Nested("netapp_ontap.models.error.ErrorSchema", data_key="error", unknown=EXCLUDE)
    r""" The error field of the cli_request. """

    input = fields.Str(
        data_key="input",
    )
    r""" Input to CLI """

    output = fields.Str(
        data_key="output",
    )
    r""" Full output from CLI """

    privilege = fields.Str(
        data_key="privilege",
        validate=enum_validation(['admin', 'advanced', 'diagnostic']),
    )
    r""" Privilege Level

Valid choices:

* admin
* advanced
* diagnostic """

    @property
    def resource(self):
        return CliRequest

    gettable_fields = [
        "error",
        "output",
    ]
    """error,output,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "input",
        "privilege",
    ]
    """input,privilege,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CliRequest.get_collection(fields=field)]
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
            raise NetAppRestError("CliRequest modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CliRequest(Resource):
    """Allows interaction with CliRequest objects on the host"""

    _schema = CliRequestSchema
    _path = "/api/private/cli"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["CliRequest"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["CliRequest"], NetAppResponse]:
        r"""Execute a CLI command"""
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
        r"""Execute a CLI command"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cli request create")
        async def cli_request_create(
        ) -> ResourceTable:
            """Create an instance of a CliRequest resource

            Args:
                error: 
                input: Input to CLI
                output: Full output from CLI
                privilege: Privilege Level
            """

            kwargs = {}
            if error is not None:
                kwargs["error"] = error
            if input is not None:
                kwargs["input"] = input
            if output is not None:
                kwargs["output"] = output
            if privilege is not None:
                kwargs["privilege"] = privilege

            resource = CliRequest(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create CliRequest: %s" % err)
            return [resource]




