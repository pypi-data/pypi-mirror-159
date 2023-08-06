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


__all__ = ["HostEms", "HostEmsSchema"]
__pdoc__ = {
    "HostEmsSchema.resource": False,
    "HostEmsSchema.opts": False,
    "HostEms.host_ems_show": False,
    "HostEms.host_ems_create": False,
    "HostEms.host_ems_modify": False,
    "HostEms.host_ems_delete": False,
}


class HostEmsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the HostEms object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the host_ems. """

    endpoint_uuid = fields.Str(
        data_key="endpoint_uuid",
    )
    r""" UUID of the endpoint for which this error is being reported. """

    error_endpoint = fields.Str(
        data_key="error_endpoint",
        validate=enum_validation(['application', 'application_component', 'host']),
    )
    r""" The endpoint for which this error is being reported.

Valid choices:

* application
* application_component
* host """

    error_message = fields.Str(
        data_key="error_message",
    )
    r""" Default message reported on the host. """

    error_number = Size(
        data_key="error_number",
    )
    r""" Default number reported on the host. """

    software_product = fields.Str(
        data_key="software_product",
        validate=enum_validation(['MAX_Data']),
    )
    r""" The software product that is reporting this error to the system.

Valid choices:

* MAX_Data """

    @property
    def resource(self):
        return HostEms

    gettable_fields = [
        "links",
        "endpoint_uuid",
        "error_endpoint",
        "error_message",
        "error_number",
        "software_product",
        "uuid",
    ]
    """links,endpoint_uuid,error_endpoint,error_message,error_number,software_product,uuid,"""

    patchable_fields = [
        "endpoint_uuid",
        "error_endpoint",
        "error_message",
        "error_number",
        "software_product",
        "uuid",
    ]
    """endpoint_uuid,error_endpoint,error_message,error_number,software_product,uuid,"""

    postable_fields = [
        "endpoint_uuid",
        "error_endpoint",
        "error_message",
        "error_number",
        "software_product",
        "uuid",
    ]
    """endpoint_uuid,error_endpoint,error_message,error_number,software_product,uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in HostEms.get_collection(fields=field)]
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
            raise NetAppRestError("HostEms modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class HostEms(Resource):
    """Allows interaction with HostEms objects on the host"""

    _schema = HostEmsSchema
    _path = "/api/host/hosts/{uuid}/report"
    _keys = ["uuid"]




    @classmethod
    def post_collection(
        cls,
        records: Iterable["HostEms"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["HostEms"], NetAppResponse]:
        r"""## Overview
Reports a host side error. The system generates an EMS alert for this error. Errors may be reported for the host, for a particular application running on the host, or for an application component.
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
        r"""## Overview
Reports a host side error. The system generates an EMS alert for this error. Errors may be reported for the host, for a particular application running on the host, or for an application component.
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="host ems create")
        async def host_ems_create(
            uuid,
            links: dict = None,
            endpoint_uuid: str = None,
            error_endpoint: str = None,
            error_message: str = None,
            error_number: Size = None,
            software_product: str = None,
        ) -> ResourceTable:
            """Create an instance of a HostEms resource

            Args:
                links: 
                endpoint_uuid: UUID of the endpoint for which this error is being reported.
                error_endpoint: The endpoint for which this error is being reported.
                error_message: Default message reported on the host.
                error_number: Default number reported on the host.
                software_product: The software product that is reporting this error to the system.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if endpoint_uuid is not None:
                kwargs["endpoint_uuid"] = endpoint_uuid
            if error_endpoint is not None:
                kwargs["error_endpoint"] = error_endpoint
            if error_message is not None:
                kwargs["error_message"] = error_message
            if error_number is not None:
                kwargs["error_number"] = error_number
            if software_product is not None:
                kwargs["software_product"] = software_product

            resource = HostEms(
                uuid,
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create HostEms: %s" % err)
            return [resource]




