"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Optional

class SourceGitlabCredentialsPrivateTokenAuthType(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGitlabCredentialsPrivateToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Log into your Gitlab account and then generate a personal Access Token."""
    auth_type: Optional[SourceGitlabCredentialsPrivateTokenAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceGitlabCredentialsOAuth20AuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGitlabCredentialsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The API ID of the Gitlab developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The API Secret the Gitlab developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access_token."""
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date-time when the access token should be refreshed."""
    auth_type: Optional[SourceGitlabCredentialsOAuth20AuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceGitlabGitlab(str, Enum):
    GITLAB = 'gitlab'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceGitlab:
    r"""The values required to configure the source."""
    credentials: Any = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    source_type: SourceGitlabGitlab = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for GitLab API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    api_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_url'), 'exclude': lambda f: f is None }})
    r"""Please enter your basic URL from GitLab instance."""
    groups: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('groups'), 'exclude': lambda f: f is None }})
    r"""Space-delimited list of groups. e.g. airbyte.io."""
    projects: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    r"""Space-delimited list of projects. e.g. airbyte.io/documentation meltano/tap-gitlab."""
    

