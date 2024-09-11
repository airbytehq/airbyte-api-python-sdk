"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final


class Prestashop(str, Enum):
    PRESTASHOP = 'prestashop'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePrestashop:
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key') }})
    r"""Your PrestaShop access key. See <a href=\\"https://devdocs.prestashop.com/1.7/webservice/tutorials/creating-access/#create-an-access-key\\"> the docs </a> for info on how to obtain this."""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The Start date in the format YYYY-MM-DD."""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""Shop URL without trailing slash."""
    SOURCE_TYPE: Final[Prestashop] = dataclasses.field(default=Prestashop.PRESTASHOP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

