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


__all__ = ["XcVolume", "XcVolumeSchema"]
__pdoc__ = {
    "XcVolumeSchema.resource": False,
    "XcVolumeSchema.opts": False,
    "XcVolume.xc_volume_show": False,
    "XcVolume.xc_volume_create": False,
    "XcVolume.xc_volume_modify": False,
    "XcVolume.xc_volume_delete": False,
}


class XcVolumeSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcVolume object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_volume. """

    access_time_enabled = fields.Boolean(
        data_key="access_time_enabled",
    )
    r""" Indicates whether or not access time updates are enabled on the volume. """

    activity_tracking = fields.Nested("netapp_ontap.models.volume_activity_tracking.VolumeActivityTrackingSchema", data_key="activity_tracking", unknown=EXCLUDE)
    r""" The activity_tracking field of the xc_volume. """

    aggregates = fields.List(fields.Nested("netapp_ontap.models.xc_s3_bucket_aggregates.XcS3BucketAggregatesSchema", unknown=EXCLUDE), data_key="aggregates")
    r""" Aggregate hosting the volume. Required on POST. """

    analytics = fields.Nested("netapp_ontap.models.volume_analytics.VolumeAnalyticsSchema", data_key="analytics", unknown=EXCLUDE)
    r""" The analytics field of the xc_volume. """

    anti_ransomware = fields.Nested("netapp_ontap.models.anti_ransomware_volume.AntiRansomwareVolumeSchema", data_key="anti_ransomware", unknown=EXCLUDE)
    r""" The anti_ransomware field of the xc_volume. """

    anti_ransomware_state = fields.Str(
        data_key="anti_ransomware_state",
        validate=enum_validation(['disabled', 'enabled', 'dry_run', 'paused', 'disable_in_progress', 'enable_paused', 'dry_run_paused']),
    )
    r""" The Anti-ransomware state of the volume. If no "anti_ransomware_state" property is specified, the volume inherits the value from its parent SVM's "anti_ransomware_default_volume_state" property. If this value is "disabled", Anti-ransomware is disabled on the volume. If this value is "enabled", Anti-ransomware is enabled on the volume and alerts are raised if any suspect is detected for those volumes. If this value is "dry_run", Anti-ransomware is enabled in the dry-run or learning mode on the volume. The "dry_run" state is same as the "enabled" state except that the analytics data is used here for learning. No alerts are raised for any detections or violations. If this value is "paused", Anti-ransomware is paused on the volume. Additionally, three more states are available, which are only valid for GET. If this value is "disable_in_progress", Anti-ransomware monitoring is being disabled and a cleanup operation is in effect. If this value is "enable_paused", Anti-ransomware is paused on the volume from its earlier enabled state. If this value is "dry_run_paused", Anti-ransomware monitoring is paused on the volume from its earlier dry_run state. For POST, the valid Anti-ransomware states are only "disabled", "enabled" and "dry_run", whereas for PATCH, "paused" is also valid along with the three valid states for POST.

Valid choices:

* disabled
* enabled
* dry_run
* paused
* disable_in_progress
* enable_paused
* dry_run_paused """

    application = fields.Nested("netapp_ontap.models.volume_application.VolumeApplicationSchema", data_key="application", unknown=EXCLUDE)
    r""" The application field of the xc_volume. """

    asynchronous_directory_delete = fields.Nested("netapp_ontap.models.volume_asynchronous_directory_delete.VolumeAsynchronousDirectoryDeleteSchema", data_key="asynchronous_directory_delete", unknown=EXCLUDE)
    r""" The asynchronous_directory_delete field of the xc_volume. """

    autosize = fields.Nested("netapp_ontap.models.volume_autosize.VolumeAutosizeSchema", data_key="autosize", unknown=EXCLUDE)
    r""" The autosize field of the xc_volume. """

    clone = fields.Nested("netapp_ontap.models.volume_clone.VolumeCloneSchema", data_key="clone", unknown=EXCLUDE)
    r""" The clone field of the xc_volume. """

    cloud_retrieval_policy = fields.Str(
        data_key="cloud_retrieval_policy",
        validate=enum_validation(['default', 'on_read', 'never', 'promote']),
    )
    r""" This parameter specifies the cloud retrieval policy for the volume. This policy determines which tiered out blocks to retrieve from the capacity tier to the performance tier. The available cloud retrieval policies are
"default" policy retrieves tiered data based on the underlying tiering policy. If the tiering policy is 'auto', tiered data is retrieved only for random client driven data reads. If the tiering policy is 'none' or 'snapshot_only', tiered data is retrieved for random and sequential client driven data reads. If the tiering policy is 'all', tiered data is not retrieved.
"on_read" policy retrieves tiered data for all client driven data reads.
"never" policy never retrieves tiered data.
"promote" policy retrieves all eligible tiered data automatically during the next scheduled scan. It is only supported when the tiering policy is 'none' or 'snapshot_only'. If the tiering policy is 'snapshot_only', the only data brought back is the data in the AFS. Data that is only in a snapshot copy stays in the cloud and if tiering policy is 'none' then all data is retrieved.


