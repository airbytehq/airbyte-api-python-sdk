"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceZuoraZuoraEnum(str, Enum):
    ZUORA = 'zuora'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZuora:
    r"""The values required to configure the source."""
    
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})

    r"""Client ID"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})

    r"""Client Secret"""
    source_type: SourceZuoraZuoraEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})

    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})

    r"""Start Date in format: YYYY-MM-DD"""
    is_sandbox: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})

    r"""Defines whether use the SANDBOX or PRODUCTION environment."""
    window_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('window_in_days'), 'exclude': lambda f: f is None }})

    r"""The amount of days for each data-chunk begining from start_date. Bigger the value - faster the fetch. (Min=1, as for a Day; Max=364, as for a Year)."""
    