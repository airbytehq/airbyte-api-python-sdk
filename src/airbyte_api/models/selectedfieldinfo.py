"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SelectedFieldInfo:
    r"""Path to a field/column/property in a stream to be selected. For example, if the field to be selected is a database column called \\"foo\\", this will be [\\"foo\\"]. Use multiple path elements for nested schemas."""
    field_path: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fieldPath'), 'exclude': lambda f: f is None }})
    

