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


__all__ = ["XcNode", "XcNodeSchema"]
__pdoc__ = {
    "XcNodeSchema.resource": False,
    "XcNodeSchema.opts": False,
    "XcNode.xc_node_show": False,
    "XcNode.xc_node_create": False,
    "XcNode.xc_node_modify": False,
    "XcNode.xc_node_delete": False,
}


class XcNodeSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcNode object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_node. """

    cluster_interface = fields.Nested("netapp_ontap.models.cluster_nodes_cluster_interface.ClusterNodesClusterInterfaceSchema", data_key="cluster_interface", unknown=EXCLUDE)
    r""" The cluster_interface field of the xc_node. """

    cluster_interfaces = fields.List(fields.Nested("netapp_ontap.models.xc_cluster_nodes_management_interfaces.XcClusterNodesManagementInterfacesSchema", unknown=EXCLUDE), data_key="cluster_interfaces")
    r""" The cluster_interfaces field of the xc_node. """

    controller = fields.Nested("netapp_ontap.models.cluster_nodes_controller.ClusterNodesControllerSchema", data_key="controller", unknown=EXCLUDE)
    r""" The controller field of the xc_node. """

    date = ImpreciseDateTime(
        data_key="date",
    )
    r""" The current or "wall clock" time of the node in ISO-8601 date, time, and time zone format.
The ISO-8601 date and time are localized based on the ONTAP cluster's timezone setting.


Example: 2019-04-17T11:49:26-04:00 """

    external_cache = fields.Nested("netapp_ontap.models.cluster_nodes_external_cache.ClusterNodesExternalCacheSchema", data_key="external_cache", unknown=EXCLUDE)
    r""" The external_cache field of the xc_node. """

    ha = fields.Nested("netapp_ontap.models.xc_node_ha.XcNodeHaSchema", data_key="ha", unknown=EXCLUDE)
    r""" The ha field of the xc_node. """

    hw_assist = fields.Nested("netapp_ontap.models.hw_assist.HwAssistSchema", data_key="hw_assist", unknown=EXCLUDE)
    r""" The hw_assist field of the xc_node. """

    is_all_flash_optimized = fields.Boolean(
        data_key="is_all_flash_optimized",
    )
    r""" Specifies whether the node is all flash optimized. """

    is_all_flash_select_optimized = fields.Boolean(
        data_key="is_all_flash_select_optimized",
    )
    r""" Specifies whether the node is all flash select optimized. """

    is_capacity_optimized = fields.Boolean(
        data_key="is_capacity_optimized",
    )
    r""" Specifies whether the node is capacity optimized. """

    is_performance_optimized = fields.Boolean(
        data_key="is_performance_optimized",
    )
    r""" Specifies whether the node is performance optimized. """

    is_spares_low = fields.Boolean(
        data_key="is_spares_low",
    )
    r""" Specifies whether or not the node is in spares low condition. """

    location = fields.Str(
        data_key="location",
    )
    r""" The location field of the xc_node.

Example: rack 2 row 5 """

    management_interface = fields.Nested("netapp_ontap.models.cluster_nodes_management_interface.ClusterNodesManagementInterfaceSchema", data_key="management_interface", unknown=EXCLUDE)
    r""" The management_interface field of the xc_node. """

    management_interfaces = fields.List(fields.Nested("netapp_ontap.models.xc_cluster_nodes_management_interfaces.XcClusterNodesManagementInterfacesSchema", unknown=EXCLUDE), data_key="management_interfaces")
    r""" The management_interfaces field of the xc_node. """

    membership = fields.Str(
        data_key="membership",
        validate=enum_validation(['available', 'joining', 'member']),
    )
    r""" Possible values:

* <i>available</i> - A node is detected on the internal cluster network and can be added to the cluster.  Nodes that have a membership of "available" are not returned when a GET request is called when the cluster exists. Provide a query on the "membership" property for <i>available</i> to scan for nodes on the cluster network. Nodes that have a membership of "available" are returned automatically before a cluster is created.
* <i>joining</i> - Joining nodes are in the process of being added to the cluster. The node might be progressing through the steps to become a member or might have failed. The job to add the node or create the cluster provides details on the current progress of the node.
* <i>member</i> - Nodes that are members have successfully joined the cluster.


