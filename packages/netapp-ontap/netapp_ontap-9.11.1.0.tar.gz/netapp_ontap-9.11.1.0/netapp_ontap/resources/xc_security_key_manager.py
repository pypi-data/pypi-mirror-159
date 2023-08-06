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


__all__ = ["XcSecurityKeyManager", "XcSecurityKeyManagerSchema"]
__pdoc__ = {
    "XcSecurityKeyManagerSchema.resource": False,
    "XcSecurityKeyManagerSchema.opts": False,
    "XcSecurityKeyManager.xc_security_key_manager_show": False,
    "XcSecurityKeyManager.xc_security_key_manager_create": False,
    "XcSecurityKeyManager.xc_security_key_manager_modify": False,
    "XcSecurityKeyManager.xc_security_key_manager_delete": False,
}


class XcSecurityKeyManagerSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSecurityKeyManager object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_security_key_manager. """

    external = fields.Nested("netapp_ontap.models.xc_security_key_manager_external.XcSecurityKeyManagerExternalSchema", data_key="external", unknown=EXCLUDE)
    r""" The external field of the xc_security_key_manager. """

    onboard = fields.Nested("netapp_ontap.models.xc_security_key_manager_onboard.XcSecurityKeyManagerOnboardSchema", data_key="onboard", unknown=EXCLUDE)
    r""" The onboard field of the xc_security_key_manager. """

    policy = fields.Str(
        data_key="policy",
    )
    r""" Security policy associated with the key manager. This value is currently ignored if specified for the onboard key manager. """

    status = fields.Nested("netapp_ontap.models.key_manager_state.KeyManagerStateSchema", data_key="status", unknown=EXCLUDE)
    r""" The status field of the xc_security_key_manager. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The uuid field of the xc_security_key_manager. """

    volume_encryption = fields.Nested("netapp_ontap.models.volume_encryption_support.VolumeEncryptionSupportSchema", data_key="volume_encryption", unknown=EXCLUDE)
    r""" The volume_encryption field of the xc_security_key_manager. """

    @property
    def resource(self):
        return XcSecurityKeyManager

    gettable_fields = [
        "links",
        "external",
        "onboard",
        "policy",
        "status",
        "uuid",
        "volume_encryption",
    ]
    """links,external,onboard,policy,status,uuid,volume_encryption,"""

    patchable_fields = [
        "external",
        "onboard",
        "policy",
    ]
    """external,onboard,policy,"""

    postable_fields = [
        "external",
        "onboard",
        "policy",
    ]
    """external,onboard,policy,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSecurityKeyManager.get_collection(fields=field)]
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
            raise NetAppRestError("XcSecurityKeyManager modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSecurityKeyManager(Resource):
    """Allows interaction with XcSecurityKeyManager objects on the host"""

    _schema = XcSecurityKeyManagerSchema
    _path = "/api/cluster/peers/{peer[uuid]}/security/key-managers"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET key_managers"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc security key manager show")
        def xc_security_key_manager_show(
            peer_uuid,
            policy: Choices.define(_get_field_list("policy"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["policy", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcSecurityKeyManager resources

            Args:
                policy: Security policy associated with the key manager. This value is currently ignored if specified for the onboard key manager.
                uuid: 
            """

            kwargs = {}
            if policy is not None:
                kwargs["policy"] = policy
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcSecurityKeyManager.get_collection(
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
        """Returns a count of all XcSecurityKeyManager resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["XcSecurityKeyManager"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["XcSecurityKeyManager"], NetAppResponse]:
        r"""Cross cluster POST key_managers"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)


    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET key_managers"""
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
        r"""Cross cluster POST key_managers"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc security key manager create")
        async def xc_security_key_manager_create(
            peer_uuid,
            links: dict = None,
            external: dict = None,
            onboard: dict = None,
            policy: str = None,
            status: dict = None,
            uuid: str = None,
            volume_encryption: dict = None,
        ) -> ResourceTable:
            """Create an instance of a XcSecurityKeyManager resource

            Args:
                links: 
                external: 
                onboard: 
                policy: Security policy associated with the key manager. This value is currently ignored if specified for the onboard key manager.
                status: 
                uuid: 
                volume_encryption: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if external is not None:
                kwargs["external"] = external
            if onboard is not None:
                kwargs["onboard"] = onboard
            if policy is not None:
                kwargs["policy"] = policy
            if status is not None:
                kwargs["status"] = status
            if uuid is not None:
                kwargs["uuid"] = uuid
            if volume_encryption is not None:
                kwargs["volume_encryption"] = volume_encryption

            resource = XcSecurityKeyManager(
                peer_uuid,
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create XcSecurityKeyManager: %s" % err)
            return [resource]




