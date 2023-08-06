r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
Cluster-wide options for the internet protocol.
The following operations are supported:

* Get: GET network/ip/options
* Patch: PATCH network/ip/options
## Retrieving the internet protocol options
The network ip options API retrieves and displays the names and values for the options that affect the behaviour of the internet protocol.
The values of these options are applied to all of the nodes in the cluster.
## Examples
## Retrieving values for all cluster-wide internet protocol options
The following output shows the cluster-wide options for the internet protocol.
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import NetworkIpOptions

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = NetworkIpOptions()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
NetworkIpOptions(
    {
        "multipath_routing": {"enabled": False},
        "_links": {"self": {"href": "/api/network/ip/options"}},
    }
)

```
</div>
</div>

---
## Modifying the values for the cluster-wide internet protocol options
The following output shows how to modify the values for the cluster-wide internet protocol option for multipath-routing.
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import NetworkIpOptions

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = NetworkIpOptions()
    resource.multipath_routing.enabled = True
    resource.patch()

```

---
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


__all__ = ["NetworkIpOptions", "NetworkIpOptionsSchema"]
__pdoc__ = {
    "NetworkIpOptionsSchema.resource": False,
    "NetworkIpOptionsSchema.opts": False,
    "NetworkIpOptions.network_ip_options_show": False,
    "NetworkIpOptions.network_ip_options_create": False,
    "NetworkIpOptions.network_ip_options_modify": False,
    "NetworkIpOptions.network_ip_options_delete": False,
}


class NetworkIpOptionsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the NetworkIpOptions object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the network_ip_options. """

    multipath_routing = fields.Nested("netapp_ontap.models.network_ip_options_multipath_routing.NetworkIpOptionsMultipathRoutingSchema", data_key="multipath_routing", unknown=EXCLUDE)
    r""" The multipath_routing field of the network_ip_options. """

    @property
    def resource(self):
        return NetworkIpOptions

    gettable_fields = [
        "links",
        "multipath_routing",
    ]
    """links,multipath_routing,"""

    patchable_fields = [
        "multipath_routing",
    ]
    """multipath_routing,"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in NetworkIpOptions.get_collection(fields=field)]
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
            raise NetAppRestError("NetworkIpOptions modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class NetworkIpOptions(Resource):
    """Allows interaction with NetworkIpOptions objects on the host"""

    _schema = NetworkIpOptionsSchema
    _path = "/api/network/ip/options"







    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves the internet protocol options.
### Related ONTAP commands
* `network options multipath-routing show`

### Learn more
* [`DOC /network/ip/options`](#docs-networking-network_ip_options)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="network ip options show")
        def network_ip_options_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single NetworkIpOptions resource

            Args:
            """

            kwargs = {}
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = NetworkIpOptions(
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
        r"""Modifies the internet protocol options.

### Learn more
* [`DOC /network/ip/options`](#docs-networking-network_ip_options)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="network ip options modify")
        async def network_ip_options_modify(
        ) -> ResourceTable:
            """Modify an instance of a NetworkIpOptions resource

            Args:
            """

            kwargs = {}
            changes = {}


            if hasattr(NetworkIpOptions, "find"):
                resource = NetworkIpOptions.find(
                    **kwargs
                )
            else:
                resource = NetworkIpOptions()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify NetworkIpOptions: %s" % err)



