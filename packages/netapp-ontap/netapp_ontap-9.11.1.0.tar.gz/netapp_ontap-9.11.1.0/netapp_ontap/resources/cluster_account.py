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


__all__ = ["ClusterAccount", "ClusterAccountSchema"]
__pdoc__ = {
    "ClusterAccountSchema.resource": False,
    "ClusterAccountSchema.opts": False,
    "ClusterAccount.cluster_account_show": False,
    "ClusterAccount.cluster_account_create": False,
    "ClusterAccount.cluster_account_modify": False,
    "ClusterAccount.cluster_account_delete": False,
}


class ClusterAccountSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ClusterAccount object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the cluster_account. """

    applications = fields.List(fields.Nested("netapp_ontap.models.account_application.AccountApplicationSchema", unknown=EXCLUDE), data_key="applications")
    r""" The applications field of the cluster_account. """

    authentication_methods = fields.List(fields.Str, data_key="authentication_methods")
    r""" The authentication_methods field of the cluster_account. """

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
    r""" The owner field of the cluster_account. """

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
    r""" The role field of the cluster_account. """

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
        return ClusterAccount

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
        return [getattr(r, field) for r in ClusterAccount.get_collection(fields=field)]
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
            raise NetAppRestError("ClusterAccount modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class ClusterAccount(Resource):
    """Allows interaction with ClusterAccount objects on the host"""

    _schema = ClusterAccountSchema
    _path = "/api/security/cluster/accounts"
    _keys = ["name"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of user and group accounts."""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cluster account show")
        def cluster_account_show(
            fields: List[Choices.define(["authentication_methods", "comment", "ldap_fastbind", "locked", "name", "password", "password_hash_algorithm", "public_key", "scope", "ssl_ca_certificate", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of ClusterAccount resources

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

            return ClusterAccount.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all ClusterAccount resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["ClusterAccount"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a user account."""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["ClusterAccount"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["ClusterAccount"], NetAppResponse]:
        r"""Creates a new user or group account."""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["ClusterAccount"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a user or group account."""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of user and group accounts."""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves a specific user or group account."""
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
        r"""Creates a new user or group account."""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cluster account create")
        async def cluster_account_create(
        ) -> ResourceTable:
            """Create an instance of a ClusterAccount resource

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

            resource = ClusterAccount(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create ClusterAccount: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a user account."""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cluster account modify")
        async def cluster_account_modify(
        ) -> ResourceTable:
            """Modify an instance of a ClusterAccount resource

            Args:
                authentication_methods: 
                query_authentication_methods: 
                comment: Optional comment for the user account.
                query_comment: Optional comment for the user account.
                ldap_fastbind: Optional property that specifies the mode of authentication is LDAP Fastbind.
                query_ldap_fastbind: Optional property that specifies the mode of authentication is LDAP Fastbind.
                locked: Locked status of the account.
                query_locked: Locked status of the account.
                name: User or group account name
                query_name: User or group account name
                password: Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters.
                query_password: Password for the account. The password can contain a mix of lower and upper case alphabetic characters, digits, and special characters.
                password_hash_algorithm: Optional property that specifies the password hash algorithm used to generate a hash of the user's password for password matching.
                query_password_hash_algorithm: Optional property that specifies the password hash algorithm used to generate a hash of the user's password for password matching.
                public_key: Public key for SSH.
                query_public_key: Public key for SSH.
                scope: Scope of the entity. Set to \"cluster\" for cluster owned objects and to \"svm\" for SVM owned objects.
                query_scope: Scope of the entity. Set to \"cluster\" for cluster owned objects and to \"svm\" for SVM owned objects.
                ssl_ca_certificate: SSL certificate for the chain of certificate authorities (CA) that have signed this user's client certificate.
                query_ssl_ca_certificate: SSL certificate for the chain of certificate authorities (CA) that have signed this user's client certificate.
            """

            kwargs = {}
            changes = {}
            if query_authentication_methods is not None:
                kwargs["authentication_methods"] = query_authentication_methods
            if query_comment is not None:
                kwargs["comment"] = query_comment
            if query_ldap_fastbind is not None:
                kwargs["ldap_fastbind"] = query_ldap_fastbind
            if query_locked is not None:
                kwargs["locked"] = query_locked
            if query_name is not None:
                kwargs["name"] = query_name
            if query_password is not None:
                kwargs["password"] = query_password
            if query_password_hash_algorithm is not None:
                kwargs["password_hash_algorithm"] = query_password_hash_algorithm
            if query_public_key is not None:
                kwargs["public_key"] = query_public_key
            if query_scope is not None:
                kwargs["scope"] = query_scope
            if query_ssl_ca_certificate is not None:
                kwargs["ssl_ca_certificate"] = query_ssl_ca_certificate

            if authentication_methods is not None:
                changes["authentication_methods"] = authentication_methods
            if comment is not None:
                changes["comment"] = comment
            if ldap_fastbind is not None:
                changes["ldap_fastbind"] = ldap_fastbind
            if locked is not None:
                changes["locked"] = locked
            if name is not None:
                changes["name"] = name
            if password is not None:
                changes["password"] = password
            if password_hash_algorithm is not None:
                changes["password_hash_algorithm"] = password_hash_algorithm
            if public_key is not None:
                changes["public_key"] = public_key
            if scope is not None:
                changes["scope"] = scope
            if ssl_ca_certificate is not None:
                changes["ssl_ca_certificate"] = ssl_ca_certificate

            if hasattr(ClusterAccount, "find"):
                resource = ClusterAccount.find(
                    **kwargs
                )
            else:
                resource = ClusterAccount()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify ClusterAccount: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a user or group account."""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="cluster account delete")
        async def cluster_account_delete(
        ) -> None:
            """Delete an instance of a ClusterAccount resource

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

            if hasattr(ClusterAccount, "find"):
                resource = ClusterAccount.find(
                    **kwargs
                )
            else:
                resource = ClusterAccount()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete ClusterAccount: %s" % err)


