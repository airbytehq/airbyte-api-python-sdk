"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class SourceLeverHiringCredentialsAuthenticateViaLeverAPIKeyAuthType(str, Enum):
    API_KEY = 'Api Key'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLeverHiringCredentialsAuthenticateViaLeverAPIKey:
    r"""Choose how to authenticate to Lever Hiring."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The Api Key of your Lever Hiring account."""
    auth_type: Optional[SourceLeverHiringCredentialsAuthenticateViaLeverAPIKeyAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceLeverHiringCredentialsAuthenticateViaLeverOAuthAuthType(str, Enum):
    CLIENT = 'Client'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLeverHiringCredentialsAuthenticateViaLeverOAuth:
    r"""Choose how to authenticate to Lever Hiring."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining new access token."""
    auth_type: Optional[SourceLeverHiringCredentialsAuthenticateViaLeverOAuthAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your Lever Hiring developer application."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your Lever Hiring developer application."""
    


class SourceLeverHiringEnvironment(str, Enum):
    r"""The environment in which you'd like to replicate data for Lever. This is used to determine which Lever API endpoint to use."""
    PRODUCTION = 'Production'
    SANDBOX = 'Sandbox'

class SourceLeverHiringLeverHiring(str, Enum):
    LEVER_HIRING = 'lever-hiring'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceLeverHiring:
    r"""The values required to configure the source."""
    source_type: SourceLeverHiringLeverHiring = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated. Note that it will be used only in the following incremental streams: comments, commits, and issues."""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate to Lever Hiring."""
    environment: Optional[SourceLeverHiringEnvironment] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""The environment in which you'd like to replicate data for Lever. This is used to determine which Lever API endpoint to use."""
    
