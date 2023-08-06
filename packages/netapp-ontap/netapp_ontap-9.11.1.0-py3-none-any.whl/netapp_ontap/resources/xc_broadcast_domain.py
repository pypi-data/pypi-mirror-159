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


__all__ = ["XcBroadcastDomain", "XcBroadcastDomainSchema"]
__pdoc__ = {
    "XcBroadcastDomainSchema.resource": False,
    "XcBroadcastDomainSchema.opts": False,
    "XcBroadcastDomain.xc_broadcast_domain_show": False,
    "XcBroadcastDomain.xc_broadcast_domain_create": False,
    "XcBroadcastDomain.xc_broadcast_domain_modify": False,
    "XcBroadcastDomain.xc_broadcast_domain_delete": False,
}


class XcBroadcastDomainSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcBroadcastDomain object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_broadcast_domain. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the xc_broadcast_domain. """

    mtu = Size(
        data_key="mtu",
        validate=integer_validation(minimum=68),
    )
    r""" Maximum transmission unit, largest packet size on this network

Example: 1500 """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the broadcast domain, scoped to its IPspace

Example: bd1 """

    ports = fields.List(fields.Nested("netapp_ontap.resources.port.PortSchema", unknown=EXCLUDE), data_key="ports")
    r""" Ports that belong to the broadcast domain """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Broadcast domain UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcBroadcastDomain

    gettable_fields = [
        "links",
        "ipspace.links",
        "ipspace.name",
        "ipspace.uuid",
        "mtu",
        "name",
        "ports.links",
        "ports.name",
        "ports.node",
        "ports.uuid",
        "uuid",
    ]
    """links,ipspace.links,ipspace.name,ipspace.uuid,mtu,name,ports.links,ports.name,ports.node,ports.uuid,uuid,"""

    patchable_fields = [
        "ipspace.name",
        "ipspace.uuid",
        "mtu",
        "name",
    ]
    """ipspace.name,ipspace.uuid,mtu,name,"""

    postable_fields = [
        "ipspace.name",
        "ipspace.uuid",
        "mtu",
        "name",
    ]
    """ipspace.name,ipspace.uuid,mtu,name,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcBroadcastDomain.get_collection(fields=field)]
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
            raise NetAppRestError("XcBroadcastDomain modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcBroadcastDomain(Resource):
    r""" broadcast_domain clone for cluster peer. """

    _schema = XcBroadcastDomainSchema
    _path = "/api/cluster/peers/{peer[uuid]}/network/ethernet/broadcast-domains"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET broadcast-domains"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc broadcast domain show")
        def xc_broadcast_domain_show(
            peer_uuid,
            mtu: Choices.define(_get_field_list("mtu"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["mtu", "name", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcBroadcastDomain resources

            Args:
                mtu: Maximum transmission unit, largest packet size on this network
                name: Name of the broadcast domain, scoped to its IPspace
                uuid: Broadcast domain UUID
            """

            kwargs = {}
            if mtu is not None:
                kwargs["mtu"] = mtu
            if name is not None:
                kwargs["name"] = name
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcBroadcastDomain.get_collection(
                peer_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all XcBroadcastDomain resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET broadcast-domains"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






