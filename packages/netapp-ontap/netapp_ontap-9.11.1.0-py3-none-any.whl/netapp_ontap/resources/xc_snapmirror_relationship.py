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


__all__ = ["XcSnapmirrorRelationship", "XcSnapmirrorRelationshipSchema"]
__pdoc__ = {
    "XcSnapmirrorRelationshipSchema.resource": False,
    "XcSnapmirrorRelationshipSchema.opts": False,
    "XcSnapmirrorRelationship.xc_snapmirror_relationship_show": False,
    "XcSnapmirrorRelationship.xc_snapmirror_relationship_create": False,
    "XcSnapmirrorRelationship.xc_snapmirror_relationship_modify": False,
    "XcSnapmirrorRelationship.xc_snapmirror_relationship_delete": False,
}


class XcSnapmirrorRelationshipSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSnapmirrorRelationship object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_snapmirror_relationship. """

    consistency_group_failover = fields.Nested("netapp_ontap.models.snapmirror_consistency_group_failover.SnapmirrorConsistencyGroupFailoverSchema", data_key="consistency_group_failover", unknown=EXCLUDE)
    r""" The consistency_group_failover field of the xc_snapmirror_relationship. """

    create_destination = fields.Nested("netapp_ontap.models.snapmirror_destination_creation.SnapmirrorDestinationCreationSchema", data_key="create_destination", unknown=EXCLUDE)
    r""" The create_destination field of the xc_snapmirror_relationship. """

    destination = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", data_key="destination", unknown=EXCLUDE)
    r""" This property is the destination endpoint of the relationship. The destination endpoint can be a FlexVol volume, FlexGroup volume, Consistency Group, object store, or SVM. For the POST request, the destination endpoint must be of type "DP" when the endpoint is a FlexVol volume or a FlexGroup volume. When specifying a Consistency Group as the destination endpoint, the "destination.consistency_group_volumes" property must be specified with the FlexVol volumes of type "DP". The POST request for SVM must have a destination endpoint of type "dp-destination". The destination endpoint path name must be specified in the "destination.path" property. For relationships of type "async", the destination endpoint for FlexVol volume and FlexGroup volume will change to type "RW" when the relationship status is "broken_off" and will revert to type "DP" when the relationship status is "snapmirrored" or "in_sync" using the PATCH request. The destination endpoint for SVM will change from "dp-destination" to type "default" when the relationship status is "broken_off" and will revert to type "dp-destination" when the relationship status is "snapmirrored" using the PATCH request. When the destination endpoint is a Consistency Group, the Consistency Group FlexVol volumes will change to type "RW" when the relationship status is "broken_off" and will revert to type "DP" when the relationship status is "in_sync" using the PATCH request. """

    exported_snapshot = fields.Str(
        data_key="exported_snapshot",
    )
    r""" Snapshot copy exported to clients on destination. """

    fabriclink = fields.Nested("netapp_ontap.models.snapmirror_relationship_fabriclink.SnapmirrorRelationshipFabriclinkSchema", data_key="fabriclink", unknown=EXCLUDE)
    r""" The fabriclink field of the xc_snapmirror_relationship. """

    group_type = fields.Str(
        data_key="group_type",
        validate=enum_validation(['none', 'svm_dr', 'consistency_group', 'flexgroup']),
    )
    r""" Specifies the group type of the top level SnapMirror relationship. The volume relationships are shown as _none_, the SVMDR relationships are shown as _svm_dr_, the Consistency Group relationships are shown as _consistency_group_, and the FlexGroup volume relationships are shown as _flexgroup_.

Valid choices:

* none
* svm_dr
* consistency_group
* flexgroup """

    healthy = fields.Boolean(
        data_key="healthy",
    )
    r""" Is the relationship healthy? """

    identity_preservation = fields.Str(
        data_key="identity_preservation",
        validate=enum_validation(['full', 'exclude_network_config', 'exclude_network_and_protocol_config']),
    )
    r""" Specifies which configuration of the source SVM is replicated to the destination SVM. This property is applicable only for SVM data protection with "async" policy type. This "identity_preservation" overrides the "identity_preservation" set on the SnapMirror relationship's policy.