Valid choices:

* available
* joining
* member """

    metric = fields.Nested("netapp_ontap.resources.node_metrics.NodeMetricsSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_node. """

    metrocluster = fields.Nested("netapp_ontap.models.cluster_nodes_metrocluster.ClusterNodesMetroclusterSchema", data_key="metrocluster", unknown=EXCLUDE)
    r""" The metrocluster field of the xc_node. """

    model = fields.Str(
        data_key="model",
    )
    r""" The model field of the xc_node.

Example: FAS3070 """

    name = fields.Str(
        data_key="name",
    )
    r""" The name field of the xc_node.

Example: node-01 """

    nvram = fields.Nested("netapp_ontap.models.cluster_nodes_nvram.ClusterNodesNvramSchema", data_key="nvram", unknown=EXCLUDE)
    r""" The nvram field of the xc_node. """

    owner = fields.Str(
        data_key="owner",
    )
    r""" Owner of the node.

Example: Example Corp """

    serial_number = fields.Str(
        data_key="serial_number",
    )
    r""" The serial_number field of the xc_node.

Example: 4048820-60-9 """

    service_processor = fields.Nested("netapp_ontap.models.service_processor.ServiceProcessorSchema", data_key="service_processor", unknown=EXCLUDE)
    r""" The service_processor field of the xc_node. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['up', 'booting', 'down', 'taken_over', 'waiting_for_giveback', 'degraded', 'unknown']),
    )
    r""" State of the node:

* <i>up</i> - Node is up and operational.
* <i>booting</i> - Node is booting up.
* <i>down</i> - Node has stopped or is dumping core.
* <i>taken_over</i> - Node has been taken over by its HA partner and is not yet waiting for giveback.
* <i>waiting_for_giveback</i> - Node has been taken over by its HA partner and is waiting for the HA partner to giveback disks.
* <i>degraded</i> - Node has one or more critical services offline.
* <i>unknown</i> - Node or its HA partner cannot be contacted and there is no information on the node's state.


Valid choices:

