r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

This API will be used by an ISV application for requesting a short-lived access token from the ONTAP cluster.
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


__all__ = ["AccessTokenRequest", "AccessTokenRequestSchema"]
__pdoc__ = {
    "AccessTokenRequestSchema.resource": False,
    "AccessTokenRequestSchema.opts": False,
    "AccessTokenRequest.access_token_request_show": False,
    "AccessTokenRequest.access_token_request_create": False,
    "AccessTokenRequest.access_token_request_modify": False,
    "AccessTokenRequest.access_token_request_delete": False,
}


class AccessTokenRequestSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AccessTokenRequest object"""

    client_id = fields.Str(
        data_key="client_id",
    )
    r""" Name of the ISV application requesting an access token.

Example: XYZ Software """

    client_secret = fields.Str(
        data_key="client_secret",
    )
    r""" Content of the ISV license.

Example: eyJzdGF0dXNSZXNwIjp7InNlcmlhbC1udW1iZXIiOiI0NTEwMDAwMTAiLCJpc3YtbG9uZyuYW1lIjoiVmVlYW0gU29mdHdhcmUiLCJpc3YtbmFtZSI6InZlZWFtIiwic """

    grant_type = fields.Str(
        data_key="grant_type",
        validate=enum_validation(['client_credentials']),
    )
    r""" ISV application grant type.

Valid choices:

* client_credentials """

    @property
    def resource(self):
        return AccessTokenRequest

    gettable_fields = [
    ]
    """"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "client_id",
        "client_secret",
        "grant_type",
    ]
    """client_id,client_secret,grant_type,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in AccessTokenRequest.get_collection(fields=field)]
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
            raise NetAppRestError("AccessTokenRequest modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class AccessTokenRequest(Resource):
    r""" Request an access token. """

    _schema = AccessTokenRequestSchema
    _path = "/api/cluster/licensing/access-tokens"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["AccessTokenRequest"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["AccessTokenRequest"], NetAppResponse]:
        r"""Requests an access token.

### Learn more
* [`DOC /cluster/licensing/access-tokens`](#docs-cluster-cluster_licensing_access-tokens)"""
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
        r"""Requests an access token.

### Learn more
* [`DOC /cluster/licensing/access-tokens`](#docs-cluster-cluster_licensing_access-tokens)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="access token request create")
        async def access_token_request_create(
        ) -> ResourceTable:
            """Create an instance of a AccessTokenRequest resource

            Args:
                client_id: Name of the ISV application requesting an access token.
                client_secret: Content of the ISV license.
                grant_type: ISV application grant type.
            """

            kwargs = {}
            if client_id is not None:
                kwargs["client_id"] = client_id
            if client_secret is not None:
                kwargs["client_secret"] = client_secret
            if grant_type is not None:
                kwargs["grant_type"] = grant_type

            resource = AccessTokenRequest(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create AccessTokenRequest: %s" % err)
            return [resource]




