r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["AccessTokenInfo", "AccessTokenInfoSchema"]
__pdoc__ = {
    "AccessTokenInfoSchema.resource": False,
    "AccessTokenInfoSchema.opts": False,
    "AccessTokenInfo": False,
}


class AccessTokenInfoSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AccessTokenInfo object"""

    access_token = fields.Str(data_key="access_token")
    r""" Access token that is used by the ISV application to access the protected APIs.

Example: eyJzdGF0dXNSZXNwIjp7InNlcmlhbC1udW1iZXIiOiI0NTEwMDAwMTAi.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk """

    expires_in = Size(data_key="expires_in")
    r""" Number of seconds after which an access token expires.

Example: 1036800 """

    token_type = fields.Str(data_key="token_type")
    r""" Access token type.

Valid choices:

* bearer """

    @property
    def resource(self):
        return AccessTokenInfo

    gettable_fields = [
        "access_token",
        "expires_in",
        "token_type",
    ]
    """access_token,expires_in,token_type,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class AccessTokenInfo(Resource):

    _schema = AccessTokenInfoSchema
