r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.

## Overview
You can use this API to retrieve the current configuration for a collection of nodes.
The following operations are supported:

  * Collection Get: GET /cluster/web/statistics
## Examples
### Retrieving the current configuration for a collection of nodes
The following example shows the list of web configuration for a collection of nodes.
"br/":
---
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import WebStatistics

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    print(list(WebStatistics.get_collection()))

```
<div class="try_it_out">
<input id="example0_try_it_out" type="checkbox", class="try_it_out_check">
<label for="example0_try_it_out" class="try_it_out_button">Try it out</label>
<div id="example0_result" class="try_it_out_content">
```
[
    WebStatistics(
        {
            "total_http_ops": 4,
            "total_connections": 100,
            "connection_wait_period": {"mean": 2, "peak": 5, "total": 4},
            "status_code": 200,
            "node": {
                "_links": {
                    "self": {
                        "href": "/api/cluster/nodes/13bb2092-458b-11e9-9c06-0050568ea64e"
                    }
                },
                "uuid": "13bb2092-458b-11e9-9c06-0050568ea64e",
                "name": "node1",
            },
            "total_bytes": 2129,
            "state": "online",
            "total_csrf_token": 0,
            "total_delayed_connections": 2,
            "concurrency": {"peak_per_address": 1, "peak": 1},
            "total_hits": 4,
            "workers": {
                "reading": 0,
                "keep_alive": 0,
                "writing": 1,
                "logging": 0,
                "available": 95,
                "total": 96,
                "busy": 1,
                "ready": 95,
                "closing": 0,
            },
            "total_rc": {
                "range_3xx": 0,
                "range_1xx": 0,
                "range_4xx": 3,
                "range_5xx": 0,
                "range_2xx": 4,
            },
            "_links": {
                "self": {
                    "href": "/api/cluster/web/statistics/13bb2092-458b-11e9-9c06-0050568ea64e"
                }
            },
            "total_https_ops": 3,
            "total_pending_authentication": 0,
        }
    )
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


__all__ = ["WebStatistics", "WebStatisticsSchema"]
__pdoc__ = {
    "WebStatisticsSchema.resource": False,
    "WebStatisticsSchema.opts": False,
    "WebStatistics.web_statistics_show": False,
    "WebStatistics.web_statistics_create": False,
    "WebStatistics.web_statistics_modify": False,
    "WebStatistics.web_statistics_delete": False,
}


class WebStatisticsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatistics object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the web_statistics. """

    concurrency = fields.Nested("netapp_ontap.models.web_statistics_concurrency.WebStatisticsConcurrencySchema", data_key="concurrency", unknown=EXCLUDE)
    r""" The concurrency field of the web_statistics. """

    connection_wait_period = fields.Nested("netapp_ontap.models.web_statistics_connection_wait_period.WebStatisticsConnectionWaitPeriodSchema", data_key="connection_wait_period", unknown=EXCLUDE)
    r""" The connection_wait_period field of the web_statistics. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", data_key="node", unknown=EXCLUDE)
    r""" The node field of the web_statistics. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['offline', 'partial', 'mixed', 'online', 'unclustered']),
    )
    r""" Describes the operational state of node-level web services. This parameter does not reflect whether protocols are externally visible, but whether the server processes are running correctly.

Valid choices:

* offline
* partial
* mixed
* online
* unclustered """

    status_code = Size(
        data_key="status_code",
    )
    r""" Indicates the HTTP protocol return code received from the web server when the state is retrieved.

Example: 200 """

    total_bytes = Size(
        data_key="total_bytes",
    )
    r""" Indicates the total number of bytes returned by the web server.

Example: 2129 """

    total_connections = Size(
        data_key="total_connections",
    )
    r""" Indicates the number of connections that have been accepted by the web server. This is persistent across restarts.

Example: 7 """

    total_csrf_token = Size(
        data_key="total_csrf_token",
    )
    r""" Indicates how many CSRF tokens currently exist.

Example: 0 """

    total_delayed_connections = Size(
        data_key="total_delayed_connections",
    )
    r""" Indicates the number of connections that have been held in the wait queue. This is persistent across restarts.

Example: 0 """

    total_hits = Size(
        data_key="total_hits",
    )
    r""" Indicates the total number of requests serviced by the web server.

Example: 4 """

    total_http_ops = Size(
        data_key="total_http_ops",
    )
    r""" Indicates the total number of requests that were serviced over a traditional HTTP protocol.

Example: 4 """

    total_https_ops = Size(
        data_key="total_https_ops",
    )
    r""" Indicates the total number of requests that were serviced over an encrypted HTTP (HTTPS) protocol.

Example: 3 """

    total_pending_authentication = Size(
        data_key="total_pending_authentication",
    )
    r""" Indicates the total number of requests that are currently waiting on authentication.

Example: 0 """

    total_rc = fields.Nested("netapp_ontap.models.web_statistics_total_rc.WebStatisticsTotalRcSchema", data_key="total_rc", unknown=EXCLUDE)
    r""" The total_rc field of the web_statistics. """

    workers = fields.Nested("netapp_ontap.models.web_statistics_workers.WebStatisticsWorkersSchema", data_key="workers", unknown=EXCLUDE)
    r""" The workers field of the web_statistics. """

    @property
    def resource(self):
        return WebStatistics

    gettable_fields = [
        "links",
        "concurrency",
        "connection_wait_period",
        "node.links",
        "node.name",
        "node.uuid",
        "state",
        "status_code",
        "total_bytes",
        "total_connections",
        "total_csrf_token",
        "total_delayed_connections",
        "total_hits",
        "total_http_ops",
        "total_https_ops",
        "total_pending_authentication",
        "total_rc",
        "workers",
    ]
    """links,concurrency,connection_wait_period,node.links,node.name,node.uuid,state,status_code,total_bytes,total_connections,total_csrf_token,total_delayed_connections,total_hits,total_http_ops,total_https_ops,total_pending_authentication,total_rc,workers,"""

    patchable_fields = [
        "concurrency",
        "connection_wait_period",
        "node.name",
        "node.uuid",
        "total_rc",
        "workers",
    ]
    """concurrency,connection_wait_period,node.name,node.uuid,total_rc,workers,"""

    postable_fields = [
        "concurrency",
        "connection_wait_period",
        "node.name",
        "node.uuid",
        "total_rc",
        "workers",
    ]
    """concurrency,connection_wait_period,node.name,node.uuid,total_rc,workers,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in WebStatistics.get_collection(fields=field)]
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
            raise NetAppRestError("WebStatistics modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class WebStatistics(Resource):
    """Allows interaction with WebStatistics objects on the host"""

    _schema = WebStatisticsSchema
    _path = "/api/cluster/web/statistics"

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves the web services configuration for a collection of nodes.
### Learn more
* [`DOC /cluster/web/statistics`](#docs-cluster-cluster_web_statistics)"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="web statistics show")
        def web_statistics_show(
            fields: List[Choices.define(["state", "status_code", "total_bytes", "total_connections", "total_csrf_token", "total_delayed_connections", "total_hits", "total_http_ops", "total_https_ops", "total_pending_authentication", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of WebStatistics resources

            Args:
                state: Describes the operational state of node-level web services. This parameter does not reflect whether protocols are externally visible, but whether the server processes are running correctly.
                status_code: Indicates the HTTP protocol return code received from the web server when the state is retrieved.
                total_bytes: Indicates the total number of bytes returned by the web server.
                total_connections: Indicates the number of connections that have been accepted by the web server. This is persistent across restarts.
                total_csrf_token: Indicates how many CSRF tokens currently exist.
                total_delayed_connections: Indicates the number of connections that have been held in the wait queue. This is persistent across restarts.
                total_hits: Indicates the total number of requests serviced by the web server.
                total_http_ops: Indicates the total number of requests that were serviced over a traditional HTTP protocol.
                total_https_ops: Indicates the total number of requests that were serviced over an encrypted HTTP (HTTPS) protocol.
                total_pending_authentication: Indicates the total number of requests that are currently waiting on authentication.
            """

            kwargs = {}
            if state is not None:
                kwargs["state"] = state
            if status_code is not None:
                kwargs["status_code"] = status_code
            if total_bytes is not None:
                kwargs["total_bytes"] = total_bytes
            if total_connections is not None:
                kwargs["total_connections"] = total_connections
            if total_csrf_token is not None:
                kwargs["total_csrf_token"] = total_csrf_token
            if total_delayed_connections is not None:
                kwargs["total_delayed_connections"] = total_delayed_connections
            if total_hits is not None:
                kwargs["total_hits"] = total_hits
            if total_http_ops is not None:
                kwargs["total_http_ops"] = total_http_ops
            if total_https_ops is not None:
                kwargs["total_https_ops"] = total_https_ops
            if total_pending_authentication is not None:
                kwargs["total_pending_authentication"] = total_pending_authentication
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return WebStatistics.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all WebStatistics resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves the web services configuration for a collection of nodes.
### Learn more
* [`DOC /cluster/web/statistics`](#docs-cluster-cluster_web_statistics)"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






