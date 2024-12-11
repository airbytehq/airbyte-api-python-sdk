"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Motherduck(str, Enum):
    MOTHERDUCK = 'motherduck'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMotherduck:
    motherduck_api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('motherduck_api_key') }})
    r"""API access token to use for authentication to a MotherDuck database."""
    DESTINATION_TYPE: Final[Motherduck] = dataclasses.field(default=Motherduck.MOTHERDUCK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    destination_path: Optional[str] = dataclasses.field(default='md:', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_path'), 'exclude': lambda f: f is None }})
    r"""Path to a .duckdb file or 'md:<DATABASE_NAME>' to connect to a MotherDuck database. If 'md:' is specified without a database name, the default MotherDuck database name ('my_db') will be used."""
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""Database schema name, defaults to 'main' if not specified."""
    

