"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSftpAuthenticationWildcardSSHKeyAuthentication:
    r"""The server authentication method"""
    auth_ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    AUTH_METHOD: Final[str] = dataclasses.field(default='SSH_KEY_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    r"""Connect through ssh key"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSftpAuthenticationWildcardPasswordAuthentication:
    r"""The server authentication method"""
    auth_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    AUTH_METHOD: Final[str] = dataclasses.field(default='SSH_PASSWORD_AUTH', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    r"""Connect through password authentication"""
    




@dataclasses.dataclass
class SourceSftpAuthenticationWildcard:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSftp:
    r"""The values required to configure the source."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The server host address"""
    user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user') }})
    r"""The server user"""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='sftp', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[SourceSftpAuthenticationWildcardPasswordAuthentication, SourceSftpAuthenticationWildcardSSHKeyAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""The server authentication method"""
    file_pattern: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_pattern'), 'exclude': lambda f: f is None }})
    r"""The regular expression to specify files for sync in a chosen Folder Path"""
    file_types: Optional[str] = dataclasses.field(default='csv,json', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_types'), 'exclude': lambda f: f is None }})
    r"""Coma separated file types. Currently only 'csv' and 'json' types are supported."""
    folder_path: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path'), 'exclude': lambda f: f is None }})
    r"""The directory to search files for sync"""
    port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The server port"""
    

