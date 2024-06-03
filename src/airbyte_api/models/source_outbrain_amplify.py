"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class BothUsernameAndPasswordIsRequiredForAuthenticationRequest(str, Enum):
    USERNAME_PASSWORD = 'username_password'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOutbrainAmplifyUsernamePassword:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Add Password for authentication."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Add Username for authentication."""
    TYPE: Final[BothUsernameAndPasswordIsRequiredForAuthenticationRequest] = dataclasses.field(default=BothUsernameAndPasswordIsRequiredForAuthenticationRequest.USERNAME_PASSWORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    



class AccessTokenIsRequiredForAuthenticationRequests(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOutbrainAmplifyAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    TYPE: Final[AccessTokenIsRequiredForAuthenticationRequests] = dataclasses.field(default=AccessTokenIsRequiredForAuthenticationRequests.ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    


SourceOutbrainAmplifyAuthenticationMethod = Union['SourceOutbrainAmplifyAccessToken', 'SourceOutbrainAmplifyUsernamePassword']


class GranularityForGeoLocationRegion(str, Enum):
    r"""The granularity used for geo location data in reports."""
    COUNTRY = 'country'
    REGION = 'region'
    SUBREGION = 'subregion'


class GranularityForPeriodicReports(str, Enum):
    r"""The granularity used for periodic data in reports. See <a href=\\"https://amplifyv01.docs.apiary.io/#reference/performance-reporting/periodic/retrieve-performance-statistics-for-all-marketer-campaigns-by-periodic-breakdown\\">the docs</a>."""
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'


class OutbrainAmplify(str, Enum):
    OUTBRAIN_AMPLIFY = 'outbrain-amplify'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOutbrainAmplify:
    credentials: SourceOutbrainAmplifyAuthenticationMethod = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Credentials for making authenticated requests requires either username/password or access_token."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Date in the format YYYY-MM-DD eg. 2017-01-25. Any data before this date will not be replicated."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""Date in the format YYYY-MM-DD."""
    geo_location_breakdown: Optional[GranularityForGeoLocationRegion] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geo_location_breakdown'), 'exclude': lambda f: f is None }})
    r"""The granularity used for geo location data in reports."""
    report_granularity: Optional[GranularityForPeriodicReports] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report_granularity'), 'exclude': lambda f: f is None }})
    r"""The granularity used for periodic data in reports. See <a href=\\"https://amplifyv01.docs.apiary.io/#reference/performance-reporting/periodic/retrieve-performance-statistics-for-all-marketer-campaigns-by-periodic-breakdown\\">the docs</a>."""
    SOURCE_TYPE: Final[OutbrainAmplify] = dataclasses.field(default=OutbrainAmplify.OUTBRAIN_AMPLIFY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

