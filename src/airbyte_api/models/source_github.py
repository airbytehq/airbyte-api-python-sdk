"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional, Union


class SourceGithubOptionTitle(str, Enum):
    PAT_CREDENTIALS = 'PAT Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGithubPersonalAccessToken:
    personal_access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('personal_access_token') }})
    r"""Log into GitHub and then generate a <a href=\\"https://github.com/settings/tokens\\">personal access token</a>. To load balance your API quota consumption across multiple API tokens, input multiple tokens separated with \\",\\" """
    OPTION_TITLE: Final[Optional[SourceGithubOptionTitle]] = dataclasses.field(default=SourceGithubOptionTitle.PAT_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    



class OptionTitle(str, Enum):
    O_AUTH_CREDENTIALS = 'OAuth Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OAuth:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""OAuth access token"""
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""OAuth Client Id"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""OAuth Client secret"""
    OPTION_TITLE: Final[Optional[OptionTitle]] = dataclasses.field(default=OptionTitle.O_AUTH_CREDENTIALS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title'), 'exclude': lambda f: f is None }})
    


SourceGithubAuthentication = Union['OAuth', 'SourceGithubPersonalAccessToken']


class SourceGithubGithub(str, Enum):
    GITHUB = 'github'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGithub:
    credentials: SourceGithubAuthentication = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Choose how to authenticate to GitHub"""
    repositories: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repositories') }})
    r"""List of GitHub organizations/repositories, e.g. `airbytehq/airbyte` for single repository, `airbytehq/*` for get all repositories from organization and `airbytehq/a* for matching multiple repositories by pattern."""
    api_url: Optional[str] = dataclasses.field(default='https://api.github.com/', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_url'), 'exclude': lambda f: f is None }})
    r"""Please enter your basic URL from self-hosted GitHub instance or leave it empty to use GitHub."""
    branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branch'), 'exclude': lambda f: f is None }})
    r"""(DEPRCATED) Space-delimited list of GitHub repository branches to pull commits for, e.g. `airbytehq/airbyte/master`. If no branches are specified for a repository, the default branch will be pulled."""
    branches: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('branches'), 'exclude': lambda f: f is None }})
    r"""List of GitHub repository branches to pull commits for, e.g. `airbytehq/airbyte/master`. If no branches are specified for a repository, the default branch will be pulled."""
    max_waiting_time: Optional[int] = dataclasses.field(default=10, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_waiting_time'), 'exclude': lambda f: f is None }})
    r"""Max Waiting Time for rate limit. Set higher value to wait till rate limits will be resetted to continue sync"""
    repository: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repository'), 'exclude': lambda f: f is None }})
    r"""(DEPRCATED) Space-delimited list of GitHub organizations/repositories, e.g. `airbytehq/airbyte` for single repository, `airbytehq/*` for get all repositories from organization and `airbytehq/airbyte airbytehq/another-repo` for multiple repositories."""
    SOURCE_TYPE: Final[SourceGithubGithub] = dataclasses.field(default=SourceGithubGithub.GITHUB, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date from which you'd like to replicate data from GitHub in the format YYYY-MM-DDT00:00:00Z. If the date is not set, all data will be replicated.  For the streams which support this configuration, only data generated on or after the start date will be replicated. This field doesn't apply to all streams, see the <a href=\\"https://docs.airbyte.com/integrations/sources/github\\">docs</a> for more info"""
    

