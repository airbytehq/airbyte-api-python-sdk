"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

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
    comic_number: Optional[str] = dataclasses.field(default='2960', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('comic_number'), 'exclude': lambda f: f is None }})
    r"""Specifies the comic number in which details are to be extracted, pagination will begin with that number to end of available comics"""
    SOURCE_TYPE: Final[Optional[Xkcd]] = dataclasses.field(default=Xkcd.XKCD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    

