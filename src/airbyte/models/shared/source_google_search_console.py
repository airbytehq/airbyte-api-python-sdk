"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Any, Optional

class SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = 'Service'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthentication:
    
    auth_type: SourceGoogleSearchConsoleAuthorizationServiceAccountKeyAuthenticationAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})

    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})

    r"""The email of the user which has permissions to access the Google Workspace Admin APIs."""
    service_account_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_info') }})

    r"""The JSON key of the service account to use for authorization. Read more <a href=\\"https://cloud.google.com/iam/docs/creating-managing-service-account-keys\\">here</a>."""
    
class SourceGoogleSearchConsoleAuthorizationOAuthAuthTypeEnum(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsoleAuthorizationOAuth:
    
    auth_type: SourceGoogleSearchConsoleAuthorizationOAuthAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})

    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})

    r"""The client ID of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})

    r"""The client secret of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})

    r"""The token for obtaining a new access token. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    access_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token'), 'exclude': lambda f: f is None }})

    r"""Access token for making authenticated requests. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    
class SourceGoogleSearchConsoleGoogleSearchConsoleEnum(str, Enum):
    GOOGLE_SEARCH_CONSOLE = 'google-search-console'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSearchConsole:
    r"""The values required to configure the source."""
    
    authorization: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})

    site_urls: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_urls') }})

    r"""The URLs of the website property attached to your GSC account. Read more <a href=\\"https://support.google.com/webmasters/answer/34592?hl=en\\">here</a>."""
    source_type: SourceGoogleSearchConsoleGoogleSearchConsoleEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})

    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})

    r"""UTC date in the format 2017-01-25. Any data before this date will not be replicated."""
    custom_reports: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})

    r"""A JSON array describing the custom reports you want to sync from Google Search Console. See <a href=\\"https://docs.airbyte.com/integrations/sources/google-search-console#step-2-set-up-the-google-search-console-connector-in-airbyte\\">the docs</a> for more information about the exact format you can use to fill out this field."""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})

    r"""UTC date in the format 2017-01-25. Any data after this date will not be replicated. Must be greater or equal to the start date field."""
    