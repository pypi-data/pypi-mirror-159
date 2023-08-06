r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SecurityCertificateAuthoritySign", "SecurityCertificateAuthoritySignSchema"]
__pdoc__ = {
    "SecurityCertificateAuthoritySignSchema.resource": False,
    "SecurityCertificateAuthoritySignSchema.opts": False,
    "SecurityCertificateAuthoritySign": False,
}


class SecurityCertificateAuthoritySignSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityCertificateAuthoritySign object"""

    expiry_time = ImpreciseDateTime(data_key="expiry_time")
    r""" Certificate expiration time. Default value is 300 days from the current date.

Example: 2021-06-04T19:00:00Z """

    extended_key_usage = fields.Str(data_key="extended_key_usage")
    r""" Extended key usage extensions.

Valid choices:

* serverauth
* clientauth
* timestamping
* anyextendedkeyusage
* critical """

    hash_function = fields.Str(data_key="hash_function")
    r""" Hashing function

Valid choices:

* sha256
* sha224
* sha384
* sha512 """

    key_usage = fields.Str(data_key="key_usage")
    r""" Key usage extensions.

Valid choices:

* digitalsignature
* nonrepudiation
* keyencipherment
* dataencipherment
* keyagreement
* keycertsign
* crlsign
* encipheronly
* decipheronly
* critical """

    public_certificate = fields.Str(data_key="public_certificate")
    r""" CA signed public key certificate """

    signing_request = fields.Str(data_key="signing_request")
    r""" Certificate signing request to be signed by the given certificate authority. Request should be in PEM format.

Example: '-----BEGIN CERTIFICATE REQUEST----- MIICYDCCAUgCAQAwGzEMMAoGA1UEAxMDQUJDMQswCQYDVQQGEwJVUzCCASIwDQYJ KoZIhvcNAQEBBQADggEPADCCAQoCggEBAPF+82SlqT3Vyu3Jx4IAwHcO5EGwLOxy zQ6KNjz71Fca0n1/A1CbCPyOsSupGVObvdWxX7xLVMJ2SXb7h43GCqYyX6FXJO4F HOpmLvB+jxdeiW7SDbiZyLUlsvA+oRO/uNlcug773QZdKLjJD64erZZMRUNbUJB8 bARxAUi0FPvgTraSQ0UW5sRLiGKeAyKA4wekYe1VgjHRTBizFbD4dI3njfva/2Bl jf+kkulgcLJTuJNtkgeimqMKyraYuleYcYk2K+C//0NuNOuPbDfTXCM7O61vik09 Szi8nLN7OXE9KoAA93U/BCpSfpl8XIb4cGnEr8hgVHOOtZSo+KZBFxMCAwEAAaAA MA0GCSqGSIb3DQEBCwUAA4IBAQC2vFYpvgsFrm5GnPx8tOBD1xsTyYjbWJMD8hAF lFrvF9Sw9QGCtDyacxkwgJhQx8l8JiIS5GOY6WWLBl9FMkLQNAhDL9xF3WF7vfYq RKgrz3bd/Vg96fsRZNYIPLGmoEaqLOh3FOCGc2VbdsR9PwOn3fwthxkIRd6ds6/q jc5cpSmVsCOgu+OKcpRXikYDbkWXfTZ1AhSfn6njBYFdZ9+PNAu/0JRQh5bX60nO 5heniTcAJLwUZP/CQ8nxHY0Wqy+1rAtM33d5cVmhUlBXQSIru/0ZkA/b9fK5Zv8E ZMADYUoEvIG59Vxhyci8lzYf+Mxl8qBSF+ZdC4yWhzDqZtM9 -----END CERTIFICATE REQUEST-----' """

    start_time = ImpreciseDateTime(data_key="start_time")
    r""" Certificate activation time. Default value is the current time. """

    @property
    def resource(self):
        return SecurityCertificateAuthoritySign

    gettable_fields = [
        "expiry_time",
        "extended_key_usage",
        "hash_function",
        "key_usage",
        "public_certificate",
        "signing_request",
        "start_time",
    ]
    """expiry_time,extended_key_usage,hash_function,key_usage,public_certificate,signing_request,start_time,"""

    patchable_fields = [
        "expiry_time",
        "extended_key_usage",
        "hash_function",
        "key_usage",
        "signing_request",
    ]
    """expiry_time,extended_key_usage,hash_function,key_usage,signing_request,"""

    postable_fields = [
        "expiry_time",
        "extended_key_usage",
        "hash_function",
        "key_usage",
        "signing_request",
    ]
    """expiry_time,extended_key_usage,hash_function,key_usage,signing_request,"""


class SecurityCertificateAuthoritySign(Resource):

    _schema = SecurityCertificateAuthoritySignSchema
