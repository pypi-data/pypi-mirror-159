r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SecurityTruststoreCertificateSubjectAlternatives", "SecurityTruststoreCertificateSubjectAlternativesSchema"]
__pdoc__ = {
    "SecurityTruststoreCertificateSubjectAlternativesSchema.resource": False,
    "SecurityTruststoreCertificateSubjectAlternativesSchema.opts": False,
    "SecurityTruststoreCertificateSubjectAlternatives": False,
}


class SecurityTruststoreCertificateSubjectAlternativesSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityTruststoreCertificateSubjectAlternatives object"""

    dns = fields.List(fields.Str, data_key="dns")
    r""" A list of DNS names for Subject Alternate name extension. """

    email = fields.List(fields.Str, data_key="email")
    r""" A list of email addresses for Subject Alternate name extension """

    ip = fields.List(fields.Str, data_key="ip")
    r""" A list of IP addresses for Subject Alternate name extension. """

    uri = fields.List(fields.Str, data_key="uri")
    r""" A list of URIs for Subject Alternate name extension. """

    @property
    def resource(self):
        return SecurityTruststoreCertificateSubjectAlternatives

    gettable_fields = [
        "dns",
        "email",
        "ip",
        "uri",
    ]
    """dns,email,ip,uri,"""

    patchable_fields = [
        "dns",
        "email",
        "ip",
        "uri",
    ]
    """dns,email,ip,uri,"""

    postable_fields = [
        "dns",
        "email",
        "ip",
        "uri",
    ]
    """dns,email,ip,uri,"""


class SecurityTruststoreCertificateSubjectAlternatives(Resource):

    _schema = SecurityTruststoreCertificateSubjectAlternativesSchema
