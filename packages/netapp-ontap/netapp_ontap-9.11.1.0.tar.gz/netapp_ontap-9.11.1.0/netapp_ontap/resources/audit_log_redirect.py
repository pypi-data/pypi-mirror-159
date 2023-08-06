r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
Use this API to specify a dedicated SVM for all NAS auditing events log to reside in.
## Examples
---
### Creating an audit log redirect configuration
To create an audit log redirect configuration:
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import AuditLogRedirect

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = AuditLogRedirect()
    resource.svm = {"uuid": "02c9e252-41be-11e9-81d5-00a0986138f7"}
    resource.post(hydrate=True, return_timeout=5, return_records=False)
    print(resource)

```

---
### Retrieving an audit log redirect configuration in the cluster
To retrieve an audit log redirect configuration in the cluster:
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import AuditLogRedirect

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = AuditLogRedirect()
    resource.get()
    print(resource)

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
AuditLogRedirect(
    {"svm": {"uuid": "24870c49-8a73-11ea-ad05-005056827898", "name": "vs2"}}
)

```
</div>
</div>

---
### Updating an audit log redirect configuration in the cluster
To update an existing audit log redirect configuration:
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import AuditLogRedirect

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = AuditLogRedirect()
    resource.svm = {"name": "svm1", "uuid": "02c9e252-41be-11e9-81d5-00a0986138f7"}
    resource.patch()

```

---
### Deleting an audit log redirect configuration in the cluster
To delete an existing audit log redirect configuration:
<br/>
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import AuditLogRedirect

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = AuditLogRedirect()
    resource.delete()

```

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


__all__ = ["AuditLogRedirect", "AuditLogRedirectSchema"]
__pdoc__ = {
    "AuditLogRedirectSchema.resource": False,
    "AuditLogRedirectSchema.opts": False,
    "AuditLogRedirect.audit_log_redirect_show": False,
    "AuditLogRedirect.audit_log_redirect_create": False,
    "AuditLogRedirect.audit_log_redirect_modify": False,
    "AuditLogRedirect.audit_log_redirect_delete": False,
}


class AuditLogRedirectSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AuditLogRedirect object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the audit_log_redirect. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the audit_log_redirect. """

    @property
    def resource(self):
        return AuditLogRedirect

    gettable_fields = [
        "links",
        "svm.links",
        "svm.name",
        "svm.uuid",
    ]
    """links,svm.links,svm.name,svm.uuid,"""

    patchable_fields = [
        "svm.name",
        "svm.uuid",
    ]
    """svm.name,svm.uuid,"""

    postable_fields = [
        "svm.name",
        "svm.uuid",
    ]
    """svm.name,svm.uuid,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in AuditLogRedirect.get_collection(fields=field)]
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
            raise NetAppRestError("AuditLogRedirect modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class AuditLogRedirect(Resource):
    """Allows interaction with AuditLogRedirect objects on the host"""

    _schema = AuditLogRedirectSchema
    _path = "/api/private/protocols/audit/audit-log-redirect"







    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves an audit log redirect configuration.
### Related ONTAP commands
* `vserver audit audit-log-redirect show`
### Learn more
* [`DOC /private/protocols/audit/audit-log-redirect`](#docs-NAS-private_protocols_audit_audit-log-redirect)
"""
        return super()._get(**kwargs)

    get.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="audit log redirect show")
        def audit_log_redirect_show(
            fields: List[str] = None,
        ) -> ResourceTable:
            """Fetch a single AuditLogRedirect resource

            Args:
            """

            kwargs = {}
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            resource = AuditLogRedirect(
                **kwargs
            )
            resource.get()
            return [resource]

    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Create an audit log redirect configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM to which NAS audit events logs are redirected to.
### Related ONTAP commands
* `vserver audit audit-log-redirect create`
### Learn more
* [`DOC /private/protocols/audit/audit-log-redirect`](#docs-NAS-private_protocols_audit_audit-log-redirect)
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="audit log redirect create")
        async def audit_log_redirect_create(
        ) -> ResourceTable:
            """Create an instance of a AuditLogRedirect resource

            Args:
                links: 
                svm: 
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if svm is not None:
                kwargs["svm"] = svm

            resource = AuditLogRedirect(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create AuditLogRedirect: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates an audit log redirect configuration.
### Required properties
* `svm.uuid` or `svm.name` - Existing SVM to which NAS audit events logs are redirected to.
### Related ONTAP commands
* `vserver audit audit-log-redirect modify`
### Learn more
* [`DOC /private/protocols/audit/audit-log-redirect`](#docs-NAS-private_protocols_audit_audit-log-redirect)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="audit log redirect modify")
        async def audit_log_redirect_modify(
        ) -> ResourceTable:
            """Modify an instance of a AuditLogRedirect resource

            Args:
            """

            kwargs = {}
            changes = {}


            if hasattr(AuditLogRedirect, "find"):
                resource = AuditLogRedirect.find(
                    **kwargs
                )
            else:
                resource = AuditLogRedirect()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify AuditLogRedirect: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes an audit log redirect configuration.
### Related ONTAP commands
* `vserver audit audit-log-redirect delete`
### Learn more
* [`DOC /private/protocols/audit/audit-log-redirect`](#docs-NAS-private_protocols_audit_audit-log-redirect)
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="audit log redirect delete")
        async def audit_log_redirect_delete(
        ) -> None:
            """Delete an instance of a AuditLogRedirect resource

            Args:
            """

            kwargs = {}

            if hasattr(AuditLogRedirect, "find"):
                resource = AuditLogRedirect.find(
                    **kwargs
                )
            else:
                resource = AuditLogRedirect()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete AuditLogRedirect: %s" % err)


