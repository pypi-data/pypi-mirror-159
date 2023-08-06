r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["WebStatisticsResponseRecords", "WebStatisticsResponseRecordsSchema"]
__pdoc__ = {
    "WebStatisticsResponseRecordsSchema.resource": False,
    "WebStatisticsResponseRecordsSchema.opts": False,
    "WebStatisticsResponseRecords": False,
}


class WebStatisticsResponseRecordsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatisticsResponseRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the web_statistics_response_records. """

    concurrency = fields.Nested("netapp_ontap.models.web_statistics_concurrency.WebStatisticsConcurrencySchema", unknown=EXCLUDE, data_key="concurrency")
    r""" The concurrency field of the web_statistics_response_records. """

    connection_wait_period = fields.Nested("netapp_ontap.models.web_statistics_connection_wait_period.WebStatisticsConnectionWaitPeriodSchema", unknown=EXCLUDE, data_key="connection_wait_period")
    r""" The connection_wait_period field of the web_statistics_response_records. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the web_statistics_response_records. """

    state = fields.Str(data_key="state")
    r""" Describes the operational state of node-level web services. This parameter does not reflect whether protocols are externally visible, but whether the server processes are running correctly.

Valid choices:

* offline
* partial
* mixed
* online
* unclustered """

    status_code = Size(data_key="status_code")
    r""" Indicates the HTTP protocol return code received from the web server when the state is retrieved.

Example: 200 """

    total_bytes = Size(data_key="total_bytes")
    r""" Indicates the total number of bytes returned by the web server.

Example: 2129 """

    total_connections = Size(data_key="total_connections")
    r""" Indicates the number of connections that have been accepted by the web server. This is persistent across restarts.

Example: 7 """

    total_csrf_token = Size(data_key="total_csrf_token")
    r""" Indicates how many CSRF tokens currently exist.

Example: 0 """

    total_delayed_connections = Size(data_key="total_delayed_connections")
    r""" Indicates the number of connections that have been held in the wait queue. This is persistent across restarts.

Example: 0 """

    total_hits = Size(data_key="total_hits")
    r""" Indicates the total number of requests serviced by the web server.

Example: 4 """

    total_http_ops = Size(data_key="total_http_ops")
    r""" Indicates the total number of requests that were serviced over a traditional HTTP protocol.

Example: 4 """

    total_https_ops = Size(data_key="total_https_ops")
    r""" Indicates the total number of requests that were serviced over an encrypted HTTP (HTTPS) protocol.

Example: 3 """

    total_pending_authentication = Size(data_key="total_pending_authentication")
    r""" Indicates the total number of requests that are currently waiting on authentication.

Example: 0 """

    total_rc = fields.Nested("netapp_ontap.models.web_statistics_total_rc.WebStatisticsTotalRcSchema", unknown=EXCLUDE, data_key="total_rc")
    r""" The total_rc field of the web_statistics_response_records. """

    workers = fields.Nested("netapp_ontap.models.web_statistics_workers.WebStatisticsWorkersSchema", unknown=EXCLUDE, data_key="workers")
    r""" The workers field of the web_statistics_response_records. """

    @property
    def resource(self):
        return WebStatisticsResponseRecords

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


class WebStatisticsResponseRecords(Resource):

    _schema = WebStatisticsResponseRecordsSchema
