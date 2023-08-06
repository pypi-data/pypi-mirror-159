r"""
Copyright &copy; 2022 NetApp Inc.
All rights reserved.

This file has been automatically generated based on the ONTAP REST API documentation.


"""

from marshmallow import EXCLUDE, fields  # type: ignore
from netapp_ontap.resource import Resource, ResourceSchema, ResourceSchemaMeta, ImpreciseDateTime, Size


__all__ = ["ClusterNodesVm", "ClusterNodesVmSchema"]
__pdoc__ = {
    "ClusterNodesVmSchema.resource": False,
    "ClusterNodesVmSchema.opts": False,
    "ClusterNodesVm": False,
}


class ClusterNodesVmSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the ClusterNodesVm object"""

    account_id = fields.Str(data_key="account_id")
    r""" The cloud provider account ID. """

    deployment_id = fields.Str(data_key="deployment_id")
    r""" The cloud provider deployment ID. """

    fault_domain = fields.Str(data_key="fault_domain")
    r""" The VM fault domain. """

    instance_id = fields.Str(data_key="instance_id")
    r""" The cloud provider instance ID. """

    primary_ip = fields.Str(data_key="primary_ip")
    r""" The VM primary IP address. """

    provider_type = fields.Str(data_key="provider_type")
    r""" Cloud provider where the VM is hosted.

Valid choices:

* GoogleCloud
* AWS_S3
* Azure_Cloud """

    update_domain = fields.Str(data_key="update_domain")
    r""" The VM update domain. """

    @property
    def resource(self):
        return ClusterNodesVm

    gettable_fields = [
        "account_id",
        "deployment_id",
        "fault_domain",
        "instance_id",
        "primary_ip",
        "provider_type",
        "update_domain",
    ]
    """account_id,deployment_id,fault_domain,instance_id,primary_ip,provider_type,update_domain,"""

    patchable_fields = [
    ]
    """"""

    postable_fields = [
    ]
    """"""


class ClusterNodesVm(Resource):

    _schema = ClusterNodesVmSchema
