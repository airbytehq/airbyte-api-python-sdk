"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class Teamwork(str, Enum):
    TEAMWORK = 'teamwork'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTeamwork:
    site_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_name') }})
    r"""The teamwork site name appearing at the url"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Teamwork] = dataclasses.field(default=Teamwork.TEAMWORK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
