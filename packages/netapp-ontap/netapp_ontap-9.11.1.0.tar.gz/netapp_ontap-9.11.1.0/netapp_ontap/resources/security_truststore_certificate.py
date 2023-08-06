r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API displays security certificate information and manages the truststore certificates in ONTAP.
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


__all__ = ["SecurityTruststoreCertificate", "SecurityTruststoreCertificateSchema"]
__pdoc__ = {
    "SecurityTruststoreCertificateSchema.resource": False,
    "SecurityTruststoreCertificateSchema.opts": False,
    "SecurityTruststoreCertificate.security_truststore_certificate_show": False,
    "SecurityTruststoreCertificate.security_truststore_certificate_create": False,
    "SecurityTruststoreCertificate.security_truststore_certificate_modify": False,
    "SecurityTruststoreCertificate.security_truststore_certificate_delete": False,
}


class SecurityTruststoreCertificateSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityTruststoreCertificate object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the security_truststore_certificate. """

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
    r""" Certificate expiration time.

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
    r""" Security strength of the certificate, in bits. """

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
    r""" Certificate validity start time. """

    subject_alternatives = fields.List(fields.Nested("netapp_ontap.models.issued_certificate_subject_alternatives.IssuedCertificateSubjectAlternativesSchema", unknown=EXCLUDE), data_key="subject_alternatives")
    r""" Array of subject alternative names. """

    subject_name = fields.Str(
        data_key="subject_name",
    )
    r""" Subject name details of the certificate.

Example: C=US,S=NC,O=NTAP,CN=test.domain.com """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the security_truststore_certificate. """

    system_installed = fields.Boolean(
        data_key="system_installed",
    )
    r""" Indicates if this is a system-installed certificate. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique ID that identifies a certificate. """

    @property
    def resource(self):
        return SecurityTruststoreCertificate

    gettable_fields = [
        "links",
        "algorithm",
        "applications",
        "expiry_time",
        "extended_key_usage",
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
        "system_installed",
        "uuid",
    ]
    """links,algorithm,applications,expiry_time,extended_key_usage,issuer_subject_name,key_usage,name,public_certificate,scope,security_strength,self_signed,serial_number,start_time,subject_alternatives,subject_name,svm.links,svm.name,svm.uuid,system_installed,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "name",
        "public_certificate",
        "svm.name",
        "svm.uuid",
    ]
    """name,public_certificate,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SecurityTruststoreCertificate.get_collection(fields=field)]
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
            raise NetAppRestError("SecurityTruststoreCertificate modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SecurityTruststoreCertificate(Resource):
    """Allows interaction with SecurityTruststoreCertificate objects on the host"""

    _schema = SecurityTruststoreCertificateSchema
    _path = "/api/security/truststore-certificates"
    _keys = ["uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves CA certificates from ONTAP's Truststore.
### Related ONTAP commands
* `security certificate truststore show`
* `security certificate truststore show-active`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security truststore certificate show")
        def security_truststore_certificate_show(
            fields: List[Choices.define(["algorithm", "applications", "expiry_time", "extended_key_usage", "issuer_subject_name", "key_usage", "name", "public_certificate", "scope", "security_strength", "self_signed", "serial_number", "start_time", "subject_name", "system_installed", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SecurityTruststoreCertificate resources

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time.
                extended_key_usage: Extended key usage extensions.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time.
                subject_name: Subject name details of the certificate.
                system_installed: Indicates if this is a system-installed certificate.
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
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
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
            if system_installed is not None:
                kwargs["system_installed"] = system_installed
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SecurityTruststoreCertificate.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SecurityTruststoreCertificate resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["SecurityTruststoreCertificate"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SecurityTruststoreCertificate"], NetAppResponse]:
        r"""Installs a CA certificate as part of ONTAP's Truststore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
* `public_certificate` - Public key certificate, in PEM format. Required when installing a certificate.
### Recommended optional properties
* `name` - A unique certificate name per SVM. If one is not provided, a name is automatically generated.
### Related ONTAP commands
* `security certificate truststore install`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SecurityTruststoreCertificate"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an installed CA certificate from ONTAP's Truststore.
### Related ONTAP commands
* `security certificate truststore delete`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves CA certificates from ONTAP's Truststore.
### Related ONTAP commands
* `security certificate truststore show`
* `security certificate truststore show-active`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an installed CA certificate from ONTAP's Truststore.
### Related ONTAP commands
* `security certificate truststore show`
* `security certificate truststore show-active`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
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
        r"""Installs a CA certificate as part of ONTAP's Truststore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
* `public_certificate` - Public key certificate, in PEM format. Required when installing a certificate.
### Recommended optional properties
* `name` - A unique certificate name per SVM. If one is not provided, a name is automatically generated.
### Related ONTAP commands
* `security certificate truststore install`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security truststore certificate create")
        async def security_truststore_certificate_create(
        ) -> ResourceTable:
            """Create an instance of a SecurityTruststoreCertificate resource

            Args:
                links: 
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time.
                extended_key_usage: Extended key usage extensions.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time.
                subject_alternatives: Array of subject alternative names.
                subject_name: Subject name details of the certificate.
                svm: 
                system_installed: Indicates if this is a system-installed certificate.
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
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
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
            if system_installed is not None:
                kwargs["system_installed"] = system_installed
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = SecurityTruststoreCertificate(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SecurityTruststoreCertificate: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an installed CA certificate from ONTAP's Truststore.
### Related ONTAP commands
* `security certificate truststore delete`

### Learn more
* [`DOC /security/truststore-certificates`](#docs-security-security_truststore-certificates)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security truststore certificate delete")
        async def security_truststore_certificate_delete(
        ) -> None:
            """Delete an instance of a SecurityTruststoreCertificate resource

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                applications: Applications actively using the certificate.
                expiry_time: Certificate expiration time.
                extended_key_usage: Extended key usage extensions.
                issuer_subject_name: Issuer Subject Name
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits.
                self_signed: Indicates if this is a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time.
                subject_name: Subject name details of the certificate.
                system_installed: Indicates if this is a system-installed certificate.
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
            if issuer_subject_name is not None:
                kwargs["issuer_subject_name"] = issuer_subject_name
            if key_usage is not None:
                kwargs["key_usage"] = key_usage
            if name is not None:
                kwargs["name"] = name
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
            if system_installed is not None:
                kwargs["system_installed"] = system_installed
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(SecurityTruststoreCertificate, "find"):
                resource = SecurityTruststoreCertificate.find(
                    **kwargs
                )
            else:
                resource = SecurityTruststoreCertificate()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SecurityTruststoreCertificate: %s" % err)


