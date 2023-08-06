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


__all__ = ["SvmAccount", "SvmAccountSchema"]
__pdoc__ = {
    "SvmAccountSchema.resource": False,
    "SvmAccountSchema.opts": False,
    "SvmAccount.svm_account_show": False,
    "SvmAccount.svm_account_create": False,
    "SvmAccount.svm_account_modify": False,
    "SvmAccount.svm_account_delete": False,
}


class SvmAccountSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SvmAccount object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the svm_account. """

    applications = fields.List(fields.Nested("netapp_ontap.models.account_application.AccountApplicationSchema", unknown=EXCLUDE), data_key="applications")
    r""" The applications field of the svm_account. """

    authentication_methods = fields.List(fields.Str, data_key="authentication_methods")
    r""" The authentication_methods field of the svm_account. """

    comment = fields.Str(
        data_key="comment",
    )
    r""" Optional comment for the user account. """

    ldap_fastbind = fields.Boolean(
        data_key="ldap_fastbind",
    )
    r""" Optional property that specifies the mode of authentication is LDAP Fastbind. """

    locked = fields.Boolean(
        data_key="locked",
    )
    r""" Locked status of the account. """

    name = fields.Str(
        data_key="name",
        validate=len_validation(minimum=3, maximum=64),
    )
    r""" User or group account name

Example: joe.smith """

    owner = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="owner", unknown=EXCLUDE)
    r""" The owner field of the svm_account. """

    password = fields.Str(
        data_key="password",
        validate=len_validation(minimum=8, maximum=128),
    )
    r""" Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters. """

    password_hash_algorithm = fields.Str(
        data_key="password_hash_algorithm",
        validate=enum_validation(['sha512', 'sha256', 'md5']),
    )
    r""" Optional property that specifies the password hash algorithm used to generate a hash of the user's password for password matching.

Valid choices:

* sha512
* sha256
* md5 """

    public_key = fields.Str(
        data_key="public_key",
    )
    r""" Public key for SSH. """

    role = fields.Nested("netapp_ontap.resources.role.RoleSchema", data_key="role", unknown=EXCLUDE)
    r""" The role field of the svm_account. """

    scope = fields.Str(
        data_key="scope",
        validate=enum_validation(['cluster', 'svm']),
    )
    r""" Scope of the entity. Set to "cluster" for cluster owned objects and to "svm" for SVM owned objects.

Valid choices:

* cluster
* svm """

    ssl_ca_certificate = fields.Str(
        data_key="ssl_ca_certificate",
    )
    r""" SSL certificate for the chain of certificate authorities (CA) that have signed this user's client certificate. """

    @property
    def resource(self):
        return SvmAccount

    gettable_fields = [
        "links",
        "applications",
        "authentication_methods",
        "comment",
        "ldap_fastbind",
        "locked",
        "name",
        "owner.links",
        "owner.name",
        "owner.uuid",
        "password_hash_algorithm",
        "public_key",
        "role.links",
        "role.name",
        "scope",
        "ssl_ca_certificate",
    ]
    """links,applications,authentication_methods,comment,ldap_fastbind,locked,name,owner.links,owner.name,owner.uuid,password_hash_algorithm,public_key,role.links,role.name,scope,ssl_ca_certificate,"""

    patchable_fields = [
        "applications",
        "authentication_methods",
        "comment",
        "ldap_fastbind",
        "locked",
        "password",
        "password_hash_algorithm",
        "public_key",
        "role.name",
        "ssl_ca_certificate",
    ]
    """applications,authentication_methods,comment,ldap_fastbind,locked,password,password_hash_algorithm,public_key,role.name,ssl_ca_certificate,"""

    postable_fields = [
        "applications",
        "authentication_methods",
        "comment",
        "ldap_fastbind",
        "locked",
        "name",
        "owner.name",
        "owner.uuid",
        "password",
        "password_hash_algorithm",
        "public_key",
        "role.name",
        "ssl_ca_certificate",
    ]
    """applications,authentication_methods,comment,ldap_fastbind,locked,name,owner.name,owner.uuid,password,password_hash_algorithm,public_key,role.name,ssl_ca_certificate,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in SvmAccount.get_collection(fields=field)]
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
            raise NetAppRestError("SvmAccount modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class SvmAccount(Resource):
    r""" Second account clone. """

    _schema = SvmAccountSchema
    _path = "/api/security/svm/accounts"

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of SVM user and group accounts."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="svm account show")
        def svm_account_show(
            fields: List[Choices.define(["authentication_methods", "comment", "ldap_fastbind", "locked", "name", "password", "password_hash_algorithm", "public_key", "scope", "ssl_ca_certificate", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of SvmAccount resources

            Args:
                authentication_methods: 
                comment: Optional comment for the user account.
                ldap_fastbind: Optional property that specifies the mode of authentication is LDAP Fastbind.
                locked: Locked status of the account.
                name: User or group account name
                password: Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters.
                password_hash_algorithm: Optional property that specifies the password hash algorithm used to generate a hash of the user's password for password matching.
                public_key: Public key for SSH.
                scope: Scope of the entity. Set to \"cluster\" for cluster owned objects and to \"svm\" for SVM owned objects.
                ssl_ca_certificate: SSL certificate for the chain of certificate authorities (CA) that have signed this user's client certificate.
            """

            kwargs = {}
            if authentication_methods is not None:
                kwargs["authentication_methods"] = authentication_methods
            if comment is not None:
                kwargs["comment"] = comment
            if ldap_fastbind is not None:
                kwargs["ldap_fastbind"] = ldap_fastbind
            if locked is not None:
                kwargs["locked"] = locked
            if name is not None:
                kwargs["name"] = name
            if password is not None:
                kwargs["password"] = password
            if password_hash_algorithm is not None:
                kwargs["password_hash_algorithm"] = password_hash_algorithm
            if public_key is not None:
                kwargs["public_key"] = public_key
            if scope is not None:
                kwargs["scope"] = scope
            if ssl_ca_certificate is not None:
                kwargs["ssl_ca_certificate"] = ssl_ca_certificate
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return SvmAccount.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all SvmAccount resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)


    @classmethod
    def post_collection(
        cls,
        records: Iterable["SvmAccount"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["SvmAccount"], NetAppResponse]:
        r"""Creates a new SVM user or group account."""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)


    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of SVM user and group accounts."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)


    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a new SVM user or group account."""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="svm account create")
        async def svm_account_create(
        ) -> ResourceTable:
            """Create an instance of a SvmAccount resource

            Args:
                links: 
                applications: 
                authentication_methods: 
                comment: Optional comment for the user account.
                ldap_fastbind: Optional property that specifies the mode of authentication is LDAP Fastbind.
                locked: Locked status of the account.
                name: User or group account name
                owner: 
                password: Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters.
                password_hash_algorithm: Optional property that specifies the password hash algorithm used to generate a hash of the user's password for password matching.
                public_key: Public key for SSH.
                role: 
                scope: Scope of the entity. Set to \"cluster\" for cluster owned objects and to \"svm\" for SVM owned objects.
                ssl_ca_certificate: SSL certificate for the chain of certificate authorities (CA) that have signed this user's client certificate.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if applications is not None:
                kwargs["applications"] = applications
            if authentication_methods is not None:
                kwargs["authentication_methods"] = authentication_methods
            if comment is not None:
                kwargs["comment"] = comment
            if ldap_fastbind is not None:
                kwargs["ldap_fastbind"] = ldap_fastbind
            if locked is not None:
                kwargs["locked"] = locked
            if name is not None:
                kwargs["name"] = name
            if owner is not None:
                kwargs["owner"] = owner
            if password is not None:
                kwargs["password"] = password
            if password_hash_algorithm is not None:
                kwargs["password_hash_algorithm"] = password_hash_algorithm
            if public_key is not None:
                kwargs["public_key"] = public_key
            if role is not None:
                kwargs["role"] = role
            if scope is not None:
                kwargs["scope"] = scope
            if ssl_ca_certificate is not None:
                kwargs["ssl_ca_certificate"] = ssl_ca_certificate

            resource = SvmAccount(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create SvmAccount: %s" % err)
            return [resource]




