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


__all__ = ["XcCifsService", "XcCifsServiceSchema"]
__pdoc__ = {
    "XcCifsServiceSchema.resource": False,
    "XcCifsServiceSchema.opts": False,
    "XcCifsService.xc_cifs_service_show": False,
    "XcCifsService.xc_cifs_service_create": False,
    "XcCifsService.xc_cifs_service_modify": False,
    "XcCifsService.xc_cifs_service_delete": False,
}


class XcCifsServiceSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcCifsService object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_cifs_service. """

    ad_domain = fields.Nested("netapp_ontap.models.ad_domain.AdDomainSchema", data_key="ad_domain", unknown=EXCLUDE)
    r""" The ad_domain field of the xc_cifs_service. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=48),
    )
    r""" A descriptive text comment for the CIFS server. SMB clients can see the CIFS server comment when browsing servers on the network. If there is a space in the comment, you must enclose the entire string in quotation marks.

Example: This CIFS Server Belongs to CS Department """

    default_unix_user = fields.Str(
        data_key="default_unix_user",
    )
    r""" Specifies the UNIX user to which any authenticated CIFS user is mapped to, if the normal user mapping rules fails. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Specifies if the CIFS service is administratively enabled. """

    metric = fields.Nested("netapp_ontap.models.performance_metric_svm.PerformanceMetricSvmSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_cifs_service. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=15),
    )
    r""" The name of the CIFS server.

Example: CIFS1 """

    netbios = fields.Nested("netapp_ontap.models.cifs_netbios.CifsNetbiosSchema", data_key="netbios", unknown=EXCLUDE)
    r""" The netbios field of the xc_cifs_service. """

    options = fields.Nested("netapp_ontap.models.cifs_service_options.CifsServiceOptionsSchema", data_key="options", unknown=EXCLUDE)
    r""" The options field of the xc_cifs_service. """

    security = fields.Nested("netapp_ontap.models.cifs_service_security.CifsServiceSecuritySchema", data_key="security", unknown=EXCLUDE)
    r""" The security field of the xc_cifs_service. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw_svm.PerformanceMetricRawSvmSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_cifs_service. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_cifs_service. """

    @property
    def resource(self):
        return XcCifsService

    gettable_fields = [
        "links",
        "ad_domain",
        "comment",
        "default_unix_user",
        "enabled",
        "metric.links",
        "metric.duration",
        "metric.iops",
        "metric.latency",
        "metric.status",
        "metric.throughput",
        "metric.timestamp",
        "name",
        "netbios",
        "options",
        "security",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "svm.links",
        "svm.name",
        "svm.uuid",
    ]
    """links,ad_domain,comment,default_unix_user,enabled,metric.links,metric.duration,metric.iops,metric.latency,metric.status,metric.throughput,metric.timestamp,name,netbios,options,security,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,svm.links,svm.name,svm.uuid,"""

    patchable_fields = [
        "ad_domain",
        "comment",
        "default_unix_user",
        "enabled",
        "name",
        "netbios",
        "options",
        "security",
        "svm.name",
        "svm.uuid",
    ]
    """ad_domain,comment,default_unix_user,enabled,name,netbios,options,security,svm.name,svm.uuid,"""

    postable_fields = [
        "ad_domain",
        "comment",
        "default_unix_user",
        "enabled",
        "name",
        "netbios",
        "options",
        "security",
        "svm.name",
        "svm.uuid",
    ]
    """ad_domain,comment,default_unix_user,enabled,name,netbios,options,security,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcCifsService.get_collection(fields=field)]
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
            raise NetAppRestError("XcCifsService modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcCifsService(Resource):
    r""" cifs_service clone for cluster peer. """

    _schema = XcCifsServiceSchema
    _path = "/api/svm/peers/{peer[uuid]}/protocols/cifs/services"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET CIFS services"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc cifs service show")
        def xc_cifs_service_show(
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            default_unix_user: Choices.define(_get_field_list("default_unix_user"), cache_choices=True, inexact=True)=None,
            enabled: Choices.define(_get_field_list("enabled"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "default_unix_user", "enabled", "name", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcCifsService resources

            Args:
                comment: A descriptive text comment for the CIFS server. SMB clients can see the CIFS server comment when browsing servers on the network. If there is a space in the comment, you must enclose the entire string in quotation marks.
                default_unix_user: Specifies the UNIX user to which any authenticated CIFS user is mapped to, if the normal user mapping rules fails.
                enabled: Specifies if the CIFS service is administratively enabled. 
                name: The name of the CIFS server.
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if default_unix_user is not None:
                kwargs["default_unix_user"] = default_unix_user
            if enabled is not None:
                kwargs["enabled"] = enabled
            if name is not None:
                kwargs["name"] = name
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcCifsService.get_collection(
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
        """Returns a count of all XcCifsService resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET CIFS services"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






