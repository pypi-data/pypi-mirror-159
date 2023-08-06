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


__all__ = ["XcCluster", "XcClusterSchema"]
__pdoc__ = {
    "XcClusterSchema.resource": False,
    "XcClusterSchema.opts": False,
    "XcCluster.xc_cluster_show": False,
    "XcCluster.xc_cluster_create": False,
    "XcCluster.xc_cluster_modify": False,
    "XcCluster.xc_cluster_delete": False,
}


class XcClusterSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcCluster object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_cluster. """

    certificate = fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", data_key="certificate", unknown=EXCLUDE)
    r""" The certificate field of the xc_cluster. """

    configuration_backup = fields.Nested("netapp_ontap.resources.configuration_backup.ConfigurationBackupSchema", data_key="configuration_backup", unknown=EXCLUDE)
    r""" The configuration_backup field of the xc_cluster. """

    contact = fields.Str(
        data_key="contact",
    )
    r""" The contact field of the xc_cluster.

Example: support@company.com """

    dns_domains = fields.List(fields.Str, data_key="dns_domains")
    r""" A list of DNS domains.
Domain names have the following requirements:

* The name must contain only the following characters: A through Z, a through z, 0 through 9, ".", "-" or "_".
* The first character of each label, delimited by ".", must be one of the following characters: A through Z or a through z or 0 through 9.
* The last character of each label, delimited by ".", must be one of the following characters: A through Z, a through z, or 0 through 9.
* The top level domain must contain only the following characters: A through Z, a through z.
* The system reserves the following names:"all", "local", and "localhost".


Example: ["example.com","example2.example3.com"] """

    license = fields.Nested("netapp_ontap.models.license_keys.LicenseKeysSchema", data_key="license", unknown=EXCLUDE)
    r""" The license field of the xc_cluster. """

    location = fields.Str(
        data_key="location",
    )
    r""" The location field of the xc_cluster.

