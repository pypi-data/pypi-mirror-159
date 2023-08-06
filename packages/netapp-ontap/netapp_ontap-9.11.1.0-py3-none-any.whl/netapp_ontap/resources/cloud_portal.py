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


__all__ = ["CloudPortal", "CloudPortalSchema"]
__pdoc__ = {
    "CloudPortalSchema.resource": False,
    "CloudPortalSchema.opts": False,
    "CloudPortal.cloud_portal_show": False,
    "CloudPortal.cloud_portal_create": False,
    "CloudPortal.cloud_portal_modify": False,
    "CloudPortal.cloud_portal_delete": False,
}


class CloudPortalSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CloudPortal object"""

    fqdn = fields.Str(
        data_key="fqdn",
    )
    r""" The fqdn field of the cloud_portal.

Example: example.aws.com """

    http_proxy = fields.Nested("netapp_ontap.models.http_proxy.HttpProxySchema", data_key="http_proxy", unknown=EXCLUDE)
    r""" HTTP Proxy """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the cloud_portal. """

    job = fields.Nested("netapp_ontap.models.job_link.JobLinkSchema", data_key="job", unknown=EXCLUDE)
    r""" The job field of the cloud_portal. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['connected', 'disconnected', 'unavailable']),
    )
    r""" State of the portal

Valid choices:

* connected
* disconnected
* unavailable """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the cloud_portal.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return CloudPortal

    gettable_fields = [
        "fqdn",
        "http_proxy",
        "ipspace.links",
        "ipspace.name",
        "ipspace.uuid",
        "job",
        "state",
        "uuid",
    ]
    """fqdn,http_proxy,ipspace.links,ipspace.name,ipspace.uuid,job,state,uuid,"""

    patchable_fields = [
        "http_proxy",
        "ipspace.name",
        "ipspace.uuid",
        "job",
    ]
    """http_proxy,ipspace.name,ipspace.uuid,job,"""

    postable_fields = [
        "http_proxy",
        "ipspace.name",
        "ipspace.uuid",
        "job",
    ]
    """http_proxy,ipspace.name,ipspace.uuid,job,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CloudPortal.get_collection(fields=field)]
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
            raise NetAppRestError("CloudPortal modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CloudPortal(Resource):
    r""" Cloud portal information. """

    _schema = CloudPortalSchema
    _path = "/api/cluster/cloud-portals"
    _keys = ["uuid"]



    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["CloudPortal"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Re-registers a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)


    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["CloudPortal"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Unregisters a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)


    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloud portal show")
        def cloud_portal_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single CloudPortal resource

            Args:
                fqdn: 
                state: State of the portal
                uuid: 
            """

            kwargs = {}
            if fqdn is not None:
                kwargs["fqdn"] = fqdn
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = CloudPortal(
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
        r"""Re-registers a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloud portal modify")
        async def cloud_portal_modify(
        ) -> ResourceTable:
            """Modify an instance of a CloudPortal resource

            Args:
                fqdn: 
                query_fqdn: 
                state: State of the portal
                query_state: State of the portal
                uuid: 
                query_uuid: 
            """

            kwargs = {}
            changes = {}
            if query_fqdn is not None:
                kwargs["fqdn"] = query_fqdn
            if query_state is not None:
                kwargs["state"] = query_state
            if query_uuid is not None:
                kwargs["uuid"] = query_uuid

            if fqdn is not None:
                changes["fqdn"] = fqdn
            if state is not None:
                changes["state"] = state
            if uuid is not None:
                changes["uuid"] = uuid

            if hasattr(CloudPortal, "find"):
                resource = CloudPortal.find(
                    **kwargs
                )
            else:
                resource = CloudPortal()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify CloudPortal: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Unregisters a cloud portal. This is intended for use only by the System Manager.
### Learn more
* [`DOC /cluster/cloud-portals`](#docs-cluster-cluster_cloud-portals)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloud portal delete")
        async def cloud_portal_delete(
        ) -> None:
            """Delete an instance of a CloudPortal resource

            Args:
                fqdn: 
                state: State of the portal
                uuid: 
            """

            kwargs = {}
            if fqdn is not None:
                kwargs["fqdn"] = fqdn
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(CloudPortal, "find"):
                resource = CloudPortal.find(
                    **kwargs
                )
            else:
                resource = CloudPortal()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete CloudPortal: %s" % err)


