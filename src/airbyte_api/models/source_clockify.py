"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Clockify(str, Enum):
    CLOCKIFY = 'clockify'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceClockify:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""You can get your api access_key <a href=\\"https://app.clockify.me/user/settings\\">here</a> This API is Case Sensitive."""
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace_id') }})
    r"""WorkSpace Id"""
    api_url: Optional[str] = dataclasses.field(default='https://api.clockify.me', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_url'), 'exclude': lambda f: f is None }})
    r"""The URL for the Clockify API. This should only need to be modified if connecting to an enterprise version of Clockify."""
    SOURCE_TYPE: Final[Clockify] = dataclasses.field(default=Clockify.CLOCKIFY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

