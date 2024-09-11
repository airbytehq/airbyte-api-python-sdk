"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class SpacexAPI(str, Enum):
    SPACEX_API = 'spacex-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSpacexAPI:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('options'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[SpacexAPI] = dataclasses.field(default=SpacexAPI.SPACEX_API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

