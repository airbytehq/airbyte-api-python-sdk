"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union


class SourceSquareSchemasAuthType(str, Enum):
    API_KEY = 'API Key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquareAPIKey:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The API key for a Square application"""
    AUTH_TYPE: Final[SourceSquareSchemasAuthType] = dataclasses.field(default=SourceSquareSchemasAuthType.API_KEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



class SourceSquareAuthType(str, Enum):
    O_AUTH = 'OAuth'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OauthAuthentication:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Square-issued ID of your application"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Square-issued application secret for your application"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""A refresh token generated using the above client ID and secret"""
    AUTH_TYPE: Final[SourceSquareAuthType] = dataclasses.field(default=SourceSquareAuthType.O_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


SourceSquareAuthentication = Union['OauthAuthentication', 'SourceSquareAPIKey']


class SourceSquareSquare(str, Enum):
    SQUARE = 'square'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSquare:
    credentials: Optional[SourceSquareAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Square."""
    include_deleted_objects: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted_objects'), 'exclude': lambda f: f is None }})
    r"""In some streams there is an option to include deleted objects (Items, Categories, Discounts, Taxes)"""
    is_sandbox: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})
    r"""Determines whether to use the sandbox or production environment."""
    SOURCE_TYPE: Final[SourceSquareSquare] = dataclasses.field(default=SourceSquareSquare.SQUARE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2021-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""UTC date in the format YYYY-MM-DD. Any data before this date will not be replicated. If not set, all data will be replicated."""
    

