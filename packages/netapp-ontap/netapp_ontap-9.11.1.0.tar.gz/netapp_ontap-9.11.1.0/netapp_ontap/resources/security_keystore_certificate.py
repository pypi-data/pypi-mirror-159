r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API displays security certificate information and manages the keystore certificates in ONTAP.
# TODO: Add examples
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


__all__ = ["SecurityKeystoreCertificate", "SecurityKeystoreCertificateSchema"]
__pdoc__ = {
    "SecurityKeystoreCertificateSchema.resource": False,
    "SecurityKeystoreCertificateSchema.opts": False,
    "SecurityKeystoreCertificate.security_keystore_certificate_show": False,
    "SecurityKeystoreCertificate.security_keystore_certificate_create": False,
    "SecurityKeystoreCertificate.security_keystore_certificate_modify": False,
    "SecurityKeystoreCertificate.security_keystore_certificate_delete": False,
}


class SecurityKeystoreCertificateSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityKeystoreCertificate object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the security_keystore_certificate. """

    algorithm = fields.Str(
        data_key="algorithm",
        validate=enum_validation(['rsa', 'ec']),
    )
    r""" Asymmetric Encryption Algorithm.

Valid choices:

* rsa
* ec """

    applications = fields.List(fields.Str, data_key="applications")
    r""" Applications actively using the certificate. """

    expiry_time = ImpreciseDateTime(
        data_key="expiry_time",
    )
    r""" Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.

Example: 2021-06-04T19:00:00Z """

    extended_key_usage = fields.Str(
        data_key="extended_key_usage",
        validate=enum_validation(['serverauth', 'clientauth', 'timestamping', 'anyextendedkeyusage', 'critical']),
    )
    r""" Extended key usage extensions.

Valid choices:

* serverauth
* clientauth
* timestamping
* anyextendedkeyusage
* critical """

    hash_function = fields.Str(
        data_key="hash_function",
        validate=enum_validation(['sha1', 'sha256', 'sha224', 'sha384', 'sha512']),
    )
    r""" Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.

Valid choices:

* sha1
* sha256
* sha224
* sha384
* sha512 """

    intermediate_certificates = fields.List(fields.Str, data_key="intermediate_certificates")
    r""" Chain of intermediate certificates, in PEM format. Can be provided in POST when installing a certificate. """

    issuer_subject_name = fields.Str(
        data_key="issuer_subject_name",
    )
    r""" Issuer Subject Name

Example: CN = ca.domain.com, OU = NTAP, C = US """

    key_usage = fields.Str(
        data_key="key_usage",
        validate=enum_validation(['digitalsignature', 'nonrepudiation', 'keyencipherment', 'dataencipherment', 'keyagreement', 'keycertsign', 'crlsign', 'encipheronly', 'decipheronly', 'critical']),
    )
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

    name = fields.Str(
        data_key="name",
    )
    r""" Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.

Example: cert1 """

    password = fields.Str(
        data_key="password",
    )
    r""" Password credentials for the private key. This is not audited.

Example: password """

    private_key = fields.Str(
        data_key="private_key",
    )
    r""" Private key certificate, in PEM format. Only valid for create when installing a CA-signed certificate. This is not audited.

Example: -----BEGIN PRIVATE KEY----- MIIBVAIBADANBgkqhkiG9w0BAQEFAASCAT4wggE6AgEAAkEAu1/a8f3G47cZ6pel Hd3aONMNkGJ8vSCH5QjicuDm92VtVwkAACEjIoZSLYlJvPD+odL+lFzVQSmkneW7 VCGqYQIDAQABAkAcfNpg6GCQxoneLOghvlUrRotNZGvqpUOEAvHK3X7AJhz5SU4V an36qvsAt5ghFMVM2iGvGaXbj0dAd+Jg64pxAiEA32Eh9mPtFSmZhTIUMeGcPmPk qIYCEuP8a/ZLmI9s4TsCIQDWvLQuvjSVfwPhi0TFAb5wqAET8X5LBFqtGX5QlUep EwIgFnqM02Gc4wtLoqa2d4qPkYu13+uUW9hLd4XSd6i/OS8CIQDT3elU+Rt+qIwW u0cFrVvNYSV3HNzDfS9N/IoxTagfewIgPvXADe5c2EWbhCUkhN+ZCf38AKewK9TW lQcDy4L+f14= -----END PRIVATE KEY----- """

    public_certificate = fields.Str(
        data_key="public_certificate",
    )
    r""" Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.

