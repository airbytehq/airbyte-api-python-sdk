"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Glassfrog(str, Enum):
    GLASSFROG = 'glassfrog'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGlassfrog:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key provided by Glassfrog"""
    SOURCE_TYPE: Final[Glassfrog] = dataclasses.field(default=Glassfrog.GLASSFROG, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

