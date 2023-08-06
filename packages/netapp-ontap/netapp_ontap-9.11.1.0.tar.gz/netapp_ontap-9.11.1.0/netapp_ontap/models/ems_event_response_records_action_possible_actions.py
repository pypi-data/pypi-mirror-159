r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsEventResponseRecordsActionPossibleActions", "EmsEventResponseRecordsActionPossibleActionsSchema"]
__pdoc__ = {
    "EmsEventResponseRecordsActionPossibleActionsSchema.resource": False,
    "EmsEventResponseRecordsActionPossibleActionsSchema.opts": False,
    "EmsEventResponseRecordsActionPossibleActions": False,
}


class EmsEventResponseRecordsActionPossibleActionsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsEventResponseRecordsActionPossibleActions object"""

    action = fields.Str(data_key="action")
    r""" Name of the action.

Example: scheduled """

    invoke = fields.Nested("netapp_ontap.models.ems_alert_action_possible_actions_invoke.EmsAlertActionPossibleActionsInvokeSchema", unknown=EXCLUDE, data_key="invoke")
    r""" The invoke field of the ems_event_response_records_action_possible_actions. """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_event_action_possible_actions_parameters.EmsEventActionPossibleActionsParametersSchema", unknown=EXCLUDE), data_key="parameters")
    r""" Parameter list for the action. """

    @property
    def resource(self):
        return EmsEventResponseRecordsActionPossibleActions

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


class EmsEventResponseRecordsActionPossibleActions(Resource):

    _schema = EmsEventResponseRecordsActionPossibleActionsSchema
