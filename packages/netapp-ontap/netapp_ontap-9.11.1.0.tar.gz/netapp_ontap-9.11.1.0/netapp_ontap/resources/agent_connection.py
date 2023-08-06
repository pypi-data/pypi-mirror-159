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


__all__ = ["AgentConnection", "AgentConnectionSchema"]
__pdoc__ = {
    "AgentConnectionSchema.resource": False,
    "AgentConnectionSchema.opts": False,
    "AgentConnection.agent_connection_show": False,
    "AgentConnection.agent_connection_create": False,
    "AgentConnection.agent_connection_modify": False,
    "AgentConnection.agent_connection_delete": False,
}


class AgentConnectionSchema(ResourceSchema, metaclass=ResourceSchemaMeta):
    """The fields of the AgentConnection object"""

    address_family = fields.Str(
        data_key="address_family",
        validate=enum_validation(['unknown', 'ipv4', 'ipv6']),
    )
    r""" IP address family to use for the connection. Auto discovery is attempted if unknown/unset.

Valid choices:

* unknown
* ipv4
* ipv6 """

    application = fields.Str(
        data_key="application",
    )
    r""" Application identification provided by the external manager. """

    application_url = fields.Str(
        data_key="application_url",
    )
    r""" Application URL (HTTP, not AMQP) provided by the external manager. """

    auto_delete_error_minutes = Size(
        data_key="auto_delete_error_minutes",
    )
    r""" Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified. """

    baseline_schedule_state = fields.Str(
        data_key="baseline_schedule_state",
        validate=enum_validation(['waiting', 'running', 'inactive', 'disabled']),
    )
    r""" State of scheduled collection of baseline data.

Valid choices:

* waiting
* running
* inactive
* disabled """

    certificate = fields.Nested("netapp_ontap.resources.security_certificate.SecurityCertificateSchema", data_key="certificate", unknown=EXCLUDE)
    r""" The certificate field of the agent_connection. """

    counters_schedule_state = fields.Str(
        data_key="counters_schedule_state",
        validate=enum_validation(['waiting', 'running', 'inactive', 'disabled']),
    )
    r""" State of scheduled collection of counters data.

Valid choices:

* waiting
* running
* inactive
* disabled """

    encoded_data = fields.Str(
        data_key="encoded_data",
    )
    r""" Encoded data from manager used to establish the connection. """

    error = fields.Nested("netapp_ontap.models.agent_connection_error.AgentConnectionErrorSchema", data_key="error", unknown=EXCLUDE)
    r""" The error field of the agent_connection. """

    ipspace = fields.Nested("netapp_ontap.resources.ipspace.IpspaceSchema", data_key="ipspace", unknown=EXCLUDE)
    r""" The ipspace field of the agent_connection. """

    name = fields.Str(
        data_key="name",
    )
    r""" Name associated with this connection. Must be unique. """

    publish_path = fields.Str(
        data_key="publish_path",
    )
    r""" AMQP path to which ONTAP publishes. Defaults to "ontap.agent.cluster". """

    state = fields.Str(
        data_key="state",
        validate=enum_validation(['connecting', 'connected', 'error', 'disabled']),
    )
    r""" State of the connection. PATCH can only set the value to disabled or connecting.

Valid choices:

* connecting
* connected
* error
* disabled """

    subscribe_path = fields.Str(
        data_key="subscribe_path",
    )
    r""" AMQP path to which ONTAP subscribes. Defaults to "ontap.agent.manager". """

    url = fields.Str(
        data_key="url",
    )
    r""" URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP).
Trailing optional [s] for secure connection. "amqpwss" is the default protocol
that is used if only a hostname is provided.


Example: amqpwss://hostname:port """

    use_proxy = fields.Boolean(
        data_key="use_proxy",
    )
    r""" Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy. """

    uuid = fields.Str(
        data_key="uuid",
    )
    r""" UUID of the connection to the external manager. """

    @property
    def resource(self):
        return AgentConnection

    gettable_fields = [
        "address_family",
        "application",
        "application_url",
        "auto_delete_error_minutes",
        "baseline_schedule_state",
        "certificate.links",
        "certificate.name",
        "certificate.uuid",
        "counters_schedule_state",
        "error",
        "ipspace.links",
        "ipspace.name",
        "ipspace.uuid",
        "name",
        "state",
        "url",
        "use_proxy",
        "uuid",
    ]
    """address_family,application,application_url,auto_delete_error_minutes,baseline_schedule_state,certificate.links,certificate.name,certificate.uuid,counters_schedule_state,error,ipspace.links,ipspace.name,ipspace.uuid,name,state,url,use_proxy,uuid,"""

    patchable_fields = [
        "address_family",
        "auto_delete_error_minutes",
        "baseline_schedule_state",
        "certificate.name",
        "certificate.uuid",
        "counters_schedule_state",
        "error",
        "ipspace.name",
        "ipspace.uuid",
        "url",
        "use_proxy",
    ]
    """address_family,auto_delete_error_minutes,baseline_schedule_state,certificate.name,certificate.uuid,counters_schedule_state,error,ipspace.name,ipspace.uuid,url,use_proxy,"""

    postable_fields = [
        "address_family",
        "auto_delete_error_minutes",
        "baseline_schedule_state",
        "certificate.name",
        "certificate.uuid",
        "counters_schedule_state",
        "encoded_data",
        "error",
        "ipspace.name",
        "ipspace.uuid",
        "name",
        "publish_path",
        "subscribe_path",
        "url",
        "use_proxy",
    ]
    """address_family,auto_delete_error_minutes,baseline_schedule_state,certificate.name,certificate.uuid,counters_schedule_state,encoded_data,error,ipspace.name,ipspace.uuid,name,publish_path,subscribe_path,url,use_proxy,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in AgentConnection.get_collection(fields=field)]
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
            raise NetAppRestError("AgentConnection modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class AgentConnection(Resource):
    """Allows interaction with AgentConnection objects on the host"""

    _schema = AgentConnectionSchema
    _path = "/api/cluster/agent/connections"
    _keys = ["uuid"]

    @classmethod
    def get_collection(
        cls,
        *args,
        connection: HostConnection = None,
        max_records: int = None,
        **kwargs
    ) -> Iterable["Resource"]:
        r"""Retrieves a list of agent connections to external managers.
