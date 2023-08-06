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


__all__ = ["XcSvmPeer", "XcSvmPeerSchema"]
__pdoc__ = {
    "XcSvmPeerSchema.resource": False,
    "XcSvmPeerSchema.opts": False,
    "XcSvmPeer.xc_svm_peer_show": False,
    "XcSvmPeer.xc_svm_peer_create": False,
    "XcSvmPeer.xc_svm_peer_modify": False,
    "XcSvmPeer.xc_svm_peer_delete": False,
}


class XcSvmPeerSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSvmPeer object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_svm_peer. """

    applications = fields.List(fields.Str, data_key="applications")
    r""" A list of applications for an SVM peer relation.

Example: ["snapmirror","lun_copy"] """

    name = fields.Str(
        data_key="name",
    )
    r""" A peer SVM alias name to avoid a name conflict on the local cluster. """

    peer = fields.Nested("netapp_ontap.models.peer.PeerSchema", data_key="peer", unknown=EXCLUDE)
    r""" The peer field of the xc_svm_peer. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['peered', 'rejected', 'suspended', 'initiated', 'pending', 'initializing']),
    )
    r""" SVM peering state. To accept a pending SVM peer request, PATCH the state to "peered". To reject a pending SVM peer request, PATCH the state to "rejected". To suspend a peered SVM peer relation, PATCH the state to "suspended". To resume a suspended SVM peer relation, PATCH the state to "peered". The states "initiated", "pending", and "initializing" are system-generated and cannot be used for PATCH.

Valid choices:

* peered
* rejected
* suspended
* initiated
* pending
* initializing """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_svm_peer. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" SVM peer relation UUID """

    @property
    def resource(self):
        return XcSvmPeer

    gettable_fields = [
        "links",
        "applications",
        "name",
        "peer.cluster",
        "peer.svm",
        "state",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
    ]
    """links,applications,name,peer.cluster,peer.svm,state,svm.links,svm.name,svm.uuid,uuid,"""

    patchable_fields = [
        "applications",
        "state",
    ]
    """applications,state,"""

    postable_fields = [
        "applications",
        "name",
        "peer.cluster",
        "peer.svm",
        "svm.name",
        "svm.uuid",
    ]
    """applications,name,peer.cluster,peer.svm,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSvmPeer.get_collection(fields=field)]
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
            raise NetAppRestError("XcSvmPeer modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSvmPeer(Resource):
    r""" svm_peer clone for cluster peer. """

    _schema = XcSvmPeerSchema
    _path = "/api/svm/peers/{peer[uuid]}/svm/peers"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET SVM peers"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc svm peer show")
        def xc_svm_peer_show(
            peer_uuid,
            applications: Choices.define(_get_field_list("applications"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["applications", "name", "state", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSvmPeer resources

            Args:
                applications: A list of applications for an SVM peer relation.
                name: A peer SVM alias name to avoid a name conflict on the local cluster.
                state: SVM peering state. To accept a pending SVM peer request, PATCH the state to \"peered\". To reject a pending SVM peer request, PATCH the state to \"rejected\". To suspend a peered SVM peer relation, PATCH the state to \"suspended\". To resume a suspended SVM peer relation, PATCH the state to \"peered\". The states \"initiated\", \"pending\", and \"initializing\" are system-generated and cannot be used for PATCH.
                uuid: SVM peer relation UUID
            """

            kwargs = {}
            if applications is not None:
                kwargs["applications"] = applications
            if name is not None:
                kwargs["name"] = name
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSvmPeer.get_collection(
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
        """Returns a count of all XcSvmPeer resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["XcSvmPeer"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["XcSvmPeer"], NetAppResponse]:
        r"""Cross cluster POST SVM peer"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)


    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET SVM peers"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)


    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Cross cluster POST SVM peer"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc svm peer create")
        async def xc_svm_peer_create(
            peer_uuid,
            links: dict = None,
            applications: List[str] = None,
            name: str = None,
            peer: dict = None,
            state: str = None,
            svm: dict = None,
            uuid: str = None,
        ) -> ResourceTable:
            """Create an instance of a XcSvmPeer resource

            Args:
                links: 
                applications: A list of applications for an SVM peer relation.
                name: A peer SVM alias name to avoid a name conflict on the local cluster.
                peer: 
                state: SVM peering state. To accept a pending SVM peer request, PATCH the state to \"peered\". To reject a pending SVM peer request, PATCH the state to \"rejected\". To suspend a peered SVM peer relation, PATCH the state to \"suspended\". To resume a suspended SVM peer relation, PATCH the state to \"peered\". The states \"initiated\", \"pending\", and \"initializing\" are system-generated and cannot be used for PATCH.
                svm: 
                uuid: SVM peer relation UUID
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if applications is not None:
                kwargs["applications"] = applications
            if name is not None:
                kwargs["name"] = name
            if peer is not None:
                kwargs["peer"] = peer
            if state is not None:
                kwargs["state"] = state
            if svm is not None:
                kwargs["svm"] = svm
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = XcSvmPeer(
                peer_uuid,
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create XcSvmPeer: %s" % err)
            return [resource]




