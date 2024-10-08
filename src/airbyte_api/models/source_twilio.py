"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class Twilio(str, Enum):
    TWILIO = 'twilio'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTwilio:
    account_sid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_sid') }})
    r"""Twilio account SID"""
    auth_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_token') }})
    r"""Twilio Auth Token."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2020-10-01T00:00:00Z. Any data before this date will not be replicated."""
    lookback_window: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window'), 'exclude': lambda f: f is None }})
    r"""How far into the past to look for records. (in minutes)"""
    SOURCE_TYPE: Final[Twilio] = dataclasses.field(default=Twilio.TWILIO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

