"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class GroupBy(str, Enum):
    r"""Category term for grouping the search results"""
    NETWORK = 'network'
    PRODUCT = 'product'
    COUNTRY = 'country'
    DATE = 'date'


class Appfigures(str, Enum):
    APPFIGURES = 'appfigures'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAppfigures:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    group_by: Optional[GroupBy] = dataclasses.field(default=GroupBy.PRODUCT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_by'), 'exclude': lambda f: f is None }})
    r"""Category term for grouping the search results"""
    search_store: Optional[str] = dataclasses.field(default='apple', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_store'), 'exclude': lambda f: f is None }})
    r"""The store which needs to be searched in streams"""
    SOURCE_TYPE: Final[Appfigures] = dataclasses.field(default=Appfigures.APPFIGURES, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
