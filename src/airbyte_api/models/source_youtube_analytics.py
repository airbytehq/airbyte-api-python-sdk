"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Dict, Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaOAuth20:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your developer application"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The client secret of your developer application"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""A refresh token generated using the above client ID and secret"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



class SourceYoutubeAnalyticsYoutubeAnalytics(str, Enum):
    YOUTUBE_ANALYTICS = 'youtube-analytics'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceYoutubeAnalytics:
    credentials: AuthenticateViaOAuth20 = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    SOURCE_TYPE: Final[SourceYoutubeAnalyticsYoutubeAnalytics] = dataclasses.field(default=SourceYoutubeAnalyticsYoutubeAnalytics.YOUTUBE_ANALYTICS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

