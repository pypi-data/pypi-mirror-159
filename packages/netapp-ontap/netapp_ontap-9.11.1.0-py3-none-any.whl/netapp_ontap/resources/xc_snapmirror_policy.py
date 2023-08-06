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


__all__ = ["XcSnapmirrorPolicy", "XcSnapmirrorPolicySchema"]
__pdoc__ = {
    "XcSnapmirrorPolicySchema.resource": False,
    "XcSnapmirrorPolicySchema.opts": False,
    "XcSnapmirrorPolicy.xc_snapmirror_policy_show": False,
    "XcSnapmirrorPolicy.xc_snapmirror_policy_create": False,
    "XcSnapmirrorPolicy.xc_snapmirror_policy_modify": False,
    "XcSnapmirrorPolicy.xc_snapmirror_policy_delete": False,
}


class XcSnapmirrorPolicySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSnapmirrorPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_snapmirror_policy. """

    archive = fields.Nested("netapp_ontap.models.snapmirror_policy_archive.SnapmirrorPolicyArchiveSchema", data_key="archive", unknown=EXCLUDE)
    r""" The archive field of the xc_snapmirror_policy. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Comment associated with the policy. """

    copy_all_source_snapshots = fields.Boolean(
        data_key="copy_all_source_snapshots",
    )
    r""" Specifies that all the source Snapshot copies (including the one created by SnapMirror before the transfer begins) should be copied to the destination on a transfer. "Retention" properties cannot be specified along with this property. This is applicable only to async policies. Property can only be set to 'true'.

Example: true """

    copy_latest_source_snapshot = fields.Boolean(
        data_key="copy_latest_source_snapshot",
    )
    r""" Specifies that the latest source Snapshot copy (created by SnapMirror before the transfer begins) should be copied to the destination on a transfer. "Retention" properties cannot be specified along with this property. This is applicable only to async policies. Property can only be set to 'true'.

Example: true """

    create_snapshot_on_source = fields.Boolean(
        data_key="create_snapshot_on_source",
    )
    r""" Specifies whether a new Snapshot copy should be created on the source at the beginning of an update or resync operation. This is applicable only to async policies. Property can only be set to 'false'.

Example: false """

    identity_preservation = fields.Str(
        data_key="identity_preservation",
        validate=enum_validation(['full', 'exclude_network_config', 'exclude_network_and_protocol_config']),
    )
    r""" Specifies which configuration of the source SVM is replicated to the destination SVM. This property is applicable only for SVM data protection with "async" policy type.

Valid choices:

* full
* exclude_network_config
* exclude_network_and_protocol_config """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the policy.

Example: Asynchronous """

    network_compression_enabled = fields.Boolean(
        data_key="network_compression_enabled",
    )
    r""" Specifies whether network compression is enabled for transfers. This is applicable only to the policies of type "async". """

    retention = fields.List(fields.Nested("netapp_ontap.models.snapmirror_policy_rule.SnapmirrorPolicyRuleSchema", unknown=EXCLUDE), data_key="retention")
    r""" Rules for Snapshot copy retention. """

    rpo = Size(
        data_key="rpo",
    )
    r""" Specifies the duration of time for which a change to be propogated to a mirror should be delayed, in seconds. This is an intentional propagation delay between mirrors and is configurable down to zero, which means an immediate propogation. This is supported for policies of type 'continuous'. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for policies owned by an SVM, otherwise set to "cluster".

Valid choices:

* svm
* cluster """

    snapshot_lock_mode = fields.Str(
        data_key="snapshot_lock_mode",
        validate=enum_validation(['none', 'compliance', 'enterprise']),
    )
    r""" Specifies the lock mode of the Snapshot copies stored in the object store. This property is applicable only to policies of type "async" with "create_snapshot_on_source" set to "false". When set to enterprise or compliance, the policy can be associated only with SnapMirror relationships where the source endpoint is a FlexVol volume and the destination endpoint is an object store. When set to compliance, no users can delete a Snapshot copy until the retention period has expired. When set to enterprise, users that have special permissions can delete a Snapshot copy before the retention period has expired.

Valid choices:

* none
* compliance
* enterprise """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_snapmirror_policy. """

    sync_common_snapshot_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="sync_common_snapshot_schedule", unknown=EXCLUDE)
    r""" The sync_common_snapshot_schedule field of the xc_snapmirror_policy. """

    sync_type = fields.Str(
        data_key="sync_type",
        validate=enum_validation(['sync', 'strict_sync', 'automated_failover']),
    )
    r""" The sync_type field of the xc_snapmirror_policy.

