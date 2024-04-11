"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Xkcd(str, Enum):
    XKCD = 'xkcd'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceXkcd:
    SOURCE_TYPE: Final[Optional[Xkcd]] = dataclasses.field(default=Xkcd.XKCD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    
