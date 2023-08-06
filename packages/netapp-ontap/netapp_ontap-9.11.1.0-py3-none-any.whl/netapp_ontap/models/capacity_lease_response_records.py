r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["CapacityLeaseResponseRecords", "CapacityLeaseResponseRecordsSchema"]
__pdoc__ = {
    "CapacityLeaseResponseRecordsSchema.resource": False,
    "CapacityLeaseResponseRecordsSchema.opts": False,
    "CapacityLeaseResponseRecords": False,
}


class CapacityLeaseResponseRecordsSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the CapacityLeaseResponseRecords object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", unknown=EXCLUDE, data_key="_links")
    r""" The links field of the capacity_lease_response_records. """

    aggregate = fields.Nested("netapp_ontap.resources.aggregate.AggregateSchema", unknown=EXCLUDE, data_key="aggregate")
    r""" The aggregate field of the capacity_lease_response_records. """

    capacity = Size(data_key="capacity")
    r""" Amount of capacity, in bytes, which this lease entitles the storage aggregate to use.


Example: 1099511627776 """

    expiry_time = ImpreciseDateTime(data_key="expiry_time")
    r""" Date and time when this lease expires.

Example: 2019-02-02T19:00:00Z """

    id = fields.Str(data_key="id")
    r""" Identifier for the lease record.

Example: 390000100-4ea7a442-86d1-11e0-ae1c-112233445566 """

    pool = fields.Nested("netapp_ontap.resources.capacity_pool.CapacityPoolSchema", unknown=EXCLUDE, data_key="pool")
    r""" The pool field of the capacity_lease_response_records. """

    start_time = ImpreciseDateTime(data_key="start_time")
    r""" Date and time when this lease was acquired.

Example: 2019-02-03T19:00:00Z """

    @property
    def resource(self):
        return CapacityLeaseResponseRecords

    gettable_fields = [
        "links",
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "capacity",
        "expiry_time",
        "id",
        "pool.links",
        "pool.serial_number",
        "start_time",
    ]
    """links,aggregate.links,aggregate.name,aggregate.uuid,capacity,expiry_time,id,pool.links,pool.serial_number,start_time,"""

    patchable_fields = [
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "pool.links",
        "pool.serial_number",
    ]
    """aggregate.links,aggregate.name,aggregate.uuid,pool.links,pool.serial_number,"""

    postable_fields = [
        "aggregate.links",
        "aggregate.name",
        "aggregate.uuid",
        "pool.links",
        "pool.serial_number",
    ]
    """aggregate.links,aggregate.name,aggregate.uuid,pool.links,pool.serial_number,"""


class CapacityLeaseResponseRecords(Resource):

    _schema = CapacityLeaseResponseRecordsSchema
