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


__all__ = ["XcConsistencyGroup", "XcConsistencyGroupSchema"]
__pdoc__ = {
    "XcConsistencyGroupSchema.resource": False,
    "XcConsistencyGroupSchema.opts": False,
    "XcConsistencyGroup.xc_consistency_group_show": False,
    "XcConsistencyGroup.xc_consistency_group_create": False,
    "XcConsistencyGroup.xc_consistency_group_modify": False,
    "XcConsistencyGroup.xc_consistency_group_delete": False,
}


class XcConsistencyGroupSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcConsistencyGroup object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_consistency_group. """

    consistency_groups = fields.List(fields.Nested("netapp_ontap.models.consistency_group_child.ConsistencyGroupChildSchema", unknown=EXCLUDE), data_key="consistency_groups")
    r""" A consistency group is a mutually exclusive aggregation of volumes or other consistency groups. A consistency group can only be associated with one direct parent consistency group. """

    luns = fields.List(fields.Nested("netapp_ontap.models.consistency_group_lun.ConsistencyGroupLunSchema", unknown=EXCLUDE), data_key="luns")
    r""" The LUNs array can be used to create or modify LUNs in a consistency group on a new or existing volume that is a member of the consistency group. LUNs are considered members of a consistency group if they are located on a volume that is a member of the consistency group. """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the consistency group. The consistency group name must be unique within an SVM.<br/>
If not provided and the consistency group contains only one volume, the name will be generated based on the volume name. If the consistency group contains more than one volume, the name is required. """

    namespaces = fields.List(fields.Nested("netapp_ontap.models.consistency_group_namespace.ConsistencyGroupNamespaceSchema", unknown=EXCLUDE), data_key="namespaces")
    r""" An NVMe namespace is a collection of addressable logical blocks presented to hosts connected to the SVM using the NVMe over Fabrics protocol.
In ONTAP, an NVMe namespace is located within a volume. Optionally, it can be located within a qtree in a volume.<br/>
An NVMe namespace is created to a specified size using thin or thick provisioning as determined by the volume on which it is created. NVMe namespaces support being cloned. An NVMe namespace cannot be renamed, resized, or moved to a different volume. NVMe namespaces do not support the assignment of a QoS policy for performance management, but a QoS policy can be assigned to the volume containing the namespace. See the NVMe namespace object model to learn more about each of the properties supported by the NVMe namespace REST API.<br/>
An NVMe namespace must be mapped to an NVMe subsystem to grant access to the subsystem's hosts. Hosts can then access the NVMe namespace and perform I/O using the NVMe over Fabrics protocol. """

    parent_consistency_group = fields.Nested("netapp_ontap.resources.consistency_group.ConsistencyGroupSchema", data_key="parent_consistency_group", unknown=EXCLUDE)
    r""" The parent_consistency_group field of the xc_consistency_group. """

    provisioning_options = fields.Nested("netapp_ontap.models.consistency_group_provisioning_options.ConsistencyGroupProvisioningOptionsSchema", data_key="provisioning_options", unknown=EXCLUDE)
    r""" The provisioning_options field of the xc_consistency_group. """

    qos = fields.Nested("netapp_ontap.models.consistency_group_qos.ConsistencyGroupQosSchema", data_key="qos", unknown=EXCLUDE)
    r""" The qos field of the xc_consistency_group. """

    replicated = fields.Boolean(
        data_key="replicated",
    )
    r""" Indicates whether or not replication has been enabled on this consistency group. """

    replication_source = fields.Boolean(
        data_key="replication_source",
    )
    r""" Indicates whether or not this consistency group is the source for replication. """

    restore_to = fields.Nested("netapp_ontap.models.consistency_group_consistency_groups_restore_to.ConsistencyGroupConsistencyGroupsRestoreToSchema", data_key="restore_to", unknown=EXCLUDE)
    r""" The restore_to field of the xc_consistency_group. """

    snapshot_policy = fields.Nested("netapp_ontap.resources.snapshot_policy.SnapshotPolicySchema", data_key="snapshot_policy", unknown=EXCLUDE)
    r""" The Snapshot copy policy of the consistency group.<br/>
This is the dedicated consistency group Snapshot copy policy, not an aggregation of the volume granular Snapshot copy policy. """

    space = fields.Nested("netapp_ontap.models.consistency_group_space.ConsistencyGroupSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the xc_consistency_group. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_consistency_group. """

    tiering = fields.Nested("netapp_ontap.models.consistency_group_tiering.ConsistencyGroupTieringSchema", data_key="tiering", unknown=EXCLUDE)
    r""" The tiering field of the xc_consistency_group. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the consistency group. The UUID is generated by ONTAP when the consistency group is created.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    volumes = fields.List(fields.Nested("netapp_ontap.models.xc_consistency_group_consistency_groups_volumes.XcConsistencyGroupConsistencyGroupsVolumesSchema", unknown=EXCLUDE), data_key="volumes")
    r""" A consistency group is a mutually exclusive aggregation of volumes or other consistency groups. A volume can only be associated with one direct parent consistency group.<br/>
The volumes array can be used to create new volumes in the consistency group, add existing volumes to the consistency group, or modify existing volumes that are already members of the consistency group.<br/>
The total number of volumes across all child consistency groups contained in a consistency group is constrained by the same limit. """

    @property
    def resource(self):
        return XcConsistencyGroup

    gettable_fields = [
        "links",
        "consistency_groups",
        "luns",
        "name",
        "parent_consistency_group.links",
        "parent_consistency_group.name",
        "parent_consistency_group.uuid",
        "qos",
        "replicated",
        "replication_source",
        "snapshot_policy.links",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
        "space",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "tiering",
        "uuid",
        "volumes",
    ]
    """links,consistency_groups,luns,name,parent_consistency_group.links,parent_consistency_group.name,parent_consistency_group.uuid,qos,replicated,replication_source,snapshot_policy.links,snapshot_policy.name,snapshot_policy.uuid,space,svm.links,svm.name,svm.uuid,tiering,uuid,volumes,"""

    patchable_fields = [
        "consistency_groups",
        "luns",
        "namespaces",
        "provisioning_options",
        "qos",
        "restore_to",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
    ]
    """consistency_groups,luns,namespaces,provisioning_options,qos,restore_to,snapshot_policy.name,snapshot_policy.uuid,"""

    postable_fields = [
        "consistency_groups",
        "luns",
        "name",
        "provisioning_options",
        "qos",
        "snapshot_policy.name",
        "snapshot_policy.uuid",
        "svm.name",
        "svm.uuid",
        "tiering",
        "volumes",
    ]
    """consistency_groups,luns,name,provisioning_options,qos,snapshot_policy.name,snapshot_policy.uuid,svm.name,svm.uuid,tiering,volumes,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcConsistencyGroup.get_collection(fields=field)]
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
            raise NetAppRestError("XcConsistencyGroup modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcConsistencyGroup(Resource):
    r""" consistency_group clone for cluster peer. """

    _schema = XcConsistencyGroupSchema
    _path = "/api/cluster/peers/{peer[uuid]}/application/consistency-groups"
    _keys = ["peer.uuid", "uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET Consistency Groups"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc consistency group show")
        def xc_consistency_group_show(
            peer_uuid,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            replicated: Choices.define(_get_field_list("replicated"), cache_choices=True, inexact=True)=None,
            replication_source: Choices.define(_get_field_list("replication_source"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["name", "replicated", "replication_source", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcConsistencyGroup resources

            Args:
                name: Name of the consistency group. The consistency group name must be unique within an SVM.<br/> If not provided and the consistency group contains only one volume, the name will be generated based on the volume name. If the consistency group contains more than one volume, the name is required. 
                replicated: Indicates whether or not replication has been enabled on this consistency group. 
                replication_source: Indicates whether or not this consistency group is the source for replication. 
                uuid: The unique identifier of the consistency group. The UUID is generated by ONTAP when the consistency group is created. 
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if replicated is not None:
                kwargs["replicated"] = replicated
            if replication_source is not None:
                kwargs["replication_source"] = replication_source
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcConsistencyGroup.get_collection(
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
        """Returns a count of all XcConsistencyGroup resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET Consistency Groups"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Cross cluster GET Consistency Groups"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





