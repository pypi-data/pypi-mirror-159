r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["WebStatisticsConnectionWaitPeriod", "WebStatisticsConnectionWaitPeriodSchema"]
__pdoc__ = {
    "WebStatisticsConnectionWaitPeriodSchema.resource": False,
    "WebStatisticsConnectionWaitPeriodSchema.opts": False,
    "WebStatisticsConnectionWaitPeriod": False,
}


class WebStatisticsConnectionWaitPeriodSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatisticsConnectionWaitPeriod object"""

    mean = Size(data_key="mean")
    r""" Indicates the mean delay incurred by delayed connections, in milliseconds. This is persistent across restarts.

Example: 0 """

    peak = Size(data_key="peak")
    r""" Indicates the maximum delay incurred by any delayed connection, in milliseconds. This is persistent across restarts.

Example: 0 """

    total = Size(data_key="total")
    r""" Indicates the sum of the delays incurred by all delayed connections, in milliseconds. This is persistent across restarts.

Example: 0 """

    @property
    def resource(self):
        return WebStatisticsConnectionWaitPeriod

    gettable_fields = [
        "mean",
        "peak",
        "total",
    ]
    """mean,peak,total,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class WebStatisticsConnectionWaitPeriod(Resource):

    _schema = WebStatisticsConnectionWaitPeriodSchema
