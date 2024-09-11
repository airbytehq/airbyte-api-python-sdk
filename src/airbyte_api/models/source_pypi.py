"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class Pypi(str, Enum):
    PYPI = 'pypi'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePypi:
    project_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_name') }})
    r"""Name of the project/package. Can only be in lowercase with hyphen. This is the name used using pip command for installing the package."""
    SOURCE_TYPE: Final[Pypi] = dataclasses.field(default=Pypi.PYPI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    r"""Version of the project/package.  Use it to find a particular release instead of all releases."""
    

