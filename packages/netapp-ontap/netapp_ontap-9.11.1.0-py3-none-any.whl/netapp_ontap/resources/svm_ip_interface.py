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


__all__ = ["SvmIpInterface", "SvmIpInterfaceSchema"]
__pdoc__ = {
    "SvmIpInterfaceSchema.resource": False,
    "SvmIpInterfaceSchema.opts": False,
    "SvmIpInterface.svm_ip_interface_show": False,
    "SvmIpInterface.svm_ip_interface_create": False,
    "SvmIpInterface.svm_ip_interface_modify": False,
    "SvmIpInterface.svm_ip_interface_delete": False,
}


class SvmIpInterfaceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SvmIpInterface object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the svm_ip_interface. """

    ddns_enabled = fields.Boolean(
        data_key="ddns_enabled",
    )
    r""" Indicates whether or not dynamic DNS updates are enabled. Defaults to true if the interface supports "data_nfs" or "data_cifs" services, otherwise false. """

    dns_zone = fields.Str(
        data_key="dns_zone",
    )
    r""" Fully qualified DNS zone name

Example: storage.company.com """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The administrative state of the interface. """

    fail_if_subnet_conflicts = fields.Boolean(
        data_key="fail_if_subnet_conflicts",
    )
    r""" This command fails if the specified IP address falls within the address range of a named subnet. Set this value to false to use the specified IP address and to assign the subnet owning that address to the interface. """

    ip = fields.Nested("netapp_ontap.models.ip_info.IpInfoSchema", data_key="ip", unknown=EXCLUDE)
    r""" The ip field of the svm_ip_interface. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the svm_ip_interface. """

    location = fields.Nested("netapp_ontap.models.ip_interface_location.IpInterfaceLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the svm_ip_interface. """

    metric = fields.Nested("netapp_ontap.models.interface_metrics_data.InterfaceMetricsDataSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the svm_ip_interface. """

    name = fields.Str(
        data_key="name",
    )
    r""" Interface name

Example: dataLif1 """

    probe_port = Size(
        data_key="probe_port",
    )
    r""" Probe port for Cloud load balancer

Example: 64001 """

    rdma_protocols = fields.List(fields.Str, data_key="rdma_protocols")
    r""" Supported RDMA offload protocols """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for interfaces owned by an SVM. Otherwise, set to "cluster".

Valid choices:

* svm
* cluster """

    service_policy = fields.Nested("netapp_ontap.resources.ip_service_policy.IpServicePolicySchema", data_key="service_policy", unknown=EXCLUDE)
    r""" The service_policy field of the svm_ip_interface. """

    services = fields.List(fields.Str, data_key="services")
    r""" The services associated with the interface. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'down']),
    )
    r""" The operational state of the interface.

Valid choices:

* up
* down """

    statistics = fields.Nested("netapp_ontap.models.interface_statistics.InterfaceStatisticsSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the svm_ip_interface. """

    subnet = fields.Nested("netapp_ontap.resources.ip_subnet.IpSubnetSchema", data_key="subnet", unknown=EXCLUDE)
    r""" Use this field to allocate an interface address from a subnet. If needed, a default route is created for this subnet. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the svm_ip_interface. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID that uniquely identifies the interface.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    vip = fields.Boolean(
        data_key="vip",
    )
    r""" True for a VIP interface, whose location is announced via BGP. """

    @property
    def resource(self):
        return SvmIpInterface

    gettable_fields = [
        "links",
        "ddns_enabled",
        "dns_zone",
        "enabled",
        "ip",
        "ipspace.links",
        "ipspace.name",
        "ipspace.uuid",
        "location",
        "metric",
        "name",
        "probe_port",
        "rdma_protocols",
        "scope",
        "service_policy.links",
        "service_policy.name",
        "service_policy.uuid",
        "services",
        "state",
        "statistics",
        "subnet.links",
        "subnet.name",
        "subnet.uuid",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
        "vip",
    ]
    """links,ddns_enabled,dns_zone,enabled,ip,ipspace.links,ipspace.name,ipspace.uuid,location,metric,name,probe_port,rdma_protocols,scope,service_policy.links,service_policy.name,service_policy.uuid,services,state,statistics,subnet.links,subnet.name,subnet.uuid,svm.links,svm.name,svm.uuid,uuid,vip,"""

    patchable_fields = [
        "ddns_enabled",
        "dns_zone",
        "enabled",
        "fail_if_subnet_conflicts",
        "ip",
        "location",
        "name",
        "rdma_protocols",
        "service_policy.name",
        "service_policy.uuid",
        "subnet.name",
        "subnet.uuid",
    ]
    """ddns_enabled,dns_zone,enabled,fail_if_subnet_conflicts,ip,location,name,rdma_protocols,service_policy.name,service_policy.uuid,subnet.name,subnet.uuid,"""

    postable_fields = [
        "ddns_enabled",
        "dns_zone",
        "enabled",
        "fail_if_subnet_conflicts",
        "ip",
        "ipspace.name",
        "ipspace.uuid",
        "location",
        "name",
        "probe_port",
        "rdma_protocols",
        "scope",
        "service_policy.name",
        "service_policy.uuid",
        "subnet.name",
        "subnet.uuid",
        "svm.name",
        "svm.uuid",
        "vip",
    ]
    """ddns_enabled,dns_zone,enabled,fail_if_subnet_conflicts,ip,ipspace.name,ipspace.uuid,location,name,probe_port,rdma_protocols,scope,service_policy.name,service_policy.uuid,subnet.name,subnet.uuid,svm.name,svm.uuid,vip,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SvmIpInterface.get_collection(fields=field)]
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
            raise NetAppRestError("SvmIpInterface modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SvmIpInterface(Resource):
    r""" ip_interface clone for SVM peer. """

    _schema = SvmIpInterfaceSchema
    _path = "/api/svm/peers/{peer[uuid]}/network/ip/interfaces"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET IP interfaces"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="svm ip interface show")
        def svm_ip_interface_show(
            peer_uuid,
            ddns_enabled: Choices.define(_get_field_list("ddns_enabled"), cache_choices=True, inexact=True)=None,
            dns_zone: Choices.define(_get_field_list("dns_zone"), cache_choices=True, inexact=True)=None,
            enabled: Choices.define(_get_field_list("enabled"), cache_choices=True, inexact=True)=None,
            fail_if_subnet_conflicts: Choices.define(_get_field_list("fail_if_subnet_conflicts"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            probe_port: Choices.define(_get_field_list("probe_port"), cache_choices=True, inexact=True)=None,
            rdma_protocols: Choices.define(_get_field_list("rdma_protocols"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            services: Choices.define(_get_field_list("services"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            vip: Choices.define(_get_field_list("vip"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["ddns_enabled", "dns_zone", "enabled", "fail_if_subnet_conflicts", "name", "probe_port", "rdma_protocols", "scope", "services", "state", "uuid", "vip", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SvmIpInterface resources

            Args:
                ddns_enabled: Indicates whether or not dynamic DNS updates are enabled. Defaults to true if the interface supports \"data_nfs\" or \"data_cifs\" services, otherwise false.
                dns_zone: Fully qualified DNS zone name
                enabled: The administrative state of the interface.
                fail_if_subnet_conflicts: This command fails if the specified IP address falls within the address range of a named subnet. Set this value to false to use the specified IP address and to assign the subnet owning that address to the interface.
                name: Interface name
                probe_port: Probe port for Cloud load balancer
                rdma_protocols: Supported RDMA offload protocols
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                services: The services associated with the interface.
                state: The operational state of the interface.
                uuid: The UUID that uniquely identifies the interface.
                vip: True for a VIP interface, whose location is announced via BGP.
            """

            kwargs = {}
            if ddns_enabled is not None:
                kwargs["ddns_enabled"] = ddns_enabled
            if dns_zone is not None:
                kwargs["dns_zone"] = dns_zone
            if enabled is not None:
                kwargs["enabled"] = enabled
            if fail_if_subnet_conflicts is not None:
                kwargs["fail_if_subnet_conflicts"] = fail_if_subnet_conflicts
            if name is not None:
                kwargs["name"] = name
            if probe_port is not None:
                kwargs["probe_port"] = probe_port
            if rdma_protocols is not None:
                kwargs["rdma_protocols"] = rdma_protocols
            if scope is not None:
                kwargs["scope"] = scope
            if services is not None:
                kwargs["services"] = services
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if vip is not None:
                kwargs["vip"] = vip
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SvmIpInterface.get_collection(
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
        """Returns a count of all SvmIpInterface resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET IP interfaces"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






