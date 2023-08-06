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


__all__ = ["XcS3Bucket", "XcS3BucketSchema"]
__pdoc__ = {
    "XcS3BucketSchema.resource": False,
    "XcS3BucketSchema.opts": False,
    "XcS3Bucket.xc_s3_bucket_show": False,
    "XcS3Bucket.xc_s3_bucket_create": False,
    "XcS3Bucket.xc_s3_bucket_modify": False,
    "XcS3Bucket.xc_s3_bucket_delete": False,
}


class XcS3BucketSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcS3Bucket object"""

    aggregates = fields.List(fields.Nested("netapp_ontap.models.volume_aggregates.VolumeAggregatesSchema", unknown=EXCLUDE), data_key="aggregates")
    r""" A list of aggregates for FlexGroup volume constituents where the bucket is hosted. If this option is not specified, the bucket is auto-provisioned as a FlexGroup volume. """

    audit_event_selector = fields.Nested("netapp_ontap.models.s3_audit_event_selector.S3AuditEventSelectorSchema", data_key="audit_event_selector", unknown=EXCLUDE)
    r""" The audit_event_selector field of the xc_s3_bucket. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Can contain any additional information about the bucket being created or modified.

Example: S3 bucket. """

    constituents_per_aggregate = Size(
        data_key="constituents_per_aggregate",
        validate=integer_validation(minimum=1, maximum=1000),
    )
    r""" Specifies the number of constituents or FlexVol volumes per aggregate. A FlexGroup volume consisting of all such constituents across all specified aggregates is created. This option is used along with the aggregates option and cannot be used independently.

Example: 4 """

    encryption = fields.Nested("netapp_ontap.models.s3_bucket_encryption.S3BucketEncryptionSchema", data_key="encryption", unknown=EXCLUDE)
    r""" The encryption field of the xc_s3_bucket. """

    logical_used_size = Size(
        data_key="logical_used_size",
    )
    r""" Specifies the bucket logical used size up to this point. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=3, maximum=63),
    )
    r""" Specifies the name of the bucket. Bucket name is a string that can only contain the following combination of ASCII-range alphanumeric characters 0-9, a-z, ".", and "-".

Example: bucket1 """

    policy = fields.Nested("netapp_ontap.models.s3_bucket_policy.S3BucketPolicySchema", data_key="policy", unknown=EXCLUDE)
    r""" The policy field of the xc_s3_bucket. """

    protection_status = fields.Nested("netapp_ontap.models.s3_bucket_protection_status.S3BucketProtectionStatusSchema", data_key="protection_status", unknown=EXCLUDE)
    r""" The protection_status field of the xc_s3_bucket. """

    qos_policy = fields.Nested("netapp_ontap.resources.qos_policy.QosPolicySchema", data_key="qos_policy", unknown=EXCLUDE)
    r""" The qos_policy field of the xc_s3_bucket. """

    role = fields.Str(
        data_key="role",
        validate=enum_validation(['standalone', 'active', 'passive']),
    )
    r""" Specifies the role of the bucket.

Valid choices:

* standalone
* active
* passive """

    size = Size(
        data_key="size",
        validate=integer_validation(minimum=83886080, maximum=70368744177664),
    )
    r""" Specifies the bucket size in bytes; ranges from 80MB to 64TB.

Example: 1677721600 """

    storage_service_level = fields.Str(
        data_key="storage_service_level",
        validate=enum_validation(['value', 'performance', 'extreme']),
    )
    r""" Specifies the storage service level of the FlexGroup volume on which the bucket should be created. Valid values are "value", "performance" or "extreme".

Valid choices:

* value
* performance
* extreme """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_s3_bucket. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Specifies the unique identifier of the bucket.

Example: 414b29a1-3b26-11e9-bd58-0050568ea055 """

    versioning_state = fields.Str(
        data_key="versioning_state",
        validate=enum_validation(['disabled', 'enabled', 'suspended']),
    )
    r""" Specifies the versioning state of the bucket. Valid values are "disabled", "enabled" or "suspended". Note that the versioning state cannot be modified to 'disabled' from any other state.

Valid choices:

