"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class BambooHr(str, Enum):
    BAMBOO_HR = 'bamboo-hr'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBambooHr:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Api key of bamboo hr"""
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    r"""Sub Domain of bamboo hr"""
    SOURCE_TYPE: Final[BambooHr] = dataclasses.field(default=BambooHr.BAMBOO_HR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    custom_reports_fields: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports_fields'), 'exclude': lambda f: f is None }})
    r"""Comma-separated list of fields to include in custom reports."""
    custom_reports_include_default_fields: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports_include_default_fields'), 'exclude': lambda f: f is None }})
    r"""If true, the custom reports endpoint will include the default fields defined here: https://documentation.bamboohr.com/docs/list-of-field-names."""
    