Example: -----BEGIN CERTIFICATE----- MIIBuzCCAWWgAwIBAgIIFTZBrqZwUUMwDQYJKoZIhvcNAQELBQAwHDENMAsGA1UE AxMEVEVTVDELMAkGA1UEBhMCVVMwHhcNMTgwNjA4MTgwOTAxWhcNMTkwNjA4MTgw OTAxWjAcMQ0wCwYDVQQDEwRURVNUMQswCQYDVQQGEwJVUzBcMA0GCSqGSIb3DQEB AQUAA0sAMEgCQQDaPvbqUJJFJ6NNTyK3Yb+ytSjJ9aa3yUmYTD9uMiP+6ycjxHWB e8u9z6yCHsW03ync+dnhE5c5z8wuDAY0fv15AgMBAAGjgYowgYcwDAYDVR0TBAUw AwEB/zALBgNVHQ8EBAMCAQYwHQYDVR0OBBYEFMJ7Ev/o/3+YNzYh5XNlqqjnw4zm MEsGA1UdIwREMEKAFMJ7Ev/o/3+YNzYh5XNlqqjnw4zmoSCkHjAcMQ0wCwYDVQQD EwRURVNUMQswCQYDVQQGEwJVU4IIFTZBrqZwUUMwDQYJKoZIhvcNAQELBQADQQAv DovYeyGNnknjGI+TVNX6nDbyzf7zUPqnri0KuvObEeybrbPW45sgsnT5dyeE/32U 9Yr6lklnkBtVBDTmLnrC -----END CERTIFICATE----- """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for interfaces owned by an SVM. Otherwise, set to "cluster".

Valid choices:

* svm
* cluster """

    security_strength = Size(
        data_key="security_strength",
    )
    r""" Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate. """

    self_signed = fields.Boolean(
        data_key="self_signed",
    )
    r""" Indicates if this is a self-signed certificate. """

    serial_number = fields.Str(
        data_key="serial_number",
        validate=len_validation(minimum=1, maximum=40),
    )
    r""" Serial number of certificate. """

    start_time = ImpreciseDateTime(
        data_key="start_time",
    )
    r""" Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.

Example: 2020-06-04T19:00:00Z """

    subject_alternatives = fields.Nested("netapp_ontap.models.subject_alternate_name.SubjectAlternateNameSchema", data_key="subject_alternatives", unknown=EXCLUDE)
    r""" The subject_alternatives field of the security_keystore_certificate. """

    subject_name = fields.Str(
        data_key="subject_name",
    )
    r""" Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.

Example: C=US,S=NC,O=NTAP,CN=test.domain.com """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the security_keystore_certificate. """

    system_generated = fields.Boolean(
        data_key="system_generated",
    )
    r""" Indicates if this is a system-generated certificate. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique ID that identifies a certificate. """

    @property
    def resource(self):
        return SecurityKeystoreCertificate

    gettable_fields = [
        "links",
        "algorithm",
        "applications",
        "expiry_time",
        "extended_key_usage",
        "hash_function",
        "intermediate_certificates",
        "issuer_subject_name",
        "key_usage",
        "name",
        "public_certificate",
        "scope",
        "security_strength",
        "self_signed",
        "serial_number",
        "start_time",
        "subject_alternatives",
        "subject_name",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "system_generated",
        "uuid",
    ]
    """links,algorithm,applications,expiry_time,extended_key_usage,hash_function,intermediate_certificates,issuer_subject_name,key_usage,name,public_certificate,scope,security_strength,self_signed,serial_number,start_time,subject_alternatives,subject_name,svm.links,svm.name,svm.uuid,system_generated,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "algorithm",
        "expiry_time",
        "extended_key_usage",
        "hash_function",
        "intermediate_certificates",
        "key_usage",
        "name",
        "password",
        "private_key",
        "public_certificate",
        "security_strength",
        "start_time",
        "subject_name",
        "svm.name",
        "svm.uuid",
    ]
    """algorithm,expiry_time,extended_key_usage,hash_function,intermediate_certificates,key_usage,name,password,private_key,public_certificate,security_strength,start_time,subject_name,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SecurityKeystoreCertificate.get_collection(fields=field)]
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
            raise NetAppRestError("SecurityKeystoreCertificate modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SecurityKeystoreCertificate(Resource):
    """Allows interaction with SecurityKeystoreCertificate objects on the host"""

    _schema = SecurityKeystoreCertificateSchema
    _path = "/api/security/keystore-certificates"
    _keys = ["uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves end entity certificates from ONTAP's Keystore.
### Related ONTAP commands
* `security certificate keystore`
* `security certificate keystore show-active`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security keystore certificate show")
        def security_keystore_certificate_show(
            fields: List[Choices.define(["algorithm", "applications", "expiry_time", "extended_key_usage", "hash_function", "intermediate_certificates", "issuer_subject_name", "key_usage", "name", "password", "private_key", "public_certificate", "scope", "security_strength", "self_signed", "serial_number", "start_time", "subject_name", "system_generated", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SecurityKeystoreCertificate resources

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                extended_key_usage: Extended key usage extensions.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                intermediate_certificates: Chain of intermediate certificates, in PEM format. Can be provided in POST when installing a certificate.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                password: Password credentials for the private key. This is not audited.
                private_key: Private key certificate, in PEM format. Only valid for create when installing a CA-signed certificate. This is not audited.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                system_generated: Indicates if this is a system-generated certificate.
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if applications is not None:
                kwargs["applications"] = applications
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if extended_key_usage is not None:
                kwargs["extended_key_usage"] = extended_key_usage
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
            if intermediate_certificates is not None:
                kwargs["intermediate_certificates"] = intermediate_certificates
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
            if password is not None:
                kwargs["password"] = password
            if private_key is not None:
                kwargs["private_key"] = private_key
            if public_certificate is not None:
                kwargs["public_certificate"] = public_certificate
            if scope is not None:
                kwargs["scope"] = scope
            if security_strength is not None:
                kwargs["security_strength"] = security_strength
            if self_signed is not None:
                kwargs["self_signed"] = self_signed
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if system_generated is not None:
                kwargs["system_generated"] = system_generated
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SecurityKeystoreCertificate.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SecurityKeystoreCertificate resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["SecurityKeystoreCertificate"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SecurityKeystoreCertificate"], NetAppResponse]:
        r"""Creates or installs an end entity certificate as part of ONTAP's Keystore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
