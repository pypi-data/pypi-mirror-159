r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API displays and manages the certificates issued by a local certificate authority.
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


__all__ = ["IssuedCertificate", "IssuedCertificateSchema"]
__pdoc__ = {
    "IssuedCertificateSchema.resource": False,
    "IssuedCertificateSchema.opts": False,
    "IssuedCertificate.issued_certificate_show": False,
    "IssuedCertificate.issued_certificate_create": False,
    "IssuedCertificate.issued_certificate_modify": False,
    "IssuedCertificate.issued_certificate_delete": False,
}


class IssuedCertificateSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the IssuedCertificate object"""

    expiry_time = ImpreciseDateTime(
        data_key="expiry_time",
    )
    r""" Issued certificate expiration time. """

    revocation_time = ImpreciseDateTime(
        data_key="revocation_time",
    )
    r""" Issued certificate revocation time. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['svm', 'cluster']),
    )
    r""" Set to "svm" for interfaces owned by an SVM. Otherwise, set to "cluster".

Valid choices:

* svm
* cluster """

    security_certificate_authority_name = fields.Str(
        data_key="security_certificate_authority_name",
    )
    r""" Unique certificate name of the local certificate authority.

Example: cert1 """

    serial_number = fields.Str(
        data_key="serial_number",
        validate=len_validation(minimum=1, maximum=40),
    )
    r""" Serial number of the issued certificate. """

    start_time = ImpreciseDateTime(
        data_key="start_time",
    )
    r""" Issued certificate activation time. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['active', 'revoked']),
    )
    r""" Certificate state.

Valid choices:

* active
* revoked """

    subject_alternatives = fields.List(fields.Nested("netapp_ontap.models.subject_alternate_name.SubjectAlternateNameSchema", unknown=EXCLUDE), data_key="subject_alternatives")
    r""" Array of subject alternative names. """

    subject_name = fields.Str(
        data_key="subject_name",
    )
    r""" Subject details of the issued certificate.

