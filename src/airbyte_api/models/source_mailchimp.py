"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional, Union


class SourceMailchimpSchemasAuthType(str, Enum):
    APIKEY = 'apikey'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIKey:
    apikey: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apikey') }})
    r"""Mailchimp API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/mailchimp\\">docs</a> for information on how to generate this key."""
    AUTH_TYPE: Final[SourceMailchimpSchemasAuthType] = dataclasses.field(default=SourceMailchimpSchemasAuthType.APIKEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    



class SourceMailchimpAuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailchimpOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""An access token generated using the above client ID and secret."""
    AUTH_TYPE: Final[SourceMailchimpAuthType] = dataclasses.field(default=SourceMailchimpAuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your OAuth application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your OAuth application."""
    



class SourceMailchimpMailchimp(str, Enum):
    MAILCHIMP = 'mailchimp'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailchimp:
    credentials: Optional[SourceMailchimpAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[SourceMailchimpMailchimp] = dataclasses.field(default=SourceMailchimpMailchimp.MAILCHIMP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date from which you want to start syncing data for Incremental streams. Only records that have been created or modified since this date will be synced. If left blank, all data will by synced."""
    


SourceMailchimpAuthentication = Union[SourceMailchimpOAuth20, APIKey]
