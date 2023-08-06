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


__all__ = ["SvmExpanded", "SvmExpandedSchema"]
__pdoc__ = {
    "SvmExpandedSchema.resource": False,
    "SvmExpandedSchema.opts": False,
    "SvmExpanded.svm_expanded_show": False,
    "SvmExpanded.svm_expanded_create": False,
    "SvmExpanded.svm_expanded_modify": False,
    "SvmExpanded.svm_expanded_delete": False,
}


class SvmExpandedSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SvmExpanded object"""

    aggregates = fields.List(fields.Nested("netapp_ontap.models.svm_aggregates.SvmAggregatesSchema", unknown=EXCLUDE), data_key="aggregates")
    r""" List of allowed aggregates for SVM volumes. An administrator is allowed to create volumes on these aggregates. """

    name = fields.Str(
        data_key="name",
    )
    r""" The name of the SVM.


Example: svm1 """

    peering_permitted = fields.Boolean(
        data_key="peering_permitted",
    )
    r""" Indicates SVM peer permission. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['starting', 'running', 'stopping', 'stopped', 'deleting']),
    )
    r""" SVM state.

Valid choices:

* starting
* running
* stopping
* stopped
* deleting """

    subtype = fields.Str(
        data_key="subtype",
        validate=enum_validation(['default', 'dp_destination', 'sync_source', 'sync_destination']),
    )
    r""" SVM subtype.

Valid choices:

* default
* dp_destination
* sync_source
* sync_destination """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the SVM.


Example: 02c9e252-41be-11e9-81d5-00a0986138f7 """

    @property
    def resource(self):
        return SvmExpanded

    gettable_fields = [
        "aggregates.links",
        "aggregates.name",
        "aggregates.uuid",
        "name",
        "peering_permitted",
        "state",
        "subtype",
        "uuid",
    ]
    """aggregates.links,aggregates.name,aggregates.uuid,name,peering_permitted,state,subtype,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SvmExpanded.get_collection(fields=field)]
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
            raise NetAppRestError("SvmExpanded modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SvmExpanded(Resource):
    r""" SVM with more detailed information, applies only to SVM-scoped objects. """

    _schema = SvmExpandedSchema
    _path = "/api/cluster/peers/{peer[uuid]}/svm/svms"
    _keys = ["peer.uuid", "uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET svm config"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="svm expanded show")
        def svm_expanded_show(
            peer_uuid,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            peering_permitted: Choices.define(_get_field_list("peering_permitted"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            subtype: Choices.define(_get_field_list("subtype"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["name", "peering_permitted", "state", "subtype", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SvmExpanded resources

            Args:
                name: The name of the SVM. 
                peering_permitted: Indicates SVM peer permission.
                state: SVM state.
                subtype: SVM subtype.
                uuid: The unique identifier of the SVM. 
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if peering_permitted is not None:
                kwargs["peering_permitted"] = peering_permitted
            if state is not None:
                kwargs["state"] = state
            if subtype is not None:
                kwargs["subtype"] = subtype
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SvmExpanded.get_collection(
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
        """Returns a count of all SvmExpanded resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET svm config"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Cross cluster GET svm config"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)





