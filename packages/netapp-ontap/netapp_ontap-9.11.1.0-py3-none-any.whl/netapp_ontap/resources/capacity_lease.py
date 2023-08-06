r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
A pool-based license, such as capacity pool, is installed on a license manager instance and its entitlement is shared by multiple ONTAP nodes and clusters. Each ONTAP node or cluster needs to acquire a lease, an ephemeral entitlement, to enable and operate the feature and resources that require the license.</br>
A lease is valid for a limited duration, which is configurable on the license manager instance, and is automatically renewed to keep it current as long as the feature is enabled and/or the resource exists. </br>
In case of capacity pools licensing, a capacity lease is required from the associated capacity pool when a data aggregate is created. </br>
---
## Examples
### Retrieving a collection of leases
```JSON
# API
GET /api/cluster/licensing/leases
# Response
200 OK
# JSON Body
{
  "records":[
    {
      "id":"390000100-4ea7a442-86d1-11e0-ae1c-123478563401",
      "serial_number":"390000101"
      "pool":{
        "serial_number":"390000101"
      },
      "aggregate":{
        "uuid":"4ea7a442-86d1-11e0-ae1c-123478563401",
        "name":"node_1_aggr_1"
      },
      "capacity":1099511627776,
      "start_time":"2019-02-02T19:00:00Z",
      "expiry_time":"2019-02-03T19:00:00Z",
      "_links":{
        "self":{
          "href":"/api/cluster/licensing/leases/390000100-4ea7a442-86d1-11e0-ae1c-123478563401"
        }
      }
    },
    {
      "serial_number":"390000102"
      "id":"390000100-4ea7a442-86d1-11e0-ae1c-123478563402",
      "pool":{
        "serial_number":"390000102"
      },
      "aggregate":{
        "uuid":"4ea7a442-86d1-11e0-ae1c-123478563402",
        "name":"node_3_aggr_2"
      },
      "capacity":1099511627776,
      "start_time":"2019-02-02T19:00:00Z",
      "expiry_time":"2019-02-03T19:00:00Z",
      "_links":{
        "self":{
          "href":"/api/cluster/licensing/leases/390000100-4ea7a442-86d1-11e0-ae1c-123478563402"
        }
      }
    }
  ],
  "num_records":2,
  "_links":{
    "self":{
      "href":"/api/cluster/licensing/leases"
    }
  }
}
```
### Retrieving a specific lease
```JSON
# API
GET /api/cluster/licensing/leases/390000100-4ea7a442-86d1-11e0-ae1c-123478563401
# Response
200 OK
# JSON Body
{
  "id":"390000100-4ea7a442-86d1-11e0-ae1c-123478563401",
  "serial_number":"390000101"
  "pool":{
    "serial_number":"390000101"
  },
  "aggregate":{
    "uuid":"4ea7a442-86d1-11e0-ae1c-123478563401",
    "name":"node_1_aggr_1"
  },
  "capacity":1099511627776,
  "start_time":"2019-02-02T19:00:00Z",
  "expiry_time":"2019-02-03T19:00:00Z",
  "_links":{
    "self":{
      "href":"/api/cluster/licensing/leases/390000100/4ea7a442-86d1-11e0-ae1c-123478563401"
    }
  }
}
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


__all__ = ["CapacityLease", "CapacityLeaseSchema"]
__pdoc__ = {
    "CapacityLeaseSchema.resource": False,
    "CapacityLeaseSchema.opts": False,
    "CapacityLease.capacity_lease_show": False,
    "CapacityLease.capacity_lease_create": False,
    "CapacityLease.capacity_lease_modify": False,
    "CapacityLease.capacity_lease_delete": False,
}


class CapacityLeaseSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CapacityLease object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the capacity_lease. """

    aggregate = fields.Nested("netapp_ontap.resources.aggregate.AggregateSchema", data_key="aggregate", unknown=EXCLUDE)
    r""" The aggregate field of the capacity_lease. """

    capacity = Size(
        data_key="capacity",
    )
    r""" Amount of capacity, in bytes, which this lease entitles the storage aggregate to use.


Example: 1099511627776 """

    expiry_time = ImpreciseDateTime(
        data_key="expiry_time",
    )
    r""" Date and time when this lease expires.

Example: 2019-02-02T19:00:00Z """

    id = fields.Str(
        data_key="id",
    )
    r""" Identifier for the lease record.

Example: 390000100-4ea7a442-86d1-11e0-ae1c-112233445566 """

    pool = fields.Nested("netapp_ontap.resources.capacity_pool.CapacityPoolSchema", data_key="pool", unknown=EXCLUDE)
    r""" The pool field of the capacity_lease. """

    start_time = ImpreciseDateTime(
        data_key="start_time",
    )
    r""" Date and time when this lease was acquired.

Example: 2019-02-03T19:00:00Z """

    @property
    def resource(self):
        return CapacityLease

    gettable_fields = [
        "links",
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "capacity",
        "expiry_time",
        "id",
        "pool.links",
        "pool.serial_number",
        "start_time",
    ]
    """links,aggregate.links,aggregate.name,aggregate.uuid,capacity,expiry_time,id,pool.links,pool.serial_number,start_time,"""

    patchable_fields = [
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "pool.links",
        "pool.serial_number",
    ]
    """aggregate.links,aggregate.name,aggregate.uuid,pool.links,pool.serial_number,"""

    postable_fields = [
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "pool.links",
        "pool.serial_number",
    ]
    """aggregate.links,aggregate.name,aggregate.uuid,pool.links,pool.serial_number,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CapacityLease.get_collection(fields=field)]
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
            raise NetAppRestError("CapacityLease modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CapacityLease(Resource):
    r""" An ephemeral entitlement to use a storage aggregate. A lease on storage capacity is automatically renewed as long as the aggregate exists. """

    _schema = CapacityLeaseSchema
    _path = "/api/cluster/licensing/leases"
    _keys = ["id"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a collection of leases.
### Learn more
* [`DOC /cluster/licensing/leases`](#docs-cluster-cluster_licensing_leases)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="capacity lease show")
        def capacity_lease_show(
            fields: List[Choices.define(["capacity", "expiry_time", "id", "start_time", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of CapacityLease resources

            Args:
                capacity: Amount of capacity, in bytes, which this lease entitles the storage aggregate to use. 
                expiry_time: Date and time when this lease expires.
                id: Identifier for the lease record.
                start_time: Date and time when this lease was acquired.
            """

            kwargs = {}
            if capacity is not None:
                kwargs["capacity"] = capacity
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if id is not None:
                kwargs["id"] = id
            if start_time is not None:
                kwargs["start_time"] = start_time
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return CapacityLease.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all CapacityLease resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a collection of leases.
### Learn more
* [`DOC /cluster/licensing/leases`](#docs-cluster-cluster_licensing_leases)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a lease.
### Learn more
* [`DOC /cluster/licensing/leases`](#docs-cluster-cluster_licensing_leases)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





