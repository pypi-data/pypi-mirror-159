r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["VolumeRebalancing", "VolumeRebalancingSchema"]
__pdoc__ = {
    "VolumeRebalancingSchema.resource": False,
    "VolumeRebalancingSchema.opts": False,
    "VolumeRebalancing": False,
}


class VolumeRebalancingSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the VolumeRebalancing object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the volume_rebalancing. """

    data_moved = Size(data_key="data_moved")
    r""" The amount of data that has been moved in or out of a constituent. A positive value represents data moving into the constituent while a negative value is data moving out of the constituent. """

    exclude_snapshots = fields.Boolean(data_key="exclude_snapshots")
    r""" Specifies whether or not to exclude files that are stuck in Snapshot copies during rebalancing operation. When a new capacity rebalancing operation is started on a FlexGroup volume, it uses the current "exclude_snapshots" value. Once the operation is started, any changes to the "exclude_snapshots" value do not affect the currently running capacity rebalancing operation. Only future capacity rebalancing operations will use the new "exclude_snapshots" value. """

    failure_reason = fields.Nested("netapp_ontap.models.volume_rebalancing1_failure_reason.VolumeRebalancing1FailureReasonSchema", unknown=EXCLUDE, data_key="failure_reason")
    r""" The failure_reason field of the volume_rebalancing. """

    imbalance_percent = Size(data_key="imbalance_percent")
    r""" Represents the percentage the volume is out of balance. """

    imbalance_size = Size(data_key="imbalance_size")
    r""" Represents how much the volume is out of balance, in bytes. """

    max_constituent_imbalance_percent = Size(data_key="max_constituent_imbalance_percent")
    r""" Absolute percentage of the constituent that is most out of balance. """

    max_file_moves = Size(data_key="max_file_moves")
    r""" Specifies the maximum number of file moves in a volume capacity rebalancing operation on a constituent of the FlexGroup volume. When a new capacity rebalancing operation is started on a FlexGroup volume, it uses the current "max_file_moves" value. Once the operation is started, any changes to the "max_file_moves" value do not affect the currently running capacity rebalancing operation. Only future capacity rebalancing operations will use the new "max_file_moves" value. """

    max_runtime = fields.Str(data_key="max_runtime")
    r""" This optional field specifies the maximum time a capacity rebalancing operation runs for. Once the maximum runtime has passed, the capacity rebalancing operation stops. If it is not set, the default value is 6 hours. This value cannot be updated while a capacity rebalancing operation is running.  The maximum runtime can be in years, months, days, hours, and minutes. A period specified for years, months, and days is represented in the ISO-8601 format as "P<num>Y", "P<num>M", "P<num>D" respectively, for example "P3D" represents a duration of 3 days. A duration in hours and minutes is represented by "PT<num>H" and "PT<num>M" respectively. """

    max_threshold = Size(data_key="max_threshold")
    r""" Specifies the maximum imbalance percentage for FlexGroup volume constituents. When a constituent's imbalance percentage is larger than this value, files are moved from the constituent. When a new capacity rebalancing operation is started on a FlexGroup volume, it uses the current "max_threshold" value. Once the operation is started, any changes to the "max_threshold" value do not affect the currently running capacity rebalancing operation. Only future capacity rebalancing operations will use the new "max_threshold" value. """

    min_file_size = Size(data_key="min_file_size")
    r""" Specifies the minimum file size to consider for a volume capacity rebalancing operation. When a new capacity rebalancing operation is started on a FlexGroup volume, it uses the current "min_file_size" value. Once the operation is started, any changes to the "min_file_size" value do not affect the currently running capacity rebalancing operation. Only future capacity rebalancing operations will use the new "min_file_size" value. The value must be a multiple of 4KB. If it is not set, the default value will be 4KB. """

    min_threshold = Size(data_key="min_threshold")
    r""" Specifies the minimum imbalance percentage for FlexGroup volume constituents. When a constituent's imbalance percentage is smaller than this value, files are not moved from the constituent. When a new capacity rebalancing operation is started on a FlexGroup volume, it will use the current "min_threshold" value. Once the operation is started, any changes to the "min_threshold" value do not affect the currently running capacity rebalancing operation. Only future capacity rebalancing operations will use the new "min_threshold" value. """

    runtime = fields.Str(data_key="runtime")
    r""" Duration the capacity rebalancing operation has been running. """

    start_time = ImpreciseDateTime(data_key="start_time")
    r""" Time when the current capacity rebalancing operation started. """

    state = fields.Str(data_key="state")
    r""" State of volume capacity rebalancing operation. PATCH the state to "starting" to trigger the capacity rebalance operation. PATCH the state to "stopping" to stop the capacity rebalance operation.

Valid choices:

* idle
* starting
* rebalancing
* rebalancing_source
* rebalancing_dest
* scanning
* stopping
* paused
* not_running
* unknown """

    stop_time = ImpreciseDateTime(data_key="stop_time")
    r""" Time when the capacity rebalancing operation stopped. """

    target_used = Size(data_key="target_used")
    r""" Represents the ideal used size of each constituent. Calculated by dividing the total FlexGroup volume used size by the number of constituents. """

    @property
    def resource(self):
        return VolumeRebalancing

    gettable_fields = [
        "links",
        "data_moved",
        "exclude_snapshots",
        "failure_reason",
        "imbalance_percent",
        "imbalance_size",
        "max_constituent_imbalance_percent",
        "max_file_moves",
        "max_runtime",
        "max_threshold",
        "min_file_size",
        "min_threshold",
        "runtime",
        "start_time",
        "state",
        "stop_time",
        "target_used",
    ]
    """links,data_moved,exclude_snapshots,failure_reason,imbalance_percent,imbalance_size,max_constituent_imbalance_percent,max_file_moves,max_runtime,max_threshold,min_file_size,min_threshold,runtime,start_time,state,stop_time,target_used,"""

    patchable_fields = [
        "exclude_snapshots",
        "failure_reason",
        "max_file_moves",
        "max_runtime",
        "max_threshold",
        "min_file_size",
        "min_threshold",
        "state",
    ]
    """exclude_snapshots,failure_reason,max_file_moves,max_runtime,max_threshold,min_file_size,min_threshold,state,"""

    postable_fields = [
        "failure_reason",
    ]
    """failure_reason,"""


class VolumeRebalancing(Resource):

    _schema = VolumeRebalancingSchema
