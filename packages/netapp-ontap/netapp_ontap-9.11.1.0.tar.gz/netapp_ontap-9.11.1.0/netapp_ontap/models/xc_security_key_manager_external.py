r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["XcSecurityKeyManagerExternal", "XcSecurityKeyManagerExternalSchema"]
__pdoc__ = {
    "XcSecurityKeyManagerExternalSchema.resource": False,
    "XcSecurityKeyManagerExternalSchema.opts": False,
    "XcSecurityKeyManagerExternal": False,
}


class XcSecurityKeyManagerExternalSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcSecurityKeyManagerExternal object"""

    client_certificate = fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", unknown=EXCLUDE, data_key="client_certificate")
    r""" The client_certificate field of the xc_security_key_manager_external. """

    server_ca_certificates = fields.List(fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", unknown=EXCLUDE), data_key="server_ca_certificates")
    r""" The UUIDs of the server CA certificates already installed in the cluster or SVM. The array of certificates are common for all the key servers per SVM. """

    servers = fields.List(fields.Nested("netapp_ontap.models.key_server_readcreate.KeyServerReadcreateSchema", unknown=EXCLUDE), data_key="servers")
    r""" The set of external key servers. """

    @property
    def resource(self):
        return XcSecurityKeyManagerExternal

    gettable_fields = [
        "client_certificate.links",
        "client_certificate.name",
        "client_certificate.uuid",
        "server_ca_certificates.links",
        "server_ca_certificates.name",
        "server_ca_certificates.uuid",
        "servers",
    ]
    """client_certificate.links,client_certificate.name,client_certificate.uuid,server_ca_certificates.links,server_ca_certificates.name,server_ca_certificates.uuid,servers,"""

    patchable_fields = [
        "client_certificate.name",
        "client_certificate.uuid",
        "server_ca_certificates.name",
        "server_ca_certificates.uuid",
        "servers",
    ]
    """client_certificate.name,client_certificate.uuid,server_ca_certificates.name,server_ca_certificates.uuid,servers,"""

    postable_fields = [
        "client_certificate.name",
        "client_certificate.uuid",
        "server_ca_certificates.name",
        "server_ca_certificates.uuid",
        "servers",
    ]
    """client_certificate.name,client_certificate.uuid,server_ca_certificates.name,server_ca_certificates.uuid,servers,"""


class XcSecurityKeyManagerExternal(Resource):

    _schema = XcSecurityKeyManagerExternalSchema
