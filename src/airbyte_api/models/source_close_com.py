"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional

class CloseCom(str, Enum):
    CLOSE_COM = 'close-com'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCloseCom:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Close.com API key (usually starts with 'api_'; find yours <a href=\\"https://app.close.com/settings/api/\\">here</a>)."""
    SOURCE_TYPE: Final[CloseCom] = dataclasses.field(default=CloseCom.CLOSE_COM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2021-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The start date to sync data; all data after this date will be replicated. Leave blank to retrieve all the data available in the account. Format: YYYY-MM-DD."""
    

