r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["HttpProxy", "HttpProxySchema"]
__pdoc__ = {
    "HttpProxySchema.resource": False,
    "HttpProxySchema.opts": False,
    "HttpProxy": False,
}


class HttpProxySchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the HttpProxy object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the http_proxy. """

    control_enabled = fields.Boolean(data_key="control_enabled")
    r""" Set to true to enable HTTP proxy for control traffic. """

    data_enabled = fields.Boolean(data_key="data_enabled")
    r""" Set to true to enable HTTP proxy for data traffic. """

    port = Size(data_key="port")
    r""" Port number of the HTTP Proxy. """

    server = fields.Str(data_key="server")
    r""" Fully qualified domain name or IP address of the HTTP Proxy. """

    @property
    def resource(self):
        return HttpProxy

    gettable_fields = [
        "links",
        "control_enabled",
        "data_enabled",
        "port",
        "server",
    ]
    """links,control_enabled,data_enabled,port,server,"""

    patchable_fields = [
        "control_enabled",
        "data_enabled",
        "port",
        "server",
    ]
    """control_enabled,data_enabled,port,server,"""

    postable_fields = [
        "control_enabled",
        "data_enabled",
        "port",
        "server",
    ]
    """control_enabled,data_enabled,port,server,"""


class HttpProxy(Resource):

    _schema = HttpProxySchema