Valid choices:

* default
* on_read
* never
* promote """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=1023),
    )
    r""" A comment for the volume. Valid in POST or PATCH. """

    consistency_group = fields.Nested("netapp_ontap.models.volume_consistency_group.VolumeConsistencyGroupSchema", data_key="consistency_group", unknown=EXCLUDE)
    r""" The consistency_group field of the xc_volume. """

    constituents = fields.List(fields.Nested("netapp_ontap.models.volume_constituents.VolumeConstituentsSchema", unknown=EXCLUDE), data_key="constituents")
    r""" FlexGroup Constituents. FlexGroup Constituents can be retrieved more efficiently by specifying "is_constituent=true" or "is_constituent=true&flexgroup.uuid=<flexgroup.uuid>" as query parameters. """

    constituents_per_aggregate = Size(
        data_key="constituents_per_aggregate",
        validate=integer_validation(minimum=1, maximum=1000),
    )
    r""" Specifies the number of times to iterate over the aggregates listed with the "aggregates.name" or "aggregates.uuid" when creating or expanding a FlexGroup volume. If a volume is being created on a single aggregate, the system creates a flexible volume if the "constituents_per_aggregate" field is not specified, or a FlexGroup volume if it is specified. If a volume is being created on multiple aggregates, the system always creates a FlexGroup volume. The root constituent of a FlexGroup volume is always placed on the first aggregate in the list. """

    convert_unicode = fields.Boolean(
        data_key="convert_unicode",
    )
    r""" Specifies whether directory Unicode format conversion is enabled when directories are accessed by NFS clients. """

    create_time = ImpreciseDateTime(
        data_key="create_time",
    )
    r""" Creation time of the volume. This field is generated when the volume is created.

Example: 2018-06-04T19:00:00Z """

    efficiency = fields.Nested("netapp_ontap.models.volume_efficiency.VolumeEfficiencySchema", data_key="efficiency", unknown=EXCLUDE)
    r""" The efficiency field of the xc_volume. """

    encryption = fields.Nested("netapp_ontap.models.volume_encryption.VolumeEncryptionSchema", data_key="encryption", unknown=EXCLUDE)
    r""" The encryption field of the xc_volume. """

    error_state = fields.Nested("netapp_ontap.models.volume_error_state.VolumeErrorStateSchema", data_key="error_state", unknown=EXCLUDE)
    r""" The error_state field of the xc_volume. """

    files = fields.Nested("netapp_ontap.models.volume_files.VolumeFilesSchema", data_key="files", unknown=EXCLUDE)
    r""" The files field of the xc_volume. """

    flash_pool = fields.Nested("netapp_ontap.models.volume_flash_pool.VolumeFlashPoolSchema", data_key="flash_pool", unknown=EXCLUDE)
    r""" The flash_pool field of the xc_volume. """

    flexcache_endpoint_type = fields.Str(
        data_key="flexcache_endpoint_type",
        validate=enum_validation(['none', 'cache', 'origin']),
    )
    r""" FlexCache endpoint type. <br>none &dash; The volume is neither a FlexCache nor origin of any FlexCache. <br>cache &dash; The volume is a FlexCache volume. <br>origin &dash; The volume is origin of a FlexCache volume.

Valid choices:

