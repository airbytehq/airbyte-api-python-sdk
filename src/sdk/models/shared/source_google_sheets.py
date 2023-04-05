"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional

class SourceGoogleSheetsCredentialsServiceAccountKeyAuthenticationAuthTypeEnum(str, Enum):
    SERVICE = 'Service'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheetsCredentialsServiceAccountKeyAuthentication:
    r"""Credentials for connecting to the Google Sheets API"""
    
    auth_type: SourceGoogleSheetsCredentialsServiceAccountKeyAuthenticationAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})  
    service_account_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account_info') }})
    r"""Enter your Google Cloud <a href=\\"https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys\\">service account key</a> in JSON format"""  
    
class SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuthAuthTypeEnum(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuth:
    r"""Credentials for connecting to the Google Sheets API"""
    
    auth_type: SourceGoogleSheetsCredentialsAuthenticateViaGoogleOAuthAuthTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})  
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Enter your Google application's Client ID"""  
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Enter your Google application's Client Secret"""  
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Enter your Google application's refresh token"""  
    
class SourceGoogleSheetsGoogleSheetsEnum(str, Enum):
    GOOGLE_SHEETS = 'google-sheets'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleSheets:
    r"""The values required to configure the source."""
    
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Credentials for connecting to the Google Sheets API"""  
    source_type: SourceGoogleSheetsGoogleSheetsEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    spreadsheet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spreadsheet_id') }})
    r"""Enter the link to the Google spreadsheet you want to sync"""  
    row_batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('row_batch_size'), 'exclude': lambda f: f is None }})
    r"""Number of rows fetched when making a Google Sheet API call. Defaults to 200."""  
    