r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

A test endpoint for instances of SMNext objects.
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


__all__ = ["Smnext", "SmnextSchema"]
__pdoc__ = {
    "SmnextSchema.resource": False,
    "SmnextSchema.opts": False,
    "Smnext.smnext_show": False,
    "Smnext.smnext_create": False,
    "Smnext.smnext_modify": False,
    "Smnext.smnext_delete": False,
}


class SmnextSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Smnext object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the smnext. """

    top1 = fields.Str(
        data_key="top1",
    )
    r""" Dummy/Generic Field 1 """

    top10 = ImpreciseDateTime(
        data_key="top10",
    )
    r""" Dummy/Generic Field 10 """

    top2 = fields.Number(
        data_key="top2",
    )
    r""" Dummy/Generic Field 2 """

    top3 = fields.Str(
        data_key="top3",
    )
    r""" Dummy/Generic Field 3 """

    top4 = ImpreciseDateTime(
        data_key="top4",
    )
    r""" Dummy/Generic Field 4 """

    top5 = fields.Boolean(
        data_key="top5",
    )
    r""" Dummy/Generic Field 5 """

    top6 = Size(
        data_key="top6",
    )
    r""" Dummy/Generic Field 6 """

    top7 = fields.Str(
        data_key="top7",
    )
    r""" Dummy/Generic Field 7 """

    top8 = fields.Str(
        data_key="top8",
    )
    r""" Dummy/Generic Field 8 """

    top9 = Size(
        data_key="top9",
    )
    r""" Dummy/Generic Field 9 """

    @property
    def resource(self):
        return Smnext

    gettable_fields = [
        "links",
        "top1",
        "top10",
        "top2",
        "top3",
        "top4",
        "top5",
        "top6",
        "top7",
        "top8",
        "top9",
    ]
    """links,top1,top10,top2,top3,top4,top5,top6,top7,top8,top9,"""

    patchable_fields = [
        "top1",
        "top10",
        "top2",
        "top3",
        "top4",
        "top5",
        "top6",
        "top7",
        "top8",
        "top9",
    ]
    """top1,top10,top2,top3,top4,top5,top6,top7,top8,top9,"""

    postable_fields = [
        "top1",
        "top10",
        "top2",
        "top3",
        "top4",
        "top5",
        "top6",
        "top7",
        "top8",
        "top9",
    ]
    """top1,top10,top2,top3,top4,top5,top6,top7,top8,top9,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Smnext.get_collection(fields=field)]
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
            raise NetAppRestError("Smnext modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Smnext(Resource):
    """Allows interaction with Smnext objects on the host"""

    _schema = SmnextSchema
    _path = "/api/test/smnext"
    _keys = ["top1"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves SMNext records.

### Learn more
* [`DOC /test/smnext`](#docs-test-test_smnext)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="smnext show")
        def smnext_show(
            fields: List[Choices.define(["top1", "top10", "top2", "top3", "top4", "top5", "top6", "top7", "top8", "top9", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Smnext resources

            Args:
                top1: Dummy/Generic Field 1
                top10: Dummy/Generic Field 10
                top2: Dummy/Generic Field 2
                top3: Dummy/Generic Field 3
                top4: Dummy/Generic Field 4
                top5: Dummy/Generic Field 5
                top6: Dummy/Generic Field 6
                top7: Dummy/Generic Field 7
                top8: Dummy/Generic Field 8
                top9: Dummy/Generic Field 9
            """

            kwargs = {}
            if top1 is not None:
                kwargs["top1"] = top1
            if top10 is not None:
                kwargs["top10"] = top10
            if top2 is not None:
                kwargs["top2"] = top2
            if top3 is not None:
                kwargs["top3"] = top3
            if top4 is not None:
                kwargs["top4"] = top4
            if top5 is not None:
                kwargs["top5"] = top5
            if top6 is not None:
                kwargs["top6"] = top6
            if top7 is not None:
                kwargs["top7"] = top7
            if top8 is not None:
                kwargs["top8"] = top8
            if top9 is not None:
                kwargs["top9"] = top9
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Smnext.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Smnext resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["Smnext"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["Smnext"], NetAppResponse]:
        r"""Creates a new SMNext record.

### Learn more
* [`DOC /test/smnext`](#docs-test-test_smnext)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["Smnext"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an SMNnext record instance.
### Learn more
* [`DOC /test/smnext/{top1}`](#docs-test-test_smnext_{top1})"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves SMNext records.

### Learn more
* [`DOC /test/smnext`](#docs-test-test_smnext)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an SMNext record instance.
### Learn more
* [`DOC /test/smnext/{top1}`](#docs-test-test_smnext_{top1})"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a new SMNext record.

### Learn more
* [`DOC /test/smnext`](#docs-test-test_smnext)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="smnext create")
        async def smnext_create(
        ) -> ResourceTable:
            """Create an instance of a Smnext resource

            Args:
                links: 
                top1: Dummy/Generic Field 1
                top10: Dummy/Generic Field 10
                top2: Dummy/Generic Field 2
                top3: Dummy/Generic Field 3
                top4: Dummy/Generic Field 4
                top5: Dummy/Generic Field 5
                top6: Dummy/Generic Field 6
                top7: Dummy/Generic Field 7
                top8: Dummy/Generic Field 8
                top9: Dummy/Generic Field 9
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if top1 is not None:
                kwargs["top1"] = top1
            if top10 is not None:
                kwargs["top10"] = top10
            if top2 is not None:
                kwargs["top2"] = top2
            if top3 is not None:
                kwargs["top3"] = top3
            if top4 is not None:
                kwargs["top4"] = top4
            if top5 is not None:
                kwargs["top5"] = top5
            if top6 is not None:
                kwargs["top6"] = top6
            if top7 is not None:
                kwargs["top7"] = top7
            if top8 is not None:
                kwargs["top8"] = top8
            if top9 is not None:
                kwargs["top9"] = top9

            resource = Smnext(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create Smnext: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an SMNnext record instance.
### Learn more
* [`DOC /test/smnext/{top1}`](#docs-test-test_smnext_{top1})"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="smnext delete")
        async def smnext_delete(
        ) -> None:
            """Delete an instance of a Smnext resource

            Args:
                top1: Dummy/Generic Field 1
                top10: Dummy/Generic Field 10
                top2: Dummy/Generic Field 2
                top3: Dummy/Generic Field 3
                top4: Dummy/Generic Field 4
                top5: Dummy/Generic Field 5
                top6: Dummy/Generic Field 6
                top7: Dummy/Generic Field 7
                top8: Dummy/Generic Field 8
                top9: Dummy/Generic Field 9
            """

            kwargs = {}
            if top1 is not None:
                kwargs["top1"] = top1
            if top10 is not None:
                kwargs["top10"] = top10
            if top2 is not None:
                kwargs["top2"] = top2
            if top3 is not None:
                kwargs["top3"] = top3
            if top4 is not None:
                kwargs["top4"] = top4
            if top5 is not None:
                kwargs["top5"] = top5
            if top6 is not None:
                kwargs["top6"] = top6
            if top7 is not None:
                kwargs["top7"] = top7
            if top8 is not None:
                kwargs["top8"] = top8
            if top9 is not None:
                kwargs["top9"] = top9

            if hasattr(Smnext, "find"):
                resource = Smnext.find(
                    **kwargs
                )
            else:
                resource = Smnext()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete Smnext: %s" % err)


