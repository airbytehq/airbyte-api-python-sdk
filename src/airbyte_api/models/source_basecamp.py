"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class Basecamp(str, Enum):
    BASECAMP = 'basecamp'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBasecamp:
    account_id: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    client_refresh_token_2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_refresh_token_2') }})
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[Basecamp] = dataclasses.field(default=Basecamp.BASECAMP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