Example: CN = test.domain.com, OU = NTAP, C = US """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the issued_certificate. """

    @property
    def resource(self):
        return IssuedCertificate

    gettable_fields = [
        "expiry_time",
        "revocation_time",
        "scope",
        "security_certificate_authority_name",
        "serial_number",
        "start_time",
        "state",
        "subject_alternatives",
        "subject_name",
        "svm.links",
        "svm.name",
        "svm.uuid",
    ]
    """expiry_time,revocation_time,scope,security_certificate_authority_name,serial_number,start_time,state,subject_alternatives,subject_name,svm.links,svm.name,svm.uuid,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in IssuedCertificate.get_collection(fields=field)]
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
            raise NetAppRestError("IssuedCertificate modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class IssuedCertificate(Resource):
    r""" Certificate signed and issued by a local certificate authority. """

    _schema = IssuedCertificateSchema
    _path = "/api/security/certificate-authorities/{security_certificate_authority[uuid]}/issued-certificates"
    _keys = ["security_certificate_authority.uuid", "serial_number"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves certificates issued by a local certificate authority in ONTAP.
### Related ONTAP commands
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities/{security_certificate_authority.uuid}/issued-certificates`](#docs-security-security_certificate-authorities_{security_certificate_authority.uuid}_issued-certificates)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="issued certificate show")
        def issued_certificate_show(
            security_certificate_authority_uuid,
            expiry_time: Choices.define(_get_field_list("expiry_time"), cache_choices=True, inexact=True)=None,
            revocation_time: Choices.define(_get_field_list("revocation_time"), cache_choices=True, inexact=True)=None,
            scope: Choices.define(_get_field_list("scope"), cache_choices=True, inexact=True)=None,
            security_certificate_authority_name: Choices.define(_get_field_list("security_certificate_authority_name"), cache_choices=True, inexact=True)=None,
            serial_number: Choices.define(_get_field_list("serial_number"), cache_choices=True, inexact=True)=None,
            start_time: Choices.define(_get_field_list("start_time"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            subject_name: Choices.define(_get_field_list("subject_name"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["expiry_time", "revocation_time", "scope", "security_certificate_authority_name", "serial_number", "start_time", "state", "subject_name", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of IssuedCertificate resources

            Args:
                expiry_time: Issued certificate expiration time.
                revocation_time: Issued certificate revocation time.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_certificate_authority_name: Unique certificate name of the local certificate authority.
                serial_number: Serial number of the issued certificate.
                start_time: Issued certificate activation time.
                state: Certificate state.
                subject_name: Subject details of the issued certificate.
            """

            kwargs = {}
            if expiry_time is not None:
                kwargs["expiry_time"] = expiry_time
            if revocation_time is not None:
                kwargs["revocation_time"] = revocation_time
            if scope is not None:
                kwargs["scope"] = scope
            if security_certificate_authority_name is not None:
                kwargs["security_certificate_authority_name"] = security_certificate_authority_name
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if start_time is not None:
                kwargs["start_time"] = start_time
            if state is not None:
                kwargs["state"] = state
            if subject_name is not None:
                kwargs["subject_name"] = subject_name
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return IssuedCertificate.get_collection(
                security_certificate_authority_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all IssuedCertificate resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["IssuedCertificate"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Revokes an issued certificate.
### Related ONTAP commands
* `security certificate authority revoke`

### Learn more
* [`DOC /security/certificate-authorities/{security_certificate_authority.uuid}/issued-certificates`](#docs-security-security_certificate-authorities_{security_certificate_authority.uuid}_issued-certificates)"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)



    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves certificates issued by a local certificate authority in ONTAP.
### Related ONTAP commands
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities/{security_certificate_authority.uuid}/issued-certificates`](#docs-security-security_certificate-authorities_{security_certificate_authority.uuid}_issued-certificates)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves details of a certificate issued by a local certificate authority in ONTAP.
### Related ONTAP commands
* `security certificate authority show-issued`

### Learn more
* [`DOC /security/certificate-authorities/{security_certificate_authority.uuid}/issued-certificates`](#docs-security-security_certificate-authorities_{security_certificate_authority.uuid}_issued-certificates)"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)


    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Revokes an issued certificate.
### Related ONTAP commands
* `security certificate authority revoke`

### Learn more
* [`DOC /security/certificate-authorities/{security_certificate_authority.uuid}/issued-certificates`](#docs-security-security_certificate-authorities_{security_certificate_authority.uuid}_issued-certificates)"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="issued certificate modify")
        async def issued_certificate_modify(
            security_certificate_authority_uuid,
            expiry_time: datetime = None,
            query_expiry_time: datetime = None,
            revocation_time: datetime = None,
            query_revocation_time: datetime = None,
            scope: str = None,
            query_scope: str = None,
            security_certificate_authority_name: str = None,
            query_security_certificate_authority_name: str = None,
            serial_number: str = None,
            query_serial_number: str = None,
            start_time: datetime = None,
            query_start_time: datetime = None,
            state: str = None,
            query_state: str = None,
            subject_name: str = None,
            query_subject_name: str = None,
        ) -> ResourceTable:
            """Modify an instance of a IssuedCertificate resource

            Args:
                expiry_time: Issued certificate expiration time.
                query_expiry_time: Issued certificate expiration time.
                revocation_time: Issued certificate revocation time.
                query_revocation_time: Issued certificate revocation time.
                scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                query_scope: Set to \"svm\" for interfaces owned by an SVM. Otherwise, set to \"cluster\".
                security_certificate_authority_name: Unique certificate name of the local certificate authority.
                query_security_certificate_authority_name: Unique certificate name of the local certificate authority.
                serial_number: Serial number of the issued certificate.
                query_serial_number: Serial number of the issued certificate.
                start_time: Issued certificate activation time.
                query_start_time: Issued certificate activation time.
                state: Certificate state.
                query_state: Certificate state.
                subject_name: Subject details of the issued certificate.
                query_subject_name: Subject details of the issued certificate.
            """

            kwargs = {}
            changes = {}
            if query_expiry_time is not None:
                kwargs["expiry_time"] = query_expiry_time
            if query_revocation_time is not None:
                kwargs["revocation_time"] = query_revocation_time
            if query_scope is not None:
                kwargs["scope"] = query_scope
            if query_security_certificate_authority_name is not None:
                kwargs["security_certificate_authority_name"] = query_security_certificate_authority_name
            if query_serial_number is not None:
                kwargs["serial_number"] = query_serial_number
            if query_start_time is not None:
                kwargs["start_time"] = query_start_time
            if query_state is not None:
                kwargs["state"] = query_state
            if query_subject_name is not None:
                kwargs["subject_name"] = query_subject_name

            if expiry_time is not None:
                changes["expiry_time"] = expiry_time
            if revocation_time is not None:
                changes["revocation_time"] = revocation_time
            if scope is not None:
                changes["scope"] = scope
            if security_certificate_authority_name is not None:
                changes["security_certificate_authority_name"] = security_certificate_authority_name
            if serial_number is not None:
                changes["serial_number"] = serial_number
            if start_time is not None:
                changes["start_time"] = start_time
            if state is not None:
                changes["state"] = state
            if subject_name is not None:
                changes["subject_name"] = subject_name

            if hasattr(IssuedCertificate, "find"):
                resource = IssuedCertificate.find(
                    security_certificate_authority_uuid,
                    **kwargs
                )
            else:
                resource = IssuedCertificate(security_certificate_authority_uuid,)
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify IssuedCertificate: %s" % err)



