r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["XcLicensePackageResponseRecords", "XcLicensePackageResponseRecordsSchema"]
__pdoc__ = {
    "XcLicensePackageResponseRecordsSchema.resource": False,
    "XcLicensePackageResponseRecordsSchema.opts": False,
    "XcLicensePackageResponseRecords": False,
}


class XcLicensePackageResponseRecordsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcLicensePackageResponseRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the xc_license_package_response_records. """

    description = fields.Str(data_key="description")
    r""" License description

Example: NFS License """

    entitlement = fields.Nested("netapp_ontap.models.entitlement.EntitlementSchema", unknown=EXCLUDE, data_key="entitlement")
    r""" The entitlement field of the xc_license_package_response_records. """

    keys = fields.List(fields.Str, data_key="keys")
    r""" The keys field of the xc_license_package_response_records. """

    licenses = fields.List(fields.Nested("netapp_ontap.models.xc_license_package_licenses.XcLicensePackageLicensesSchema", unknown=EXCLUDE), data_key="licenses")
    r""" Installed licenses of the package. """

    name = fields.Str(data_key="name")
    r""" Name of the license.

Example: NFS """

    scope = fields.Str(data_key="scope")
    r""" Scope of the license.

Valid choices:

* not_available
* site
* cluster
* node """

    state = fields.Str(data_key="state")
    r""" Summary state of package based on all installed licenses.

Valid choices:

* compliant
* noncompliant
* unlicensed
* unknown """

    @property
    def resource(self):
        return XcLicensePackageResponseRecords

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


class XcLicensePackageResponseRecords(Resource):

    _schema = XcLicensePackageResponseRecordsSchema
