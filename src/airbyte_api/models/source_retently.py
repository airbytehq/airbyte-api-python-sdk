"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, Final, Optional, Union


class SourceRetentlySchemasAuthType(str, Enum):
    TOKEN = 'Token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateWithAPIToken:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Retently API Token. See the <a href=\\"https://app.retently.com/settings/api/tokens\\">docs</a> for more information on how to obtain this key."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceRetentlySchemasAuthType]] = dataclasses.field(default=SourceRetentlySchemasAuthType.TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class SourceRetentlyAuthType(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaRetentlyOAuth:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Retently developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Retently developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Retently Refresh Token which can be used to fetch new Bearer Tokens when the current one expires."""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    AUTH_TYPE: Final[Optional[SourceRetentlyAuthType]] = dataclasses.field(default=SourceRetentlyAuthType.CLIENT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class SourceRetentlyRetently(str, Enum):
    RETENTLY = 'retently'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRetently:
    credentials: Optional[SourceRetentlyAuthenticationMechanism] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Retently"""
    SOURCE_TYPE: Final[Optional[SourceRetentlyRetently]] = dataclasses.field(default=SourceRetentlyRetently.RETENTLY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    


SourceRetentlyAuthenticationMechanism = Union[AuthenticateViaRetentlyOAuth, AuthenticateWithAPIToken]
