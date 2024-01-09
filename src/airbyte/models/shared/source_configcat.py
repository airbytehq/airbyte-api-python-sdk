"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Configcat(str, Enum):
    CONFIGCAT = 'configcat'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceConfigcat:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Basic auth password. See <a href=\\"https://api.configcat.com/docs/#section/Authentication\\">here</a>."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Basic auth user name. See <a href=\\"https://api.configcat.com/docs/#section/Authentication\\">here</a>."""
    SOURCE_TYPE: Final[Configcat] = dataclasses.field(default=Configcat.CONFIGCAT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

