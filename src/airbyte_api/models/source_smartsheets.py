"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional, Union


class SourceSmartsheetsSchemasAuthType(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class APIAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The access token to use for accessing your data from Smartsheets. This access token must be generated by a user with at least read access to the data you'd like to replicate. Generate an access token in the Smartsheets main menu by clicking Account > Apps & Integrations > API Access. See the <a href=\\"https://docs.airbyte.com/integrations/sources/smartsheets/#setup-guide\\">setup guide</a> for information on how to obtain this token."""
    AUTH_TYPE: Final[Optional[SourceSmartsheetsSchemasAuthType]] = dataclasses.field(default=SourceSmartsheetsSchemasAuthType.ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class SourceSmartsheetsAuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSmartsheetsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The API ID of the SmartSheets developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The API Secret the SmartSheets developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access_token."""
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date-time when the access token should be refreshed."""
    AUTH_TYPE: Final[Optional[SourceSmartsheetsAuthType]] = dataclasses.field(default=SourceSmartsheetsAuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class Validenums(str, Enum):
    SHEETCREATED_AT = 'sheetcreatedAt'
    SHEETID = 'sheetid'
    SHEETMODIFIED_AT = 'sheetmodifiedAt'
    SHEETNAME = 'sheetname'
    SHEETPERMALINK = 'sheetpermalink'
    SHEETVERSION = 'sheetversion'
    SHEETACCESS_LEVEL = 'sheetaccess_level'
    ROW_ID = 'row_id'
    ROW_ACCESS_LEVEL = 'row_access_level'
    ROW_CREATED_AT = 'row_created_at'
    ROW_CREATED_BY = 'row_created_by'
    ROW_EXPANDED = 'row_expanded'
    ROW_MODIFIED_BY = 'row_modified_by'
    ROW_PARENT_ID = 'row_parent_id'
    ROW_PERMALINK = 'row_permalink'
    ROW_NUMBER = 'row_number'
    ROW_VERSION = 'row_version'


class SourceSmartsheetsSmartsheets(str, Enum):
    SMARTSHEETS = 'smartsheets'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSmartsheets:
    credentials: SourceSmartsheetsAuthorizationMethod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    spreadsheet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('spreadsheet_id') }})
    r"""The spreadsheet ID. Find it by opening the spreadsheet then navigating to File > Properties"""
    metadata_fields: Optional[List[Validenums]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata_fields'), 'exclude': lambda f: f is None }})
    r"""A List of available columns which metadata can be pulled from."""
    SOURCE_TYPE: Final[SourceSmartsheetsSmartsheets] = dataclasses.field(default=SourceSmartsheetsSmartsheets.SMARTSHEETS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


SourceSmartsheetsAuthorizationMethod = Union[SourceSmartsheetsOAuth20, APIAccessToken]
