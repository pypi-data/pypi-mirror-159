r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["WebStatisticsWorkers", "WebStatisticsWorkersSchema"]
__pdoc__ = {
    "WebStatisticsWorkersSchema.resource": False,
    "WebStatisticsWorkersSchema.opts": False,
    "WebStatisticsWorkers": False,
}


class WebStatisticsWorkersSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatisticsWorkers object"""

    available = Size(data_key="available")
    r""" Indicates the total number of running worker threads available for request processing.

Example: 95 """

    busy = Size(data_key="busy")
    r""" Indicates the total number of running worker threads actively processing requests.

Example: 1 """

    closing = Size(data_key="closing")
    r""" Indicates the total number of worker threads closing their connections.

Example: 0 """

    keep_alive = Size(data_key="keep_alive")
    r""" Indicates the total number of worker threads servicing session keep-alive requests.

Example: 0 """

    logging = Size(data_key="logging")
    r""" Indicates the total number of worker threads logging their results.

Example: 0 """

    reading = Size(data_key="reading")
    r""" Indicates the total number of worker threads reading data from the input stream.

Example: 0 """

    ready = Size(data_key="ready")
    r""" Indicates the total number of worker threads waiting for requests.

Example: 95 """

    total = Size(data_key="total")
    r""" Indicates the maximum number of worker threads that can be started in the server to service requests.

Example: 96 """

    writing = Size(data_key="writing")
    r""" Indicates the total number of worker threads writing data to the output stream.

Example: 1 """

    @property
    def resource(self):
        return WebStatisticsWorkers

    gettable_fields = [
        "available",
        "busy",
        "closing",
        "keep_alive",
        "logging",
        "reading",
        "ready",
        "total",
        "writing",
    ]
    """available,busy,closing,keep_alive,logging,reading,ready,total,writing,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class WebStatisticsWorkers(Resource):

    _schema = WebStatisticsWorkersSchema
