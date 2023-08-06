r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

try:
    RECLINE_INSTALLED = False
    import recline
    from recline.arg_types.choices import Choices
    from recline.commands import ReclineCommandError
    from netapp_ontap.resource_table import ResourceTable
    RECLINE_INSTALLED = True
except ImportError:
    pass

from marshmallow import fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["XcLun", "XcLunSchema"]
__pdoc__ = {
    "XcLunSchema.resource": False,
    "XcLunSchema.opts": False,
    "XcLun.xc_lun_show": False,
    "XcLun.xc_lun_create": False,
    "XcLun.xc_lun_modify": False,
    "XcLun.xc_lun_delete": False,
}


class XcLunSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcLun object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_lun. """

    attributes = fields.List(fields.Nested("netapp_ontap.models.lun_attributes.LunAttributesSchema", unknown=EXCLUDE), data_key="attributes")
    r""" An array of name/value pairs optionally stored with the LUN. Attributes are available to callers to persist small amounts of application-specific metadata. They are in no way interpreted by ONTAP.<br/>
Attribute names and values must be at least one byte and no more than 4091 bytes in length. The sum of the name and value lengths must be no more than 4092 bytes.<br/>
Valid in POST except when creating a LUN clone. A cloned can already have attributes from its source. You can add, modify, and delete the attributes of a LUN clone in separate requests after creation of the LUN.<br/>
Attributes may be added/modified/removed for an existing LUN using the /api/storage/luns/{lun.uuid}/attributes endpoint. For further information, see [`DOC /storage/luns/{lun.uuid}/attributes`](#docs-SAN-storage_luns_{lun.uuid}_attributes).<br/>
There is an added cost to retrieving property values for `attributes`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. """

    auto_delete = fields.Boolean(
        data_key="auto_delete",
    )
    r""" This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/>
When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/>
This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/>
There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. """

    class_ = fields.Str(
        data_key="class",
        validate=enum_validation(['regular', 'protocol_endpoint', 'vvol']),
    )
    r""" The class of LUN.<br/>
Optional in POST.


Valid choices:

* regular
* protocol_endpoint
* vvol """

    clone = fields.Nested("netapp_ontap.models.consistency_group_consistency_groups_luns_clone.ConsistencyGroupConsistencyGroupsLunsCloneSchema", data_key="clone", unknown=EXCLUDE)
    r""" The clone field of the xc_lun. """

    comment = fields.Str(
        data_key="comment",
        validate=len_validation(minimum=0, maximum=254),
    )
    r""" A configurable comment available for use by the administrator. Valid in POST and PATCH. """

    consistency_group = fields.Nested("netapp_ontap.models.lun_consistency_group.LunConsistencyGroupSchema", data_key="consistency_group", unknown=EXCLUDE)
    r""" The consistency_group field of the xc_lun. """

    convert = fields.Nested("netapp_ontap.models.lun_convert.LunConvertSchema", data_key="convert", unknown=EXCLUDE)
    r""" The convert field of the xc_lun. """

    copy = fields.Nested("netapp_ontap.models.lun_copy.LunCopySchema", data_key="copy", unknown=EXCLUDE)
    r""" The copy field of the xc_lun. """

    create_time = ImpreciseDateTime(
        data_key="create_time",
    )
    r""" The time the LUN was created.

Example: 2018-06-04T19:00:00Z """

    enabled = fields.Boolean(
        data_key="enabled",
    )
    r""" The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. """

    location = fields.Nested("netapp_ontap.models.lun_location.LunLocationSchema", data_key="location", unknown=EXCLUDE)
    r""" The location field of the xc_lun. """

    lun_maps = fields.List(fields.Nested("netapp_ontap.models.lun_lun_maps.LunLunMapsSchema", unknown=EXCLUDE), data_key="lun_maps")
    r""" The LUN maps with which the LUN is associated.<br/>
There is an added cost to retrieving property values for `lun_maps`. They are not populated for either a collection GET or an instance GET unless explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. """

    metric = fields.Nested("netapp_ontap.resources.performance_metric.PerformanceMetricSchema", data_key="metric", unknown=EXCLUDE)
    r""" The metric field of the xc_lun. """

    movement = fields.Nested("netapp_ontap.models.lun_movement.LunMovementSchema", data_key="movement", unknown=EXCLUDE)
    r""" The movement field of the xc_lun. """

    name = fields.Str(
        data_key="name",
    )
    r""" The fully qualified path name of the LUN composed of a "/vol" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/>
A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/>
A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation.


Example: /vol/volume1/qtree1/lun1 """

    os_type = fields.Str(
        data_key="os_type",
        validate=enum_validation(['aix', 'hpux', 'hyper_v', 'linux', 'netware', 'openvms', 'solaris', 'solaris_efi', 'vmware', 'windows', 'windows_2008', 'windows_gpt', 'xen']),
    )
    r""" The operating system type of the LUN.<br/>
Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone.


Valid choices:

* aix
* hpux
* hyper_v
* linux
* netware
* openvms
* solaris
* solaris_efi
* vmware
* windows
* windows_2008
* windows_gpt
* xen """

    qos_policy = fields.Nested("netapp_ontap.models.lun_qos_policy.LunQosPolicySchema", data_key="qos_policy", unknown=EXCLUDE)
    r""" The qos_policy field of the xc_lun. """

    serial_number = fields.Str(
        data_key="serial_number",
        validate=len_validation(minimum=12, maximum=12),
    )
    r""" The LUN serial number. The serial number is generated by ONTAP when the LUN is created. """

    space = fields.Nested("netapp_ontap.models.lun_space.LunSpaceSchema", data_key="space", unknown=EXCLUDE)
    r""" The space field of the xc_lun. """

    statistics = fields.Nested("netapp_ontap.models.performance_metric_raw.PerformanceMetricRawSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_lun. """

    status = fields.Nested("netapp_ontap.models.lun_status.LunStatusSchema", data_key="status", unknown=EXCLUDE)
    r""" The status field of the xc_lun. """

    svm = fields.Nested("netapp_ontap.resources.svm.SvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_lun. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created.


Example: 1cd8a442-86d1-11e0-ae1c-123478563412 """

    vvol = fields.Nested("netapp_ontap.models.lun_vvol.LunVvolSchema", data_key="vvol", unknown=EXCLUDE)
    r""" The vvol field of the xc_lun. """

    @property
    def resource(self):
        return XcLun

    gettable_fields = [
        "links",
        "attributes",
        "auto_delete",
        "class_",
        "comment",
        "consistency_group",
        "copy",
        "create_time",
        "enabled",
        "location",
        "lun_maps",
        "metric",
        "movement",
        "name",
        "os_type",
        "qos_policy",
        "serial_number",
        "space",
        "statistics.iops_raw",
        "statistics.latency_raw",
        "statistics.status",
        "statistics.throughput_raw",
        "statistics.timestamp",
        "status",
        "svm.links",
        "svm.name",
        "svm.uuid",
        "uuid",
        "vvol",
    ]
    """links,attributes,auto_delete,class_,comment,consistency_group,copy,create_time,enabled,location,lun_maps,metric,movement,name,os_type,qos_policy,serial_number,space,statistics.iops_raw,statistics.latency_raw,statistics.status,statistics.throughput_raw,statistics.timestamp,status,svm.links,svm.name,svm.uuid,uuid,vvol,"""

    patchable_fields = [
        "auto_delete",
        "clone",
        "comment",
        "consistency_group",
        "copy",
        "enabled",
        "location",
        "movement",
        "name",
        "qos_policy",
        "space",
        "status",
        "svm.name",
        "svm.uuid",
        "vvol",
    ]
    """auto_delete,clone,comment,consistency_group,copy,enabled,location,movement,name,qos_policy,space,status,svm.name,svm.uuid,vvol,"""

    postable_fields = [
        "attributes",
        "auto_delete",
        "class_",
        "clone",
        "comment",
        "consistency_group",
        "convert",
        "copy",
        "location",
        "movement",
        "name",
        "os_type",
        "qos_policy",
        "space",
        "status",
        "svm.name",
        "svm.uuid",
        "vvol",
    ]
    """attributes,auto_delete,class_,clone,comment,consistency_group,convert,copy,location,movement,name,os_type,qos_policy,space,status,svm.name,svm.uuid,vvol,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcLun.get_collection(fields=field)]
    return getter

async def _wait_for_job(response: NetAppResponse) -> None:
    """Examine the given response. If it is a job, asynchronously wait for it to
    complete. While polling, prints the current status message of the job.
    """

    if not response.is_job:
        return
    from netapp_ontap.resources import Job
    job = Job(**response.http_response.json()["job"])
    while True:
        job.get(fields="state,message")
        if hasattr(job, "message"):
            print("[%s]: %s" % (job.state, job.message))
        if job.state == "failure":
            raise NetAppRestError("XcLun modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcLun(Resource):
    r""" lun clone for cluster peer. """

    _schema = XcLunSchema
    _path = "/api/svm/peers/{peer[uuid]}/storage/luns"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET LUNs"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc lun show")
        def xc_lun_show(
            peer_uuid,
            auto_delete: Choices.define(_get_field_list("auto_delete"), cache_choices=True, inexact=True)=None,
            class_: Choices.define(_get_field_list("class_"), cache_choices=True, inexact=True)=None,
            comment: Choices.define(_get_field_list("comment"), cache_choices=True, inexact=True)=None,
            create_time: Choices.define(_get_field_list("create_time"), cache_choices=True, inexact=True)=None,
            enabled: Choices.define(_get_field_list("enabled"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            os_type: Choices.define(_get_field_list("os_type"), cache_choices=True, inexact=True)=None,
            serial_number: Choices.define(_get_field_list("serial_number"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["auto_delete", "class_", "comment", "create_time", "enabled", "name", "os_type", "serial_number", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcLun resources

            Args:
                auto_delete: This property marks the LUN for auto deletion when the volume containing the LUN runs out of space. This is most commonly set on LUN clones.<br/> When set to _true_, the LUN becomes eligible for automatic deletion when the volume runs out of space. Auto deletion only occurs when the volume containing the LUN is also configured for auto deletion and free space in the volume decreases below a particular threshold.<br/> This property is optional in POST and PATCH. The default value for a new LUN is _false_.<br/> There is an added cost to retrieving this property's value. It is not populated for either a collection GET or an instance GET unless it is explicitly requested using the `fields` query parameter. See [`Requesting specific fields`](#Requesting_specific_fields) to learn more. 
                class_: The class of LUN.<br/> Optional in POST. 
                comment: A configurable comment available for use by the administrator. Valid in POST and PATCH. 
                create_time: The time the LUN was created.
                enabled: The enabled state of the LUN. LUNs can be disabled to prevent access to the LUN. Certain error conditions also cause the LUN to become disabled. If the LUN is disabled, you can consult the `state` property to determine if the LUN is administratively disabled (_offline_) or has become disabled as a result of an error. A LUN in an error condition can be brought online by setting the `enabled` property to _true_ or brought administratively offline by setting the `enabled` property to _false_. Upon creation, a LUN is enabled by default. Valid in PATCH. 
                name: The fully qualified path name of the LUN composed of a \"/vol\" prefix, the volume name, the (optional) qtree name, and base name of the LUN. Valid in POST and PATCH.<br/> A PATCH that modifies the qtree and/or base name portion of the LUN path is considered a rename operation.<br/> A PATCH that modifies the volume portion of the LUN path begins an asynchronous LUN movement operation. 
                os_type: The operating system type of the LUN.<br/> Required in POST when creating a LUN that is not a clone of another. Disallowed in POST when creating a LUN clone. 
                serial_number: The LUN serial number. The serial number is generated by ONTAP when the LUN is created. 
                uuid: The unique identifier of the LUN.  The UUID is generated by ONTAP when the LUN is created. 
            """

            kwargs = {}
            if auto_delete is not None:
                kwargs["auto_delete"] = auto_delete
            if class_ is not None:
                kwargs["class_"] = class_
            if comment is not None:
                kwargs["comment"] = comment
            if create_time is not None:
                kwargs["create_time"] = create_time
            if enabled is not None:
                kwargs["enabled"] = enabled
            if name is not None:
                kwargs["name"] = name
            if os_type is not None:
                kwargs["os_type"] = os_type
            if serial_number is not None:
                kwargs["serial_number"] = serial_number
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcLun.get_collection(
                peer_uuid,
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all XcLun resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET LUNs"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