Example: building 1 """

    management_interface = fields.Nested("netapp_ontap.models.cluster_management_interface.ClusterManagementInterfaceSchema", data_key="management_interface", unknown=EXCLUDE)
    r""" The management_interface field of the xc_cluster. """

    management_interfaces = fields.List(fields.Nested("netapp_ontap.models.network_route_interfaces.NetworkRouteInterfacesSchema", unknown=EXCLUDE), data_key="management_interfaces")
    r""" The management_interfaces field of the xc_cluster. """

    metric = fields.Nested("netapp_ontap.resources.performance_metric.PerformanceMetricSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_cluster. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the xc_cluster.

Example: cluster1 """

    name_servers = fields.List(fields.Str, data_key="name_servers")
    r""" The list of IP addresses of the DNS servers. Addresses can be either
IPv4 or IPv6 addresses.


Example: ["10.224.65.20","2001:db08:a0b:12f0::1"] """

    nodes = fields.List(fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE), data_key="nodes")
    r""" The nodes field of the xc_cluster. """

    ntp_servers = fields.List(fields.Str, data_key="ntp_servers")
    r""" Host name, IPv4 address, or IPv6 address for the external NTP time servers.

Example: ["time.nist.gov","10.98.19.20","2610:20:6F15:15::27"] """

    password = fields.Str(
        data_key="password",
    )
    r""" Initial admin password used to create the cluster.

Example: mypassword """

    peering_policy = fields.Nested("netapp_ontap.models.cluster_peering_policy.ClusterPeeringPolicySchema", data_key="peering_policy", unknown=EXCLUDE)
    r""" The peering_policy field of the xc_cluster. """

    san_optimized = fields.Boolean(
        data_key="san_optimized",
    )
    r""" Specifies if this cluster is an All SAN Array. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw.PerformanceMetricRawSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_cluster. """

    timezone = fields.Nested("netapp_ontap.models.timezone_cluster.TimezoneClusterSchema", data_key="timezone", unknown=EXCLUDE)
    r""" The timezone field of the xc_cluster. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_cluster.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    version = fields.Nested("netapp_ontap.models.version.VersionSchema", data_key="version", unknown=EXCLUDE)
    r""" The version field of the xc_cluster. """

    @property
    def resource(self):
        return XcCluster

    gettable_fields = [
        "links",
        "certificate.links",
        "certificate.name",
        "certificate.uuid",
        "contact",
        "dns_domains",
        "location",
        "management_interfaces.links",
        "management_interfaces.ip",
        "management_interfaces.name",
        "management_interfaces.uuid",
        "metric",
        "name",
        "name_servers",
        "ntp_servers",
        "peering_policy",
        "san_optimized",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "timezone",
        "uuid",
        "version",
    ]
    """links,certificate.links,certificate.name,certificate.uuid,contact,dns_domains,location,management_interfaces.links,management_interfaces.ip,management_interfaces.name,management_interfaces.uuid,metric,name,name_servers,ntp_servers,peering_policy,san_optimized,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,timezone,uuid,version,"""

    patchable_fields = [
        "certificate.name",
        "certificate.uuid",
        "contact",
        "dns_domains",
        "location",
        "name",
        "name_servers",
        "peering_policy",
        "timezone",
    ]
    """certificate.name,certificate.uuid,contact,dns_domains,location,name,name_servers,peering_policy,timezone,"""

    postable_fields = [
        "configuration_backup",
        "contact",
        "dns_domains",
        "license",
        "location",
        "management_interface",
        "name",
        "name_servers",
        "nodes",
        "ntp_servers",
        "password",
        "peering_policy",
        "timezone",
    ]
    """configuration_backup,contact,dns_domains,license,location,management_interface,name,name_servers,nodes,ntp_servers,password,peering_policy,timezone,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcCluster.get_collection(fields=field)]
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
            raise NetAppRestError("XcCluster modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcCluster(Resource):
    r""" Cluster clone for cross_cluster. """

    _schema = XcClusterSchema
    _path = "/api/cluster/peers/{peer[uuid]}/cluster"
    _keys = ["peer.uuid"]







    def get(self, **kwargs) -> NetAppResponse:
        r"""Cross cluster GET cluster"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc cluster show")
        def xc_cluster_show(
            peer_uuid,
            contact: Choices.define(_get_field_list("contact"), cache_choices=True, inexact=True)=None,
            dns_domains: Choices.define(_get_field_list("dns_domains"), cache_choices=True, inexact=True)=None,
            location: Choices.define(_get_field_list("location"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            name_servers: Choices.define(_get_field_list("name_servers"), cache_choices=True, inexact=True)=None,
            ntp_servers: Choices.define(_get_field_list("ntp_servers"), cache_choices=True, inexact=True)=None,
            password: Choices.define(_get_field_list("password"), cache_choices=True, inexact=True)=None,
            san_optimized: Choices.define(_get_field_list("san_optimized"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single XcCluster resource

            Args:
                contact: 
                dns_domains: A list of DNS domains. Domain names have the following requirements: * The name must contain only the following characters: A through Z,   a through z, 0 through 9, \".\", \"-\" or \"_\". * The first character of each label, delimited by \".\", must be one   of the following characters: A through Z or a through z or 0   through 9. * The last character of each label, delimited by \".\", must be one of   the following characters: A through Z, a through z, or 0 through 9. * The top level domain must contain only the following characters: A   through Z, a through z. * The system reserves the following names:\"all\", \"local\", and \"localhost\". 
                location: 
                name: 
                name_servers: The list of IP addresses of the DNS servers. Addresses can be either IPv4 or IPv6 addresses. 
                ntp_servers: Host name, IPv4 address, or IPv6 address for the external NTP time servers.
                password: Initial admin password used to create the cluster.
                san_optimized: Specifies if this cluster is an All SAN Array.
                uuid: 
            """

            kwargs = {}
            if contact is not None:
                kwargs["contact"] = contact
            if dns_domains is not None:
                kwargs["dns_domains"] = dns_domains
            if location is not None:
                kwargs["location"] = location
            if name is not None:
                kwargs["name"] = name
            if name_servers is not None:
                kwargs["name_servers"] = name_servers
            if ntp_servers is not None:
                kwargs["ntp_servers"] = ntp_servers
            if password is not None:
                kwargs["password"] = password
            if san_optimized is not None:
                kwargs["san_optimized"] = san_optimized
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = XcCluster(
                peer_uuid,
                **kwargs
            )
            resource.get()
            return [resource]





