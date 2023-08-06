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


__all__ = ["XcAggregate", "XcAggregateSchema"]
__pdoc__ = {
    "XcAggregateSchema.resource": False,
    "XcAggregateSchema.opts": False,
    "XcAggregate.xc_aggregate_show": False,
    "XcAggregate.xc_aggregate_create": False,
    "XcAggregate.xc_aggregate_modify": False,
    "XcAggregate.xc_aggregate_delete": False,
}


class XcAggregateSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcAggregate object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_aggregate. """

    block_storage = fields.Nested("netapp_ontap.models.aggregate_block_storage.AggregateBlockStorageSchema", data_key="block_storage", unknown=EXCLUDE)
    r""" The block_storage field of the xc_aggregate. """

    cloud_storage = fields.Nested("netapp_ontap.models.aggregate_cloud_storage.AggregateCloudStorageSchema", data_key="cloud_storage", unknown=EXCLUDE)
    r""" The cloud_storage field of the xc_aggregate. """

    create_time = fields.Str(
        data_key="create_time",
    )
    r""" Timestamp of aggregate creation.

Example: 2018-01-01T12:00:00-04:00 """

    data_encryption = fields.Nested("netapp_ontap.models.aggregate_data_encryption.AggregateDataEncryptionSchema", data_key="data_encryption", unknown=EXCLUDE)
    r""" The data_encryption field of the xc_aggregate. """

    dr_home_node = fields.Nested("netapp_ontap.models.dr_node.DrNodeSchema", data_key="dr_home_node", unknown=EXCLUDE)
    r""" The dr_home_node field of the xc_aggregate. """

    home_node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="home_node", unknown=EXCLUDE)
    r""" The home_node field of the xc_aggregate. """

    inactive_data_reporting = fields.Nested("netapp_ontap.models.aggregate_inactive_data_reporting.AggregateInactiveDataReportingSchema", data_key="inactive_data_reporting", unknown=EXCLUDE)
    r""" The inactive_data_reporting field of the xc_aggregate. """

    inode_attributes = fields.Nested("netapp_ontap.models.aggregate_inode_attributes.AggregateInodeAttributesSchema", data_key="inode_attributes", unknown=EXCLUDE)
    r""" The inode_attributes field of the xc_aggregate. """

    is_spare_low = fields.Boolean(
        data_key="is_spare_low",
    )
    r""" Specifies whether the aggregate is in a spares low condition on any of the RAID groups.
This is an advanced property; there is an added cost to retrieving its value. The field is not populated for either a collection GET or an instance GET unless it is explicitly requested using the <i>fields</i> query parameter containing either footprint or **.