* disabled
* enabled
* suspended """

    volume = fields.Nested("netapp_ontap.resources.volume.VolumeSchema", data_key="volume", unknown=EXCLUDE)
    r""" The volume field of the xc_s3_bucket. """

    @property
    def resource(self):
        return XcS3Bucket

    gettable_fields = [
        "audit_event_selector",
        "comment",
        "encryption",
        "logical_used_size",
        "name",
        "policy",
        "protection_status",
        "qos_policy.links",
        "qos_policy.max_throughput_iops",
        "qos_policy.max_throughput_mbps",
        "qos_policy.min_throughput_iops",
        "qos_policy.min_throughput_mbps",
        "qos_policy.name",
        "qos_policy.uuid",
        "role",
        "size",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
        "versioning_state",
        "volume.links",
        "volume.name",
        "volume.uuid",
    ]
    """audit_event_selector,comment,encryption,logical_used_size,name,policy,protection_status,qos_policy.links,qos_policy.max_throughput_iops,qos_policy.max_throughput_mbps,qos_policy.min_throughput_iops,qos_policy.min_throughput_mbps,qos_policy.name,qos_policy.uuid,role,size,svm.links,svm.name,svm.uuid,uuid,versioning_state,volume.links,volume.name,volume.uuid,"""

    patchable_fields = [
        "audit_event_selector",
        "comment",
        "encryption",
        "policy",
        "protection_status",
        "qos_policy.max_throughput_iops",
        "qos_policy.max_throughput_mbps",
        "qos_policy.min_throughput_iops",
        "qos_policy.min_throughput_mbps",
        "qos_policy.name",
        "qos_policy.uuid",
        "size",
        "versioning_state",
        "volume.name",
        "volume.uuid",
    ]
    """audit_event_selector,comment,encryption,policy,protection_status,qos_policy.max_throughput_iops,qos_policy.max_throughput_mbps,qos_policy.min_throughput_iops,qos_policy.min_throughput_mbps,qos_policy.name,qos_policy.uuid,size,versioning_state,volume.name,volume.uuid,"""

    postable_fields = [
        "aggregates.links",
        "aggregates.name",
        "aggregates.uuid",
        "audit_event_selector",
        "comment",
        "constituents_per_aggregate",
        "encryption",
        "name",
        "policy",
        "protection_status",
        "qos_policy.max_throughput_iops",
        "qos_policy.max_throughput_mbps",
        "qos_policy.min_throughput_iops",
        "qos_policy.min_throughput_mbps",
        "qos_policy.name",
        "qos_policy.uuid",
        "size",
        "storage_service_level",
        "svm.name",
        "svm.uuid",
        "versioning_state",
        "volume.name",
        "volume.uuid",
    ]
    """aggregates.links,aggregates.name,aggregates.uuid,audit_event_selector,comment,constituents_per_aggregate,encryption,name,policy,protection_status,qos_policy.max_throughput_iops,qos_policy.max_throughput_mbps,qos_policy.min_throughput_iops,qos_policy.min_throughput_mbps,qos_policy.name,qos_policy.uuid,size,storage_service_level,svm.name,svm.uuid,versioning_state,volume.name,volume.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcS3Bucket.get_collection(fields=field)]
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
            raise NetAppRestError("XcS3Bucket modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcS3Bucket(Resource):
    r""" s3_bucket clone for cluster peer. """

    _schema = XcS3BucketSchema
    _path = "/api/svm/peers/{peer[uuid]}/protocols/s3/buckets"
    _keys = ["peer.uuid", "svm.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves cross cluster buckets on an S3 server."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc s3 bucket show")
        def xc_s3_bucket_show(
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            constituents_per_aggregate: Choices.define(_get_field_list("constituents_per_aggregate"), cache_choices=True, inexact=True)=None,
            logical_used_size: Choices.define(_get_field_list("logical_used_size"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            role: Choices.define(_get_field_list("role"), cache_choices=True, inexact=True)=None,
            size: Choices.define(_get_field_list("size"), cache_choices=True, inexact=True)=None,
            storage_service_level: Choices.define(_get_field_list("storage_service_level"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            versioning_state: Choices.define(_get_field_list("versioning_state"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "constituents_per_aggregate", "logical_used_size", "name", "role", "size", "storage_service_level", "uuid", "versioning_state", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcS3Bucket resources

            Args:
                comment: Can contain any additional information about the bucket being created or modified.
                constituents_per_aggregate: Specifies the number of constituents or FlexVol volumes per aggregate. A FlexGroup volume consisting of all such constituents across all specified aggregates is created. This option is used along with the aggregates option and cannot be used independently.
                logical_used_size: Specifies the bucket logical used size up to this point.
                name: Specifies the name of the bucket. Bucket name is a string that can only contain the following combination of ASCII-range alphanumeric characters 0-9, a-z, \".\", and \"-\".
                role: Specifies the role of the bucket.
                size: Specifies the bucket size in bytes; ranges from 80MB to 64TB.
                storage_service_level: Specifies the storage service level of the FlexGroup volume on which the bucket should be created. Valid values are \"value\", \"performance\" or \"extreme\".
                uuid: Specifies the unique identifier of the bucket.
                versioning_state: Specifies the versioning state of the bucket. Valid values are \"disabled\", \"enabled\" or \"suspended\". Note that the versioning state cannot be modified to 'disabled' from any other state.
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if constituents_per_aggregate is not None:
                kwargs["constituents_per_aggregate"] = constituents_per_aggregate
            if logical_used_size is not None:
                kwargs["logical_used_size"] = logical_used_size
            if name is not None:
                kwargs["name"] = name
            if role is not None:
                kwargs["role"] = role
            if size is not None:
                kwargs["size"] = size
            if storage_service_level is not None:
                kwargs["storage_service_level"] = storage_service_level
            if uuid is not None:
                kwargs["uuid"] = uuid
            if versioning_state is not None:
                kwargs["versioning_state"] = versioning_state
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcS3Bucket.get_collection(
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
        """Returns a count of all XcS3Bucket resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves cross cluster buckets on an S3 server."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






