"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class Gorgias(str, Enum):
    GORGIAS = 'gorgias'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGorgias:
    domain_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_name') }})
    r"""Domain name given for gorgias, found as your url prefix for accessing your website"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Gorgias] = dataclasses.field(default=Gorgias.GORGIAS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

