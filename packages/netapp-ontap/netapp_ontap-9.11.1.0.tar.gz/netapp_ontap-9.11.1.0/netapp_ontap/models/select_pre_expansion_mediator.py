r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["SelectPreExpansionMediator", "SelectPreExpansionMediatorSchema"]
__pdoc__ = {
    "SelectPreExpansionMediatorSchema.resource": False,
    "SelectPreExpansionMediatorSchema.opts": False,
    "SelectPreExpansionMediator": False,
}


class SelectPreExpansionMediatorSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the SelectPreExpansionMediator object"""

    ip = fields.Str(data_key="ip")
    r""" IP of the external mediator.

Example: 10.1.3.13 """

    target = fields.Str(data_key="target")
    r""" Mediator target name.

Example: iqn.2012-05.local:mailbox.target.tgtname """

    @property
    def resource(self):
        return SelectPreExpansionMediator

    gettable_fields = [
        "ip",
        "target",
    ]
    """ip,target,"""

    patchable_fields = [
        "ip",
        "target",
    ]
    """ip,target,"""

    postable_fields = [
        "ip",
        "target",
    ]
    """ip,target,"""


class SelectPreExpansionMediator(Resource):

    _schema = SelectPreExpansionMediatorSchema
