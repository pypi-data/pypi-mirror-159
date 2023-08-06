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


__all__ = ["UsageList", "UsageListSchema"]
__pdoc__ = {
    "UsageListSchema.resource": False,
    "UsageListSchema.opts": False,
    "UsageList.usage_list_show": False,
    "UsageList.usage_list_create": False,
    "UsageList.usage_list_modify": False,
    "UsageList.usage_list_delete": False,
}


class UsageListSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the UsageList object"""

    records = fields.List(fields.Nested("netapp_ontap.models.usage.UsageSchema", unknown=EXCLUDE), data_key="records")
    r""" The records field of the usage_list. """

    @property
    def resource(self):
        return UsageList

    gettable_fields = [
        "records",
    ]
    """records,"""

    patchable_fields = [
        "records",
    ]
    """records,"""

    postable_fields = [
        "records",
    ]
    """records,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in UsageList.get_collection(fields=field)]
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
            raise NetAppRestError("UsageList modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class UsageList(Resource):
    """Allows interaction with UsageList objects on the host"""

    _schema = UsageListSchema
    _path = "/api/private/cluster/usage"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["UsageList"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["UsageList"], NetAppResponse]:
        r"""Records incremental usage of a particular instrumention point.
Example POST:
curl -k -u admin -X POST  https://10.234.45.17/api/private/cluster/usage -d '{ "records": [ { "name":"hi.there.folks","count":100,"milliseconds":100} ] }'
"""
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
        r"""Records incremental usage of a particular instrumention point.
Example POST:
curl -k -u admin -X POST  https://10.234.45.17/api/private/cluster/usage -d '{ "records": [ { "name":"hi.there.folks","count":100,"milliseconds":100} ] }'
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="usage list create")
        async def usage_list_create(
        ) -> ResourceTable:
            """Create an instance of a UsageList resource

            Args:
                records: 
            """

            kwargs = {}
            if records is not None:
                kwargs["records"] = records

            resource = UsageList(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create UsageList: %s" % err)
            return [resource]




