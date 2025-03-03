"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Intruder(str, Enum):
    INTRUDER = 'intruder'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIntruder:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Your API Access token. See <a href=\\"https://developers.intruder.io/docs/authentication\\">here</a>."""
    SOURCE_TYPE: Final[Intruder] = dataclasses.field(default=Intruder.INTRUDER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

