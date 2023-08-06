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


__all__ = ["XcApplication", "XcApplicationSchema"]
__pdoc__ = {
    "XcApplicationSchema.resource": False,
    "XcApplicationSchema.opts": False,
    "XcApplication.xc_application_show": False,
    "XcApplication.xc_application_create": False,
    "XcApplication.xc_application_modify": False,
    "XcApplication.xc_application_delete": False,
}


class XcApplicationSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the XcApplication object"""

    links = fields.Nested("netapp_ontap.models.application_links.ApplicationLinksSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the xc_application. """

    creation_timestamp = fields.Str(
        data_key="creation_timestamp",
    )
    r""" The time when the application was created. """

    delete_data = fields.Boolean(
        data_key="delete_data",
    )
    r""" Should application storage elements be deleted? An application is considered to use storage elements from a shared storage pool. Possible values are 'true' and 'false'. If the value is 'true', the application will be deleted in its entirety. If the value is 'false', the storage elements will be disassociated from the application and preserved. The application will then be deleted. """

    generation = Size(
        data_key="generation",
    )
    r""" The generation number of the application. This indicates which features are supported on the application. For example, generation 1 applications do not support Snapshot copies. Support for Snapshot copies was added at generation 2. Any future generation numbers and their feature set will be documented. """

    maxdata_on_san = fields.Nested("netapp_ontap.models.maxdata_on_san.MaxdataOnSanSchema", data_key="maxdata_on_san", unknown=EXCLUDE)
    r""" The maxdata_on_san field of the xc_application. """

    mongo_db_on_san = fields.Nested("netapp_ontap.models.mongo_db_on_san.MongoDbOnSanSchema", data_key="mongo_db_on_san", unknown=EXCLUDE)
    r""" The mongo_db_on_san field of the xc_application. """

    name = fields.Str(
        data_key="name",
    )
    r""" Application Name. This field is user supplied when the application is created. """

    nas = fields.Nested("netapp_ontap.models.nas.NasSchema", data_key="nas", unknown=EXCLUDE)
    r""" The nas field of the xc_application. """

    nvme = fields.Nested("netapp_ontap.models.zapp_nvme.ZappNvmeSchema", data_key="nvme", unknown=EXCLUDE)
    r""" The nvme field of the xc_application. """

    oracle_on_nfs = fields.Nested("netapp_ontap.models.oracle_on_nfs.OracleOnNfsSchema", data_key="oracle_on_nfs", unknown=EXCLUDE)
    r""" The oracle_on_nfs field of the xc_application. """

    oracle_on_san = fields.Nested("netapp_ontap.models.oracle_on_san.OracleOnSanSchema", data_key="oracle_on_san", unknown=EXCLUDE)
    r""" The oracle_on_san field of the xc_application. """

    oracle_rac_on_nfs = fields.Nested("netapp_ontap.models.oracle_rac_on_nfs.OracleRacOnNfsSchema", data_key="oracle_rac_on_nfs", unknown=EXCLUDE)
    r""" The oracle_rac_on_nfs field of the xc_application. """

    oracle_rac_on_san = fields.Nested("netapp_ontap.models.oracle_rac_on_san.OracleRacOnSanSchema", data_key="oracle_rac_on_san", unknown=EXCLUDE)
    r""" The oracle_rac_on_san field of the xc_application. """

    protection_granularity = fields.Str(
        data_key="protection_granularity",
        validate=enum_validation(['application', 'component']),
    )
    r""" Protection granularity determines the scope of Snapshot copy operations for the application. Possible values are "application" and "component". If the value is "application", Snapshot copy operations are performed on the entire application. If the value is "component", Snapshot copy operations are performed separately on the application components.

Valid choices:

* application
* component """

    rpo = fields.Nested("netapp_ontap.models.application_rpo.ApplicationRpoSchema", data_key="rpo", unknown=EXCLUDE)
    r""" The rpo field of the xc_application. """

    s3_bucket = fields.Nested("netapp_ontap.models.zapp_s3_bucket.ZappS3BucketSchema", data_key="s3_bucket", unknown=EXCLUDE)
    r""" The s3_bucket field of the xc_application. """

    san = fields.Nested("netapp_ontap.models.san.SanSchema", data_key="san", unknown=EXCLUDE)
    r""" The san field of the xc_application. """

    smart_container = fields.Boolean(
        data_key="smart_container",
    )
    r""" Identifies if this is a smart container or not. """

    sql_on_san = fields.Nested("netapp_ontap.models.sql_on_san.SqlOnSanSchema", data_key="sql_on_san", unknown=EXCLUDE)
    r""" The sql_on_san field of the xc_application. """

    sql_on_smb = fields.Nested("netapp_ontap.models.sql_on_smb.SqlOnSmbSchema", data_key="sql_on_smb", unknown=EXCLUDE)
    r""" The sql_on_smb field of the xc_application. """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['creating', 'deleting', 'modifying', 'online', 'restoring']),
    )
    r""" The state of the application. For full functionality, applications must be in the online state. Other states indicate that the application is in a transient state and not all operations are supported.

Valid choices:

* creating
* deleting
* modifying
* online
* restoring """

    statistics = fields.Nested("netapp_ontap.models.application_statistics.ApplicationStatisticsSchema", data_key="statistics", unknown=EXCLUDE)
    r""" The statistics field of the xc_application. """

    svm = fields.Nested("netapp_ontap.models.application_svm.ApplicationSvmSchema", data_key="svm", unknown=EXCLUDE)
    r""" The svm field of the xc_application. """

    template = fields.Nested("netapp_ontap.models.application_template1.ApplicationTemplate1Schema", data_key="template", unknown=EXCLUDE)
    r""" The template field of the xc_application. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" Application UUID. This field is generated when the application is created. """

    vdi_on_nas = fields.Nested("netapp_ontap.models.vdi_on_nas.VdiOnNasSchema", data_key="vdi_on_nas", unknown=EXCLUDE)
    r""" The vdi_on_nas field of the xc_application. """

    vdi_on_san = fields.Nested("netapp_ontap.models.vdi_on_san.VdiOnSanSchema", data_key="vdi_on_san", unknown=EXCLUDE)
    r""" The vdi_on_san field of the xc_application. """

    vsi_on_nas = fields.Nested("netapp_ontap.models.vsi_on_nas.VsiOnNasSchema", data_key="vsi_on_nas", unknown=EXCLUDE)
    r""" The vsi_on_nas field of the xc_application. """

    vsi_on_san = fields.Nested("netapp_ontap.models.vsi_on_san.VsiOnSanSchema", data_key="vsi_on_san", unknown=EXCLUDE)
    r""" The vsi_on_san field of the xc_application. """

    @property
    def resource(self):
        return XcApplication

    gettable_fields = [
        "links",
        "creation_timestamp",
        "generation",
        "maxdata_on_san",
        "mongo_db_on_san",
        "name",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "protection_granularity",
        "rpo",
        "s3_bucket",
        "san",
        "smart_container",
        "sql_on_san",
        "sql_on_smb",
        "state",
        "statistics",
        "svm",
        "template",
        "uuid",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """links,creation_timestamp,generation,maxdata_on_san,mongo_db_on_san,name,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,protection_granularity,rpo,s3_bucket,san,smart_container,sql_on_san,sql_on_smb,state,statistics,svm,template,uuid,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

    patchable_fields = [
        "links",
        "maxdata_on_san",
        "mongo_db_on_san",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "rpo",
        "s3_bucket",
        "san",
        "sql_on_san",
        "sql_on_smb",
        "statistics",
        "template",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """links,maxdata_on_san,mongo_db_on_san,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,rpo,s3_bucket,san,sql_on_san,sql_on_smb,statistics,template,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

    postable_fields = [
        "links",
        "delete_data",
        "maxdata_on_san",
        "mongo_db_on_san",
        "name",
        "nas",
        "nvme",
        "oracle_on_nfs",
        "oracle_on_san",
        "oracle_rac_on_nfs",
        "oracle_rac_on_san",
        "rpo",
        "s3_bucket",
        "san",
        "smart_container",
        "sql_on_san",
        "sql_on_smb",
        "statistics",
        "svm",
        "template",
        "vdi_on_nas",
        "vdi_on_san",
        "vsi_on_nas",
        "vsi_on_san",
    ]
    """links,delete_data,maxdata_on_san,mongo_db_on_san,name,nas,nvme,oracle_on_nfs,oracle_on_san,oracle_rac_on_nfs,oracle_rac_on_san,rpo,s3_bucket,san,smart_container,sql_on_san,sql_on_smb,statistics,svm,template,vdi_on_nas,vdi_on_san,vsi_on_nas,vsi_on_san,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in XcApplication.get_collection(fields=field)]
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
            raise NetAppRestError("XcApplication modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class XcApplication(Resource):
    r""" application clone for cluster peer. """

    _schema = XcApplicationSchema
    _path = "/api/svm/peers/{peer[uuid]}/application/applications"
    _keys = ["peer.uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Cross cluster GET applications"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="xc application show")
        def xc_application_show(
            peer_uuid,
            creation_timestamp: Choices.define(_get_field_list("creation_timestamp"), cache_choices=True, inexact=True)=None,
            delete_data: Choices.define(_get_field_list("delete_data"), cache_choices=True, inexact=True)=None,
            generation: Choices.define(_get_field_list("generation"), cache_choices=True, inexact=True)=None,
            name: Choices.define(_get_field_list("name"), cache_choices=True, inexact=True)=None,
            protection_granularity: Choices.define(_get_field_list("protection_granularity"), cache_choices=True, inexact=True)=None,
            smart_container: Choices.define(_get_field_list("smart_container"), cache_choices=True, inexact=True)=None,
            state: Choices.define(_get_field_list("state"), cache_choices=True, inexact=True)=None,
            uuid: Choices.define(_get_field_list("uuid"), cache_choices=True, inexact=True)=None,
            fields: List[Choices.define(["creation_timestamp", "delete_data", "generation", "name", "protection_granularity", "smart_container", "state", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of XcApplication resources

            Args:
                creation_timestamp: The time when the application was created.
                delete_data: Should application storage elements be deleted? An application is considered to use storage elements from a shared storage pool. Possible values are 'true' and 'false'. If the value is 'true', the application will be deleted in its entirety. If the value is 'false', the storage elements will be disassociated from the application and preserved. The application will then be deleted.
                generation: The generation number of the application. This indicates which features are supported on the application. For example, generation 1 applications do not support Snapshot copies. Support for Snapshot copies was added at generation 2. Any future generation numbers and their feature set will be documented.
                name: Application Name. This field is user supplied when the application is created.
                protection_granularity: Protection granularity determines the scope of Snapshot copy operations for the application. Possible values are \"application\" and \"component\". If the value is \"application\", Snapshot copy operations are performed on the entire application. If the value is \"component\", Snapshot copy operations are performed separately on the application components.
                smart_container: Identifies if this is a smart container or not.
                state: The state of the application. For full functionality, applications must be in the online state. Other states indicate that the application is in a transient state and not all operations are supported.
                uuid: Application UUID. This field is generated when the application is created.
            """

            kwargs = {}
            if creation_timestamp is not None:
                kwargs["creation_timestamp"] = creation_timestamp
            if delete_data is not None:
                kwargs["delete_data"] = delete_data
            if generation is not None:
                kwargs["generation"] = generation
            if name is not None:
                kwargs["name"] = name
            if protection_granularity is not None:
                kwargs["protection_granularity"] = protection_granularity
            if smart_container is not None:
                kwargs["smart_container"] = smart_container
            if state is not None:
                kwargs["state"] = state
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return XcApplication.get_collection(
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
        """Returns a count of all XcApplication resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)




    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Cross cluster GET applications"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)






