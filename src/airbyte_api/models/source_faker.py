"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Faker(str, Enum):
    FAKER = 'faker'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceFaker:
    always_updated: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('always_updated'), 'exclude': lambda f: f is None }})
    r"""Should the updated_at values for every record be new each sync?  Setting this to false will case the source to stop emitting records after COUNT records have been emitted."""
    count: Optional[int] = dataclasses.field(default=1000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count'), 'exclude': lambda f: f is None }})
    r"""How many users should be generated in total. The purchases table will be scaled to match, with 10 purchases created per 10 users. This setting does not apply to the products stream."""
    parallelism: Optional[int] = dataclasses.field(default=4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parallelism'), 'exclude': lambda f: f is None }})
    r"""How many parallel workers should we use to generate fake data?  Choose a value equal to the number of CPUs you will allocate to this source."""
    records_per_slice: Optional[int] = dataclasses.field(default=1000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('records_per_slice'), 'exclude': lambda f: f is None }})
    r"""How many fake records will be in each page (stream slice), before a state message is emitted?"""
    seed: Optional[int] = dataclasses.field(default=-1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is None }})
    r"""Manually control the faker random seed to return the same values on subsequent runs (leave -1 for random)"""
    SOURCE_TYPE: Final[Faker] = dataclasses.field(default=Faker.FAKER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