* none
* cache
* origin """

    flexgroup = fields.Nested("netapp_ontap.models.volume_flexgroup.VolumeFlexgroupSchema", data_key="flexgroup", unknown=EXCLUDE)
    r""" The flexgroup field of the xc_volume. """

    granular_data = fields.Boolean(
        data_key="granular_data",
    )
    r""" State of granular data on the volume. This setting is true by default when creating a new FlexGroup volume, but can be specified as false at the time of creation via a POST request. On FlexVol volumes, the setting is always false, as only FlexGroup volumes and FlexGroup constituents support this feature. Once enabled, this setting can only be disabled by restoring a Snapshot copy. Earlier versions of ONTAP (pre 9.11) are not compatible with this feature. Therefore, reverting to an earlier version of ONTAP is not possible unless this volume is deleted or restored to a Snapshot copy that was taken before the setting was enabled. """

    guarantee = fields.Nested("netapp_ontap.models.volume_guarantee.VolumeGuaranteeSchema", data_key="guarantee", unknown=EXCLUDE)
    r""" The guarantee field of the xc_volume. """

    idcs_scanner = fields.Nested("netapp_ontap.models.volume_idcs_scanner.VolumeIdcsScannerSchema", data_key="idcs_scanner", unknown=EXCLUDE)
    r""" The idcs_scanner field of the xc_volume. """

    is_object_store = fields.Boolean(
        data_key="is_object_store",
    )
    r""" Specifies whether the volume is provisioned for an object store server. """

    is_svm_root = fields.Boolean(
        data_key="is_svm_root",
    )
    r""" Specifies whether the volume is a root volume of the SVM it belongs to. """

    language = fields.Str(
        data_key="language",
        validate=enum_validation(['ar', 'ar.utf_8', 'c', 'c.utf_8', 'cs', 'cs.utf_8', 'da', 'da.utf_8', 'de', 'de.utf_8', 'en', 'en.utf_8', 'en_us', 'en_us.utf_8', 'es', 'es.utf_8', 'fi', 'fi.utf_8', 'fr', 'fr.utf_8', 'he', 'he.utf_8', 'hr', 'hr.utf_8', 'hu', 'hu.utf_8', 'it', 'it.utf_8', 'ja', 'ja.utf_8', 'ja_jp.932', 'ja_jp.932.utf_8', 'ja_jp.pck', 'ja_jp.pck.utf_8', 'ja_jp.pck_v2', 'ja_jp.pck_v2.utf_8', 'ja_v1', 'ja_v1.utf_8', 'ko', 'ko.utf_8', 'nl', 'nl.utf_8', 'no', 'no.utf_8', 'pl', 'pl.utf_8', 'pt', 'pt.utf_8', 'ro', 'ro.utf_8', 'ru', 'ru.utf_8', 'sk', 'sk.utf_8', 'sl', 'sl.utf_8', 'sv', 'sv.utf_8', 'tr', 'tr.utf_8', 'utf8mb4', 'zh', 'zh.gbk', 'zh.gbk.utf_8', 'zh.utf_8', 'zh_tw', 'zh_tw.big5', 'zh_tw.big5.utf_8', 'zh_tw.utf_8']),
    )
    r""" Language encoding setting for volume. If no language is specified, the volume inherits its SVM language encoding setting.

Valid choices:

* ar
* ar.utf_8
* c
* c.utf_8
* cs
* cs.utf_8
* da
* da.utf_8
* de
* de.utf_8
* en
* en.utf_8
* en_us
* en_us.utf_8
* es
* es.utf_8
* fi
* fi.utf_8
* fr
* fr.utf_8
* he
* he.utf_8
* hr
* hr.utf_8
* hu
* hu.utf_8
* it
* it.utf_8
* ja
* ja.utf_8
* ja_jp.932
* ja_jp.932.utf_8
* ja_jp.pck
* ja_jp.pck.utf_8
* ja_jp.pck_v2
* ja_jp.pck_v2.utf_8
* ja_v1
* ja_v1.utf_8
* ko
* ko.utf_8
* nl
* nl.utf_8
* no
* no.utf_8
* pl
* pl.utf_8
* pt
* pt.utf_8
* ro
* ro.utf_8
* ru
* ru.utf_8
* sk
* sk.utf_8
* sl
* sl.utf_8
* sv
* sv.utf_8
* tr
* tr.utf_8
* utf8mb4
* zh
* zh.gbk
* zh.gbk.utf_8
* zh.utf_8
* zh_tw
* zh_tw.big5
* zh_tw.big5.utf_8
* zh_tw.utf_8 """

    max_dir_size = Size(
        data_key="max_dir_size",
    )
    r""" Maximum directory size. This value sets maximum size, in bytes, to which a directory can grow. The default maximum directory size for FlexVol volumes is model-dependent, and optimized for the size of system memory. Before increasing the maximum directory size, involve technical support. """

    metric = fields.Nested("netapp_ontap.resources.volume_metrics.VolumeMetricsSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_volume. """

    movement = fields.Nested("netapp_ontap.models.volume_movement.VolumeMovementSchema", data_key="movement", unknown=EXCLUDE)
    r""" The movement field of the xc_volume. """

    msid = Size(
        data_key="msid",
    )
    r""" The volume's Mirror Set ID. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=203),
    )
    r""" Volume name. The name of volume must start with an alphabetic character (a to z or A to Z) or an underscore (_). The name must be 197 or fewer characters in length for FlexGroups, and 203 or fewer characters in length for all other types of volumes. Volume names must be unique within an SVM. Required on POST.

