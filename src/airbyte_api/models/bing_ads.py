"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BingAds:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your Microsoft Advertising developer application."""
    client_secret: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your Microsoft Advertising developer application."""
    
