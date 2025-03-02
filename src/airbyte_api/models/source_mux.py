"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class Mux(str, Enum):
    MUX = 'mux'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMux:
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    playback_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('playback_id'), 'exclude': lambda f: f is None }})
    r"""The playback id for your video asset shown in website details"""
    SOURCE_TYPE: Final[Mux] = dataclasses.field(default=Mux.MUX, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