Example: vol_cs_dept """

    nas = fields.Nested("netapp_ontap.models.volume_nas.VolumeNasSchema", data_key="nas", unknown=EXCLUDE)
    r""" The nas field of the xc_volume. """

    qos = fields.Nested("netapp_ontap.models.volume_qos.VolumeQosSchema", data_key="qos", unknown=EXCLUDE)
    r""" The qos field of the xc_volume. """

    queue_for_encryption = fields.Boolean(
        data_key="queue_for_encryption",
    )
    r""" Specifies whether the volume is queued for encryption. """

    quota = fields.Nested("netapp_ontap.models.volume_quota.VolumeQuotaSchema", data_key="quota", unknown=EXCLUDE)
    r""" The quota field of the xc_volume. """

    rebalancing = fields.Nested("netapp_ontap.models.volume_rebalancing.VolumeRebalancingSchema", data_key="rebalancing", unknown=EXCLUDE)
    r""" The rebalancing field of the xc_volume. """

    scheduled_snapshot_naming_scheme = fields.Str(
        data_key="scheduled_snapshot_naming_scheme",
        validate=enum_validation(['create_time', 'ordinal']),
    )
    r""" Naming Scheme for automatic Snapshot copies:

* create_time - Automatic Snapshot copies are saved as per the start of their current date and time.
* ordinal - Latest automatic snapshot copy is saved as <scheduled_frequency>.0 and subsequent copies will follow the create_time naming convention.


Valid choices:

* create_time
* ordinal """

    size = Size(
        data_key="size",
    )
    r""" Physical size of the volume, in bytes. The minimum size for a FlexVol volume is 20MB and the minimum size for a FlexGroup volume is 200MB per constituent. The recommended size for a FlexGroup volume is a minimum of 100GB per constituent. For all volumes, the default size is equal to the minimum size. """

    snaplock = fields.Nested("netapp_ontap.models.volume_snaplock.VolumeSnaplockSchema", data_key="snaplock", unknown=EXCLUDE)
    r""" The snaplock field of the xc_volume. """

    snapmirror = fields.Nested("netapp_ontap.models.volume_snapmirror.VolumeSnapmirrorSchema", data_key="snapmirror", unknown=EXCLUDE)
    r""" The snapmirror field of the xc_volume. """

    snapshot_count = Size(
        data_key="snapshot_count",
        validate=integer_validation(minimum=0, maximum=1023),
    )
    r""" Number of Snapshot copies in the volume. """

    snapshot_policy = fields.Nested("netapp_ontap.resources.snapshot_policy.SnapshotPolicySchema", data_key="snapshot_policy", unknown=EXCLUDE)
    r""" The snapshot_policy field of the xc_volume. """

    space = fields.Nested("netapp_ontap.models.volume_space.VolumeSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the xc_volume. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['error', 'mixed', 'offline', 'online', 'restricted']),
    )
    r""" Volume state. Client access is supported only when volume is online and junctioned. Taking volume to offline or restricted state removes its junction path and blocks client access. When volume is in restricted state some operations like parity reconstruction and iron on commit are allowed. The 'mixed' state applies to FlexGroup volumes only and cannot be specified as a target state. An 'error' state implies that the volume is not in a state to serve data.

Valid choices:

* error
* mixed
* offline
* online
* restricted """

    statistics = fields.Nested("netapp_ontap.models.volume_statistics.VolumeStatisticsSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_volume. """

    status = fields.List(fields.Str, data_key="status")
    r""" Describes the current status of a volume. """

    style = fields.Str(
        data_key="style",
        validate=enum_validation(['flexvol', 'flexgroup', 'flexgroup_constituent']),
    )
    r""" The style of the volume. If "style" is not specified, the volume type is determined based on the specified aggregates. Specifying a single aggregate, without "constituents_per_aggregate", creates a flexible volume. Specifying multiple aggregates, or a single aggregate with "constituents_per_aggregate", creates a FlexGroup. Specifying a volume "style" creates a volume of that type. For example, if the style is "flexvol" you must specify a single aggregate. If the style is "flexgroup", the system either uses the specified aggregates or automatically provisions aggregates if there are no specified aggregates. The style "flexgroup_constiutent" is not supported when creating a volume.<br>flexvol &dash; flexible volumes and FlexClone volumes<br>flexgroup &dash; FlexGroup volumes<br>flexgroup_constituent &dash; FlexGroup constituents.

Valid choices:

* flexvol
* flexgroup
* flexgroup_constituent """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_volume. """

    tiering = fields.Nested("netapp_ontap.models.volume_tiering.VolumeTieringSchema", data_key="tiering", unknown=EXCLUDE)
    r""" The tiering field of the xc_volume. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['rw', 'dp', 'ls']),
    )
    r""" Type of the volume.<br>rw &dash; read-write volume.<br>dp &dash; data-protection volume.<br>ls &dash; load-sharing `dp` volume. Valid in GET.

Valid choices:

* rw
* dp
* ls """

    use_mirrored_aggregates = fields.Boolean(
        data_key="use_mirrored_aggregates",
    )
    r""" Specifies whether mirrored aggregates are selected when provisioning a FlexGroup without specifying "aggregates.name" or "aggregates.uuid". Only mirrored aggregates are used if this parameter is set to 'true' and only unmirrored aggregates are used if this parameter is set to 'false'. Aggregate level mirroring for a FlexGroup can be changed by moving all of the constituents to the required aggregates. The default value is 'true' for a MetroCluster configuration and is 'false' for a non-MetroCluster configuration. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique identifier for the volume. This corresponds to the instance-uuid that is exposed in the CLI and ONTAPI. It does not change due to a volume move.

Example: 028baa66-41bd-11e9-81d5-00a0986138f7 """

    @property
    def resource(self):
        return XcVolume

    gettable_fields = [
        "links",
        "access_time_enabled",
        "activity_tracking",
        "aggregates.links",
        "aggregates.name",
        "aggregates.uuid",
        "analytics",
        "anti_ransomware",
        "anti_ransomware_state",
        "application",
        "asynchronous_directory_delete",
        "autosize",
        "clone",
        "cloud_retrieval_policy",
        "comment",
        "consistency_group",
        "constituents",
        "convert_unicode",
        "create_time",
        "efficiency",
        "encryption",
        "error_state",
        "files",
        "flash_pool",
        "flexcache_endpoint_type",
        "flexgroup",
        "granular_data",
        "guarantee",
        "idcs_scanner",
        "is_object_store",
        "is_svm_root",
        "language",
        "max_dir_size",
        "metric",
        "movement",
        "msid",
        "name",
        "nas",
        "qos",
        "queue_for_encryption",
        "quota",
        "rebalancing",
        "scheduled_snapshot_naming_scheme",
        "size",
        "snaplock",
        "snapmirror",
        "snapshot_count",
        "snapshot_policy.links",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
        "space",
        "state",
        "statistics.cifs_ops_raw",
        "statistics.cloud",
        "statistics.flexcache_raw",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.nfs_ops_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "status",
        "style",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "tiering",
        "type",
        "uuid",
    ]
    """links,access_time_enabled,activity_tracking,aggregates.links,aggregates.name,aggregates.uuid,analytics,anti_ransomware,anti_ransomware_state,application,asynchronous_directory_delete,autosize,clone,cloud_retrieval_policy,comment,consistency_group,constituents,convert_unicode,create_time,efficiency,encryption,error_state,files,flash_pool,flexcache_endpoint_type,flexgroup,granular_data,guarantee,idcs_scanner,is_object_store,is_svm_root,language,max_dir_size,metric,movement,msid,name,nas,qos,queue_for_encryption,quota,rebalancing,scheduled_snapshot_naming_scheme,size,snaplock,snapmirror,snapshot_count,snapshot_policy.links,snapshot_policy.name,snapshot_policy.uuid,space,state,statistics.cifs_ops_raw,statistics.cloud,statistics.flexcache_raw,statistics.iops_raw,statistics.latency_raw,statistics.nfs_ops_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,status,style,svm.links,svm.name,svm.uuid,tiering,type,uuid,"""

    patchable_fields = [
        "access_time_enabled",
        "activity_tracking",
        "aggregates.links",
        "aggregates.name",
        "aggregates.uuid",
        "analytics",
        "anti_ransomware",
        "anti_ransomware_state",
        "application",
        "asynchronous_directory_delete",
        "autosize",
        "clone",
        "cloud_retrieval_policy",
        "comment",
        "consistency_group",
        "constituents",
        "constituents_per_aggregate",
        "convert_unicode",
        "efficiency",
        "encryption",
        "error_state",
        "files",
        "flash_pool",
        "flexgroup",
        "granular_data",
        "guarantee",
        "idcs_scanner",
        "max_dir_size",
        "movement",
        "msid",
        "name",
        "nas",
        "qos",
        "queue_for_encryption",
        "quota",
        "rebalancing",
        "scheduled_snapshot_naming_scheme",
        "size",
        "snaplock",
        "snapmirror",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
        "space",
        "state",
        "tiering",
    ]
    """access_time_enabled,activity_tracking,aggregates.links,aggregates.name,aggregates.uuid,analytics,anti_ransomware,anti_ransomware_state,application,asynchronous_directory_delete,autosize,clone,cloud_retrieval_policy,comment,consistency_group,constituents,constituents_per_aggregate,convert_unicode,efficiency,encryption,error_state,files,flash_pool,flexgroup,granular_data,guarantee,idcs_scanner,max_dir_size,movement,msid,name,nas,qos,queue_for_encryption,quota,rebalancing,scheduled_snapshot_naming_scheme,size,snaplock,snapmirror,snapshot_policy.name,snapshot_policy.uuid,space,state,tiering,"""

    postable_fields = [
        "activity_tracking",
        "aggregates.links",
        "aggregates.name",
        "aggregates.uuid",
        "analytics",
        "anti_ransomware",
        "anti_ransomware_state",
        "application",
        "asynchronous_directory_delete",
        "autosize",
        "clone",
        "cloud_retrieval_policy",
        "comment",
        "consistency_group",
        "constituents",
        "constituents_per_aggregate",
        "convert_unicode",
        "efficiency",
        "encryption",
        "error_state",
        "files",
        "flash_pool",
        "flexgroup",
        "granular_data",
        "guarantee",
        "idcs_scanner",
        "language",
        "max_dir_size",
        "movement",
        "msid",
        "name",
        "nas",
        "qos",
        "quota",
        "rebalancing",
        "scheduled_snapshot_naming_scheme",
        "size",
        "snaplock",
        "snapmirror",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
        "space",
        "state",
        "style",
        "svm.name",
        "svm.uuid",
        "tiering",
        "type",
        "use_mirrored_aggregates",
    ]
    """activity_tracking,aggregates.links,aggregates.name,aggregates.uuid,analytics,anti_ransomware,anti_ransomware_state,application,asynchronous_directory_delete,autosize,clone,cloud_retrieval_policy,comment,consistency_group,constituents,constituents_per_aggregate,convert_unicode,efficiency,encryption,error_state,files,flash_pool,flexgroup,granular_data,guarantee,idcs_scanner,language,max_dir_size,movement,msid,name,nas,qos,quota,rebalancing,scheduled_snapshot_naming_scheme,size,snaplock,snapmirror,snapshot_policy.name,snapshot_policy.uuid,space,state,style,svm.name,svm.uuid,tiering,type,use_mirrored_aggregates,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcVolume.get_collection(fields=field)]
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
            raise NetAppRestError("XcVolume modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcVolume(Resource):
    r""" volume clone for cluster peer. """

    _schema = XcVolumeSchema
    _path = "/api/svm/peers/{peer[uuid]}/storage/volumes"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET volumes"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc volume show")
        def xc_volume_show(
            peer_uuid,
            access_time_enabled: Choices.define(_get_field_list("access_time_enabled"), cache_choices=True, inexact=True)=None,
            anti_ransomware_state: Choices.define(_get_field_list("anti_ransomware_state"), cache_choices=True, inexact=True)=None,
            cloud_retrieval_policy: Choices.define(_get_field_list("cloud_retrieval_policy"), cache_choices=True, inexact=True)=None,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            constituents_per_aggregate: Choices.define(_get_field_list("constituents_per_aggregate"), cache_choices=True, inexact=True)=None,
            convert_unicode: Choices.define(_get_field_list("convert_unicode"), cache_choices=True, inexact=True)=None,
            create_time: Choices.define(_get_field_list("create_time"), cache_choices=True, inexact=True)=None,
            flexcache_endpoint_type: Choices.define(_get_field_list("flexcache_endpoint_type"), cache_choices=True, inexact=True)=None,
            granular_data: Choices.define(_get_field_list("granular_data"), cache_choices=True, inexact=True)=None,
            is_object_store: Choices.define(_get_field_list("is_object_store"), cache_choices=True, inexact=True)=None,
            is_svm_root: Choices.define(_get_field_list("is_svm_root"), cache_choices=True, inexact=True)=None,
            language: Choices.define(_get_field_list("language"), cache_choices=True, inexact=True)=None,
            max_dir_size: Choices.define(_get_field_list("max_dir_size"), cache_choices=True, inexact=True)=None,
            msid: Choices.define(_get_field_list("msid"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            queue_for_encryption: Choices.define(_get_field_list("queue_for_encryption"), cache_choices=True, inexact=True)=None,
            scheduled_snapshot_naming_scheme: Choices.define(_get_field_list("scheduled_snapshot_naming_scheme"), cache_choices=True, inexact=True)=None,
            size: Choices.define(_get_field_list("size"), cache_choices=True, inexact=True)=None,
            snapshot_count: Choices.define(_get_field_list("snapshot_count"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            status: Choices.define(_get_field_list("status"), cache_choices=True, inexact=True)=None,
            style: Choices.define(_get_field_list("style"), cache_choices=True, inexact=True)=None,
            type: Choices.define(_get_field_list("type"), cache_choices=True, inexact=True)=None,
            use_mirrored_aggregates: Choices.define(_get_field_list("use_mirrored_aggregates"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["access_time_enabled", "anti_ransomware_state", "cloud_retrieval_policy", "comment", "constituents_per_aggregate", "convert_unicode", "create_time", "flexcache_endpoint_type", "granular_data", "is_object_store", "is_svm_root", "language", "max_dir_size", "msid", "name", "queue_for_encryption", "scheduled_snapshot_naming_scheme", "size", "snapshot_count", "state", "status", "style", "type", "use_mirrored_aggregates", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcVolume resources

            Args:
                access_time_enabled: Indicates whether or not access time updates are enabled on the volume.
                anti_ransomware_state: The Anti-ransomware state of the volume. If no \"anti_ransomware_state\" property is specified, the volume inherits the value from its parent SVM's \"anti_ransomware_default_volume_state\" property. If this value is \"disabled\", Anti-ransomware is disabled on the volume. If this value is \"enabled\", Anti-ransomware is enabled on the volume and alerts are raised if any suspect is detected for those volumes. If this value is \"dry_run\", Anti-ransomware is enabled in the dry-run or learning mode on the volume. The \"dry_run\" state is same as the \"enabled\" state except that the analytics data is used here for learning. No alerts are raised for any detections or violations. If this value is \"paused\", Anti-ransomware is paused on the volume. Additionally, three more states are available, which are only valid for GET. If this value is \"disable_in_progress\", Anti-ransomware monitoring is being disabled and a cleanup operation is in effect. If this value is \"enable_paused\", Anti-ransomware is paused on the volume from its earlier enabled state. If this value is \"dry_run_paused\", Anti-ransomware monitoring is paused on the volume from its earlier dry_run state. For POST, the valid Anti-ransomware states are only \"disabled\", \"enabled\" and \"dry_run\", whereas for PATCH, \"paused\" is also valid along with the three valid states for POST.
                cloud_retrieval_policy: This parameter specifies the cloud retrieval policy for the volume. This policy determines which tiered out blocks to retrieve from the capacity tier to the performance tier. The available cloud retrieval policies are \"default\" policy retrieves tiered data based on the underlying tiering policy. If the tiering policy is 'auto', tiered data is retrieved only for random client driven data reads. If the tiering policy is 'none' or 'snapshot_only', tiered data is retrieved for random and sequential client driven data reads. If the tiering policy is 'all', tiered data is not retrieved. \"on_read\" policy retrieves tiered data for all client driven data reads. \"never\" policy never retrieves tiered data. \"promote\" policy retrieves all eligible tiered data automatically during the next scheduled scan. It is only supported when the tiering policy is 'none' or 'snapshot_only'. If the tiering policy is 'snapshot_only', the only data brought back is the data in the AFS. Data that is only in a snapshot copy stays in the cloud and if tiering policy is 'none' then all data is retrieved. 
                comment: A comment for the volume. Valid in POST or PATCH.
                constituents_per_aggregate: Specifies the number of times to iterate over the aggregates listed with the \"aggregates.name\" or \"aggregates.uuid\" when creating or expanding a FlexGroup volume. If a volume is being created on a single aggregate, the system creates a flexible volume if the \"constituents_per_aggregate\" field is not specified, or a FlexGroup volume if it is specified. If a volume is being created on multiple aggregates, the system always creates a FlexGroup volume. The root constituent of a FlexGroup volume is always placed on the first aggregate in the list.
                convert_unicode: Specifies whether directory Unicode format conversion is enabled when directories are accessed by NFS clients.
                create_time: Creation time of the volume. This field is generated when the volume is created.
                flexcache_endpoint_type: FlexCache endpoint type. <br>none &dash; The volume is neither a FlexCache nor origin of any FlexCache. <br>cache &dash; The volume is a FlexCache volume. <br>origin &dash; The volume is origin of a FlexCache volume.
                granular_data: State of granular data on the volume. This setting is true by default when creating a new FlexGroup volume, but can be specified as false at the time of creation via a POST request. On FlexVol volumes, the setting is always false, as only FlexGroup volumes and FlexGroup constituents support this feature. Once enabled, this setting can only be disabled by restoring a Snapshot copy. Earlier versions of ONTAP (pre 9.11) are not compatible with this feature. Therefore, reverting to an earlier version of ONTAP is not possible unless this volume is deleted or restored to a Snapshot copy that was taken before the setting was enabled.
                is_object_store: Specifies whether the volume is provisioned for an object store server.
                is_svm_root: Specifies whether the volume is a root volume of the SVM it belongs to.
                language: Language encoding setting for volume. If no language is specified, the volume inherits its SVM language encoding setting.
                max_dir_size: Maximum directory size. This value sets maximum size, in bytes, to which a directory can grow. The default maximum directory size for FlexVol volumes is model-dependent, and optimized for the size of system memory. Before increasing the maximum directory size, involve technical support.
                msid: The volume's Mirror Set ID.
                name: Volume name. The name of volume must start with an alphabetic character (a to z or A to Z) or an underscore (_). The name must be 197 or fewer characters in length for FlexGroups, and 203 or fewer characters in length for all other types of volumes. Volume names must be unique within an SVM. Required on POST.
                queue_for_encryption: Specifies whether the volume is queued for encryption.
                scheduled_snapshot_naming_scheme: Naming Scheme for automatic Snapshot copies: * create_time - Automatic Snapshot copies are saved as per the start of their current date and time. * ordinal - Latest automatic snapshot copy is saved as <scheduled_frequency>.0 and subsequent copies will follow the create_time naming convention. 
                size: Physical size of the volume, in bytes. The minimum size for a FlexVol volume is 20MB and the minimum size for a FlexGroup volume is 200MB per constituent. The recommended size for a FlexGroup volume is a minimum of 100GB per constituent. For all volumes, the default size is equal to the minimum size.
                snapshot_count: Number of Snapshot copies in the volume.
                state: Volume state. Client access is supported only when volume is online and junctioned. Taking volume to offline or restricted state removes its junction path and blocks client access. When volume is in restricted state some operations like parity reconstruction and iron on commit are allowed. The 'mixed' state applies to FlexGroup volumes only and cannot be specified as a target state. An 'error' state implies that the volume is not in a state to serve data.
                status: Describes the current status of a volume.
                style: The style of the volume. If \"style\" is not specified, the volume type is determined based on the specified aggregates. Specifying a single aggregate, without \"constituents_per_aggregate\", creates a flexible volume. Specifying multiple aggregates, or a single aggregate with \"constituents_per_aggregate\", creates a FlexGroup. Specifying a volume \"style\" creates a volume of that type. For example, if the style is \"flexvol\" you must specify a single aggregate. If the style is \"flexgroup\", the system either uses the specified aggregates or automatically provisions aggregates if there are no specified aggregates. The style \"flexgroup_constiutent\" is not supported when creating a volume.<br>flexvol &dash; flexible volumes and FlexClone volumes<br>flexgroup &dash; FlexGroup volumes<br>flexgroup_constituent &dash; FlexGroup constituents.
                type: Type of the volume.<br>rw &dash; read-write volume.<br>dp &dash; data-protection volume.<br>ls &dash; load-sharing `dp` volume. Valid in GET.
                use_mirrored_aggregates: Specifies whether mirrored aggregates are selected when provisioning a FlexGroup without specifying \"aggregates.name\" or \"aggregates.uuid\". Only mirrored aggregates are used if this parameter is set to 'true' and only unmirrored aggregates are used if this parameter is set to 'false'. Aggregate level mirroring for a FlexGroup can be changed by moving all of the constituents to the required aggregates. The default value is 'true' for a MetroCluster configuration and is 'false' for a non-MetroCluster configuration.
                uuid: Unique identifier for the volume. This corresponds to the instance-uuid that is exposed in the CLI and ONTAPI. It does not change due to a volume move.
            """

            kwargs = {}
            if access_time_enabled is not None:
                kwargs["access_time_enabled"] = access_time_enabled
            if anti_ransomware_state is not None:
                kwargs["anti_ransomware_state"] = anti_ransomware_state
            if cloud_retrieval_policy is not None:
                kwargs["cloud_retrieval_policy"] = cloud_retrieval_policy
            if comment is not None:
                kwargs["comment"] = comment
            if constituents_per_aggregate is not None:
                kwargs["constituents_per_aggregate"] = constituents_per_aggregate
            if convert_unicode is not None:
                kwargs["convert_unicode"] = convert_unicode
            if create_time is not None:
                kwargs["create_time"] = create_time
            if flexcache_endpoint_type is not None:
                kwargs["flexcache_endpoint_type"] = flexcache_endpoint_type
            if granular_data is not None:
                kwargs["granular_data"] = granular_data
            if is_object_store is not None:
                kwargs["is_object_store"] = is_object_store
            if is_svm_root is not None:
                kwargs["is_svm_root"] = is_svm_root
            if language is not None:
                kwargs["language"] = language
            if max_dir_size is not None:
                kwargs["max_dir_size"] = max_dir_size
            if msid is not None:
                kwargs["msid"] = msid
            if name is not None:
                kwargs["name"] = name
            if queue_for_encryption is not None:
                kwargs["queue_for_encryption"] = queue_for_encryption
            if scheduled_snapshot_naming_scheme is not None:
                kwargs["scheduled_snapshot_naming_scheme"] = scheduled_snapshot_naming_scheme
            if size is not None:
                kwargs["size"] = size
            if snapshot_count is not None:
                kwargs["snapshot_count"] = snapshot_count
            if state is not None:
                kwargs["state"] = state
            if status is not None:
                kwargs["status"] = status
            if style is not None:
                kwargs["style"] = style
            if type is not None:
                kwargs["type"] = type
            if use_mirrored_aggregates is not None:
                kwargs["use_mirrored_aggregates"] = use_mirrored_aggregates
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcVolume.get_collection(
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
        """Returns a count of all XcVolume resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET volumes"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