* `public_certificate` - Public key certificate, in PEM format. Required when installing a certificate.
* `private_key` - Private key certificate, in PEM format. Required when installing a CA-signed certificate.
### Recommended optional properties
* `cert-name` - Unique name to identify the certificate within the SVM.
* `subject_name` - Subject details of the certificate.
* `expiry_time` - Certificate expiration time. Specifying an expiration time is recommended when creating a certificate.
* `security_strength` - Key size of the certificate, in bits. Specifying a stronger security strength in bits is recommended when creating a certificate.
* `algorithm` - Asymmetric algorithm. Algroithm to use to generate public/private key pair when creating a certificate.
* `key_password` - Password for encrypting the private key when creating a self signed certificate.
* `hash_function` - Hashing function. Can be provided on POST when creating a self-signed certificate.
* `rfc822_name` - Email address for subject alternate name extension.
* `uri` - URI for subject alternate name extension.
* `dns_name` - DNS name for subject alternate name extension.
* `ipaddr` - IP address for subject alternate name extension.
### Default property values
If not specified in POST, the following default property values are assigned:
* `security_strength` - _112_
* `expiry_time` - _P365DT_
* `hash_function` - _sha256_
### Related ONTAP commands
* `security certificate keystore create`
* `security certificate keystore install`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SecurityKeystoreCertificate"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an installed end entity certificate from ONTAP's Keystore.
### Related ONTAP commands
* `security certificate keystore delete`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves end entity certificates from ONTAP's Keystore.
### Related ONTAP commands
* `security certificate keystore`
* `security certificate keystore show-active`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an installed or created end entity certificate from ONTAP's Keystore.
### Related ONTAP commands
* `security certificate keystore show`
* `security certificate keystore show-active`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
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
        r"""Creates or installs an end entity certificate as part of ONTAP's Keystore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
* `public_certificate` - Public key certificate, in PEM format. Required when installing a certificate.
* `private_key` - Private key certificate, in PEM format. Required when installing a CA-signed certificate.
### Recommended optional properties
* `cert-name` - Unique name to identify the certificate within the SVM.
* `subject_name` - Subject details of the certificate.
* `expiry_time` - Certificate expiration time. Specifying an expiration time is recommended when creating a certificate.
* `security_strength` - Key size of the certificate, in bits. Specifying a stronger security strength in bits is recommended when creating a certificate.
* `algorithm` - Asymmetric algorithm. Algroithm to use to generate public/private key pair when creating a certificate.
* `key_password` - Password for encrypting the private key when creating a self signed certificate.
* `hash_function` - Hashing function. Can be provided on POST when creating a self-signed certificate.
* `rfc822_name` - Email address for subject alternate name extension.
* `uri` - URI for subject alternate name extension.
* `dns_name` - DNS name for subject alternate name extension.
* `ipaddr` - IP address for subject alternate name extension.
### Default property values
If not specified in POST, the following default property values are assigned:
* `security_strength` - _112_
* `expiry_time` - _P365DT_
* `hash_function` - _sha256_
### Related ONTAP commands
* `security certificate keystore create`
* `security certificate keystore install`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security keystore certificate create")
        async def security_keystore_certificate_create(
        ) -> ResourceTable:
            """Create an instance of a SecurityKeystoreCertificate resource

            Args:
                links: 
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                extended_key_usage: Extended key usage extensions.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                intermediate_certificates: Chain of intermediate certificates, in PEM format. Can be provided in POST when installing a certificate.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                password: Password credentials for the private key. This is not audited.
                private_key: Private key certificate, in PEM format. Only valid for create when installing a CA-signed certificate. This is not audited.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_alternatives: 
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                svm: 
                system_generated: Indicates if this is a system-generated certificate.
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if applications is not None:
                kwargs["applications"] = applications
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if extended_key_usage is not None:
                kwargs["extended_key_usage"] = extended_key_usage
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
            if intermediate_certificates is not None:
                kwargs["intermediate_certificates"] = intermediate_certificates
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
            if password is not None:
                kwargs["password"] = password
            if private_key is not None:
                kwargs["private_key"] = private_key
            if public_certificate is not None:
                kwargs["public_certificate"] = public_certificate
            if scope is not None:
                kwargs["scope"] = scope
            if security_strength is not None:
                kwargs["security_strength"] = security_strength
            if self_signed is not None:
                kwargs["self_signed"] = self_signed
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if subject_alternatives is not None:
                kwargs["subject_alternatives"] = subject_alternatives
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if svm is not None:
                kwargs["svm"] = svm
            if system_generated is not None:
                kwargs["system_generated"] = system_generated
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = SecurityKeystoreCertificate(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SecurityKeystoreCertificate: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an installed end entity certificate from ONTAP's Keystore.
### Related ONTAP commands
* `security certificate keystore delete`

### Learn more
* [`DOC /security/keystore-certificates`](#docs-security-security_keystore-certificates)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security keystore certificate delete")
        async def security_keystore_certificate_delete(
        ) -> None:
            """Delete an instance of a SecurityKeystoreCertificate resource

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                extended_key_usage: Extended key usage extensions.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                intermediate_certificates: Chain of intermediate certificates, in PEM format. Can be provided in POST when installing a certificate.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                password: Password credentials for the private key. This is not audited.
                private_key: Private key certificate, in PEM format. Only valid for create when installing a CA-signed certificate. This is not audited.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                system_generated: Indicates if this is a system-generated certificate.
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if applications is not None:
                kwargs["applications"] = applications
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if extended_key_usage is not None:
                kwargs["extended_key_usage"] = extended_key_usage
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
            if intermediate_certificates is not None:
                kwargs["intermediate_certificates"] = intermediate_certificates
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
            if password is not None:
                kwargs["password"] = password
            if private_key is not None:
                kwargs["private_key"] = private_key
            if public_certificate is not None:
                kwargs["public_certificate"] = public_certificate
            if scope is not None:
                kwargs["scope"] = scope
            if security_strength is not None:
                kwargs["security_strength"] = security_strength
            if self_signed is not None:
                kwargs["self_signed"] = self_signed
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if system_generated is not None:
                kwargs["system_generated"] = system_generated
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(SecurityKeystoreCertificate, "find"):
                resource = SecurityKeystoreCertificate.find(
                    **kwargs
                )
            else:
                resource = SecurityKeystoreCertificate()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SecurityKeystoreCertificate: %s" % err)