Example: false """

    metric = fields.Nested("netapp_ontap.resources.performance_metric.PerformanceMetricSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_aggregate. """

    name = fields.Str(
        data_key="name",
    )
    r""" Aggregate name.

Example: node1_aggr_1 """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the xc_aggregate. """

    recommendation_spares = fields.List(fields.Nested("netapp_ontap.models.aggregate_spare.AggregateSpareSchema", unknown=EXCLUDE), data_key="recommendation_spares")
    r""" Information on the aggregate's remaining hot spare disks. """

    sidl_enabled = fields.Boolean(
        data_key="sidl_enabled",
    )
    r""" Specifies whether or not SIDL is enabled on the aggregate. """

    snaplock_type = fields.Str(
        data_key="snaplock_type",
        validate=enum_validation(['non_snaplock', 'compliance', 'enterprise']),
    )
    r""" SnapLock type.

Valid choices:

* non_snaplock
* compliance
* enterprise """

    snapshot = fields.Nested("netapp_ontap.models.aggregate_snapshot.AggregateSnapshotSchema", data_key="snapshot", unknown=EXCLUDE)
    r""" The snapshot field of the xc_aggregate. """

    space = fields.Nested("netapp_ontap.models.aggregate_space.AggregateSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the xc_aggregate. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['online', 'onlining', 'offline', 'offlining', 'relocating', 'unmounted', 'restricted', 'inconsistent', 'failed', 'unknown']),
    )
    r""" Operational state of the aggregate.

Valid choices:

* online
* onlining
* offline
* offlining
* relocating
* unmounted
* restricted
* inconsistent
* failed
* unknown """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw.PerformanceMetricRawSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_aggregate. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Aggregate UUID. """

    volume_count = Size(
        data_key="volume-count",
    )
    r""" Number of volumes in the aggregate. """

    @property
    def resource(self):
        return XcAggregate

    gettable_fields = [
        "links",
        "block_storage",
        "create_time",
        "data_encryption",
        "dr_home_node.name",
        "dr_home_node.uuid",
        "home_node.links",
        "home_node.name",
        "home_node.uuid",
        "inactive_data_reporting",
        "inode_attributes",
        "is_spare_low",
        "metric",
        "name",
        "node.links",
        "node.name",
        "node.uuid",
        "recommendation_spares",
        "sidl_enabled",
        "snaplock_type",
        "snapshot",
        "space",
        "state",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "uuid",
        "volume_count",
    ]
    """links,block_storage,create_time,data_encryption,dr_home_node.name,dr_home_node.uuid,home_node.links,home_node.name,home_node.uuid,inactive_data_reporting,inode_attributes,is_spare_low,metric,name,node.links,node.name,node.uuid,recommendation_spares,sidl_enabled,snaplock_type,snapshot,space,state,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,uuid,volume_count,"""

    patchable_fields = [
        "block_storage",
        "cloud_storage",
        "data_encryption",
        "home_node.name",
        "home_node.uuid",
        "inactive_data_reporting",
        "name",
        "node.name",
        "node.uuid",
        "recommendation_spares",
        "sidl_enabled",
        "snapshot",
        "space",
        "state",
    ]
    """block_storage,cloud_storage,data_encryption,home_node.name,home_node.uuid,inactive_data_reporting,name,node.name,node.uuid,recommendation_spares,sidl_enabled,snapshot,space,state,"""

    postable_fields = [
        "block_storage",
        "data_encryption",
        "home_node.name",
        "home_node.uuid",
        "inactive_data_reporting",
        "name",
        "node.name",
        "node.uuid",
        "recommendation_spares",
        "sidl_enabled",
        "snaplock_type",
        "snapshot",
        "space",
        "state",
    ]
    """block_storage,data_encryption,home_node.name,home_node.uuid,inactive_data_reporting,name,node.name,node.uuid,recommendation_spares,sidl_enabled,snaplock_type,snapshot,space,state,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcAggregate.get_collection(fields=field)]
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
            raise NetAppRestError("XcAggregate modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcAggregate(Resource):
    r""" aggregate clone for cluster peer. """

    _schema = XcAggregateSchema
    _path = "/api/cluster/peers/{peer[uuid]}/storage/aggregates"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET aggregates"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc aggregate show")
        def xc_aggregate_show(
            peer_uuid,
            create_time: Choices.define(_get_field_list("create_time"), cache_choices=True, inexact=True)=None,
            is_spare_low: Choices.define(_get_field_list("is_spare_low"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            sidl_enabled: Choices.define(_get_field_list("sidl_enabled"), cache_choices=True, inexact=True)=None,
            snaplock_type: Choices.define(_get_field_list("snaplock_type"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            volume_count: Choices.define(_get_field_list("volume_count"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["create_time", "is_spare_low", "name", "sidl_enabled", "snaplock_type", "state", "uuid", "volume_count", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcAggregate resources

            Args:
                create_time: Timestamp of aggregate creation.
                is_spare_low: Specifies whether the aggregate is in a spares low condition on any of the RAID groups. This is an advanced property; there is an added cost to retrieving its value. The field is not populated for either a collection GET or an instance GET unless it is explicitly requested using the <i>fields</i> query parameter containing either footprint or **. 
                name: Aggregate name.
                sidl_enabled: Specifies whether or not SIDL is enabled on the aggregate.
                snaplock_type: SnapLock type.
                state: Operational state of the aggregate.
                uuid: Aggregate UUID.
                volume_count: Number of volumes in the aggregate.
            """

            kwargs = {}
            if create_time is not None:
                kwargs["create_time"] = create_time
            if is_spare_low is not None:
                kwargs["is_spare_low"] = is_spare_low
            if name is not None:
                kwargs["name"] = name
            if sidl_enabled is not None:
                kwargs["sidl_enabled"] = sidl_enabled
            if snaplock_type is not None:
                kwargs["snaplock_type"] = snaplock_type
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if volume_count is not None:
                kwargs["volume_count"] = volume_count
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcAggregate.get_collection(
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
        """Returns a count of all XcAggregate resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET aggregates"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






