"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceCartSchemasAuthType(str, Enum):
    SINGLE_STORE_ACCESS_TOKEN = 'SINGLE_STORE_ACCESS_TOKEN'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SingleStoreAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    store_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_name') }})
    r"""The name of Cart.com Online Store. All API URLs start with https://[mystorename.com]/api/v1/, where [mystorename.com] is the domain name of your store."""
    AUTH_TYPE: Final[SourceCartSchemasAuthType] = dataclasses.field(default=SourceCartSchemasAuthType.SINGLE_STORE_ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



class SourceCartAuthType(str, Enum):
    CENTRAL_API_ROUTER = 'CENTRAL_API_ROUTER'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CentralAPIRouter:
    site_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_id') }})
    r"""You can determine a site provisioning site Id by hitting https://site.com/store/sitemonitor.aspx and reading the response param PSID"""
    user_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_name') }})
    r"""Enter your application's User Name"""
    user_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_secret') }})
    r"""Enter your application's User Secret"""
    AUTH_TYPE: Final[SourceCartAuthType] = dataclasses.field(default=SourceCartAuthType.CENTRAL_API_ROUTER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



class Cart(str, Enum):
    CART = 'cart'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCart:
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The date from which you'd like to replicate the data"""
    credentials: Optional[SourceCartAuthorizationMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Cart] = dataclasses.field(default=Cart.CART, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


SourceCartAuthorizationMethod = Union[CentralAPIRouter, SingleStoreAccessToken]
