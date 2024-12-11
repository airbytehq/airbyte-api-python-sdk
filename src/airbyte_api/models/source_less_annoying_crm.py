"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final


class LessAnnoyingCrm(str, Enum):
    LESS_ANNOYING_CRM = 'less-annoying-crm'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceLessAnnoyingCrm:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API key to use. Manage and create your API keys on the Programmer API settings page at https://account.lessannoyingcrm.com/app/Settings/Api."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[LessAnnoyingCrm] = dataclasses.field(default=LessAnnoyingCrm.LESS_ANNOYING_CRM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

