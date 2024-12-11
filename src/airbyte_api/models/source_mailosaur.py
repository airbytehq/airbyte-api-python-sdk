"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Mailosaur(str, Enum):
    MAILOSAUR = 'mailosaur'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMailosaur:
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Enter \\"api\\" here"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Enter your api key here"""
    SOURCE_TYPE: Final[Mailosaur] = dataclasses.field(default=Mailosaur.MAILOSAUR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

