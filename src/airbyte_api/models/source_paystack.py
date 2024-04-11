"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Paystack(str, Enum):
    PAYSTACK = 'paystack'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePaystack:
    secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_key') }})
    r"""The Paystack API key (usually starts with 'sk_live_'; find yours <a href=\\"https://dashboard.paystack.com/#/settings/developer\\">here</a>)."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    lookback_window_days: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    r"""When set, the connector will always reload data from the past N days, where N is the value set here. This is useful if your data is updated after creation."""
    SOURCE_TYPE: Final[Paystack] = dataclasses.field(default=Paystack.PAYSTACK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
