"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class RkiCovid(str, Enum):
    RKI_COVID = 'rki-covid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRkiCovid:
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date in the format 2017-01-25. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[RkiCovid] = dataclasses.field(default=RkiCovid.RKI_COVID, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

