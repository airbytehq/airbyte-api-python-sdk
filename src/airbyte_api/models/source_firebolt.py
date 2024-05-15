"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Firebolt(str, Enum):
    FIREBOLT = 'firebolt'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFirebolt:
    account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account') }})
    r"""Firebolt account to login."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Firebolt service account ID."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Firebolt secret, corresponding to the service account ID."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The database to connect to."""
    engine: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('engine') }})
    r"""Engine name to connect to."""
    host: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host'), 'exclude': lambda f: f is None }})
    r"""The host name of your Firebolt database."""
    SOURCE_TYPE: Final[Firebolt] = dataclasses.field(default=Firebolt.FIREBOLT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

