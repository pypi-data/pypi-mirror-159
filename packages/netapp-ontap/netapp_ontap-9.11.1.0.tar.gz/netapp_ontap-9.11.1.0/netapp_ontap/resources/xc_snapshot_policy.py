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


__all__ = ["XcSnapshotPolicy", "XcSnapshotPolicySchema"]
__pdoc__ = {
    "XcSnapshotPolicySchema.resource": False,
    "XcSnapshotPolicySchema.opts": False,
    "XcSnapshotPolicy.xc_snapshot_policy_show": False,
    "XcSnapshotPolicy.xc_snapshot_policy_create": False,
    "XcSnapshotPolicy.xc_snapshot_policy_modify": False,
    "XcSnapshotPolicy.xc_snapshot_policy_delete": False,
}


class XcSnapshotPolicySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSnapshotPolicy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_snapshot_policy. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" A comment associated with the Snapshot copy policy. """

    copies = fields.List(fields.Nested("netapp_ontap.models.snapshot_policy_copies.SnapshotPolicyCopiesSchema", unknown=EXCLUDE), data_key="copies")
    r""" The copies field of the xc_snapshot_policy. """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" Is the Snapshot copy policy enabled?

Example: true """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the Snapshot copy policy.

Example: default """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" when the request is on a data SVM, otherwise set to "cluster".

Valid choices:

* svm
* cluster """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_snapshot_policy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_snapshot_policy.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcSnapshotPolicy

    gettable_fields = [
        "links",
        "comment",
        "copies",
        "enabled",
        "name",
        "scope",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
    ]
    """links,comment,copies,enabled,name,scope,svm.links,svm.name,svm.uuid,uuid,"""

    patchable_fields = [
        "comment",
        "enabled",
    ]
    """comment,enabled,"""

    postable_fields = [
        "comment",
        "copies",
        "enabled",
        "name",
        "svm.name",
        "svm.uuid",
    ]
    """comment,copies,enabled,name,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSnapshotPolicy.get_collection(fields=field)]
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
            raise NetAppRestError("XcSnapshotPolicy modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSnapshotPolicy(Resource):
    r""" snapshot_policy clone for cluster peer. """

    _schema = XcSnapshotPolicySchema
    _path = "/api/svm/peers/{peer[uuid]}/storage/snapshot-policies"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET snapshot policies"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc snapshot policy show")
        def xc_snapshot_policy_show(
            peer_uuid,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            enabled: Choices.define(_get_field_list("enabled"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["comment", "enabled", "name", "scope", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSnapshotPolicy resources

            Args:
                comment: A comment associated with the Snapshot copy policy.
                enabled: Is the Snapshot copy policy enabled?
                name: Name of the Snapshot copy policy.
                scope: Set to \"svm\" when the request is on a data SVM, otherwise set to \"cluster\".
                uuid: 
            """

            kwargs = {}
            if comment is not None:
                kwargs["comment"] = comment
            if enabled is not None:
                kwargs["enabled"] = enabled
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSnapshotPolicy.get_collection(
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
        """Returns a count of all XcSnapshotPolicy resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET snapshot policies"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






