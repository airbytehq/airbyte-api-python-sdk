"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceLinkedinAdsCredentialsAccessTokenAuthMethod(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinAdsCredentialsAccessToken:
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The token value generated using the authentication code. See the <a href=\\"https://docs.airbyte.com/integrations/sources/linkedin-ads#authentication\\">docs</a> to obtain yours."""
    auth_method: Optional[SourceLinkedinAdsCredentialsAccessTokenAuthMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    
class SourceLinkedinAdsCredentialsOAuth20AuthMethod(str, Enum):
    O_AUTH2_0 = 'oAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinAdsCredentialsOAuth20:
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of the LinkedIn Ads developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret the LinkedIn Ads developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access token."""
    auth_method: Optional[SourceLinkedinAdsCredentialsOAuth20AuthMethod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    
class SourceLinkedinAdsLinkedinAds(str, Enum):
    LINKEDIN_ADS = 'linkedin-ads'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinAds:
    r"""The values required to configure the source."""
    
    source_type: SourceLinkedinAdsLinkedinAds = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""UTC date in the format 2020-09-17. Any data before this date will not be replicated."""
    account_ids: Optional[list[int]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_ids'), 'exclude': lambda f: f is None }})
    r"""Specify the account IDs separated by a space, to pull the data from. Leave empty, if you want to pull the data from all associated accounts. See the <a href=\\"https://www.linkedin.com/help/linkedin/answer/a424270/find-linkedin-ads-account-details?lang=en\\">LinkedIn Ads docs</a> for more info."""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    