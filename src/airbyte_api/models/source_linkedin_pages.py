"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class SourceLinkedinPagesSchemasAuthMethod(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinPagesAccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The token value generated using the LinkedIn Developers OAuth Token Tools. See the <a href=\\"https://docs.airbyte.com/integrations/sources/linkedin-pages/\\">docs</a> to obtain yours."""
    AUTH_METHOD: Final[Optional[SourceLinkedinPagesSchemasAuthMethod]] = dataclasses.field(default=SourceLinkedinPagesSchemasAuthMethod.ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    



class SourceLinkedinPagesAuthMethod(str, Enum):
    O_AUTH2_0 = 'oAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinPagesOAuth20:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The client ID of the LinkedIn developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret of the LinkedIn developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token value generated using the LinkedIn Developers OAuth Token Tools. See the <a href=\\"https://docs.airbyte.com/integrations/sources/linkedin-pages/\\">docs</a> to obtain yours."""
    AUTH_METHOD: Final[Optional[SourceLinkedinPagesAuthMethod]] = dataclasses.field(default=SourceLinkedinPagesAuthMethod.O_AUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    


SourceLinkedinPagesAuthentication = Union['SourceLinkedinPagesOAuth20', 'SourceLinkedinPagesAccessToken']


class LinkedinPages(str, Enum):
    LINKEDIN_PAGES = 'linkedin-pages'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLinkedinPages:
    org_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('org_id') }})
    r"""Specify the Organization ID"""
    credentials: Optional[SourceLinkedinPagesAuthentication] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[LinkedinPages] = dataclasses.field(default=LinkedinPages.LINKEDIN_PAGES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

