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


__all__ = ["Fiji", "FijiSchema"]
__pdoc__ = {
    "FijiSchema.resource": False,
    "FijiSchema.opts": False,
    "Fiji.fiji_show": False,
    "Fiji.fiji_create": False,
    "Fiji.fiji_modify": False,
    "Fiji.fiji_delete": False,
}


class FijiSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Fiji object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the fiji. """

    action = fields.Str(
        data_key="action",
        validate=enum_validation(['FAULT_ACTION_SLEEP', 'FAULT_ACTION_ABORT', 'FAULT_ACTION_RETURNCODE', 'FAULT_ACTION_PANIC_NODE', 'FAULT_ACTION_REBOOT_NODE']),
    )
    r""" Action to be performed.

Valid choices:

* FAULT_ACTION_SLEEP
* FAULT_ACTION_ABORT
* FAULT_ACTION_RETURNCODE
* FAULT_ACTION_PANIC_NODE
* FAULT_ACTION_REBOOT_NODE """

    action_arg = Size(
        data_key="action-arg",
    )
    r""" Action argument. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Fault status. """

    end_call = Size(
        data_key="end-call",
    )
    r""" End call number for sequence. """

    fault_id = fields.Str(
        data_key="fault-id",
    )
    r""" Fault name.

Example: bcomd.amid.newfail.nonintdblade """

    fault_mode = fields.Str(
        data_key="fault-mode",
        validate=enum_validation(['FAULT_ACTION_NONE', 'FAULT_ACTION_SLEEP', 'FAULT_ACTION_ABORT', 'FAULT_ACTION_RETURNCODE', 'FAULT_ACTION_PANIC_NODE', 'FAULT_ACTION_REBOOT_NODE']),
    )
    r""" Fault mode.

Valid choices:

* FAULT_ACTION_NONE
* FAULT_ACTION_SLEEP
* FAULT_ACTION_ABORT
* FAULT_ACTION_RETURNCODE
* FAULT_ACTION_PANIC_NODE
* FAULT_ACTION_REBOOT_NODE """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the fiji. """

    num_calls = Size(
        data_key="num-calls",
    )
    r""" Periodic calls. """

    period = Size(
        data_key="period",
    )
    r""" Period, if a periodic fault. """

    probability = Size(
        data_key="probability",
    )
    r""" Fault probability. """

    start_call = Size(
        data_key="start-call",
    )
    r""" Start call number for sequence. """

    total_calls = Size(
        data_key="total-calls",
    )
    r""" Total number of calls to fault injection. """

    @property
    def resource(self):
        return Fiji

    gettable_fields = [
        "links",
        "action",
        "action_arg",
        "enabled",
        "end_call",
        "fault_id",
        "fault_mode",
        "node.links",
        "node.name",
        "node.uuid",
        "num_calls",
        "period",
        "probability",
        "start_call",
        "total_calls",
    ]
    """links,action,action_arg,enabled,end_call,fault_id,fault_mode,node.links,node.name,node.uuid,num_calls,period,probability,start_call,total_calls,"""

    patchable_fields = [
        "action",
        "action_arg",
        "enabled",
        "end_call",
        "fault_mode",
        "node.name",
        "node.uuid",
        "num_calls",
        "period",
        "probability",
        "start_call",
        "total_calls",
    ]
    """action,action_arg,enabled,end_call,fault_mode,node.name,node.uuid,num_calls,period,probability,start_call,total_calls,"""

    postable_fields = [
        "action",
        "action_arg",
        "enabled",
        "end_call",
        "fault_mode",
        "node.name",
        "node.uuid",
        "num_calls",
        "period",
        "probability",
        "start_call",
        "total_calls",
    ]
    """action,action_arg,enabled,end_call,fault_mode,node.name,node.uuid,num_calls,period,probability,start_call,total_calls,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Fiji.get_collection(fields=field)]
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
            raise NetAppRestError("Fiji modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Fiji(Resource):
    r""" Information on the fault injection REST API. """

    _schema = FijiSchema
    _path = "/api/test/fijis"
    _keys = ["node", "fault-id"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves fault injection information."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="fiji show")
        def fiji_show(
            fields: List[Choices.define(["action", "action_arg", "enabled", "end_call", "fault_id", "fault_mode", "num_calls", "period", "probability", "start_call", "total_calls", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Fiji resources

            Args:
                action: Action to be performed.
                action_arg: Action argument.
                enabled: Fault status.
                end_call: End call number for sequence.
                fault_id: Fault name.
                fault_mode: Fault mode.
                num_calls: Periodic calls.
                period: Period, if a periodic fault.
                probability: Fault probability.
                start_call: Start call number for sequence.
                total_calls: Total number of calls to fault injection.
            """

            kwargs = {}
            if action is not None:
                kwargs["action"] = action
            if action_arg is not None:
                kwargs["action_arg"] = action_arg
            if enabled is not None:
                kwargs["enabled"] = enabled
            if end_call is not None:
                kwargs["end_call"] = end_call
            if fault_id is not None:
                kwargs["fault_id"] = fault_id
            if fault_mode is not None:
                kwargs["fault_mode"] = fault_mode
            if num_calls is not None:
                kwargs["num_calls"] = num_calls
            if period is not None:
                kwargs["period"] = period
            if probability is not None:
                kwargs["probability"] = probability
            if start_call is not None:
                kwargs["start_call"] = start_call
            if total_calls is not None:
                kwargs["total_calls"] = total_calls
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Fiji.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Fiji resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Fiji"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a fault injection."""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)



    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves fault injection information."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific fault injection."""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a fault injection."""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="fiji modify")
        async def fiji_modify(
        ) -> ResourceTable:
            """Modify an instance of a Fiji resource

            Args:
                action: Action to be performed.
                query_action: Action to be performed.
                action_arg: Action argument.
                query_action_arg: Action argument.
                enabled: Fault status.
                query_enabled: Fault status.
                end_call: End call number for sequence.
                query_end_call: End call number for sequence.
                fault_id: Fault name.
                query_fault_id: Fault name.
                fault_mode: Fault mode.
                query_fault_mode: Fault mode.
                num_calls: Periodic calls.
                query_num_calls: Periodic calls.
                period: Period, if a periodic fault.
                query_period: Period, if a periodic fault.
                probability: Fault probability.
                query_probability: Fault probability.
                start_call: Start call number for sequence.
                query_start_call: Start call number for sequence.
                total_calls: Total number of calls to fault injection.
                query_total_calls: Total number of calls to fault injection.
            """

            kwargs = {}
            changes = {}
            if query_action is not None:
                kwargs["action"] = query_action
            if query_action_arg is not None:
                kwargs["action_arg"] = query_action_arg
            if query_enabled is not None:
                kwargs["enabled"] = query_enabled
            if query_end_call is not None:
                kwargs["end_call"] = query_end_call
            if query_fault_id is not None:
                kwargs["fault_id"] = query_fault_id
            if query_fault_mode is not None:
                kwargs["fault_mode"] = query_fault_mode
            if query_num_calls is not None:
                kwargs["num_calls"] = query_num_calls
            if query_period is not None:
                kwargs["period"] = query_period
            if query_probability is not None:
                kwargs["probability"] = query_probability
            if query_start_call is not None:
                kwargs["start_call"] = query_start_call
            if query_total_calls is not None:
                kwargs["total_calls"] = query_total_calls

            if action is not None:
                changes["action"] = action
            if action_arg is not None:
                changes["action_arg"] = action_arg
            if enabled is not None:
                changes["enabled"] = enabled
            if end_call is not None:
                changes["end_call"] = end_call
            if fault_id is not None:
                changes["fault_id"] = fault_id
            if fault_mode is not None:
                changes["fault_mode"] = fault_mode
            if num_calls is not None:
                changes["num_calls"] = num_calls
            if period is not None:
                changes["period"] = period
            if probability is not None:
                changes["probability"] = probability
            if start_call is not None:
                changes["start_call"] = start_call
            if total_calls is not None:
                changes["total_calls"] = total_calls

            if hasattr(Fiji, "find"):
                resource = Fiji.find(
                    **kwargs
                )
            else:
                resource = Fiji()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Fiji: %s" % err)



