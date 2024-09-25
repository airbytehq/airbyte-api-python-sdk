"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class Productboard(str, Enum):
    PRODUCTBOARD = 'productboard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceProductboard:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Your Productboard access token. See https://developer.productboard.com/reference/authentication for steps to generate one."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[Productboard] = dataclasses.field(default=Productboard.PRODUCTBOARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

