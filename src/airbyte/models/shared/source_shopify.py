"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union

class SourceShopifyShopifyAuthorizationMethodAPIPasswordAuthMethod(str, Enum):
    API_PASSWORD = 'api_password'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceShopifyShopifyAuthorizationMethodAPIPassword:
    r"""API Password Auth"""
    api_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_password') }})
    r"""The API Password for your private application in the `Shopify` store."""
    AUTH_METHOD: Final[SourceShopifyShopifyAuthorizationMethodAPIPasswordAuthMethod] = dataclasses.field(default=SourceShopifyShopifyAuthorizationMethodAPIPasswordAuthMethod.API_PASSWORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    


class SourceShopifyShopifyAuthorizationMethodOAuth20AuthMethod(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceShopifyShopifyAuthorizationMethodOAuth20:
    r"""OAuth2.0"""
    AUTH_METHOD: Final[SourceShopifyShopifyAuthorizationMethodOAuth20AuthMethod] = dataclasses.field(default=SourceShopifyShopifyAuthorizationMethodOAuth20AuthMethod.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})
    r"""The Access Token for making authenticated requests."""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of the Shopify developer application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of the Shopify developer application."""
    




@dataclasses.dataclass
class SourceShopifyShopifyAuthorizationMethod:
    pass

class SourceShopifyShopify(str, Enum):
    SHOPIFY = 'shopify'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceShopify:
    r"""The values required to configure the source."""
    shop: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shop') }})
    r"""The name of your Shopify store found in the URL. For example, if your URL was https://NAME.myshopify.com, then the name would be 'NAME' or 'NAME.myshopify.com'."""
    SOURCE_TYPE: Final[SourceShopifyShopify] = dataclasses.field(default=SourceShopifyShopify.SHOPIFY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[SourceShopifyShopifyAuthorizationMethodOAuth20, SourceShopifyShopifyAuthorizationMethodAPIPassword]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""The authorization method to use to retrieve data from Shopify"""
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2020-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date you would like to replicate data from. Format: YYYY-MM-DD. Any data before this date will not be replicated."""
    

