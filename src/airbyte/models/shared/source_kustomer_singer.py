"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum

class SourceKustomerSingerKustomerSingerEnum(str, Enum):
    KUSTOMER_SINGER = 'kustomer-singer'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKustomerSinger:
    r"""The values required to configure the source."""
    
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})

    r"""Kustomer API Token. See the <a href=\\"https://developer.kustomer.com/kustomer-api-docs/reference/authentication\\">docs</a> on how to obtain this"""
    source_type: SourceKustomerSingerKustomerSingerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})

    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})

    r"""The date from which you'd like to replicate the data"""
    