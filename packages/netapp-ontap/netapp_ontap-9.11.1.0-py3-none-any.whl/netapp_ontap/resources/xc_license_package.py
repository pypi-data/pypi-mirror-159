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


__all__ = ["XcLicensePackage", "XcLicensePackageSchema"]
__pdoc__ = {
    "XcLicensePackageSchema.resource": False,
    "XcLicensePackageSchema.opts": False,
    "XcLicensePackage.xc_license_package_show": False,
    "XcLicensePackage.xc_license_package_create": False,
    "XcLicensePackage.xc_license_package_modify": False,
    "XcLicensePackage.xc_license_package_delete": False,
}


class XcLicensePackageSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcLicensePackage object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_license_package. """

    description = fields.Str(
        data_key="description",
    )
    r""" License description

Example: NFS License """

    entitlement = fields.Nested("netapp_ontap.models.entitlement.EntitlementSchema", data_key="entitlement", unknown=EXCLUDE)
    r""" The entitlement field of the xc_license_package. """

    keys = fields.List(fields.Str, data_key="keys")
    r""" The keys field of the xc_license_package. """

    licenses = fields.List(fields.Nested("netapp_ontap.models.license_package_response_records_licenses.LicensePackageResponseRecordsLicensesSchema", unknown=EXCLUDE), data_key="licenses")
    r""" Installed licenses of the package. """

    name = fields.Str(
        data_key="name",
    )
    r""" Name of the license.

Example: NFS """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['not_available', 'site', 'cluster', 'node']),
    )
    r""" Scope of the license.

Valid choices:

* not_available
* site
* cluster
* node """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['compliant', 'noncompliant', 'unlicensed', 'unknown']),
    )
    r""" Summary state of package based on all installed licenses.

Valid choices:

* compliant
* noncompliant
* unlicensed
* unknown """

    @property
    def resource(self):
        return XcLicensePackage

    gettable_fields = [
        "links",
        "description",
        "entitlement",
        "licenses",
        "name",
        "scope",
        "state",
    ]
    """links,description,entitlement,licenses,name,scope,state,"""

    patchable_fields = [
        "entitlement",
    ]
    """entitlement,"""

    postable_fields = [
        "entitlement",
        "keys",
    ]
    """entitlement,keys,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcLicensePackage.get_collection(fields=field)]
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
            raise NetAppRestError("XcLicensePackage modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcLicensePackage(Resource):
    r""" license_package clone for cluster peer. """

    _schema = XcLicensePackageSchema
    _path = "/api/cluster/peers/{peer[uuid]}/cluster/licensing/licenses"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET licenses"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc license package show")
        def xc_license_package_show(
            peer_uuid,
            description: Choices.define(_get_field_list("description"), cache_choices=True, inexact=True)=None,
            keys: Choices.define(_get_field_list("keys"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["description", "keys", "name", "scope", "state", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcLicensePackage resources

            Args:
                description: License description
                keys: 
                name: Name of the license.
                scope: Scope of the license.
                state: Summary state of package based on all installed licenses.
            """

            kwargs = {}
            if description is not None:
                kwargs["description"] = description
            if keys is not None:
                kwargs["keys"] = keys
            if name is not None:
                kwargs["name"] = name
            if scope is not None:
                kwargs["scope"] = scope
            if state is not None:
                kwargs["state"] = state
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcLicensePackage.get_collection(
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
        """Returns a count of all XcLicensePackage resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET licenses"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






