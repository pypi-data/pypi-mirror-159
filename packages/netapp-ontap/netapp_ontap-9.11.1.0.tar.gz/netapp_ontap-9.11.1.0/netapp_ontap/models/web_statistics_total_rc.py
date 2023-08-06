r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["WebStatisticsTotalRc", "WebStatisticsTotalRcSchema"]
__pdoc__ = {
    "WebStatisticsTotalRcSchema.resource": False,
    "WebStatisticsTotalRcSchema.opts": False,
    "WebStatisticsTotalRc": False,
}


class WebStatisticsTotalRcSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatisticsTotalRc object"""

    range_1xx = Size(data_key="range_1xx")
    r""" Indicates the total number of requests that produced HTTP return codes in the range of 100 to 199. These are described as 'informational' results.

Example: 0 """

    range_2xx = Size(data_key="range_2xx")
    r""" Indicates the total number of requests that produced HTTP return codes in the range of 200 to 299. These are described as 'successful' results.

Example: 4 """

    range_3xx = Size(data_key="range_3xx")
    r""" Indicates the total number of requests that produced HTTP return codes in the range of 300 to 399. These are described as 'redirection' results.

Example: 0 """

    range_4xx = Size(data_key="range_4xx")
    r""" Indicates the total number of requests that produced HTTP return codes in the range of 400 to 499. These are described as 'client' error results, indicating a miscommunication initiated by the web services client program, usually a browser.

Example: 3 """

    range_5xx = Size(data_key="range_5xx")
    r""" Indicates the total number of requests that produced HTTP return codes in the range of 500 to 599. These are described as 'server' error results, indicating an internal system failure.

Example: 0 """

    @property
    def resource(self):
        return WebStatisticsTotalRc

    gettable_fields = [
        "range_1xx",
        "range_2xx",
        "range_3xx",
        "range_4xx",
        "range_5xx",
    ]
    """range_1xx,range_2xx,range_3xx,range_4xx,range_5xx,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class WebStatisticsTotalRc(Resource):

    _schema = WebStatisticsTotalRcSchema
