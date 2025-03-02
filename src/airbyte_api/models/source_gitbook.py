"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Gitbook(str, Enum):
    GITBOOK = 'gitbook'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGitbook:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Personal access token for authenticating with the GitBook API. You can view and manage your access tokens in the Developer settings of your GitBook user account."""
    space_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('space_id') }})
    SOURCE_TYPE: Final[Gitbook] = dataclasses.field(default=Gitbook.GITBOOK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