### Related ONTAP commands
* `cluster agent connection show`
"""
        return super()._get_collection(*args, connection=connection, max_records=max_records, **kwargs)

    get_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._get_collection.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="agent connection show")
        def agent_connection_show(
            fields: List[Choices.define(["address_family", "application", "application_url", "auto_delete_error_minutes", "baseline_schedule_state", "counters_schedule_state", "encoded_data", "name", "publish_path", "state", "subscribe_path", "url", "use_proxy", "uuid", "*"])]=None,
        ) -> ResourceTable:
            """Fetch a list of AgentConnection resources

            Args:
                address_family: IP address family to use for the connection. Auto discovery is attempted if unknown/unset.
                application: Application identification provided by the external manager.
                application_url: Application URL (HTTP, not AMQP) provided by the external manager.
                auto_delete_error_minutes: Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified.
                baseline_schedule_state: State of scheduled collection of baseline data.
                counters_schedule_state: State of scheduled collection of counters data.
                encoded_data: Encoded data from manager used to establish the connection.
                name: Name associated with this connection. Must be unique.
                publish_path: AMQP path to which ONTAP publishes. Defaults to \"ontap.agent.cluster\". 
                state: State of the connection. PATCH can only set the value to disabled or connecting.
                subscribe_path: AMQP path to which ONTAP subscribes. Defaults to \"ontap.agent.manager\". 
                url: URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP). Trailing optional [s] for secure connection. \"amqpwss\" is the default protocol that is used if only a hostname is provided. 
                use_proxy: Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy.
                uuid: UUID of the connection to the external manager.
            """

            kwargs = {}
            if address_family is not None:
                kwargs["address_family"] = address_family
            if application is not None:
                kwargs["application"] = application
            if application_url is not None:
                kwargs["application_url"] = application_url
            if auto_delete_error_minutes is not None:
                kwargs["auto_delete_error_minutes"] = auto_delete_error_minutes
            if baseline_schedule_state is not None:
                kwargs["baseline_schedule_state"] = baseline_schedule_state
            if counters_schedule_state is not None:
                kwargs["counters_schedule_state"] = counters_schedule_state
            if encoded_data is not None:
                kwargs["encoded_data"] = encoded_data
            if name is not None:
                kwargs["name"] = name
            if publish_path is not None:
                kwargs["publish_path"] = publish_path
            if state is not None:
                kwargs["state"] = state
            if subscribe_path is not None:
                kwargs["subscribe_path"] = subscribe_path
            if url is not None:
                kwargs["url"] = url
            if use_proxy is not None:
                kwargs["use_proxy"] = use_proxy
            if uuid is not None:
                kwargs["uuid"] = uuid
            if fields is not None:
                fields = ",".join(fields)
                kwargs["fields"] = fields

            return AgentConnection.get_collection(
                **kwargs
            )

    @classmethod
    def count_collection(
        cls,
        *args,
        connection: HostConnection = None,
        **kwargs
    ) -> int:
        """Returns a count of all AgentConnection resources that match the provided query"""
        return super()._count_collection(*args, connection=connection, **kwargs)

    count_collection.__func__.__doc__ = "\n\n---\n" + inspect.cleandoc(Resource._count_collection.__doc__)

    @classmethod
    def patch_collection(
        cls,
        body: dict,
        *args,
        records: Iterable["AgentConnection"] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a connection to an external manager.
### Required properties
* `uuid` - UUID for the specified manager.
### Related ONTAP commands
* `cluster agent connection modify`
"""
        return super()._patch_collection(
            body, *args, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    patch_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch_collection.__doc__)

    @classmethod
    def post_collection(
        cls,
        records: Iterable["AgentConnection"],
        *args,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> Union[List["AgentConnection"], NetAppResponse]:
        r"""Creates a connection to an external manager to enable efficient delivery of any cluster metadata.
Every connection has full access to GET on any REST API and all Counter Manager objects.
### Required properties
* `uri` - Path for the specified manager.
* `name` - Name for the connection.
### Related ONTAP commands
* `cluster agent connection create`
"""
        return super()._post_collection(
            records, *args, hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    post_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post_collection.__doc__)

    @classmethod
    def delete_collection(
        cls,
        *args,
        records: Iterable["AgentConnection"] = None,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a connection to an external manager.
### Required properties
* `uuid` - UUID for the specified manager.
### Related ONTAP commands
* `cluster agent connection delete`
"""
        return super()._delete_collection(
            *args, body=body, records=records, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, connection=connection, **kwargs
        )

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)

    @classmethod
    def find(cls, *args, connection: HostConnection = None, **kwargs) -> Resource:
        r"""Retrieves a list of agent connections to external managers.
### Related ONTAP commands
* `cluster agent connection show`
"""
        return super()._find(*args, connection=connection, **kwargs)

    find.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._find.__doc__)


    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Creates a connection to an external manager to enable efficient delivery of any cluster metadata.
Every connection has full access to GET on any REST API and all Counter Manager objects.
### Required properties
* `uri` - Path for the specified manager.
* `name` - Name for the connection.
### Related ONTAP commands
* `cluster agent connection create`
"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="agent connection create")
        async def agent_connection_create(
        ) -> ResourceTable:
            """Create an instance of a AgentConnection resource

            Args:
                address_family: IP address family to use for the connection. Auto discovery is attempted if unknown/unset.
                application: Application identification provided by the external manager.
                application_url: Application URL (HTTP, not AMQP) provided by the external manager.
                auto_delete_error_minutes: Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified.
                baseline_schedule_state: State of scheduled collection of baseline data.
                certificate: 
                counters_schedule_state: State of scheduled collection of counters data.
                encoded_data: Encoded data from manager used to establish the connection.
                error: 
                ipspace: 
                name: Name associated with this connection. Must be unique.
                publish_path: AMQP path to which ONTAP publishes. Defaults to \"ontap.agent.cluster\". 
                state: State of the connection. PATCH can only set the value to disabled or connecting.
                subscribe_path: AMQP path to which ONTAP subscribes. Defaults to \"ontap.agent.manager\". 
                url: URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP). Trailing optional [s] for secure connection. \"amqpwss\" is the default protocol that is used if only a hostname is provided. 
                use_proxy: Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy.
                uuid: UUID of the connection to the external manager.
            """

            kwargs = {}
            if address_family is not None:
                kwargs["address_family"] = address_family
            if application is not None:
                kwargs["application"] = application
            if application_url is not None:
                kwargs["application_url"] = application_url
            if auto_delete_error_minutes is not None:
                kwargs["auto_delete_error_minutes"] = auto_delete_error_minutes
            if baseline_schedule_state is not None:
                kwargs["baseline_schedule_state"] = baseline_schedule_state
            if certificate is not None:
                kwargs["certificate"] = certificate
            if counters_schedule_state is not None:
                kwargs["counters_schedule_state"] = counters_schedule_state
            if encoded_data is not None:
                kwargs["encoded_data"] = encoded_data
            if error is not None:
                kwargs["error"] = error
            if ipspace is not None:
                kwargs["ipspace"] = ipspace
            if name is not None:
                kwargs["name"] = name
            if publish_path is not None:
                kwargs["publish_path"] = publish_path
            if state is not None:
                kwargs["state"] = state
            if subscribe_path is not None:
                kwargs["subscribe_path"] = subscribe_path
            if url is not None:
                kwargs["url"] = url
            if use_proxy is not None:
                kwargs["use_proxy"] = use_proxy
            if uuid is not None:
                kwargs["uuid"] = uuid

            resource = AgentConnection(
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to create AgentConnection: %s" % err)
            return [resource]

    def patch(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Updates a connection to an external manager.
### Required properties
* `uuid` - UUID for the specified manager.
### Related ONTAP commands
* `cluster agent connection modify`
"""
        return super()._patch(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    patch.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._patch.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="agent connection modify")
        async def agent_connection_modify(
        ) -> ResourceTable:
            """Modify an instance of a AgentConnection resource

            Args:
                address_family: IP address family to use for the connection. Auto discovery is attempted if unknown/unset.
                query_address_family: IP address family to use for the connection. Auto discovery is attempted if unknown/unset.
                application: Application identification provided by the external manager.
                query_application: Application identification provided by the external manager.
                application_url: Application URL (HTTP, not AMQP) provided by the external manager.
                query_application_url: Application URL (HTTP, not AMQP) provided by the external manager.
                auto_delete_error_minutes: Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified.
                query_auto_delete_error_minutes: Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified.
                baseline_schedule_state: State of scheduled collection of baseline data.
                query_baseline_schedule_state: State of scheduled collection of baseline data.
                counters_schedule_state: State of scheduled collection of counters data.
                query_counters_schedule_state: State of scheduled collection of counters data.
                encoded_data: Encoded data from manager used to establish the connection.
                query_encoded_data: Encoded data from manager used to establish the connection.
                name: Name associated with this connection. Must be unique.
                query_name: Name associated with this connection. Must be unique.
                publish_path: AMQP path to which ONTAP publishes. Defaults to \"ontap.agent.cluster\". 
                query_publish_path: AMQP path to which ONTAP publishes. Defaults to \"ontap.agent.cluster\". 
                state: State of the connection. PATCH can only set the value to disabled or connecting.
                query_state: State of the connection. PATCH can only set the value to disabled or connecting.
                subscribe_path: AMQP path to which ONTAP subscribes. Defaults to \"ontap.agent.manager\". 
                query_subscribe_path: AMQP path to which ONTAP subscribes. Defaults to \"ontap.agent.manager\". 
                url: URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP). Trailing optional [s] for secure connection. \"amqpwss\" is the default protocol that is used if only a hostname is provided. 
                query_url: URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP). Trailing optional [s] for secure connection. \"amqpwss\" is the default protocol that is used if only a hostname is provided. 
                use_proxy: Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy.
                query_use_proxy: Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy.
                uuid: UUID of the connection to the external manager.
                query_uuid: UUID of the connection to the external manager.
            """

            kwargs = {}
            changes = {}
            if query_address_family is not None:
                kwargs["address_family"] = query_address_family
            if query_application is not None:
                kwargs["application"] = query_application
            if query_application_url is not None:
                kwargs["application_url"] = query_application_url
            if query_auto_delete_error_minutes is not None:
                kwargs["auto_delete_error_minutes"] = query_auto_delete_error_minutes
            if query_baseline_schedule_state is not None:
                kwargs["baseline_schedule_state"] = query_baseline_schedule_state
            if query_counters_schedule_state is not None:
                kwargs["counters_schedule_state"] = query_counters_schedule_state
            if query_encoded_data is not None:
                kwargs["encoded_data"] = query_encoded_data
            if query_name is not None:
                kwargs["name"] = query_name
            if query_publish_path is not None:
                kwargs["publish_path"] = query_publish_path
            if query_state is not None:
                kwargs["state"] = query_state
            if query_subscribe_path is not None:
                kwargs["subscribe_path"] = query_subscribe_path
            if query_url is not None:
                kwargs["url"] = query_url
            if query_use_proxy is not None:
                kwargs["use_proxy"] = query_use_proxy
            if query_uuid is not None:
                kwargs["uuid"] = query_uuid

            if address_family is not None:
                changes["address_family"] = address_family
            if application is not None:
                changes["application"] = application
            if application_url is not None:
                changes["application_url"] = application_url
            if auto_delete_error_minutes is not None:
                changes["auto_delete_error_minutes"] = auto_delete_error_minutes
            if baseline_schedule_state is not None:
                changes["baseline_schedule_state"] = baseline_schedule_state
            if counters_schedule_state is not None:
                changes["counters_schedule_state"] = counters_schedule_state
            if encoded_data is not None:
                changes["encoded_data"] = encoded_data
            if name is not None:
                changes["name"] = name
            if publish_path is not None:
                changes["publish_path"] = publish_path
            if state is not None:
                changes["state"] = state
            if subscribe_path is not None:
                changes["subscribe_path"] = subscribe_path
            if url is not None:
                changes["url"] = url
            if use_proxy is not None:
                changes["use_proxy"] = use_proxy
            if uuid is not None:
                changes["uuid"] = uuid

            if hasattr(AgentConnection, "find"):
                resource = AgentConnection.find(
                    **kwargs
                )
            else:
                resource = AgentConnection()
            try:
                for key, value in changes.items():
                    setattr(resource, key, value)
                response = resource.patch(poll=False)
                await _wait_for_job(response)
                resource.get(fields=",".join(changes.keys()))
                return [resource]
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to modify AgentConnection: %s" % err)

    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a connection to an external manager.
### Required properties
* `uuid` - UUID for the specified manager.
### Related ONTAP commands
* `cluster agent connection delete`
"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if RECLINE_INSTALLED:
        @recline.command(name="agent connection delete")
        async def agent_connection_delete(
        ) -> None:
            """Delete an instance of a AgentConnection resource

            Args:
                address_family: IP address family to use for the connection. Auto discovery is attempted if unknown/unset.
                application: Application identification provided by the external manager.
                application_url: Application URL (HTTP, not AMQP) provided by the external manager.
                auto_delete_error_minutes: Specifies the time to live, in minutes for a cloud agent connection in the error state. A connection is deleted if it remains in this state beyond the time specified.
                baseline_schedule_state: State of scheduled collection of baseline data.
                counters_schedule_state: State of scheduled collection of counters data.
                encoded_data: Encoded data from manager used to establish the connection.
                name: Name associated with this connection. Must be unique.
                publish_path: AMQP path to which ONTAP publishes. Defaults to \"ontap.agent.cluster\". 
                state: State of the connection. PATCH can only set the value to disabled or connecting.
                subscribe_path: AMQP path to which ONTAP subscribes. Defaults to \"ontap.agent.manager\". 
                url: URL for external manager. Supports amqpws[s] (AMQP over websocket) and amqp[s] (AMQP). Trailing optional [s] for secure connection. \"amqpwss\" is the default protocol that is used if only a hostname is provided. 
                use_proxy: Establish this connection through the HTTP Proxy server associated with this connection's IPspace. See /api/network/http-proxy.
                uuid: UUID of the connection to the external manager.
            """

            kwargs = {}
            if address_family is not None:
                kwargs["address_family"] = address_family
            if application is not None:
                kwargs["application"] = application
            if application_url is not None:
                kwargs["application_url"] = application_url
            if auto_delete_error_minutes is not None:
                kwargs["auto_delete_error_minutes"] = auto_delete_error_minutes
            if baseline_schedule_state is not None:
                kwargs["baseline_schedule_state"] = baseline_schedule_state
            if counters_schedule_state is not None:
                kwargs["counters_schedule_state"] = counters_schedule_state
            if encoded_data is not None:
                kwargs["encoded_data"] = encoded_data
            if name is not None:
                kwargs["name"] = name
            if publish_path is not None:
                kwargs["publish_path"] = publish_path
            if state is not None:
                kwargs["state"] = state
            if subscribe_path is not None:
                kwargs["subscribe_path"] = subscribe_path
            if url is not None:
                kwargs["url"] = url
            if use_proxy is not None:
                kwargs["use_proxy"] = use_proxy
            if uuid is not None:
                kwargs["uuid"] = uuid

            if hasattr(AgentConnection, "find"):
                resource = AgentConnection.find(
                    **kwargs
                )
            else:
                resource = AgentConnection()
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ReclineCommandError("Unable to delete AgentConnection: %s" % err)


