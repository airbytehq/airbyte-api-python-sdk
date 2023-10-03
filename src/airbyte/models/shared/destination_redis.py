"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedisSSLModesVerifyFull:
    r"""Verify-full SSL mode."""
    ca_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ca_certificate') }})
    r"""CA certificate"""
    client_certificate: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_certificate') }})
    r"""Client certificate"""
    client_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key') }})
    r"""Client key"""
    client_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_key_password'), 'exclude': lambda f: f is None }})
    r"""Password for keystorage. If you do not add it - the password will be generated automatically."""
    MODE: Final[Optional[str]] = dataclasses.field(default='verify-full', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedisSSLModesDisable:
    r"""Disable SSL."""
    MODE: Final[Optional[str]] = dataclasses.field(default='disable', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class DestinationRedisSSLModes:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedisSSHTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='SSH_PASSWORD_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedisSSHTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='SSH_KEY_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedisSSHTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    TUNNEL_METHOD: Final[str] = dataclasses.field(default='NO_TUNNEL', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    




@dataclasses.dataclass
class DestinationRedisSSHTunnelMethod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationRedis:
    r"""The values required to configure the destination."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Redis host to connect to."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username associated with Redis."""
    DESTINATION_TYPE: Final[str] = dataclasses.field(default='redis', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    CACHE_TYPE: Final[Optional[str]] = dataclasses.field(default='hash', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cache_type'), 'exclude': lambda f: f is None }})
    r"""Redis cache type to store data in."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with Redis."""
    port: Optional[int] = dataclasses.field(default=6379, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of Redis."""
    ssl: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl'), 'exclude': lambda f: f is None }})
    r"""Indicates whether SSL encryption protocol will be used to connect to Redis. It is recommended to use SSL connection if possible."""
    ssl_mode: Optional[Union[DestinationRedisSSLModesDisable, DestinationRedisSSLModesVerifyFull]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_mode'), 'exclude': lambda f: f is None }})
    r"""SSL connection modes.
      <li><b>verify-full</b> - This is the most secure mode. Always require encryption and verifies the identity of the source database server
    """
    tunnel_method: Optional[Union[DestinationRedisSSHTunnelMethodNoTunnel, DestinationRedisSSHTunnelMethodSSHKeyAuthentication, DestinationRedisSSHTunnelMethodPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

