"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .scheduletypeenum import ScheduleTypeEnum
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AirbyteAPIConnectionSchedule:
    r"""schedule for when the the connection should run, per the schedule type"""
    schedule_type: ScheduleTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleType') }})
    cron_expression: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cronExpression'), 'exclude': lambda f: f is None }})
    

