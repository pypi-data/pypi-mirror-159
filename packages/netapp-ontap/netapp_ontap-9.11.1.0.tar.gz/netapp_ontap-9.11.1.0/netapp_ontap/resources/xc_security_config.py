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


__all__ = ["XcSecurityConfig", "XcSecurityConfigSchema"]
__pdoc__ = {
    "XcSecurityConfigSchema.resource": False,
    "XcSecurityConfigSchema.opts": False,
    "XcSecurityConfig.xc_security_config_show": False,
    "XcSecurityConfig.xc_security_config_create": False,
    "XcSecurityConfig.xc_security_config_modify": False,
    "XcSecurityConfig.xc_security_config_delete": False,
}


class XcSecurityConfigSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSecurityConfig object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_security_config. """

    fips = fields.Nested("netapp_ontap.models.fips.FipsSchema", data_key="fips", unknown=EXCLUDE)
    r""" The fips field of the xc_security_config. """

    management_protocols = fields.Nested("netapp_ontap.models.management_protocols.ManagementProtocolsSchema", data_key="management_protocols", unknown=EXCLUDE)
    r""" The management_protocols field of the xc_security_config. """

    onboard_key_manager_configurable_status = fields.Nested("netapp_ontap.models.onboard_key_manager_configurable_status.OnboardKeyManagerConfigurableStatusSchema", data_key="onboard_key_manager_configurable_status", unknown=EXCLUDE)
    r""" The onboard_key_manager_configurable_status field of the xc_security_config. """

    software_data_encryption = fields.Nested("netapp_ontap.models.software_data_encryption.SoftwareDataEncryptionSchema", data_key="software_data_encryption", unknown=EXCLUDE)
    r""" The software_data_encryption field of the xc_security_config. """

    tls = fields.Nested("netapp_ontap.models.tls.TlsSchema", data_key="tls", unknown=EXCLUDE)
    r""" The tls field of the xc_security_config. """

    @property
    def resource(self):
        return XcSecurityConfig

    gettable_fields = [
        "links",
        "fips",
        "management_protocols",
        "onboard_key_manager_configurable_status",
        "software_data_encryption",
        "tls",
    ]
    """links,fips,management_protocols,onboard_key_manager_configurable_status,software_data_encryption,tls,"""

    patchable_fields = [
        "fips",
        "management_protocols",
        "software_data_encryption",
        "tls",
    ]
    """fips,management_protocols,software_data_encryption,tls,"""

    postable_fields = [
        "fips",
        "management_protocols",
        "software_data_encryption",
        "tls",
    ]
    """fips,management_protocols,software_data_encryption,tls,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcSecurityConfig.get_collection(fields=field)]
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
            raise NetAppRestError("XcSecurityConfig modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcSecurityConfig(Resource):
    r""" security_config clone for cluster peer. """

    _schema = XcSecurityConfigSchema
    _path = "/api/cluster/peers/{peer[uuid]}/security"
    _keys = ["peer.uuid"]







    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information about the security configured on the remote cluster.
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc security config show")
        def xc_security_config_show(
            peer_uuid,
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single XcSecurityConfig resource

            Args:
            """

            kwargs = {}
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = XcSecurityConfig(
                peer_uuid,
                **kwargs
            )
            resource.get()
            return [resource]





