"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class TvmazeSchedule(str, Enum):
    TVMAZE_SCHEDULE = 'tvmaze-schedule'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTvmazeSchedule:
    domestic_schedule_country_code: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domestic_schedule_country_code') }})
    r"""Country code for domestic TV schedule retrieval."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Start date for TV schedule retrieval. May be in the future."""
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""End date for TV schedule retrieval. May be in the future. Optional."""
    SOURCE_TYPE: Final[TvmazeSchedule] = dataclasses.field(default=TvmazeSchedule.TVMAZE_SCHEDULE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    web_schedule_country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('web_schedule_country_code'), 'exclude': lambda f: f is None }})
    r"""ISO 3166-1 country code for web TV schedule retrieval. Leave blank for
    all countries plus global web channels (e.g. Netflix). Alternatively,
    set to 'global' for just global web channels.
    """
    