* up
* booting
* down
* taken_over
* waiting_for_giveback
* degraded
* unknown """

    statistics = fields.Nested("netapp_ontap.models.node_statistics.NodeStatisticsSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_node. """

    storage_configuration = fields.Str(
        data_key="storage_configuration",
        validate=enum_validation(['unknown', 'single_path', 'multi_path', 'mixed_path', 'quad_path', 'single_path_ha', 'multi_path_ha', 'mixed_path_ha', 'quad_path_ha']),
    )
    r""" The storage configuration in the system. Possible values:

* <i>mixed_path</i>
* <i>single_path</i>
* <i>multi_path</i>
* <i>quad_path</i>
* <i>mixed_path_ha</i>
* <i>single_path_ha</i>
* <i>multi_path_ha</i>
* <i>quad_path_ha</i>
* <i>unknown</i>


Valid choices:

* unknown
* single_path
* multi_path
* mixed_path
* quad_path
* single_path_ha
* multi_path_ha
* mixed_path_ha
* quad_path_ha """

    system_id = fields.Str(
        data_key="system_id",
    )
    r""" The system_id field of the xc_node.

Example: 0537035403 """

    system_machine_type = fields.Str(
        data_key="system_machine_type",
    )
    r""" OEM system machine type.

Example: 7Y56-CTOWW1 """

    uptime = Size(
        data_key="uptime",
    )
    r""" The total time, in seconds, that the node has been up.

Example: 300536 """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_node.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    vendor_serial_number = fields.Str(
        data_key="vendor_serial_number",
    )
    r""" OEM vendor serial number.

Example: 791603000068 """

    version = fields.Nested("netapp_ontap.models.version.VersionSchema", data_key="version", unknown=EXCLUDE)
    r""" The version field of the xc_node. """

    vm = fields.Nested("netapp_ontap.models.cluster_nodes_vm.ClusterNodesVmSchema", data_key="vm", unknown=EXCLUDE)
    r""" The vm field of the xc_node. """

    @property
    def resource(self):
        return XcNode

    gettable_fields = [
        "links",
        "cluster_interfaces.links",
        "cluster_interfaces.ip",
        "cluster_interfaces.name",
        "cluster_interfaces.uuid",
        "controller",
        "date",
        "external_cache",
        "ha",
        "hw_assist",
        "is_all_flash_optimized",
        "is_all_flash_select_optimized",
        "is_capacity_optimized",
        "is_performance_optimized",
        "is_spares_low",
        "location",
        "management_interfaces.links",
        "management_interfaces.ip",
        "management_interfaces.name",
        "management_interfaces.uuid",
        "membership",
        "metric",
        "metrocluster",
        "model",
        "name",
        "nvram",
        "owner",
        "serial_number",
        "service_processor",
        "state",
        "statistics",
        "storage_configuration",
        "system_id",
        "system_machine_type",
        "uptime",
        "uuid",
        "vendor_serial_number",
        "version",
        "vm",
    ]
    """links,cluster_interfaces.links,cluster_interfaces.ip,cluster_interfaces.name,cluster_interfaces.uuid,controller,date,external_cache,ha,hw_assist,is_all_flash_optimized,is_all_flash_select_optimized,is_capacity_optimized,is_performance_optimized,is_spares_low,location,management_interfaces.links,management_interfaces.ip,management_interfaces.name,management_interfaces.uuid,membership,metric,metrocluster,model,name,nvram,owner,serial_number,service_processor,state,statistics,storage_configuration,system_id,system_machine_type,uptime,uuid,vendor_serial_number,version,vm,"""

    patchable_fields = [
        "controller",
        "ha",
        "location",
        "metrocluster",
        "name",
        "nvram",
        "owner",
        "service_processor",
        "vm",
    ]
    """controller,ha,location,metrocluster,name,nvram,owner,service_processor,vm,"""

    postable_fields = [
        "cluster_interface",
        "controller",
        "ha",
        "location",
        "management_interface",
        "metrocluster",
        "name",
        "nvram",
        "owner",
        "service_processor",
        "vm",
    ]
    """cluster_interface,controller,ha,location,management_interface,metrocluster,name,nvram,owner,service_processor,vm,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcNode.get_collection(fields=field)]
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
            raise NetAppRestError("XcNode modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcNode(Resource):
    r""" Node clone for cross_cluster. """

    _schema = XcNodeSchema
    _path = "/api/cluster/peers/{peer[uuid]}/cluster/nodes"
    _keys = ["peer.uuid", "uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET cluster"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc node show")
        def xc_node_show(
            peer_uuid,
            date: Choices.define(_get_field_list("date"), cache_choices=True, inexact=True)=None,
            is_all_flash_optimized: Choices.define(_get_field_list("is_all_flash_optimized"), cache_choices=True, inexact=True)=None,
            is_all_flash_select_optimized: Choices.define(_get_field_list("is_all_flash_select_optimized"), cache_choices=True, inexact=True)=None,
            is_capacity_optimized: Choices.define(_get_field_list("is_capacity_optimized"), cache_choices=True, inexact=True)=None,
            is_performance_optimized: Choices.define(_get_field_list("is_performance_optimized"), cache_choices=True, inexact=True)=None,
            is_spares_low: Choices.define(_get_field_list("is_spares_low"), cache_choices=True, inexact=True)=None,
            location: Choices.define(_get_field_list("location"), cache_choices=True, inexact=True)=None,
            membership: Choices.define(_get_field_list("membership"), cache_choices=True, inexact=True)=None,
            model: Choices.define(_get_field_list("model"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            owner: Choices.define(_get_field_list("owner"), cache_choices=True, inexact=True)=None,
            serial_number: Choices.define(_get_field_list("serial_number"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            storage_configuration: Choices.define(_get_field_list("storage_configuration"), cache_choices=True, inexact=True)=None,
            system_id: Choices.define(_get_field_list("system_id"), cache_choices=True, inexact=True)=None,
            system_machine_type: Choices.define(_get_field_list("system_machine_type"), cache_choices=True, inexact=True)=None,
            uptime: Choices.define(_get_field_list("uptime"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            vendor_serial_number: Choices.define(_get_field_list("vendor_serial_number"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["date", "is_all_flash_optimized", "is_all_flash_select_optimized", "is_capacity_optimized", "is_performance_optimized", "is_spares_low", "location", "membership", "model", "name", "owner", "serial_number", "state", "storage_configuration", "system_id", "system_machine_type", "uptime", "uuid", "vendor_serial_number", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcNode resources

            Args:
                date: The current or \"wall clock\" time of the node in ISO-8601 date, time, and time zone format. The ISO-8601 date and time are localized based on the ONTAP cluster's timezone setting. 
                is_all_flash_optimized: Specifies whether the node is all flash optimized.
                is_all_flash_select_optimized: Specifies whether the node is all flash select optimized.
                is_capacity_optimized: Specifies whether the node is capacity optimized.
                is_performance_optimized: Specifies whether the node is performance optimized.
                is_spares_low: Specifies whether or not the node is in spares low condition.
                location: 
                membership: Possible values: * <i>available</i> - A node is detected on the internal cluster network and can be added to the cluster.  Nodes that have a membership of \"available\" are not returned when a GET request is called when the cluster exists. Provide a query on the \"membership\" property for <i>available</i> to scan for nodes on the cluster network. Nodes that have a membership of \"available\" are returned automatically before a cluster is created. * <i>joining</i> - Joining nodes are in the process of being added to the cluster. The node might be progressing through the steps to become a member or might have failed. The job to add the node or create the cluster provides details on the current progress of the node. * <i>member</i> - Nodes that are members have successfully joined the cluster. 
                model: 
                name: 
                owner: Owner of the node.
                serial_number: 
                state: State of the node: * <i>up</i> - Node is up and operational. * <i>booting</i> - Node is booting up. * <i>down</i> - Node has stopped or is dumping core. * <i>taken_over</i> - Node has been taken over by its HA partner and is not yet waiting for giveback. * <i>waiting_for_giveback</i> - Node has been taken over by its HA partner and is waiting for the HA partner to giveback disks. * <i>degraded</i> - Node has one or more critical services offline. * <i>unknown</i> - Node or its HA partner cannot be contacted and there is no information on the node's state. 
                storage_configuration: The storage configuration in the system. Possible values: * <i>mixed_path</i> * <i>single_path</i> * <i>multi_path</i> * <i>quad_path</i> * <i>mixed_path_ha</i> * <i>single_path_ha</i> * <i>multi_path_ha</i> * <i>quad_path_ha</i> * <i>unknown</i> 
                system_id: 
                system_machine_type: OEM system machine type.
                uptime: The total time, in seconds, that the node has been up.
                uuid: 
                vendor_serial_number: OEM vendor serial number.
            """

            kwargs = {}
            if date is not None:
                kwargs["date"] = date
            if is_all_flash_optimized is not None:
                kwargs["is_all_flash_optimized"] = is_all_flash_optimized
            if is_all_flash_select_optimized is not None:
                kwargs["is_all_flash_select_optimized"] = is_all_flash_select_optimized
            if is_capacity_optimized is not None:
                kwargs["is_capacity_optimized"] = is_capacity_optimized
            if is_performance_optimized is not None:
                kwargs["is_performance_optimized"] = is_performance_optimized
            if is_spares_low is not None:
                kwargs["is_spares_low"] = is_spares_low
            if location is not None:
                kwargs["location"] = location
            if membership is not None:
                kwargs["membership"] = membership
            if model is not None:
                kwargs["model"] = model
            if name is not None:
                kwargs["name"] = name
            if owner is not None:
                kwargs["owner"] = owner
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if state is not None:
                kwargs["state"] = state
            if storage_configuration is not None:
                kwargs["storage_configuration"] = storage_configuration
            if system_id is not None:
                kwargs["system_id"] = system_id
            if system_machine_type is not None:
                kwargs["system_machine_type"] = system_machine_type
            if uptime is not None:
                kwargs["uptime"] = uptime
            if uuid is not None:
                kwargs["uuid"] = uuid
            if vendor_serial_number is not None:
                kwargs["vendor_serial_number"] = vendor_serial_number
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcNode.get_collection(
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
        """Returns a count of all XcNode resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET cluster"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Cross cluster GET cluster"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





