"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationCumulio:
    r"""The values required to configure the destination."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""An API key generated in Cumul.io's platform (can be generated here: https://app.cumul.io/start/profile/integration)."""
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""The corresponding API token generated in Cumul.io's platform (can be generated here: https://app.cumul.io/start/profile/integration)."""
    DESTINATION_TYPE: Final[str] = dataclasses.field(default='cumulio', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    api_host: Optional[str] = dataclasses.field(default='https://api.cumul.io', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_host'), 'exclude': lambda f: f is None }})
    r"""URL of the Cumul.io API (e.g. 'https://api.cumul.io', 'https://api.us.cumul.io', or VPC-specific API url). Defaults to 'https://api.cumul.io'."""
    

