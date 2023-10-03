"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceRkiCovid:
    r"""The values required to configure the source."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""UTC date in the format 2017-01-25. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='rki-covid', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

