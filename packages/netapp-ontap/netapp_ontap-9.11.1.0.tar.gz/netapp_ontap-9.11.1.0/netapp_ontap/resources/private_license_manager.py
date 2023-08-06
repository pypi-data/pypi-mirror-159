r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
When an ONTAP cluster is initially created to use the capacity pools licensing model, information about the license manager instance that the cluster should use is pre-configured. When converting a capacity tiers cluster to a pools cluster, however, information about the license manager needs to be configured by using this API, since no information about the license manager is pre-configured initially.</br>
This API is designed to support multiple license manager instances, but the system currently only support one license manager instance per cluster.
---
## Examples
### Configuring a new license manager instance
####
```JSON
# API
POST /api/cluster/licensing/licensing-managers
# JSON Body
{
  "uri": {
    "host":"10.1.1.1"
  }
}
# Response
202 Accepted
```
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


__all__ = ["PrivateLicenseManager", "PrivateLicenseManagerSchema"]
__pdoc__ = {
    "PrivateLicenseManagerSchema.resource": False,
    "PrivateLicenseManagerSchema.opts": False,
    "PrivateLicenseManager.private_license_manager_show": False,
    "PrivateLicenseManager.private_license_manager_create": False,
    "PrivateLicenseManager.private_license_manager_modify": False,
    "PrivateLicenseManager.private_license_manager_delete": False,
}


class PrivateLicenseManagerSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the PrivateLicenseManager object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the private_license_manager. """

    default = fields.Boolean(
        data_key="default",
    )
    r""" Flag that indicates whether it's the default license manager instance used by the cluster.'
When a capacity pool is created and if the license manager field is omitted, it is assumed that the license of the capacity pool is installed on the default license manager instance. """

    uri = fields.Nested("netapp_ontap.models.license_manager_uri.LicenseManagerUriSchema", data_key="uri", unknown=EXCLUDE)
    r""" The uri field of the private_license_manager. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the private_license_manager.

Example: 4ea7a442-86d1-11e0-ae1c-112233445566 """

    @property
    def resource(self):
        return PrivateLicenseManager

    gettable_fields = [
        "links",
        "default",
        "uri",
        "uuid",
    ]
    """links,default,uri,uuid,"""

    patchable_fields = [
        "uri",
    ]
    """uri,"""

    postable_fields = [
        "uri",
    ]
    """uri,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in PrivateLicenseManager.get_collection(fields=field)]
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
            raise NetAppRestError("PrivateLicenseManager modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class PrivateLicenseManager(Resource):
    r""" Information on a license manager instance associated with the cluster. """

    _schema = PrivateLicenseManagerSchema
    _path = "/api/private/cluster/licensing/license-managers"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["PrivateLicenseManager"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["PrivateLicenseManager"], NetAppResponse]:
        r"""Configures a new license manager instance.
### Learn more
* [`DOC /private/cluster/licensing/license-managers`](#docs-cluster-private_cluster_licensing_license-managers)
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
        r"""Configures a new license manager instance.
### Learn more
* [`DOC /private/cluster/licensing/license-managers`](#docs-cluster-private_cluster_licensing_license-managers)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="private license manager create")
        async def private_license_manager_create(
        ) -> ResourceTable:
            """Create an instance of a PrivateLicenseManager resource

            Args:
                links: 
                default: Flag that indicates whether it's the default license manager instance used by the cluster.' When a capacity pool is created and if the license manager field is omitted, it is assumed that the license of the capacity pool is installed on the default license manager instance. 
                uri: 
                uuid: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if default is not None:
                kwargs["default"] = default
            if uri is not None:
                kwargs["uri"] = uri
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = PrivateLicenseManager(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create PrivateLicenseManager: %s" % err)
            return [resource]




