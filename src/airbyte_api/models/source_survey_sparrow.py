"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Final, List, Optional, Union


class SourceSurveySparrowURLBase(str, Enum):
    HTTPS_API_SURVEYSPARROW_COM_V3 = 'https://api.surveysparrow.com/v3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GlobalAccount:
    URL_BASE: Final[Optional[SourceSurveySparrowURLBase]] = dataclasses.field(default=SourceSurveySparrowURLBase.HTTPS_API_SURVEYSPARROW_COM_V3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    



class URLBase(str, Enum):
    HTTPS_EU_API_SURVEYSPARROW_COM_V3 = 'https://eu-api.surveysparrow.com/v3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EUBasedAccount:
    URL_BASE: Final[Optional[URLBase]] = dataclasses.field(default=URLBase.HTTPS_EU_API_SURVEYSPARROW_COM_V3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_base'), 'exclude': lambda f: f is None }})
    



class SurveySparrow(str, Enum):
    SURVEY_SPARROW = 'survey-sparrow'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSurveySparrow:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Your access token. See <a href=\\"https://developers.surveysparrow.com/rest-apis#authentication\\">here</a>. The key is case sensitive."""
    region: Optional[BaseURL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region'), 'exclude': lambda f: f is None }})
    r"""Is your account location is EU based? If yes, the base url to retrieve data will be different."""
    SOURCE_TYPE: Final[SurveySparrow] = dataclasses.field(default=SurveySparrow.SURVEY_SPARROW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    survey_id: Optional[List[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('survey_id'), 'exclude': lambda f: f is None }})
    r"""A List of your survey ids for survey-specific stream"""
    


BaseURL = Union[EUBasedAccount, GlobalAccount]
