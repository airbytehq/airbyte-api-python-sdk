"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Paperform(str, Enum):
    PAPERFORM = 'paperform'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePaperform:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. Generate it on your account page at https://paperform.co/account/developer."""
    SOURCE_TYPE: Final[Paperform] = dataclasses.field(default=Paperform.PAPERFORM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