Valid choices:

* full
* exclude_network_config
* exclude_network_and_protocol_config """

    lag_time = fields.Str(
        data_key="lag_time",
    )
    r""" Time since the exported Snapshot copy was created.

Example: PT8H35M42S """

    last_transfer_type = fields.Str(
        data_key="last_transfer_type",
        validate=enum_validation(['initialize', 'update', 'resync', 'restore']),
    )
    r""" Specifies the operation type of the last transfer that occured on the relationship. The _initialize_ transfer occurs when the relationship state changes from uninitialized to snapmirrored or in_sync. The _update_ transfer occurs when the snapshots are transferred from the source endpoint to the destination endpoint as part of scheduled or manual update. The _resync_ transfer occurs when the relationship state changes from broken_off to snapmirrored or in_sync. The _restore_ transfer occurs when the snapshot is restored from a destination endpoint to another endpoint.

Valid choices:

* initialize
* update
* resync
* restore """

    policy = fields.Nested("netapp_ontap.models.snapmirror_relationship_policy.SnapmirrorRelationshipPolicySchema", data_key="policy", unknown=EXCLUDE)
    r""" The policy field of the xc_snapmirror_relationship. """

    preserve = fields.Boolean(
        data_key="preserve",
    )
    r""" Set to true on resync to preserve Snapshot copies on the destination that are newer than the latest common Snapshot copy. This property is applicable only for relationships with FlexVol volume or FlexGroup volume endpoints and when the PATCH state is being changed to "snapmirrored". """

    quick_resync = fields.Boolean(
        data_key="quick_resync",
    )
    r""" Set to true to reduce resync time by not preserving storage efficiency. This property is applicable only for relationships with FlexVol volume endpoints and SVMDR relationships when the PATCH state is being changed to "snapmirrored". """

    recover_after_break = fields.Boolean(
        data_key="recover_after_break",
    )
    r""" Set to true to recover from a failed SnapMirror break operation on a FlexGroup volume relationship. This restores all destination FlexGroup constituent volumes to the latest Snapshot copy, and any writes to the read-write constituents are lost. This property is applicable only for SnapMirror relationships with FlexGroup volume endpoints and when the PATCH state is being changed to "broken_off". """

    restore = fields.Boolean(
        data_key="restore",
    )
    r""" Set to true to create a relationship for restore. To trigger restore-transfer, use transfers POST on the restore relationship. SnapMirror relationships with the policy type "async" can be restored. SnapMirror relationships with the policy type "sync" cannot be restored. """

    restore_to_snapshot = fields.Str(
        data_key="restore_to_snapshot",
    )
    r""" Specifies the Snapshot copy to restore to on the destination during the break operation. This property is applicable only for SnapMirror relationships with FlexVol volume endpoints and when the PATCH state is being changed to "broken_off". """

    source = fields.Nested("netapp_ontap.models.snapmirror_endpoint.SnapmirrorEndpointSchema", data_key="source", unknown=EXCLUDE)
    r""" This property is the source endpoint of the relationship. The source endpoint can be a FlexVol volume, FlexGroup volume, Consistency Group, object store, or SVM. To establish a SnapMirror relationship with SVM as source endpoint, the SVM must have only FlexVol volumes. For a Consistency Group this property identifies the source Consistency Group name. When specifying a Consistency Group as the source endpoint, the "source.consistency_group_volumes" property must be specified with the FlexVol volumes of type "RW". FlexVol volumes of type "DP" cannot be specified in the "source.consistency_group_volumes" list. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['broken_off', 'paused', 'snapmirrored', 'uninitialized', 'in_sync', 'out_of_sync', 'synchronizing']),
    )
    r""" State of the relationship.<br>To initialize the relationship, PATCH the state to "snapmirrored" for relationships with a policy of type "async" or to state "in_sync" for relationships with a policy of type "sync".<br>To break the relationship, PATCH the state to "broken_off" for relationships with a policy of type "async" or "sync". SnapMirror relationships with the policy type as "sync" and "sync_type" as "automated_failover" cannot be "broken_off".<br>To resync the relationship, PATCH the state to "snapmirrored" for relationships with a policy of type "async" or to state "in_sync" for relationships with a policy of type "sync". SnapMirror relationships with the policy type as "sync" and "sync_type" as "automated_failover" can be in "broken_off" state due to a failed attempt of SnapMirror failover.<br>To pause the relationship, suspending further transfers, PATCH the state to "paused" for relationships with a policy of type "async" or "sync". SnapMirror relationships with the policy type as "sync" and "sync_type" as "automated_failover" cannot be "paused".<br>To resume transfers for a paused relationship, PATCH the state to "snapmirrored" for relationships with a policy of type "async" or to state "in_sync" for relationships with a policy of type "sync".<br>The entries "in_sync", "out_of_sync", and "synchronizing" are only applicable to relationships with a policy of type "sync". A PATCH call on the state change only triggers the transition to the specified state. You must poll on the "state", "healthy" and "unhealthy_reason" properties using a GET request to determine if the transition is successful. To automatically initialize the relationship when specifying "create_destination" property, set the state to "snapmirrored" for relationships with a policy of type "async" or to state "in_sync" for relationships with a policy of type "sync".

Valid choices:

* broken_off
* paused
* snapmirrored
* uninitialized
* in_sync
* out_of_sync
* synchronizing """

    throttle = Size(
        data_key="throttle",
    )
    r""" Throttle, in KBs per second. This "throttle" overrides the "throttle" set on the SnapMirror relationship's policy. If neither of these are set, defaults to 0, which is interpreted as unlimited. """

    transfer = fields.Nested("netapp_ontap.models.snapmirror_relationship_transfer.SnapmirrorRelationshipTransferSchema", data_key="transfer", unknown=EXCLUDE)
    r""" The transfer field of the xc_snapmirror_relationship. """

    transfer_schedule = fields.Nested("netapp_ontap.resources.schedule.ScheduleSchema", data_key="transfer_schedule", unknown=EXCLUDE)
    r""" The transfer_schedule field of the xc_snapmirror_relationship. """

    unhealthy_reason = fields.List(fields.Nested("netapp_ontap.models.snapmirror_error.SnapmirrorErrorSchema", unknown=EXCLUDE), data_key="unhealthy_reason")
    r""" Reason the relationship is not healthy. It is a concatenation of up to four levels of error messages.

Example: [{"code":"6621444","message":"Failed to complete update operation on one or more item relationships.","parameters":[]},{"code":"6621445","message":"Group Update failed","parameters":[]}] """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_snapmirror_relationship.

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcSnapmirrorRelationship

    gettable_fields = [
        "links",
        "consistency_group_failover",
        "destination",
        "exported_snapshot",
        "fabriclink",
        "group_type",
        "healthy",
        "identity_preservation",
        "lag_time",
        "last_transfer_type",
        "policy",
        "restore",
        "source",
        "state",
        "throttle",
        "transfer",
        "transfer_schedule.links",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
        "unhealthy_reason",
        "uuid",
    ]
    """links,consistency_group_failover,destination,exported_snapshot,fabriclink,group_type,healthy,identity_preservation,lag_time,last_transfer_type,policy,restore,source,state,throttle,transfer,transfer_schedule.links,transfer_schedule.name,transfer_schedule.uuid,unhealthy_reason,uuid,"""

    patchable_fields = [
        "destination",
        "group_type",
        "identity_preservation",
        "last_transfer_type",
        "policy",
        "preserve",
        "quick_resync",
        "recover_after_break",
        "restore_to_snapshot",
        "source",
        "state",
        "throttle",
        "transfer",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
    ]
    """destination,group_type,identity_preservation,last_transfer_type,policy,preserve,quick_resync,recover_after_break,restore_to_snapshot,source,state,throttle,transfer,transfer_schedule.name,transfer_schedule.uuid,"""

    postable_fields = [
        "create_destination",
        "destination",
        "group_type",
        "identity_preservation",
        "last_transfer_type",
        "policy",
        "restore",
        "source",
        "state",
        "throttle",
        "transfer",
        "transfer_schedule.name",
        "transfer_schedule.uuid",
    ]
    """create_destination,destination,group_type,identity_preservation,last_transfer_type,policy,restore,source,state,throttle,transfer,transfer_schedule.name,transfer_schedule.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSnapmirrorRelationship.get_collection(fields=field)]
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
            raise NetAppRestError("XcSnapmirrorRelationship modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSnapmirrorRelationship(Resource):
    r""" snapmirror_relationship clone for cluster peer. """

    _schema = XcSnapmirrorRelationshipSchema
    _path = "/api/cluster/peers/{peer[uuid]}/snapmirror/relationships"
    _keys = ["peer.uuid", "uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET snapmirror config"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc snapmirror relationship show")
        def xc_snapmirror_relationship_show(
            peer_uuid,
            exported_snapshot: Choices.define(_get_field_list("exported_snapshot"), cache_choices=True, inexact=True)=None,
            group_type: Choices.define(_get_field_list("group_type"), cache_choices=True, inexact=True)=None,
            healthy: Choices.define(_get_field_list("healthy"), cache_choices=True, inexact=True)=None,
            identity_preservation: Choices.define(_get_field_list("identity_preservation"), cache_choices=True, inexact=True)=None,
            lag_time: Choices.define(_get_field_list("lag_time"), cache_choices=True, inexact=True)=None,
            last_transfer_type: Choices.define(_get_field_list("last_transfer_type"), cache_choices=True, inexact=True)=None,
            preserve: Choices.define(_get_field_list("preserve"), cache_choices=True, inexact=True)=None,
            quick_resync: Choices.define(_get_field_list("quick_resync"), cache_choices=True, inexact=True)=None,
            recover_after_break: Choices.define(_get_field_list("recover_after_break"), cache_choices=True, inexact=True)=None,
            restore: Choices.define(_get_field_list("restore"), cache_choices=True, inexact=True)=None,
            restore_to_snapshot: Choices.define(_get_field_list("restore_to_snapshot"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            throttle: Choices.define(_get_field_list("throttle"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["exported_snapshot", "group_type", "healthy", "identity_preservation", "lag_time", "last_transfer_type", "preserve", "quick_resync", "recover_after_break", "restore", "restore_to_snapshot", "state", "throttle", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSnapmirrorRelationship resources

            Args:
                exported_snapshot: Snapshot copy exported to clients on destination.
                group_type: Specifies the group type of the top level SnapMirror relationship. The volume relationships are shown as _none_, the SVMDR relationships are shown as _svm_dr_, the Consistency Group relationships are shown as _consistency_group_, and the FlexGroup volume relationships are shown as _flexgroup_.
                healthy: Is the relationship healthy?
                identity_preservation: Specifies which configuration of the source SVM is replicated to the destination SVM. This property is applicable only for SVM data protection with \"async\" policy type. This \"identity_preservation\" overrides the \"identity_preservation\" set on the SnapMirror relationship's policy.
                lag_time: Time since the exported Snapshot copy was created.
                last_transfer_type: Specifies the operation type of the last transfer that occured on the relationship. The _initialize_ transfer occurs when the relationship state changes from uninitialized to snapmirrored or in_sync. The _update_ transfer occurs when the snapshots are transferred from the source endpoint to the destination endpoint as part of scheduled or manual update. The _resync_ transfer occurs when the relationship state changes from broken_off to snapmirrored or in_sync. The _restore_ transfer occurs when the snapshot is restored from a destination endpoint to another endpoint.
                preserve: Set to true on resync to preserve Snapshot copies on the destination that are newer than the latest common Snapshot copy. This property is applicable only for relationships with FlexVol volume or FlexGroup volume endpoints and when the PATCH state is being changed to \"snapmirrored\".
                quick_resync: Set to true to reduce resync time by not preserving storage efficiency. This property is applicable only for relationships with FlexVol volume endpoints and SVMDR relationships when the PATCH state is being changed to \"snapmirrored\".
                recover_after_break: Set to true to recover from a failed SnapMirror break operation on a FlexGroup volume relationship. This restores all destination FlexGroup constituent volumes to the latest Snapshot copy, and any writes to the read-write constituents are lost. This property is applicable only for SnapMirror relationships with FlexGroup volume endpoints and when the PATCH state is being changed to \"broken_off\".
                restore: Set to true to create a relationship for restore. To trigger restore-transfer, use transfers POST on the restore relationship. SnapMirror relationships with the policy type \"async\" can be restored. SnapMirror relationships with the policy type \"sync\" cannot be restored.
                restore_to_snapshot: Specifies the Snapshot copy to restore to on the destination during the break operation. This property is applicable only for SnapMirror relationships with FlexVol volume endpoints and when the PATCH state is being changed to \"broken_off\".
                state: State of the relationship.<br>To initialize the relationship, PATCH the state to \"snapmirrored\" for relationships with a policy of type \"async\" or to state \"in_sync\" for relationships with a policy of type \"sync\".<br>To break the relationship, PATCH the state to \"broken_off\" for relationships with a policy of type \"async\" or \"sync\". SnapMirror relationships with the policy type as \"sync\" and \"sync_type\" as \"automated_failover\" cannot be \"broken_off\".<br>To resync the relationship, PATCH the state to \"snapmirrored\" for relationships with a policy of type \"async\" or to state \"in_sync\" for relationships with a policy of type \"sync\". SnapMirror relationships with the policy type as \"sync\" and \"sync_type\" as \"automated_failover\" can be in \"broken_off\" state due to a failed attempt of SnapMirror failover.<br>To pause the relationship, suspending further transfers, PATCH the state to \"paused\" for relationships with a policy of type \"async\" or \"sync\". SnapMirror relationships with the policy type as \"sync\" and \"sync_type\" as \"automated_failover\" cannot be \"paused\".<br>To resume transfers for a paused relationship, PATCH the state to \"snapmirrored\" for relationships with a policy of type \"async\" or to state \"in_sync\" for relationships with a policy of type \"sync\".<br>The entries \"in_sync\", \"out_of_sync\", and \"synchronizing\" are only applicable to relationships with a policy of type \"sync\". A PATCH call on the state change only triggers the transition to the specified state. You must poll on the \"state\", \"healthy\" and \"unhealthy_reason\" properties using a GET request to determine if the transition is successful. To automatically initialize the relationship when specifying \"create_destination\" property, set the state to \"snapmirrored\" for relationships with a policy of type \"async\" or to state \"in_sync\" for relationships with a policy of type \"sync\".
                throttle: Throttle, in KBs per second. This \"throttle\" overrides the \"throttle\" set on the SnapMirror relationship's policy. If neither of these are set, defaults to 0, which is interpreted as unlimited.
                uuid: 
            """

            kwargs = {}
            if exported_snapshot is not None:
                kwargs["exported_snapshot"] = exported_snapshot
            if group_type is not None:
                kwargs["group_type"] = group_type
            if healthy is not None:
                kwargs["healthy"] = healthy
            if identity_preservation is not None:
                kwargs["identity_preservation"] = identity_preservation
            if lag_time is not None:
                kwargs["lag_time"] = lag_time
            if last_transfer_type is not None:
                kwargs["last_transfer_type"] = last_transfer_type
            if preserve is not None:
                kwargs["preserve"] = preserve
            if quick_resync is not None:
                kwargs["quick_resync"] = quick_resync
            if recover_after_break is not None:
                kwargs["recover_after_break"] = recover_after_break
            if restore is not None:
                kwargs["restore"] = restore
            if restore_to_snapshot is not None:
                kwargs["restore_to_snapshot"] = restore_to_snapshot
            if state is not None:
                kwargs["state"] = state
            if throttle is not None:
                kwargs["throttle"] = throttle
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSnapmirrorRelationship.get_collection(
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
        """Returns a count of all XcSnapmirrorRelationship resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET snapmirror config"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Cross cluster GET snapmirror relationship config"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





