"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticationViaGoogleOAuth:
    r"""Google API Credentials for connecting to Google Sheets and Google Drive APIs"""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Google Sheets developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Google Sheets developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining new access token."""
    



class DestinationGoogleSheetsGoogleSheets(str, Enum):
    GOOGLE_SHEETS = 'google-sheets'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationGoogleSheets:
    credentials: AuthenticationViaGoogleOAuth = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Google API Credentials for connecting to Google Sheets and Google Drive APIs"""
    spreadsheet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spreadsheet_id') }})
    r"""The link to your spreadsheet. See <a href='https://docs.airbyte.com/integrations/destinations/google-sheets#sheetlink'>this guide</a> for more details."""
    DESTINATION_TYPE: Final[DestinationGoogleSheetsGoogleSheets] = dataclasses.field(default=DestinationGoogleSheetsGoogleSheets.GOOGLE_SHEETS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    

