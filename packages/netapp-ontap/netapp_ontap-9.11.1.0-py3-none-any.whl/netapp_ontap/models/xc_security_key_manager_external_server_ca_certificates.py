r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["XcSecurityKeyManagerExternalServerCaCertificates", "XcSecurityKeyManagerExternalServerCaCertificatesSchema"]
__pdoc__ = {
    "XcSecurityKeyManagerExternalServerCaCertificatesSchema.resource": False,
    "XcSecurityKeyManagerExternalServerCaCertificatesSchema.opts": False,
    "XcSecurityKeyManagerExternalServerCaCertificates": False,
}


class XcSecurityKeyManagerExternalServerCaCertificatesSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSecurityKeyManagerExternalServerCaCertificates object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the xc_security_key_manager_external_server_ca_certificates. """

    name = fields.Str(data_key="name")
    r""" Certificate name

Example: cert1 """

    uuid = fields.Str(data_key="uuid")
    r""" Certificate UUID

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return XcSecurityKeyManagerExternalServerCaCertificates

    gettable_fields = [
        "links",
        "name",
        "uuid",
    ]
    """links,name,uuid,"""

    patchable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""

    postable_fields = [
        "name",
        "uuid",
    ]
    """name,uuid,"""


class XcSecurityKeyManagerExternalServerCaCertificates(Resource):

    _schema = XcSecurityKeyManagerExternalServerCaCertificatesSchema
