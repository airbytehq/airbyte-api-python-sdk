"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class Mailerlite(str, Enum):
    MAILERLITE = 'mailerlite'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailerlite:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""Your API Token. See <a href=\\"https://developers.mailerlite.com/docs/#authentication\\">here</a>."""
    SOURCE_TYPE: Final[Mailerlite] = dataclasses.field(default=Mailerlite.MAILERLITE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

