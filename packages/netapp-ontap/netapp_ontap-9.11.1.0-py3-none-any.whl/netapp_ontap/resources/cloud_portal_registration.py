r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

This is the cloud portal description.
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


__all__ = ["CloudPortalRegistration", "CloudPortalRegistrationSchema"]
__pdoc__ = {
    "CloudPortalRegistrationSchema.resource": False,
    "CloudPortalRegistrationSchema.opts": False,
    "CloudPortalRegistration.cloud_portal_registration_show": False,
    "CloudPortalRegistration.cloud_portal_registration_create": False,
    "CloudPortalRegistration.cloud_portal_registration_modify": False,
    "CloudPortalRegistration.cloud_portal_registration_delete": False,
}


class CloudPortalRegistrationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CloudPortalRegistration object"""

    http_proxy = fields.Nested("netapp_ontap.models.http_proxy.HttpProxySchema", data_key="http_proxy", unknown=EXCLUDE)
    r""" HTTP Proxy """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the cloud_portal_registration. """

    token = fields.Str(
        data_key="token",
    )
    r""" The token field of the cloud_portal_registration.

Example: 1AcqyS2MAeRsRshCZ5Vgezp9TWUJQ83wg3 """

    @property
    def resource(self):
        return CloudPortalRegistration

    gettable_fields = [
        "http_proxy",
        "ipspace.links",
        "ipspace.name",
        "ipspace.uuid",
        "token",
    ]
    """http_proxy,ipspace.links,ipspace.name,ipspace.uuid,token,"""

    patchable_fields = [
        "http_proxy",
        "ipspace.name",
        "ipspace.uuid",
        "token",
    ]
    """http_proxy,ipspace.name,ipspace.uuid,token,"""

    postable_fields = [
        "http_proxy",
        "ipspace.name",
        "ipspace.uuid",
        "token",
    ]
    """http_proxy,ipspace.name,ipspace.uuid,token,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CloudPortalRegistration.get_collection(fields=field)]
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
            raise NetAppRestError("CloudPortalRegistration modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CloudPortalRegistration(Resource):
    r""" Information for cloud portal registration. """

    _schema = CloudPortalRegistrationSchema
    _path = "/api/cluster/cloud-portals"

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves cloud portals registered to the cluster. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloud portal registration show")
        def cloud_portal_registration_show(
            fields: List[Choices.define(["token", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of CloudPortalRegistration resources

            Args:
                token: 
            """

            kwargs = {}
            if token is not None:
                kwargs["token"] = token
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return CloudPortalRegistration.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all CloudPortalRegistration resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["CloudPortalRegistration"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["CloudPortalRegistration"], NetAppResponse]:
        r"""Registers a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)


    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves cloud portals registered to the cluster. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)


    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Registers a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloud portal registration create")
        async def cloud_portal_registration_create(
        ) -> ResourceTable:
            """Create an instance of a CloudPortalRegistration resource

            Args:
                http_proxy: HTTP Proxy
                ipspace: 
                token: 
            """

            kwargs = {}
            if http_proxy is not None:
                kwargs["http_proxy"] = http_proxy
            if ipspace is not None:
                kwargs["ipspace"] = ipspace
            if token is not None:
                kwargs["token"] = token

            resource = CloudPortalRegistration(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create CloudPortalRegistration: %s" % err)
            return [resource]




