r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsEventActionPossibleActions", "EmsEventActionPossibleActionsSchema"]
__pdoc__ = {
    "EmsEventActionPossibleActionsSchema.resource": False,
    "EmsEventActionPossibleActionsSchema.opts": False,
    "EmsEventActionPossibleActions": False,
}


class EmsEventActionPossibleActionsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsEventActionPossibleActions object"""

    action = fields.Str(data_key="action")
    r""" Name of the action.

Example: scheduled """

    invoke = fields.Nested("netapp_ontap.models.ems_alert_action_possible_actions_invoke.EmsAlertActionPossibleActionsInvokeSchema", unknown=EXCLUDE, data_key="invoke")
    r""" The invoke field of the ems_event_action_possible_actions. """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_alert_response_records_action_possible_actions_parameters.EmsAlertResponseRecordsActionPossibleActionsParametersSchema", unknown=EXCLUDE), data_key="parameters")
    r""" Parameter list for the action. """

    @property
    def resource(self):
        return EmsEventActionPossibleActions

    gettable_fields = [
        "action",
        "invoke",
        "parameters",
    ]
    """action,invoke,parameters,"""

    patchable_fields = [
        "invoke",
    ]
    """invoke,"""

    postable_fields = [
        "invoke",
    ]
    """invoke,"""


class EmsEventActionPossibleActions(Resource):

    _schema = EmsEventActionPossibleActionsSchema
