"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceMondaySchemasAuthType(str, Enum):
    API_TOKEN = 'api_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIToken:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""API Token for making authenticated requests."""
    AUTH_TYPE: Final[SourceMondaySchemasAuthType] = dataclasses.field(default=SourceMondaySchemasAuthType.API_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



class SourceMondayAuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMondayOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your OAuth application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your OAuth application."""
    AUTH_TYPE: Final[SourceMondayAuthType] = dataclasses.field(default=SourceMondayAuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    subdomain: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain'), 'exclude': lambda f: f is None }})
    r"""Slug/subdomain of the account, or the first part of the URL that comes before .monday.com"""
    



class SourceMondayMonday(str, Enum):
    MONDAY = 'monday'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMonday:
    credentials: Optional[Union[SourceMondayOAuth20, APIToken]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[SourceMondayMonday] = dataclasses.field(default=SourceMondayMonday.MONDAY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

