r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["EmsAlertResponseRecords", "EmsAlertResponseRecordsSchema"]
__pdoc__ = {
    "EmsAlertResponseRecordsSchema.resource": False,
    "EmsAlertResponseRecordsSchema.opts": False,
    "EmsAlertResponseRecords": False,
}


class EmsAlertResponseRecordsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the EmsAlertResponseRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the ems_alert_response_records. """

    action = fields.Nested("netapp_ontap.models.ems_alert_action.EmsAlertActionSchema", unknown=EXCLUDE, data_key="action")
    r""" The action field of the ems_alert_response_records. """

    creation_time = ImpreciseDateTime(data_key="creation_time")
    r""" Timestamp of the event creation. """

    index = Size(data_key="index")
    r""" Index of the event. Returned by default.

Example: 1 """

    last_update_time = ImpreciseDateTime(data_key="last_update_time")
    r""" Timestamp of the last update to the alert. """

    log_message = fields.Str(data_key="log_message")
    r""" A formatted text string populated with parameter details. Returned by default. """

    message = fields.Nested("netapp_ontap.models.ems_alert_message.EmsAlertMessageSchema", unknown=EXCLUDE, data_key="message")
    r""" The message field of the ems_alert_response_records. """

    node = fields.Nested("netapp_ontap.resources.node.NodeSchema", unknown=EXCLUDE, data_key="node")
    r""" The node field of the ems_alert_response_records. """

    parameters = fields.List(fields.Nested("netapp_ontap.models.ems_alert_parameters.EmsAlertParametersSchema", unknown=EXCLUDE), data_key="parameters")
    r""" A list of parameters provided with the EMS event. """

    source = fields.Str(data_key="source")
    r""" Source """

    state = fields.Str(data_key="state")
    r""" Indicates the event state. A stateful event tracks the state changes of a system condition and reflects the current system condition.

Valid choices:

* stateless
* opened
* resolving
* resolved
* closed """

    stateful = fields.Boolean(data_key="stateful")
    r""" Indicates whether the event is stateful. A stateful event tracks the state changes of a system condition and reflects the current system condition while a stateless event simply reports a certain system condition that has occurred sometime in the past. """

    time = ImpreciseDateTime(data_key="time")
    r""" Timestamp of the event. Returned by default. """

    uuid = fields.Str(data_key="uuid")
    r""" The UUID that uniquely identifies the alert.

Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    @property
    def resource(self):
        return EmsAlertResponseRecords

    gettable_fields = [
        "links",
        "action",
        "creation_time",
        "index",
        "last_update_time",
        "log_message",
        "message",
        "node.links",
        "node.name",
        "node.uuid",
        "parameters",
        "source",
        "state",
        "stateful",
        "time",
        "uuid",
    ]
    """links,action,creation_time,index,last_update_time,log_message,message,node.links,node.name,node.uuid,parameters,source,state,stateful,time,uuid,"""

    patchable_fields = [
        "action",
        "message",
        "node.name",
        "node.uuid",
    ]
    """action,message,node.name,node.uuid,"""

    postable_fields = [
        "action",
        "message",
        "node.name",
        "node.uuid",
    ]
    """action,message,node.name,node.uuid,"""


class EmsAlertResponseRecords(Resource):

    _schema = EmsAlertResponseRecordsSchema
