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


__all__ = ["XcEmsEvent", "XcEmsEventSchema"]
__pdoc__ = {
    "XcEmsEventSchema.resource": False,
    "XcEmsEventSchema.opts": False,
    "XcEmsEvent.xc_ems_event_show": False,
    "XcEmsEvent.xc_ems_event_create": False,
    "XcEmsEvent.xc_ems_event_modify": False,
    "XcEmsEvent.xc_ems_event_delete": False,
}


class XcEmsEventSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcEmsEvent object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_ems_event. """

    action = fields.Nested("netapp_ontap.models.ems_alert_action.EmsAlertActionSchema", data_key="action", unknown=EXCLUDE)
    r""" The action field of the xc_ems_event. """

    creation_time = ImpreciseDateTime(
        data_key="creation_time",
    )
    r""" Timestamp of the event creation. """

    index = Size(
        data_key="index",
    )
    r""" Index of the event. Returned by default.

Example: 1 """

    last_update_time = ImpreciseDateTime(
        data_key="last_update_time",
    )
    r""" Timestamp of the last update to the alert. """

    log_message = fields.Str(
        data_key="log_message",
    )
    r""" A formatted text string populated with parameter details. Returned by default. """

    message = fields.Nested("netapp_ontap.models.ems_event_message1.EmsEventMessage1Schema", data_key="message", unknown=EXCLUDE)
    r""" The message field of the xc_ems_event. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the xc_ems_event. """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_event_response_records_parameters.EmsEventResponseRecordsParametersSchema", unknown=EXCLUDE), data_key="parameters")
    r""" A list of parameters provided with the EMS event. """

    source = fields.Str(
        data_key="source",
    )
    r""" Source """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['stateless', 'opened', 'resolving', 'resolved', 'closed']),
    )
    r""" Indicates the event state. A stateful event tracks the state changes of a system condition and reflects the current system condition.

Valid choices:

* stateless
* opened
* resolving
* resolved
* closed """

    stateful = fields.Boolean(
        data_key="stateful",
    )
    r""" Indicates whether the event is stateful. A stateful event tracks the state changes of a system condition and reflects the current system condition while a stateless event simply reports a certain system condition that has occurred sometime in the past. """

    time = ImpreciseDateTime(
        data_key="time",
    )
    r""" Timestamp of the event. Returned by default. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The UUID that uniquely identifies the alert.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcEmsEvent

    gettable_fields = [
        "links",
        "action",
        "creation_time",
        "index",
        "last_update_time",
        "log_message",
        "message",
        "node.links",
        "node.name",
        "node.uuid",
        "parameters",
        "source",
        "state",
        "stateful",
        "time",
        "uuid",
    ]
    """links,action,creation_time,index,last_update_time,log_message,message,node.links,node.name,node.uuid,parameters,source,state,stateful,time,uuid,"""

    patchable_fields = [
        "action",
        "message",
        "node.name",
        "node.uuid",
    ]
    """action,message,node.name,node.uuid,"""

    postable_fields = [
        "action",
        "message",
        "node.name",
        "node.uuid",
    ]
    """action,message,node.name,node.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcEmsEvent.get_collection(fields=field)]
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
            raise NetAppRestError("XcEmsEvent modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcEmsEvent(Resource):
    r""" ems_event clone for cluster peer. """

    _schema = XcEmsEventSchema
    _path = "/api/cluster/peers/{peer[uuid]}/support/ems/events"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET of observed EMS events"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc ems event show")
        def xc_ems_event_show(
            peer_uuid,
            creation_time: Choices.define(_get_field_list("creation_time"), cache_choices=True, inexact=True)=None,
            index: Choices.define(_get_field_list("index"), cache_choices=True, inexact=True)=None,
            last_update_time: Choices.define(_get_field_list("last_update_time"), cache_choices=True, inexact=True)=None,
            log_message: Choices.define(_get_field_list("log_message"), cache_choices=True, inexact=True)=None,
            source: Choices.define(_get_field_list("source"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            stateful: Choices.define(_get_field_list("stateful"), cache_choices=True, inexact=True)=None,
            time: Choices.define(_get_field_list("time"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["creation_time", "index", "last_update_time", "log_message", "source", "state", "stateful", "time", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcEmsEvent resources

            Args:
                creation_time: Timestamp of the event creation.
                index: Index of the event. Returned by default.
                last_update_time: Timestamp of the last update to the alert.
                log_message: A formatted text string populated with parameter details. Returned by default.
                source: Source
                state: Indicates the event state. A stateful event tracks the state changes of a system condition and reflects the current system condition.
                stateful: Indicates whether the event is stateful. A stateful event tracks the state changes of a system condition and reflects the current system condition while a stateless event simply reports a certain system condition that has occurred sometime in the past.
                time: Timestamp of the event. Returned by default.
                uuid: The UUID that uniquely identifies the alert.
            """

            kwargs = {}
            if creation_time is not None:
                kwargs["creation_time"] = creation_time
            if index is not None:
                kwargs["index"] = index
            if last_update_time is not None:
                kwargs["last_update_time"] = last_update_time
            if log_message is not None:
                kwargs["log_message"] = log_message
            if source is not None:
                kwargs["source"] = source
            if state is not None:
                kwargs["state"] = state
            if stateful is not None:
                kwargs["stateful"] = stateful
            if time is not None:
                kwargs["time"] = time
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcEmsEvent.get_collection(
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
        """Returns a count of all XcEmsEvent resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET of observed EMS events"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






