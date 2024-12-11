"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Bigmailer(str, Enum):
    BIGMAILER = 'bigmailer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBigmailer:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. You can create and find it on the API key management page in your BigMailer account."""
    SOURCE_TYPE: Final[Bigmailer] = dataclasses.field(default=Bigmailer.BIGMAILER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

