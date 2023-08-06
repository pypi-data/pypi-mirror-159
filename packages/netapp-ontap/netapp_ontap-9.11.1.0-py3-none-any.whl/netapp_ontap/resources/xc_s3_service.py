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


__all__ = ["XcS3Service", "XcS3ServiceSchema"]
__pdoc__ = {
    "XcS3ServiceSchema.resource": False,
    "XcS3ServiceSchema.opts": False,
    "XcS3Service.xc_s3_service_show": False,
    "XcS3Service.xc_s3_service_create": False,
    "XcS3Service.xc_s3_service_modify": False,
    "XcS3Service.xc_s3_service_delete": False,
}


class XcS3ServiceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcS3Service object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_s3_service. """

    buckets = fields.List(fields.Nested("netapp_ontap.resources.s3_bucket.S3BucketSchema", unknown=EXCLUDE), data_key="buckets")
    r""" The buckets field of the xc_s3_service. """

    certificate = fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", data_key="certificate", unknown=EXCLUDE)
    r""" The certificate field of the xc_s3_service. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=256),
    )
    r""" Can contain any additional information about the server being created or modified.

Example: S3 server """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies whether the S3 server being created or modified should be up or down. """

    is_http_enabled = fields.Boolean(
        data_key="is_http_enabled",
    )
    r""" Specifies whether HTTP is enabled on the S3 server being created or modified. By default, HTTP is disabled on the S3 server. """

    is_https_enabled = fields.Boolean(
        data_key="is_https_enabled",
    )
    r""" Specifies whether HTTPS is enabled on the S3 server being created or modified. By default, HTTPS is enabled on the S3 server. """

    metric = fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_s3_service. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=253),
    )
    r""" Specifies the name of the S3 server. A server name can contain 1 to 253 characters using only the following combination of characters':' 0-9, A-Z, a-z, ".", and "-".

Example: Server-1 """

    port = Size(
        data_key="port",
    )
    r""" Specifies the HTTP listener port for the S3 server. By default, HTTP is enabled on port 80. """

    secure_port = Size(
        data_key="secure_port",
    )
    r""" Specifies the HTTPS listener port for the S3 server. By default, HTTPS is enabled on port 443. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw_svm.PerformanceMetricRawSvmSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_s3_service. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_s3_service. """

    users = fields.List(fields.Nested("netapp_ontap.resources.s3_user.S3UserSchema", unknown=EXCLUDE), data_key="users")
    r""" The users field of the xc_s3_service. """

    @property
    def resource(self):
        return XcS3Service

    gettable_fields = [
        "links",
        "buckets",
        "certificate.links",
        "certificate.name",
        "certificate.uuid",
        "comment",
        "enabled",
        "is_http_enabled",
        "is_https_enabled",
        "metric.links",
        "metric.duration",
        "metric.iops",
        "metric.latency",
        "metric.status",
        "metric.throughput",
        "metric.timestamp",
        "name",
        "port",
        "secure_port",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "users",
    ]
    """links,buckets,certificate.links,certificate.name,certificate.uuid,comment,enabled,is_http_enabled,is_https_enabled,metric.links,metric.duration,metric.iops,metric.latency,metric.status,metric.throughput,metric.timestamp,name,port,secure_port,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,svm.links,svm.name,svm.uuid,users,"""

    patchable_fields = [
        "certificate.name",
        "certificate.uuid",
        "comment",
        "enabled",
        "is_http_enabled",
        "is_https_enabled",
        "name",
        "port",
        "secure_port",
    ]
    """certificate.name,certificate.uuid,comment,enabled,is_http_enabled,is_https_enabled,name,port,secure_port,"""

    postable_fields = [
        "buckets",
        "certificate.name",
        "certificate.uuid",
        "comment",
        "enabled",
        "is_http_enabled",
        "is_https_enabled",
        "name",
        "port",
        "secure_port",
        "svm.name",
        "svm.uuid",
        "users",
    ]
    """buckets,certificate.name,certificate.uuid,comment,enabled,is_http_enabled,is_https_enabled,name,port,secure_port,svm.name,svm.uuid,users,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcS3Service.get_collection(fields=field)]
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
            raise NetAppRestError("XcS3Service modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcS3Service(Resource):
    r""" s3_service clone for cluster peer. """

    _schema = XcS3ServiceSchema
    _path = "/api/svm/peers/{peer[uuid]}/protocols/s3/services"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves cross cluster S3 services."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc s3 service show")
        def xc_s3_service_show(
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            enabled: Choices.define(_get_field_list("enabled"), cache_choices=True, inexact=True)=None,
            is_http_enabled: Choices.define(_get_field_list("is_http_enabled"), cache_choices=True, inexact=True)=None,
            is_https_enabled: Choices.define(_get_field_list("is_https_enabled"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            port: Choices.define(_get_field_list("port"), cache_choices=True, inexact=True)=None,
            secure_port: Choices.define(_get_field_list("secure_port"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "enabled", "is_http_enabled", "is_https_enabled", "name", "port", "secure_port", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcS3Service resources

            Args:
                comment: Can contain any additional information about the server being created or modified.
                enabled: Specifies whether the S3 server being created or modified should be up or down.
                is_http_enabled: Specifies whether HTTP is enabled on the S3 server being created or modified. By default, HTTP is disabled on the S3 server.
                is_https_enabled: Specifies whether HTTPS is enabled on the S3 server being created or modified. By default, HTTPS is enabled on the S3 server.
                name: Specifies the name of the S3 server. A server name can contain 1 to 253 characters using only the following combination of characters':' 0-9, A-Z, a-z, \".\", and \"-\".
                port: Specifies the HTTP listener port for the S3 server. By default, HTTP is enabled on port 80.
                secure_port: Specifies the HTTPS listener port for the S3 server. By default, HTTPS is enabled on port 443.
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if enabled is not None:
                kwargs["enabled"] = enabled
            if is_http_enabled is not None:
                kwargs["is_http_enabled"] = is_http_enabled
            if is_https_enabled is not None:
                kwargs["is_https_enabled"] = is_https_enabled
            if name is not None:
                kwargs["name"] = name
            if port is not None:
                kwargs["port"] = port
            if secure_port is not None:
                kwargs["secure_port"] = secure_port
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcS3Service.get_collection(
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
        """Returns a count of all XcS3Service resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves cross cluster S3 services."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






