"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional


class SourceStravaAuthType(str, Enum):
    CLIENT = 'Client'


class Strava(str, Enum):
    STRAVA = 'strava'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceStrava:
    athlete_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('athlete_id') }})
    r"""The Athlete ID of your Strava developer application."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Strava developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Strava developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The Refresh Token with the activity: read_all permissions."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time. Any data before this date will not be replicated."""
    AUTH_TYPE: Final[Optional[SourceStravaAuthType]] = dataclasses.field(default=SourceStravaAuthType.CLIENT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    SOURCE_TYPE: Final[Strava] = dataclasses.field(default=Strava.STRAVA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

