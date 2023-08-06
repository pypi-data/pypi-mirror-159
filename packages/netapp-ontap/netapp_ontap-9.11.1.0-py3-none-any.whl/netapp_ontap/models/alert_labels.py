r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["AlertLabels", "AlertLabelsSchema"]
__pdoc__ = {
    "AlertLabelsSchema.resource": False,
    "AlertLabelsSchema.opts": False,
    "AlertLabels": False,
}


class AlertLabelsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AlertLabels object"""

    label = fields.Str(data_key="label")
    r""" The label field of the alert_labels. """

    value = fields.Str(data_key="value")
    r""" The value field of the alert_labels. """

    @property
    def resource(self):
        return AlertLabels

    gettable_fields = [
        "label",
        "value",
    ]
    """label,value,"""

    patchable_fields = [
        "label",
        "value",
    ]
    """label,value,"""

    postable_fields = [
        "label",
        "value",
    ]
    """label,value,"""


class AlertLabels(Resource):

    _schema = AlertLabelsSchema
