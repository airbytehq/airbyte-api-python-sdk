"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkedinAdsCredentials:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The client ID of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The client secret of your developer application. Refer to our <a href='https://docs.airbyte.com/integrations/sources/linkedin-ads#setup-guide'>documentation</a> for more information."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LinkedinAds:
    credentials: Optional[LinkedinAdsCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

