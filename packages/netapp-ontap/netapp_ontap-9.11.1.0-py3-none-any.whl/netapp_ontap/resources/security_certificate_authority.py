r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API displays security certificate information and manages the local certificate authorities in ONTAP.
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


__all__ = ["SecurityCertificateAuthority", "SecurityCertificateAuthoritySchema"]
__pdoc__ = {
    "SecurityCertificateAuthoritySchema.resource": False,
    "SecurityCertificateAuthoritySchema.opts": False,
    "SecurityCertificateAuthority.security_certificate_authority_show": False,
    "SecurityCertificateAuthority.security_certificate_authority_create": False,
    "SecurityCertificateAuthority.security_certificate_authority_modify": False,
    "SecurityCertificateAuthority.security_certificate_authority_delete": False,
}


class SecurityCertificateAuthoritySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SecurityCertificateAuthority object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the security_certificate_authority. """

    algorithm = fields.Str(
        data_key="algorithm",
        validate=enum_validation(['rsa', 'ec']),
    )
    r""" Asymmetric Encryption Algorithm.

Valid choices:

* rsa
* ec """

    expiry_time = ImpreciseDateTime(
        data_key="expiry_time",
    )
    r""" Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.

Example: 2021-06-04T19:00:00Z """

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
    r""" Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate. """

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
    r""" The subject_alternatives field of the security_certificate_authority. """

    subject_name = fields.Str(
        data_key="subject_name",
    )
    r""" Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.

