r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
This API is used to retrieve ONTAP alerts from the cluster.<p/>
This API supports GET and PATCH requests. The GET request retrieves ONTAP alerts, while the PATCH request updates the acknowledge and suppress fields.
---
## Examples
### Configuring an alerts' acknowledge state
The following example configures the acknowledge and acknowledger state for an alert.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Alert

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = Alert(
        resource="sconqa-corduroyl-03",
        name="SwitchCommunityString_Alert",
        monitor="ethernet_switch",
        **{"node.uuid": "a79d919e-885a-11e9-9c44-005056bbbffe"}
    )
    resource.acknowledge = True
    resource.acknowledger = "dummy_user"
    resource.patch()

```

---
### Retrieving ONTAP alerts from a healthy cluster
The following example retrieves the active ONTAP alerts from the cluster with no outstanding alerts.
Note that if the <i>fields=*</i> parameter is not specified, the fields perceived-severity, probable-cause, possible-effect, alerting-resource-name and tags are not returned.
Filters can be added on the fields to limit the results.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Alert

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Alert.get_collection()))

```
<div class="try_it_out">
<input id="example1_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example1_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example1_result" class="try_it_out_content">
```
[]

```
</div>
</div>

### Retrieving ONTAP alerts from a cluster with active alerts
The following example retrieves the active ONTAP alerts from the cluster with outstanding alerts.
Note that if the <i>fields=*</i> parameter is not specified, the fields perceived-severity, probable-cause, possible-effect, alerting-resource-name and tags are not returned.
Filters can be added on the fields to limit the results.
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import Alert

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(Alert.get_collection()))

```
<div class="try_it_out">
<input id="example2_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example2_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example2_result" class="try_it_out_content">
```
[
    Alert(
        {
            "labels": [
                {"label": "Slot", "value": "0"},
                {"label": "State", "value": "disabled"},
                {"label": "Status", "value": "offline"},
                {"label": "Cable ID", "value": "500a098004b9fb34-500a0980044d167f"},
            ],
            "name": "DisabledInuseSASPort_Alert",
            "acknowledger": "tgf",
            "node": {"uuid": "a79d919e-885a-11e9-9c44-005056bbbffe", "name": "node-05"},
            "cause": {
                "message": "SAS 0b port is disabled. This might occur if the port has been administratively disabled or the attached cable is faulty."
            },
            "possible_effect": {
                "message": "Controller node-05 might lose a path to storage devices connected behind port 0b."
            },
            "suppress": False,
            "corrective_action": {
                "message": "1. Verify that the physical cable connection is secure and operational, and replace the cable, if necessary.\n2. Verify that SAS port 0b is online and enabled.\n3. If the SAS port 0b is connected to disk shelves, verify that IOMs and disks are properly seated."
            },
            "monitor": "node_connect",
            "time": "2019-06-06T11:30:03-04:00",
            "acknowledge": True,
            "tags": ["quality_of_service"],
        }
    ),
    Alert(
        {
            "labels": [
                {"label": "Switch Name", "value": "switch-05"},
                {"label": "Switch Model", "value": "CN1610"},
            ],
            "name": "SwitchCommunityString_Alert",
            "node": {"uuid": "a79d919e-885a-11e9-9c44-005056bbbffe", "name": "node-05"},
            "cause": {
                "message": 'Ethernet switch "switch-05" with IP address "10.235.79.82" is not reachable via SNMP. Incorrect SNMP community string might be configured on the Ethernet switch.'
            },
            "possible_effect": {
                "message": "Ethernet switch communication problems and accessibility issues."
            },
            "suppress": False,
            "corrective_action": {
                "message": 'Check the SNMP community string on the Ethernet switch to verify the expected community string is configured. Use the "system switch ethernet show -snmp-config" command to view the expected community string.'
            },
            "monitor": "ethernet_switch",
            "time": "2019-06-06T11:16:05-04:00",
            "acknowledge": False,
        }
    ),
    Alert(
        {
            "labels": [
                {"label": "Switch Name", "value": "switch-06"},
                {"label": "Switch Model", "value": "CN1610"},
            ],
            "name": "SwitchCommunityString_Alert",
            "node": {"uuid": "a79d919e-885a-11e9-9c44-005056bbbffe", "name": "node-05"},
            "cause": {
                "message": 'Ethernet switch "switch-06" with IP address "10.235.79.83" is not reachable via SNMP. Incorrect SNMP community string might be configured on the Ethernet switch.'
            },
            "possible_effect": {
                "message": "Ethernet switch communication problems and accessibility issues."
            },
            "suppress": False,
            "corrective_action": {
                "message": 'Check the SNMP community string on the Ethernet switch to verify the expected community string is configured. Use the "system switch ethernet show -snmp-config" command to view the expected community string.'
            },
            "monitor": "ethernet_switch",
            "time": "2019-06-06T11:16:05-04:00",
            "acknowledge": False,
        }
    ),
]

