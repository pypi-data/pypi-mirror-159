r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
Sets configuration parameters required for ONTAP Select cluster expansion.
Expansion depends on the operation-type: Single node to 2-node, single node to 4-node or 2-node to 4-node.<br/>
## Select Pre-expansion APIs
Following API is used to set the configuration parameters:

* POST     /api/private/cluster/select-pre-expansion
## Example
### Setting the parameters for 1 to 2-node cluster expansion
The POST request is used to set the configuration parameters required for 1-node to 2-node cluster expansion.
````python
from netapp_ontap import HostConnection
from netapp_ontap.resources import SelectPreExpansion

with HostConnection("<mgmt-ip", username="admin", password="password", verify=False):
    resource = SelectPreExpansion()
    resource.operation_type = "1to2"
    resource.mediator = {
        "ip": "10.1.2.3",
        "target": "iqn.2012-05.local:mailbox.target.test",
    }
    resource.local_mac = "00:16:3e:1a:16:2d"
    resource.partner = {"mac": "00:16:3e:48:c9:6d", "name": "node2"}
    resource.mtu = "9000"
    resource.post(hydrate=True)
    print(resource)

```
`
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


__all__ = ["SelectPreExpansion", "SelectPreExpansionSchema"]
__pdoc__ = {
    "SelectPreExpansionSchema.resource": False,
    "SelectPreExpansionSchema.opts": False,
    "SelectPreExpansion.select_pre_expansion_show": False,
    "SelectPreExpansion.select_pre_expansion_create": False,
    "SelectPreExpansion.select_pre_expansion_modify": False,
    "SelectPreExpansion.select_pre_expansion_delete": False,
}


class SelectPreExpansionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SelectPreExpansion object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the select_pre_expansion. """

    local_mac = fields.Str(
        data_key="local_mac",
    )
    r""" MAC address of local node. Not applicable for operation_type 2to4.

Example: 00:16:3e:1a:16:2d """

    mediator = fields.Nested("netapp_ontap.models.select_pre_expansion_mediator.SelectPreExpansionMediatorSchema", data_key="mediator", unknown=EXCLUDE)
    r""" The mediator field of the select_pre_expansion. """

    mtu = Size(
        data_key="mtu",
        validate=integer_validation(minimum=7500, maximum=9000),
    )
    r""" Maximum Transmission Unit size for internal network. Not applicable for operation_type 2to4. """

    operation_type = fields.Str(
        data_key="operation_type",
        validate=enum_validation(['1to2', '1to4', '2to4']),
    )
    r""" Type of expansion.

Valid choices:

* 1to2
* 1to4
* 2to4 """

    partner = fields.Nested("netapp_ontap.models.select_pre_expansion_partner.SelectPreExpansionPartnerSchema", data_key="partner", unknown=EXCLUDE)
    r""" The partner field of the select_pre_expansion. """

    @property
    def resource(self):
        return SelectPreExpansion

    gettable_fields = [
        "links",
        "local_mac",
        "mediator",
        "mtu",
        "operation_type",
        "partner",
    ]
    """links,local_mac,mediator,mtu,operation_type,partner,"""

    patchable_fields = [
        "local_mac",
        "mediator",
        "mtu",
        "operation_type",
        "partner",
    ]
    """local_mac,mediator,mtu,operation_type,partner,"""

    postable_fields = [
        "local_mac",
        "mediator",
        "mtu",
        "operation_type",
        "partner",
    ]
    """local_mac,mediator,mtu,operation_type,partner,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SelectPreExpansion.get_collection(fields=field)]
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
            raise NetAppRestError("SelectPreExpansion modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SelectPreExpansion(Resource):
    r""" Configuration parameters for ONTAP Select cluster expansion. """

    _schema = SelectPreExpansionSchema
    _path = "/api/private/cluster/select-pre-expansion"




    @classmethod
    def post_collection(
        cls,
        records: Iterable["SelectPreExpansion"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SelectPreExpansion"], NetAppResponse]:
        r"""Sets the configuration parameters required for expanding an ONTAP Select cluster.
After setting the parameters, deploy automates the workflow of node reconfiguration and node join.

### Learn more
* [`DOC /private/cluster/select-pre-expansion`](#docs-cluster-private_cluster_select-pre-expansion)"""
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
        r"""Sets the configuration parameters required for expanding an ONTAP Select cluster.
After setting the parameters, deploy automates the workflow of node reconfiguration and node join.

### Learn more
* [`DOC /private/cluster/select-pre-expansion`](#docs-cluster-private_cluster_select-pre-expansion)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="select pre expansion create")
        async def select_pre_expansion_create(
        ) -> ResourceTable:
            """Create an instance of a SelectPreExpansion resource

            Args:
                links: 
                local_mac: MAC address of local node. Not applicable for operation_type 2to4.
                mediator: 
                mtu: Maximum Transmission Unit size for internal network. Not applicable for operation_type 2to4.
                operation_type: Type of expansion.
                partner: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if local_mac is not None:
                kwargs["local_mac"] = local_mac
            if mediator is not None:
                kwargs["mediator"] = mediator
            if mtu is not None:
                kwargs["mtu"] = mtu
            if operation_type is not None:
                kwargs["operation_type"] = operation_type
            if partner is not None:
                kwargs["partner"] = partner

            resource = SelectPreExpansion(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SelectPreExpansion: %s" % err)
            return [resource]




