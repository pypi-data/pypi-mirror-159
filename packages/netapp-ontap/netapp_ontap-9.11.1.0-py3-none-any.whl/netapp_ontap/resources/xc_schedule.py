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


__all__ = ["XcSchedule", "XcScheduleSchema"]
__pdoc__ = {
    "XcScheduleSchema.resource": False,
    "XcScheduleSchema.opts": False,
    "XcSchedule.xc_schedule_show": False,
    "XcSchedule.xc_schedule_create": False,
    "XcSchedule.xc_schedule_modify": False,
    "XcSchedule.xc_schedule_delete": False,
}


class XcScheduleSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSchedule object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_schedule. """

    cluster = fields.Nested("netapp_ontap.models.schedule_cluster.ScheduleClusterSchema", data_key="cluster", unknown=EXCLUDE)
    r""" The cluster field of the xc_schedule. """

    cron = fields.Nested("netapp_ontap.models.schedule_cron.ScheduleCronSchema", data_key="cron", unknown=EXCLUDE)
    r""" The cron field of the xc_schedule. """

    interval = fields.Str(
        data_key="interval",
    )
    r""" An ISO-8601 duration formatted string.

Example: P1DT2H3M4S """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=1, maximum=256),
    )
    r""" Schedule name. Required in the URL or POST body. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['cluster', 'svm']),
    )
    r""" If the schedule is owned by a data SVM, then the scope is set to svm. Otherwise it will be set to cluster.

Valid choices:

* cluster
* svm """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_schedule. """

    type = fields.Str(
        data_key="type",
        validate=enum_validation(['cron', 'interval']),
    )
    r""" Schedule type

Valid choices:

* cron
* interval """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Job schedule UUID

Example: 4ea7a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcSchedule

    gettable_fields = [
        "links",
        "cluster",
        "cron",
        "interval",
        "name",
        "scope",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "type",
        "uuid",
    ]
    """links,cluster,cron,interval,name,scope,svm.links,svm.name,svm.uuid,type,uuid,"""

    patchable_fields = [
        "cron",
        "interval",
    ]
    """cron,interval,"""

    postable_fields = [
        "cluster",
        "cron",
        "interval",
        "name",
        "svm.name",
        "svm.uuid",
    ]
    """cluster,cron,interval,name,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSchedule.get_collection(fields=field)]
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
            raise NetAppRestError("XcSchedule modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSchedule(Resource):
    r""" schedule clone for cluster peer. """

    _schema = XcScheduleSchema
    _path = "/api/cluster/peers/{peer[uuid]}/cluster/schedules"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET schedules"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc schedule show")
        def xc_schedule_show(
            peer_uuid,
            interval: Choices.define(_get_field_list("interval"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            type: Choices.define(_get_field_list("type"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["interval", "name", "scope", "type", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSchedule resources

            Args:
                interval: An ISO-8601 duration formatted string.
                name: Schedule name. Required in the URL or POST body.
                scope: If the schedule is owned by a data SVM, then the scope is set to svm. Otherwise it will be set to cluster.
                type: Schedule type
                uuid: Job schedule UUID
            """

            kwargs = {}
            if interval is not None:
                kwargs["interval"] = interval
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if type is not None:
                kwargs["type"] = type
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSchedule.get_collection(
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
        """Returns a count of all XcSchedule resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET schedules"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






