r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API manages associations between ONTAP nodes in the cluster with capacity pools.</br>
Associations are originally made when an ONTAP cluster is created if the capacity pools licensing model is used. You can update the associations by using this API. </br>
Also, if a cluster is originally created to use the capacity tiers licensing model, either with purchased licenses or as an evaluation cluster, you can use this API to update the cluster to use the capacity pools licensing model. Before doing so, configure the license manager instance on which the capacity pool licenses are installed that the cluster will be using. This can be done by sending a POST request on the /api/private/cluster/licensing/license-managers path. Because the node serial number is associated with the original capacity tier license, a new node serial number associated with the capacity pool license must be provided for each of the nodes in the cluster. </br>
**Note:** If a node has the High Availability (HA) feature turned on, both of the HA pair nodes must be associated with the same capacity pool. This is so that new leases from a different capacity pool are not required for storage aggregates when they move from one node to the other during a takeover/giveback event. </br>
---
## Examples
### Updating all the nodes to be associated with capacity pools that are currently not associated with the cluster
This example updates the two HA pairs of nodes in a four-node cluster to be associated with capacity pools that are currently not associated with the cluster. The license_manager field is omitted in the request, because the licenses of the new capacity pools are installed on the default license manager instance.
####
```JSON
# API
POST /api/private/cluster/licensing/capacity-pools
# JSON Body
{
  "records" : [
    {
      "serial_number":"390000200",
      "nodes":[
        {
          "node":{
            "name":"node-1"
          }
        },
        {
          "node":{
            "name":"node-2"
          }
        }
      ]
    },
    {
      "serial_number":"390000201",
      "nodes":[
        {
          "node":{
            "name":"node-3"
          }
        },
        {
          "node":{
            "name":"node-4"
          }
        }
      ]
    }
  ]
}
# Response
202 Accepted
```
### Updating HA pair nodes to be associated with capacity pool that is currently associated with the other HA pair nodes
This example updates one HA pair of nodes in a four-node cluster to be associated with capacity pool that is currently associated with the other HA pair. Once complete, all of the nodes in the cluster will be associated with the capacity pool whose license serial number is 390000100.
####
```JSON
# API
PATCH /api/private/cluster/licensing/capacity-pools/390000100
# JSON Body
{
  "nodes":[
    {
      "node":{
        "name":"node-3"
      }
    },
    {
      "node":{
        "name":"node-4"
      }
    }
  ]
}
# Response
202 Accepted
```
### Updating a four-node cluster from capacity tiers licensing to pools licensing
This example updates a four-node cluster that is currently using the capacity tiers licensing model to the capacity pools licensing. All of the nodes are assigned to a single capacity pool.
First, configure the license manager instance on which the capacity pool license is installed:
####
```JSON
# API
POST /api/private/cluster/licensing/license-managers
# JSON Body
{
  "uri": {
    "host":"10.1.1.1"
  }
}
# Response
202 Accepted
```
Then, make a request to convert the cluster from capacity tiers licensing to pools licensing:
####
```JSON
# API
POST /api/private/cluster/licensing/capacity-pools
# JSON Body
{
  "serial_number":"390000300",
  "nodes":[
    {
      "node":{
        "name":"node-1"
      },
      "new_node_serial_number":"99939000030000000001"
    },
    {
      "node":{
        "name":"node-2"
      },
      "new_node_serial_number":"99939000030000000002"
    },
    {
      "node":{
        "name":"node-3"
      },
      "new_node_serial_number":"99939000030000000003"
    },
    {
      "node":{
        "name":"node-4"
      },
      "new_node_serial_number":"99939000030000000004"
    }
  ]
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


__all__ = ["CapacityPoolWithOptionalNodeSerials", "CapacityPoolWithOptionalNodeSerialsSchema"]
__pdoc__ = {
    "CapacityPoolWithOptionalNodeSerialsSchema.resource": False,
    "CapacityPoolWithOptionalNodeSerialsSchema.opts": False,
    "CapacityPoolWithOptionalNodeSerials.capacity_pool_with_optional_node_serials_show": False,
    "CapacityPoolWithOptionalNodeSerials.capacity_pool_with_optional_node_serials_create": False,
    "CapacityPoolWithOptionalNodeSerials.capacity_pool_with_optional_node_serials_modify": False,
    "CapacityPoolWithOptionalNodeSerials.capacity_pool_with_optional_node_serials_delete": False,
}


class CapacityPoolWithOptionalNodeSerialsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CapacityPoolWithOptionalNodeSerials object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the capacity_pool_with_optional_node_serials. """

    license_manager = fields.Nested("netapp_ontap.resources.license_manager.LicenseManagerSchema", data_key="license_manager", unknown=EXCLUDE)
    r""" The license_manager field of the capacity_pool_with_optional_node_serials. """

    nodes = fields.List(fields.Nested("netapp_ontap.models.capacity_pool_node_with_optional_new_serial.CapacityPoolNodeWithOptionalNewSerialSchema", unknown=EXCLUDE), data_key="nodes")
    r""" Nodes in the cluster associated with this capacity pool. """

    records = fields.List(fields.Nested("netapp_ontap.models.capacity_pool_with_optional_node_serials_no_records.CapacityPoolWithOptionalNodeSerialsNoRecordsSchema", unknown=EXCLUDE), data_key="records")
    r""" An array of capacity pools specified to add multiple capacity pools in a single API call. Valid in POST only. """

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" Serial number of the capacity pool license.

Example: 390000100 """

    @property
    def resource(self):
        return CapacityPoolWithOptionalNodeSerials

    gettable_fields = [
        "links",
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "serial_number",
    ]
    """links,license_manager.links,license_manager.uuid,nodes,serial_number,"""

    patchable_fields = [
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "serial_number",
    ]
    """license_manager.links,license_manager.uuid,nodes,serial_number,"""

    postable_fields = [
        "license_manager.links",
        "license_manager.uuid",
        "nodes",
        "records",
        "serial_number",
    ]
    """license_manager.links,license_manager.uuid,nodes,records,serial_number,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in CapacityPoolWithOptionalNodeSerials.get_collection(fields=field)]
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
            raise NetAppRestError("CapacityPoolWithOptionalNodeSerials modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class CapacityPoolWithOptionalNodeSerials(Resource):
    r""" A capacity pool license to which to reassign nodes. When reassigning nodes as part of converting from capacity tiers licensing, a new node serial number must be provided for each node being converted. """

    _schema = CapacityPoolWithOptionalNodeSerialsSchema
    _path = "/api/private/cluster/licensing/capacity-pools"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["CapacityPoolWithOptionalNodeSerials"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["CapacityPoolWithOptionalNodeSerials"], NetAppResponse]:
        r"""Assigns nodes in the cluster to new capacity pools.
### Learn more
* [`DOC /private/cluster/licensing/capacity-pools`](#docs-cluster-private_cluster_licensing_capacity-pools)
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
        r"""Assigns nodes in the cluster to new capacity pools.
### Learn more
* [`DOC /private/cluster/licensing/capacity-pools`](#docs-cluster-private_cluster_licensing_capacity-pools)
* [`DOC /private/cluster/licensing/license-managers`](#docs-cluster-private_cluster_licensing_license-managers)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="capacity pool with optional node serials create")
        async def capacity_pool_with_optional_node_serials_create(
        ) -> ResourceTable:
            """Create an instance of a CapacityPoolWithOptionalNodeSerials resource

            Args:
                links: 
                license_manager: 
                nodes: Nodes in the cluster associated with this capacity pool.
                records: An array of capacity pools specified to add multiple capacity pools in a single API call. Valid in POST only. 
                serial_number: Serial number of the capacity pool license.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if license_manager is not None:
                kwargs["license_manager"] = license_manager
            if nodes is not None:
                kwargs["nodes"] = nodes
            if records is not None:
                kwargs["records"] = records
            if serial_number is not None:
                kwargs["serial_number"] = serial_number

            resource = CapacityPoolWithOptionalNodeSerials(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create CapacityPoolWithOptionalNodeSerials: %s" % err)
            return [resource]




