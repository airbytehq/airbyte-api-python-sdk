"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Final, List, Optional


class Clockodo(str, Enum):
    CLOCKODO = 'clockodo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceClockodo:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. Find it in the 'Personal data' section of your Clockodo account."""
    email_address: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_address') }})
    r"""Your Clockodo account email address. Find it in your Clockodo account settings."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    years: List[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('years') }})
    r"""2024, 2025"""
    external_application: Optional[str] = dataclasses.field(default='Airbyte', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_application'), 'exclude': lambda f: f is None }})
    r"""Identification of the calling application, including the email address of a technical contact person. Format: [name of application or company];[email address]."""
    SOURCE_TYPE: Final[Clockodo] = dataclasses.field(default=Clockodo.CLOCKODO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

