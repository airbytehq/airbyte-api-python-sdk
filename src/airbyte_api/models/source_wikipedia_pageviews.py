"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final


class WikipediaPageviews(str, Enum):
    WIKIPEDIA_PAGEVIEWS = 'wikipedia-pageviews'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceWikipediaPageviews:
    access: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access') }})
    r"""If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access."""
    agent: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('agent') }})
    r"""If you want to filter by agent type, use one of user, automated or spider. If you are interested in pageviews regardless of agent type, use all-agents."""
    article: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('article') }})
    r"""The title of any article in the specified project. Any spaces should be replaced with underscores. It also should be URI-encoded, so that non-URI-safe characters like %, / or ? are accepted."""
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""The ISO 3166-1 alpha-2 code of a country for which to retrieve top articles."""
    end: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end') }})
    r"""The date of the last day to include, in YYYYMMDD or YYYYMMDDHH format."""
    project: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project') }})
    r"""If you want to filter by project, use the domain of any Wikimedia project."""
    start: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start') }})
    r"""The date of the first day to include, in YYYYMMDD or YYYYMMDDHH format. Also serves as the date to retrieve data for the top articles."""
    SOURCE_TYPE: Final[WikipediaPageviews] = dataclasses.field(default=WikipediaPageviews.WIKIPEDIA_PAGEVIEWS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

