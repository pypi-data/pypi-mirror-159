r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsAlertAction", "EmsAlertActionSchema"]
__pdoc__ = {
    "EmsAlertActionSchema.resource": False,
    "EmsAlertActionSchema.opts": False,
    "EmsAlertAction": False,
}


class EmsAlertActionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsAlertAction object"""

    possible_actions = fields.List(fields.Nested("netapp_ontap.models.ems_alert_possible_actions.EmsAlertPossibleActionsSchema", unknown=EXCLUDE), data_key="possible_actions")
    r""" A list of possible actions along with the parameter names and types that can be used with the opaque URL. """

    @property
    def resource(self):
        return EmsAlertAction

    gettable_fields = [
        "possible_actions",
    ]
    """possible_actions,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class EmsAlertAction(Resource):

    _schema = EmsAlertActionSchema