Example: C=US,S=NC,O=NTAP,CN=test.domain.com """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the security_certificate_authority. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Unique ID that identifies a certificate. """

    @property
    def resource(self):
        return SecurityCertificateAuthority

    gettable_fields = [
        "links",
        "algorithm",
        "expiry_time",
        "hash_function",
        "key_usage",
        "name",
        "public_certificate",
        "scope",
        "security_strength",
        "serial_number",
        "start_time",
        "subject_alternatives",
        "subject_name",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
    ]
    """links,algorithm,expiry_time,hash_function,key_usage,name,public_certificate,scope,security_strength,serial_number,start_time,subject_alternatives,subject_name,svm.links,svm.name,svm.uuid,uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
        "algorithm",
        "expiry_time",
        "hash_function",
        "key_usage",
        "name",
        "security_strength",
        "start_time",
        "subject_name",
        "svm.name",
        "svm.uuid",
    ]
    """algorithm,expiry_time,hash_function,key_usage,name,security_strength,start_time,subject_name,svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SecurityCertificateAuthority.get_collection(fields=field)]
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
            raise NetAppRestError("SecurityCertificateAuthority modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SecurityCertificateAuthority(Resource):
    """Allows interaction with SecurityCertificateAuthority objects on the host"""

    _schema = SecurityCertificateAuthoritySchema
    _path = "/api/security/certificate-authorities"
    _keys = ["uuid"]
    _action_form_data_parameters = { 'file':'file', }

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves certificate authorities created in ONTAP.
### Related ONTAP commands
* `security certificate authority show`
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security certificate authority show")
        def security_certificate_authority_show(
            fields: List[Choices.define(["algorithm", "expiry_time", "hash_function", "key_usage", "name", "public_certificate", "scope", "security_strength", "serial_number", "start_time", "subject_name", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SecurityCertificateAuthority resources

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
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
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SecurityCertificateAuthority.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SecurityCertificateAuthority resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["SecurityCertificateAuthority"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SecurityCertificateAuthority"], NetAppResponse]:
        r"""Creates a certificate authority in ONTAP and installs its public certificate in truststore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
### Recommended optional properties
* `cert-name` - Unique name to identify the certificate within the SVM.
* `subject_name` - Subject details of the certificate.
* `expiry_time` - Certificate expiration time. Specifying an expiration time is recommended when creating a certificate authority.
* `security_strength` - Key size of the certificate, in bits Specifying a stronger security strength in bits is recommended when creating a certificate authority.
* `algorithm` - Asymmetric algorithm. Algroithm to use to generate public/private key pair when creating a certificate authority.
* `key_password` - Password for encrypting the private key when creating a self signed certificatea authority.
* `hash_function` - Hashing function. Can be provided on POST when creating a self-signed certificate authority.
* `rfc822_name` - Email address for the subject alternate name extension.
* `uri` - URI for the subject alternate name extension.
* `dns_name` - DNS name for the subject alternate name extension.
* `ipaddr` - IP address for the subject alternate name extension.
### Default property values
If not specified in POST, the following default property values are assigned:
* `security_strength` - _112_
* `expiry_time` - _P365DT_
* `hash_function` - _sha256_
### Related ONTAP commands
* `security certificate authority create`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["SecurityCertificateAuthority"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a local certificate authority from ONTAP.
### Related ONTAP commands
* `security certificate authority delete`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves certificate authorities created in ONTAP.
### Related ONTAP commands
* `security certificate authority show`
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a local certificate authority from ONTAP.
### Related ONTAP commands
* `security certificate authority show`
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
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
        r"""Creates a certificate authority in ONTAP and installs its public certificate in truststore.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM in which to create or install the certificate.
### Recommended optional properties
* `cert-name` - Unique name to identify the certificate within the SVM.
* `subject_name` - Subject details of the certificate.
* `expiry_time` - Certificate expiration time. Specifying an expiration time is recommended when creating a certificate authority.
* `security_strength` - Key size of the certificate, in bits Specifying a stronger security strength in bits is recommended when creating a certificate authority.
* `algorithm` - Asymmetric algorithm. Algroithm to use to generate public/private key pair when creating a certificate authority.
* `key_password` - Password for encrypting the private key when creating a self signed certificatea authority.
* `hash_function` - Hashing function. Can be provided on POST when creating a self-signed certificate authority.
* `rfc822_name` - Email address for the subject alternate name extension.
* `uri` - URI for the subject alternate name extension.
* `dns_name` - DNS name for the subject alternate name extension.
* `ipaddr` - IP address for the subject alternate name extension.
### Default property values
If not specified in POST, the following default property values are assigned:
* `security_strength` - _112_
* `expiry_time` - _P365DT_
* `hash_function` - _sha256_
### Related ONTAP commands
* `security certificate authority create`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security certificate authority create")
        async def security_certificate_authority_create(
        ) -> ResourceTable:
            """Create an instance of a SecurityCertificateAuthority resource

            Args:
                links: 
                algorithm: Asymmetric Encryption Algorithm.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_alternatives: 
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                svm: 
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
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
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = SecurityCertificateAuthority(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SecurityCertificateAuthority: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a local certificate authority from ONTAP.
### Related ONTAP commands
* `security certificate authority delete`

### Learn more
* [`DOC /security/certificate-authorities`](#docs-security-security_certificate-authorities)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="security certificate authority delete")
        async def security_certificate_authority_delete(
        ) -> None:
            """Delete an instance of a SecurityCertificateAuthority resource

            Args:
                algorithm: Asymmetric Encryption Algorithm.
                expiry_time: Certificate expiration time. Can be provided on POST if creating a self-signed certificate. Default value is 300 days from the current date.
                hash_function: Hashing function. Can be provided on POST when creating a self-signed certificate. Hash function sha1 is not allowed on POST.
                key_usage: Key usage extensions.
                name: Certificate name. If not provided in POST, a unique name specific to the SVM is automatically generated.
                public_certificate: Public key certificate, in PEM format. If this is not provided in POST, a self-signed certificate is created.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_strength: Security strength of the certificate, in bits. Can be provided on POST if creating a self-signed certificate.
                serial_number: Serial number of certificate.
                start_time: Certificate validity start time. Can be provided on POST if creating a self-signed certificate. Default value is current time.
                subject_name: Subject name details of the certificate. Provide on POST when creating a self-signed certificate. The format is a list of comma seperated key=value pairs.
                uuid: Unique ID that identifies a certificate.
            """

            kwargs = {}
            if algorithm is not None:
                kwargs["algorithm"] = algorithm
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if hash_function is not None:
                kwargs["hash_function"] = hash_function
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
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(SecurityCertificateAuthority, "find"):
                resource = SecurityCertificateAuthority.find(
                    **kwargs
                )
            else:
                resource = SecurityCertificateAuthority()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete SecurityCertificateAuthority: %s" % err)

    def sign(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Signs a certificate.
### Required properties
* `signing_request` - Certificate signing request to be signed by the given certificate authority.
### Recommended optional properties
* `expiry_time` - Certificate expiration time. Specifying an expiration time for a signed certificate is recommended.
* `hash_function` - Hashing function. Specifying a strong hashing function is recommended when signing a certificate.
### Default property values
If not specified in POST, the following default property values are assigned:
* `expiry_time` - _P300DT_
* `hash_function` - _sha256_
### Related ONTAP commands
* `security certificate authority sign`
This API is used to sign a certificate request using an existing local certificate authority. The local certificate authority maintains the records of its signed certificates. <br/>
The root certificate can be created for a given SVM or for the cluster using [`POST security/certificate-authorities`].<br/>
"""
        return super()._action(
            "sign", body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    sign.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._action.__doc__)