Valid choices:

* sync
* strict_sync
* automated_failover """

    throttle = Size(
        data_key="throttle",
    )
    r""" Throttle in KB/s. Default to unlimited. """

    transfer_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="transfer_schedule", unknown=EXCLUDE)
    r""" The transfer_schedule field of the xc_snapmirror_policy. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['async', 'sync', 'continuous']),
    )
    r""" The type field of the xc_snapmirror_policy.

Valid choices:

* async
* sync
* continuous """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_snapmirror_policy.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcSnapmirrorPolicy

    gettable_fields = [
        "links",
        "archive",
        "comment",
        "copy_all_source_snapshots",
        "copy_latest_source_snapshot",
        "create_snapshot_on_source",
        "identity_preservation",
        "name",
        "network_compression_enabled",
        "retention",
        "rpo",
        "scope",
        "snapshot_lock_mode",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "sync_common_snapshot_schedule.links",
        "sync_common_snapshot_schedule.name",
        "sync_common_snapshot_schedule.uuid",
        "sync_type",
        "throttle",
        "transfer_schedule.links",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
        "type",
        "uuid",
    ]
    """links,archive,comment,copy_all_source_snapshots,copy_latest_source_snapshot,create_snapshot_on_source,identity_preservation,name,network_compression_enabled,retention,rpo,scope,snapshot_lock_mode,svm.links,svm.name,svm.uuid,sync_common_snapshot_schedule.links,sync_common_snapshot_schedule.name,sync_common_snapshot_schedule.uuid,sync_type,throttle,transfer_schedule.links,transfer_schedule.name,transfer_schedule.uuid,type,uuid,"""

    patchable_fields = [
        "archive",
        "comment",
        "identity_preservation",
        "network_compression_enabled",
        "retention",
        "rpo",
        "snapshot_lock_mode",
        "sync_common_snapshot_schedule.name",
        "sync_common_snapshot_schedule.uuid",
        "throttle",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
    ]
    """archive,comment,identity_preservation,network_compression_enabled,retention,rpo,snapshot_lock_mode,sync_common_snapshot_schedule.name,sync_common_snapshot_schedule.uuid,throttle,transfer_schedule.name,transfer_schedule.uuid,"""

    postable_fields = [
        "archive",
        "comment",
        "copy_all_source_snapshots",
        "copy_latest_source_snapshot",
        "create_snapshot_on_source",
        "identity_preservation",
        "name",
        "network_compression_enabled",
        "retention",
        "rpo",
        "snapshot_lock_mode",
        "svm.name",
        "svm.uuid",
        "sync_common_snapshot_schedule.name",
        "sync_common_snapshot_schedule.uuid",
        "sync_type",
        "throttle",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
        "type",
    ]
    """archive,comment,copy_all_source_snapshots,copy_latest_source_snapshot,create_snapshot_on_source,identity_preservation,name,network_compression_enabled,retention,rpo,snapshot_lock_mode,svm.name,svm.uuid,sync_common_snapshot_schedule.name,sync_common_snapshot_schedule.uuid,sync_type,throttle,transfer_schedule.name,transfer_schedule.uuid,type,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSnapmirrorPolicy.get_collection(fields=field)]
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
            raise NetAppRestError("XcSnapmirrorPolicy modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSnapmirrorPolicy(Resource):
    r""" snapmirror_policy clone for cluster peer. """

    _schema = XcSnapmirrorPolicySchema
    _path = "/api/svm/peers/{peer[uuid]}/snapmirror/policies"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET snapmirror policies"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc snapmirror policy show")
        def xc_snapmirror_policy_show(
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            copy_all_source_snapshots: Choices.define(_get_field_list("copy_all_source_snapshots"), cache_choices=True, inexact=True)=None,
            copy_latest_source_snapshot: Choices.define(_get_field_list("copy_latest_source_snapshot"), cache_choices=True, inexact=True)=None,
            create_snapshot_on_source: Choices.define(_get_field_list("create_snapshot_on_source"), cache_choices=True, inexact=True)=None,
            identity_preservation: Choices.define(_get_field_list("identity_preservation"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            network_compression_enabled: Choices.define(_get_field_list("network_compression_enabled"), cache_choices=True, inexact=True)=None,
            rpo: Choices.define(_get_field_list("rpo"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            snapshot_lock_mode: Choices.define(_get_field_list("snapshot_lock_mode"), cache_choices=True, inexact=True)=None,
            sync_type: Choices.define(_get_field_list("sync_type"), cache_choices=True, inexact=True)=None,
            throttle: Choices.define(_get_field_list("throttle"), cache_choices=True, inexact=True)=None,
            type: Choices.define(_get_field_list("type"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "copy_all_source_snapshots", "copy_latest_source_snapshot", "create_snapshot_on_source", "identity_preservation", "name", "network_compression_enabled", "rpo", "scope", "snapshot_lock_mode", "sync_type", "throttle", "type", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSnapmirrorPolicy resources

            Args:
                comment: Comment associated with the policy.
                copy_all_source_snapshots: Specifies that all the source Snapshot copies (including the one created by SnapMirror before the transfer begins) should be copied to the destination on a transfer. \"Retention\" properties cannot be specified along with this property. This is applicable only to async policies. Property can only be set to 'true'.
                copy_latest_source_snapshot: Specifies that the latest source Snapshot copy (created by SnapMirror before the transfer begins) should be copied to the destination on a transfer. \"Retention\" properties cannot be specified along with this property. This is applicable only to async policies. Property can only be set to 'true'.
                create_snapshot_on_source: Specifies whether a new Snapshot copy should be created on the source at the beginning of an update or resync operation. This is applicable only to async policies. Property can only be set to 'false'.
                identity_preservation: Specifies which configuration of the source SVM is replicated to the destination SVM. This property is applicable only for SVM data protection with \"async\" policy type.
                name: Name of the policy.
                network_compression_enabled: Specifies whether network compression is enabled for transfers. This is applicable only to the policies of type \"async\".
                rpo: Specifies the duration of time for which a change to be propogated to a mirror should be delayed, in seconds. This is an intentional propagation delay between mirrors and is configurable down to zero, which means an immediate propogation. This is supported for policies of type 'continuous'.
                scope: Set to \"svm\" for policies owned by an SVM, otherwise set to \"cluster\".
                snapshot_lock_mode: Specifies the lock mode of the Snapshot copies stored in the object store. This property is applicable only to policies of type \"async\" with \"create_snapshot_on_source\" set to \"false\". When set to enterprise or compliance, the policy can be associated only with SnapMirror relationships where the source endpoint is a FlexVol volume and the destination endpoint is an object store. When set to compliance, no users can delete a Snapshot copy until the retention period has expired. When set to enterprise, users that have special permissions can delete a Snapshot copy before the retention period has expired.
                sync_type: 
                throttle: Throttle in KB/s. Default to unlimited.
                type: 
                uuid: 
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if copy_all_source_snapshots is not None:
                kwargs["copy_all_source_snapshots"] = copy_all_source_snapshots
            if copy_latest_source_snapshot is not None:
                kwargs["copy_latest_source_snapshot"] = copy_latest_source_snapshot
            if create_snapshot_on_source is not None:
                kwargs["create_snapshot_on_source"] = create_snapshot_on_source
            if identity_preservation is not None:
                kwargs["identity_preservation"] = identity_preservation
            if name is not None:
                kwargs["name"] = name
            if network_compression_enabled is not None:
                kwargs["network_compression_enabled"] = network_compression_enabled
            if rpo is not None:
                kwargs["rpo"] = rpo
            if scope is not None:
                kwargs["scope"] = scope
            if snapshot_lock_mode is not None:
                kwargs["snapshot_lock_mode"] = snapshot_lock_mode
            if sync_type is not None:
                kwargs["sync_type"] = sync_type
            if throttle is not None:
                kwargs["throttle"] = throttle
            if type is not None:
                kwargs["type"] = type
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSnapmirrorPolicy.get_collection(
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
        """Returns a count of all XcSnapmirrorPolicy resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET snapmirror policies"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






