"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Outreach(str, Enum):
    OUTREACH = 'outreach'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceOutreach:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Outreach developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Outreach developer application."""
    redirect_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('redirect_uri') }})
    r"""A Redirect URI is the location where the authorization server sends the user once the app has been successfully authorized and granted an authorization code or access token."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The token for obtaining the new access token."""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The date from which you'd like to replicate data for Outreach API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    SOURCE_TYPE: Final[Outreach] = dataclasses.field(default=Outreach.OUTREACH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
