"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional


class PlaidEnvironment(str, Enum):
    r"""The Plaid environment."""
    SANDBOX = 'sandbox'
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'


class Plaid(str, Enum):
    PLAID = 'plaid'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePlaid:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The end-user's Link access token."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The Plaid API key to use to hit the API."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Plaid client id."""
    plaid_env: PlaidEnvironment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plaid_env') }})
    r"""The Plaid environment."""
    SOURCE_TYPE: Final[Plaid] = dataclasses.field(default=Plaid.PLAID, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date from which you'd like to replicate data for Plaid in the format YYYY-MM-DD. All data generated after this date will be replicated."""
    

