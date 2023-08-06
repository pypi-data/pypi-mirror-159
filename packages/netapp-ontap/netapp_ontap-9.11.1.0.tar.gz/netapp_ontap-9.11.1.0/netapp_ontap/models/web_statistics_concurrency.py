r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["WebStatisticsConcurrency", "WebStatisticsConcurrencySchema"]
__pdoc__ = {
    "WebStatisticsConcurrencySchema.resource": False,
    "WebStatisticsConcurrencySchema.opts": False,
    "WebStatisticsConcurrency": False,
}


class WebStatisticsConcurrencySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the WebStatisticsConcurrency object"""

    peak = Size(data_key="peak")
    r""" Indicates the peak number of concurrent connections that the server has accepted including both delayed and active connections. This is persistent across restarts.

Example: 1 """

    peak_per_address = Size(data_key="peak_per_address")
    r""" Indicates the peak number of concurrent connections from a single remote address including both delayed and active connections. This is persistent across restarts.

Example: 1 """

    @property
    def resource(self):
        return WebStatisticsConcurrency

    gettable_fields = [
        "peak",
        "peak_per_address",
    ]
    """peak,peak_per_address,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class WebStatisticsConcurrency(Resource):

    _schema = WebStatisticsConcurrencySchema
