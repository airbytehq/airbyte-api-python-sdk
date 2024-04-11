"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleAdsCredentials:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The Client ID of your Google Ads developer application. For detailed instructions on finding this value, refer to our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">documentation</a>."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The Client Secret of your Google Ads developer application. For detailed instructions on finding this value, refer to our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">documentation</a>."""
    developer_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('developer_token'), 'exclude': lambda f: f is None }})
    r"""The Developer Token granted by Google to use their APIs. For detailed instructions on finding this value, refer to our <a href=\\"https://docs.airbyte.com/integrations/sources/google-ads#setup-guide\\">documentation</a>."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleAds:
    credentials: Optional[GoogleAdsCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

