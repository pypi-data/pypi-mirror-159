r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API can be used to display hosts belonging to the specified netgroup.
While this endpoint provides supportability, it is not recommended for use since a netgroup can have 1000s of hosts.
### Important information

* Use the "count" property to determine the total number of hosts belonging to the specified netgroup.
* Only the first 100 hosts belonging to the netgroup are retrieved.
## Retrieving netgroup information
You can use the netgroup GET endpoint to retrieve netgroup host configurations for data SVMs.
## Examples
### Retrieving hosts belonging to the specific netgroup and SVM
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Netgroup

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Netgroup(
        name="netgroup1", **{"svm.uuid": "25b363a6-2971-11eb-88e1-0050568eefd4"}
    )
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
Netgroup(
    {
        "svm": {"uuid": "25b363a6-2971-11eb-88e1-0050568eefd4", "name": "vs1"},
        "name": "netgroup1",
        "hosts": [
            "host1.netapp.com",
            "host2.netapp.com",
            "host3.netapp.com",
            "host4.netapp.com",
            "host5.netapp.com",
        ],
        "count": 5,
        "status": "Success",
        "source": "nis",
    }
)

```
</div>
</div>

---
### Retrieving hosts belonging to the specific netgroup and SVM with partial results
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Netgroup

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Netgroup(
        name="netgroup2", **{"svm.uuid": "25b363a6-2971-11eb-88e1-0050568eefd4"}
    )
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
Netgroup(
    {
        "svm": {"uuid": "25b363a6-2971-11eb-88e1-0050568eefd4", "name": "vs1"},
        "name": "netgroup2",
        "hosts": ["host-pc.netapp.com", "host-ng.netapp.com", "host-nb.netapp.com"],
        "count": 3,
        "status": "Partial: Error processing netgroup file /etc/netgroup: Nesting levels greater than 1000 are not supported.",
        "source": "files",
    }
)

```
</div>
</div>

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


__all__ = ["Netgroup", "NetgroupSchema"]
__pdoc__ = {
    "NetgroupSchema.resource": False,
    "NetgroupSchema.opts": False,
    "Netgroup.netgroup_show": False,
    "Netgroup.netgroup_create": False,
    "Netgroup.netgroup_modify": False,
    "Netgroup.netgroup_delete": False,
}


class NetgroupSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Netgroup object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the netgroup. """

    count = Size(
        data_key="count",
    )
    r""" Number of hosts belonging to the specified netgroup. """

    hosts = fields.List(fields.Str, data_key="hosts")
    r""" Name of host belonging to the specified netgroup. """

    name = fields.Str(
        data_key="name",
    )
    r""" Netgroup name.


Example: netgroup1 """

    source = fields.Str(
        data_key="source",
        validate=enum_validation(['unknown', 'files', 'nis', 'ldap']),
    )
    r""" Source used for netgroup lookup.


Valid choices:

* unknown
* files
* nis
* ldap """

    status = fields.Str(
        data_key="status",
    )
    r""" Status of netgroup hosts retrieval.


Example: success """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the netgroup. """

    @property
    def resource(self):
        return Netgroup

    gettable_fields = [
        "links",
        "count",
        "hosts",
        "name",
        "source",
        "status",
        "svm.links",
        "svm.name",
        "svm.uuid",
    ]
    """links,count,hosts,name,source,status,svm.links,svm.name,svm.uuid,"""

    patchable_fields = [
        "name",
        "svm.name",
        "svm.uuid",
    ]
    """name,svm.name,svm.uuid,"""

    postable_fields = [
        "name",
        "svm.name",
        "svm.uuid",
    ]
    """name,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Netgroup.get_collection(fields=field)]
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
            raise NetAppRestError("Netgroup modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Netgroup(Resource):
    """Allows interaction with Netgroup objects on the host"""

    _schema = NetgroupSchema
    _path = "/api/name-services/netgroups"
    _keys = ["svm.uuid", "name"]







    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves all hosts belonging to the specified netgroup.
### Learn more
* [`DOC /name-services/netgroups/{svm.uuid}/{name}`](#docs-name-services-name-services_netgroups_{svm.uuid}_{name})
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="netgroup show")
        def netgroup_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single Netgroup resource

            Args:
                count: Number of hosts belonging to the specified netgroup. 
                hosts: Name of host belonging to the specified netgroup. 
                name: Netgroup name. 
                source: Source used for netgroup lookup. 
                status: Status of netgroup hosts retrieval. 
            """

            kwargs = {}
            if count is not None:
                kwargs["count"] = count
            if hosts is not None:
                kwargs["hosts"] = hosts
            if name is not None:
                kwargs["name"] = name
            if source is not None:
                kwargs["source"] = source
            if status is not None:
                kwargs["status"] = status
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = Netgroup(
                **kwargs
            )
            resource.get()
            return [resource]





