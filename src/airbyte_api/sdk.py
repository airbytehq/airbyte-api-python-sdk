"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

import requests as requests_http
from .connections import Connections
from .destinations import Destinations
from .health import Health
from .jobs import Jobs
from .organizations import Organizations
from .permissions import Permissions
from .sdkconfiguration import SDKConfiguration
from .sources import Sources
from .streams import Streams
from .tags import Tags
from .users import Users
from .utils.retries import RetryConfig
from .workspaces import Workspaces
from airbyte_api import models, utils
from airbyte_api._hooks import SDKHooks
from typing import Callable, Dict, Optional, Union

class AirbyteAPI:
    r"""airbyte-api: Programmatically control Airbyte Cloud, OSS & Enterprise."""
    connections: Connections
    destinations: Destinations
    health: Health
    jobs: Jobs
    organizations: Organizations
    permissions: Permissions
    sources: Sources
    streams: Streams
    tags: Tags
    users: Users
    workspaces: Workspaces

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[models.Security,Callable[[], models.Security]] = None,
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param security: The security details required for authentication
        :type security: Union[models.Security,Callable[[], models.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.connections = Connections(self.sdk_configuration)
        self.destinations = Destinations(self.sdk_configuration)
        self.health = Health(self.sdk_configuration)
        self.jobs = Jobs(self.sdk_configuration)
        self.organizations = Organizations(self.sdk_configuration)
        self.permissions = Permissions(self.sdk_configuration)
        self.sources = Sources(self.sdk_configuration)
        self.streams = Streams(self.sdk_configuration)
        self.tags = Tags(self.sdk_configuration)
        self.users = Users(self.sdk_configuration)
        self.workspaces = Workspaces(self.sdk_configuration)
