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


__all__ = ["Cloned2Role", "Cloned2RoleSchema"]
__pdoc__ = {
    "Cloned2RoleSchema.resource": False,
    "Cloned2RoleSchema.opts": False,
    "Cloned2Role.cloned2_role_show": False,
    "Cloned2Role.cloned2_role_create": False,
    "Cloned2Role.cloned2_role_modify": False,
    "Cloned2Role.cloned2_role_delete": False,
}


class Cloned2RoleSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Cloned2Role object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cloned2_role. """

    builtin = fields.Boolean(
        data_key="builtin",
    )
    r""" Indicates if this is a built-in (pre-defined) role which cannot be modified or deleted. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Comment """

    name = fields.Str(
        data_key="name",
    )
    r""" Role name

Example: admin """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the cloned2_role. """

    privileges = fields.List(fields.Nested("netapp_ontap.resources.role_privilege.RolePrivilegeSchema", unknown=EXCLUDE), data_key="privileges")
    r""" The list of privileges that this role has been granted. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['cluster', 'svm']),
    )
    r""" Scope of the entity. Set to "cluster" for cluster owned objects and to "svm" for SVM owned objects.

Valid choices:

* cluster
* svm """

    @property
    def resource(self):
        return Cloned2Role

    gettable_fields = [
        "links",
        "builtin",
        "comment",
        "name",
        "owner.links",
        "owner.name",
        "owner.uuid",
        "privileges",
        "scope",
    ]
    """links,builtin,comment,name,owner.links,owner.name,owner.uuid,privileges,scope,"""

    patchable_fields = [
        "comment",
        "privileges",
    ]
    """comment,privileges,"""

    postable_fields = [
        "comment",
        "name",
        "owner.name",
        "owner.uuid",
        "privileges",
    ]
    """comment,name,owner.name,owner.uuid,privileges,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Cloned2Role.get_collection(fields=field)]
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
            raise NetAppRestError("Cloned2Role modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Cloned2Role(Resource):
    r""" Second role clone. """

    _schema = Cloned2RoleSchema
    _path = "/api/security/svm/roles"

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of SVM roles."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cloned2 role show")
        def cloned2_role_show(
            fields: List[Choices.define(["builtin", "comment", "name", "scope", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Cloned2Role resources

            Args:
                builtin: Indicates if this is a built-in (pre-defined) role which cannot be modified or deleted.
                comment: Comment
                name: Role name
                scope: Scope of the entity. Set to \"cluster\" for cluster owned objects and to \"svm\" for SVM owned objects.
            """

            kwargs = {}
            if builtin is not None:
                kwargs["builtin"] = builtin
            if comment is not None:
                kwargs["comment"] = comment
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Cloned2Role.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Cloned2Role resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of SVM roles."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






