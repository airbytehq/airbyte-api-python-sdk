"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Luma(str, Enum):
    LUMA = 'luma'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLuma:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Get your API key on lu.ma Calendars dashboard → Settings."""
    SOURCE_TYPE: Final[Luma] = dataclasses.field(default=Luma.LUMA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

