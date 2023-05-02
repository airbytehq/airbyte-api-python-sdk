"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceRecurlyRecurlyEnum(str, Enum):
    RECURLY = 'recurly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRecurly:
    r"""The values required to configure the source."""
    
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Recurly API Key. See the  <a href=\\"https://docs.airbyte.com/integrations/sources/recurly\\">docs</a> for more information on how to generate this key."""
    source_type: SourceRecurlyRecurlyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    begin_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('begin_time'), 'exclude': lambda f: f is None }})
    r"""ISO8601 timestamp from which the replication from Recurly API will start from."""
    end_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'exclude': lambda f: f is None }})
    r"""ISO8601 timestamp to which the replication from Recurly API will stop. Records after that date won't be imported."""
    