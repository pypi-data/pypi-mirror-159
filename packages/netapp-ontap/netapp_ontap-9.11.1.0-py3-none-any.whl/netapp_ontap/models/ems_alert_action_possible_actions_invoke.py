r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsAlertActionPossibleActionsInvoke", "EmsAlertActionPossibleActionsInvokeSchema"]
__pdoc__ = {
    "EmsAlertActionPossibleActionsInvokeSchema.resource": False,
    "EmsAlertActionPossibleActionsInvokeSchema.opts": False,
    "EmsAlertActionPossibleActionsInvoke": False,
}


class EmsAlertActionPossibleActionsInvokeSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsAlertActionPossibleActionsInvoke object"""

    links = fields.Nested("netapp_ontap.models.href.HrefSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the ems_alert_action_possible_actions_invoke. """

    verb = fields.Str(data_key="verb")
    r""" The verb field of the ems_alert_action_possible_actions_invoke.

Valid choices:

* patch
* post
* delete """

    @property
    def resource(self):
        return EmsAlertActionPossibleActionsInvoke

    gettable_fields = [
        "links",
        "verb",
    ]
    """links,verb,"""

    patchable_fields = [
        "verb",
    ]
    """verb,"""

    postable_fields = [
        "verb",
    ]
    """verb,"""


class EmsAlertActionPossibleActionsInvoke(Resource):

    _schema = EmsAlertActionPossibleActionsInvokeSchema