```
</div>
</div>

---
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


__all__ = ["Alert", "AlertSchema"]
__pdoc__ = {
    "AlertSchema.resource": False,
    "AlertSchema.opts": False,
    "Alert.alert_show": False,
    "Alert.alert_create": False,
    "Alert.alert_modify": False,
    "Alert.alert_delete": False,
}


class AlertSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the Alert object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the alert. """

    acknowledge = fields.Boolean(
        data_key="acknowledge",
    )
    r""" The acknowledge state of the alert. """

    acknowledger = fields.Str(
        data_key="acknowledger",
    )
    r""" The ID of the acknowledger of the alert. """

    asup_enable = fields.Boolean(
        data_key="asup_enable",
    )
    r""" True indicates that this alert will be included in the next AutoSupport(r) message. """

    cause = fields.Nested("netapp_ontap.models.alert_message.AlertMessageSchema", data_key="cause", unknown=EXCLUDE)
    r""" The cause field of the alert. """

    corrective_action = fields.Nested("netapp_ontap.models.alert_message.AlertMessageSchema", data_key="corrective_action", unknown=EXCLUDE)
    r""" The corrective_action field of the alert. """

    labels = fields.List(fields.Nested("netapp_ontap.models.alert_labels.AlertLabelsSchema", unknown=EXCLUDE), data_key="labels")
    r""" Additional Information. """

    monitor = fields.Str(
        data_key="monitor",
        validate=enum_validation(['chassis', 'cluster_switch', 'controller', 'example', 'ethernet_switch', 'node_connect', 'system', 'system_connect']),
    )
    r""" The monitor raising the alert.

Valid choices:

* chassis
* cluster_switch
* controller
* example
* ethernet_switch
* node_connect
* system
* system_connect """

    name = fields.Str(
        data_key="name",
    )
    r""" The alert ID which is a short name for an alert condition. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the alert. """

    possible_effect = fields.Nested("netapp_ontap.models.alert_message.AlertMessageSchema", data_key="possible_effect", unknown=EXCLUDE)
    r""" The possible_effect field of the alert. """

    resource = fields.Str(
        data_key="resource",
    )
    r""" The display friendly name of the resource. """

    suppress = fields.Boolean(
        data_key="suppress",
    )
    r""" The suppress state of the alert. """

    suppressor = fields.Str(
        data_key="suppressor",
    )
    r""" The ID of the suppressor of the alert. """

    tags = fields.List(fields.Str, data_key="tags")
    r""" The tags field of the alert. """

    time = ImpreciseDateTime(
        data_key="time",
    )
    r""" The time at which the alert condition was detected. """

    @property
    def resource(self):
        return Alert

    gettable_fields = [
        "links",
        "acknowledge",
        "acknowledger",
        "asup_enable",
        "cause",
        "corrective_action",
        "labels",
        "monitor",
        "name",
        "node.links",
        "node.name",
        "node.uuid",
        "possible_effect",
        "resource",
        "suppress",
        "suppressor",
        "tags",
        "time",
    ]
    """links,acknowledge,acknowledger,asup_enable,cause,corrective_action,labels,monitor,name,node.links,node.name,node.uuid,possible_effect,resource,suppress,suppressor,tags,time,"""

    patchable_fields = [
        "acknowledge",
        "acknowledger",
        "asup_enable",
        "cause",
        "corrective_action",
        "node.name",
        "node.uuid",
        "possible_effect",
        "suppress",
        "suppressor",
    ]
    """acknowledge,acknowledger,asup_enable,cause,corrective_action,node.name,node.uuid,possible_effect,suppress,suppressor,"""

    postable_fields = [
        "cause",
        "corrective_action",
        "node.name",
        "node.uuid",
        "possible_effect",
    ]
    """cause,corrective_action,node.name,node.uuid,possible_effect,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in Alert.get_collection(fields=field)]
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
            raise NetAppRestError("Alert modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class Alert(Resource):
    r""" Alert REST API """

    _schema = AlertSchema
    _path = "/api/private/support/alerts"
    _keys = ["node.uuid", "monitor", "name", "resource"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the active ONTAP alerts from all subsystems in the cluster.
### Related ONTAP commands
* `system health alert show`
### Learn more
* [`DOC /private/support/alerts`](#docs-support-private_support_alerts)
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="alert show")
        def alert_show(
            fields: List[Choices.define(["acknowledge", "acknowledger", "asup_enable", "monitor", "name", "resource", "suppress", "suppressor", "tags", "time", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of Alert resources

            Args:
                acknowledge: The acknowledge state of the alert.
                acknowledger: The ID of the acknowledger of the alert.
                asup_enable: True indicates that this alert will be included in the next AutoSupport(r) message.
                monitor: The monitor raising the alert.
                name: The alert ID which is a short name for an alert condition.
                resource: The display friendly name of the resource.
                suppress: The suppress state of the alert.
                suppressor: The ID of the suppressor of the alert.
                tags: 
                time: The time at which the alert condition was detected.
            """

            kwargs = {}
            if acknowledge is not None:
                kwargs["acknowledge"] = acknowledge
            if acknowledger is not None:
                kwargs["acknowledger"] = acknowledger
            if asup_enable is not None:
                kwargs["asup_enable"] = asup_enable
            if monitor is not None:
                kwargs["monitor"] = monitor
            if name is not None:
                kwargs["name"] = name
            if resource is not None:
                kwargs["resource"] = resource
            if suppress is not None:
                kwargs["suppress"] = suppress
            if suppressor is not None:
                kwargs["suppressor"] = suppressor
            if tags is not None:
                kwargs["tags"] = tags
            if time is not None:
                kwargs["time"] = time
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return Alert.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all Alert resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["Alert"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates the acknowledge and suppress fields for an alert.
### Related ONTAP commands
* `system health alert modify`
### Learn more
* [`DOC /private/support/alerts`](#docs-support-private_support_alerts)
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)



    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the active ONTAP alerts from all subsystems in the cluster.
### Related ONTAP commands
* `system health alert show`
### Learn more
* [`DOC /private/support/alerts`](#docs-support-private_support_alerts)
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)

    def get(self, **kwargs) -> NetAppResponse:
        r"""Retrieves information for the alert.

### Learn more
* [`DOC /private/support/alerts`](#docs-support-private_support_alerts)"""
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
        r"""Updates the acknowledge and suppress fields for an alert.
### Related ONTAP commands
* `system health alert modify`
### Learn more
* [`DOC /private/support/alerts`](#docs-support-private_support_alerts)
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="alert modify")
        async def alert_modify(
        ) -> ResourceTable:
            """Modify an instance of a Alert resource

            Args:
                acknowledge: The acknowledge state of the alert.
                query_acknowledge: The acknowledge state of the alert.
                acknowledger: The ID of the acknowledger of the alert.
                query_acknowledger: The ID of the acknowledger of the alert.
                asup_enable: True indicates that this alert will be included in the next AutoSupport(r) message.
                query_asup_enable: True indicates that this alert will be included in the next AutoSupport(r) message.
                monitor: The monitor raising the alert.
                query_monitor: The monitor raising the alert.
                name: The alert ID which is a short name for an alert condition.
                query_name: The alert ID which is a short name for an alert condition.
                resource: The display friendly name of the resource.
                query_resource: The display friendly name of the resource.
                suppress: The suppress state of the alert.
                query_suppress: The suppress state of the alert.
                suppressor: The ID of the suppressor of the alert.
                query_suppressor: The ID of the suppressor of the alert.
                tags: 
                query_tags: 
                time: The time at which the alert condition was detected.
                query_time: The time at which the alert condition was detected.
            """

            kwargs = {}
            changes = {}
            if query_acknowledge is not None:
                kwargs["acknowledge"] = query_acknowledge
            if query_acknowledger is not None:
                kwargs["acknowledger"] = query_acknowledger
            if query_asup_enable is not None:
                kwargs["asup_enable"] = query_asup_enable
            if query_monitor is not None:
                kwargs["monitor"] = query_monitor
            if query_name is not None:
                kwargs["name"] = query_name
            if query_resource is not None:
                kwargs["resource"] = query_resource
            if query_suppress is not None:
                kwargs["suppress"] = query_suppress
            if query_suppressor is not None:
                kwargs["suppressor"] = query_suppressor
            if query_tags is not None:
                kwargs["tags"] = query_tags
            if query_time is not None:
                kwargs["time"] = query_time

            if acknowledge is not None:
                changes["acknowledge"] = acknowledge
            if acknowledger is not None:
                changes["acknowledger"] = acknowledger
            if asup_enable is not None:
                changes["asup_enable"] = asup_enable
            if monitor is not None:
                changes["monitor"] = monitor
            if name is not None:
                changes["name"] = name
            if resource is not None:
                changes["resource"] = resource
            if suppress is not None:
                changes["suppress"] = suppress
            if suppressor is not None:
                changes["suppressor"] = suppressor
            if tags is not None:
                changes["tags"] = tags
            if time is not None:
                changes["time"] = time

            if hasattr(Alert, "find"):
                resource = Alert.find(
                    **kwargs
                )
            else:
                resource = Alert()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify Alert: %s" % err)



