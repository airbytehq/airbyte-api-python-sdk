"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceGoogleDirectorySchemasCredentialsTitle(str, Enum):
    r"""Authentication Scenario"""
    SERVICE_ACCOUNTS = 'Service accounts'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServiceAccountKey:
    r"""For these scenario user should obtain service account's credentials from the Google API Console and provide delegated email."""
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    r"""The contents of the JSON service account key. See the <a href=\\"https://developers.google.com/admin-sdk/directory/v1/guides/delegation\\">docs</a> for more information on how to generate this key."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The email of the user, which has permissions to access the Google Workspace Admin APIs."""
    CREDENTIALS_TITLE: Final[Optional[SourceGoogleDirectorySchemasCredentialsTitle]] = dataclasses.field(default=SourceGoogleDirectorySchemasCredentialsTitle.SERVICE_ACCOUNTS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    r"""Authentication Scenario"""
    



class SourceGoogleDirectoryCredentialsTitle(str, Enum):
    r"""Authentication Scenario"""
    WEB_SERVER_APP = 'Web server app'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SignInViaGoogleOAuth:
    r"""For these scenario user only needs to give permission to read Google Directory data."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of the developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of the developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The Token for obtaining a new access token."""
    CREDENTIALS_TITLE: Final[Optional[SourceGoogleDirectoryCredentialsTitle]] = dataclasses.field(default=SourceGoogleDirectoryCredentialsTitle.WEB_SERVER_APP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_title'), 'exclude': lambda f: f is None }})
    r"""Authentication Scenario"""
    



class GoogleDirectory(str, Enum):
    GOOGLE_DIRECTORY = 'google-directory'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGoogleDirectory:
    credentials: Optional[SourceGoogleDirectoryGoogleCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Google APIs use the OAuth 2.0 protocol for authentication and authorization. The Source supports <a href=\\"https://developers.google.com/identity/protocols/oauth2#webserver\\" target=\\"_blank\\">Web server application</a> and <a href=\\"https://developers.google.com/identity/protocols/oauth2#serviceaccount\\" target=\\"_blank\\">Service accounts</a> scenarios."""
    SOURCE_TYPE: Final[GoogleDirectory] = dataclasses.field(default=GoogleDirectory.GOOGLE_DIRECTORY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


SourceGoogleDirectoryGoogleCredentials = Union[SignInViaGoogleOAuth, ServiceAccountKey]
