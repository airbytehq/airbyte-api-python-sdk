"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional


class Category(str, Enum):
    r"""The category you want to get top headlines for."""
    BUSINESS = 'business'
    ENTERTAINMENT = 'entertainment'
    GENERAL = 'general'
    HEALTH = 'health'
    SCIENCE = 'science'
    SPORTS = 'sports'
    TECHNOLOGY = 'technology'


class Country(str, Enum):
    r"""The 2-letter ISO 3166-1 code of the country you want to get headlines
    for. You can't mix this with the sources parameter.
    """
    AE = 'ae'
    AR = 'ar'
    AT = 'at'
    AU = 'au'
    BE = 'be'
    BG = 'bg'
    BR = 'br'
    CA = 'ca'
    CH = 'ch'
    CN = 'cn'
    CO = 'co'
    CU = 'cu'
    CZ = 'cz'
    DE = 'de'
    EG = 'eg'
    FR = 'fr'
    GB = 'gb'
    GR = 'gr'
    HK = 'hk'
    HU = 'hu'
    ID = 'id'
    IE = 'ie'
    IL = 'il'
    IN = 'in'
    IT = 'it'
    JP = 'jp'
    KR = 'kr'
    LT = 'lt'
    LV = 'lv'
    MA = 'ma'
    MX = 'mx'
    MY = 'my'
    NG = 'ng'
    NL = 'nl'
    NO = 'no'
    NZ = 'nz'
    PH = 'ph'
    PL = 'pl'
    PT = 'pt'
    RO = 'ro'
    RS = 'rs'
    RU = 'ru'
    SA = 'sa'
    SE = 'se'
    SG = 'sg'
    SI = 'si'
    SK = 'sk'
    TH = 'th'
    TR = 'tr'
    TW = 'tw'
    UA = 'ua'
    US = 'us'
    VE = 've'
    ZA = 'za'


class Language(str, Enum):
    r"""The 2-letter ISO-639-1 code of the language you want to get headlines
    for. Possible options: ar de en es fr he it nl no pt ru se ud zh.
    """
    AR = 'ar'
    DE = 'de'
    EN = 'en'
    ES = 'es'
    FR = 'fr'
    HE = 'he'
    IT = 'it'
    NL = 'nl'
    NO = 'no'
    PT = 'pt'
    RU = 'ru'
    SE = 'se'
    UD = 'ud'
    ZH = 'zh'


class SearchIn(str, Enum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    CONTENT = 'content'


class SortBy(str, Enum):
    r"""The order to sort the articles in. Possible options: relevancy,
    popularity, publishedAt.
    """
    RELEVANCY = 'relevancy'
    POPULARITY = 'popularity'
    PUBLISHED_AT = 'publishedAt'


class NewsAPI(str, Enum):
    NEWS_API = 'news-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceNewsAPI:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    category: Optional[Category] = dataclasses.field(default=Category.BUSINESS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('category'), 'exclude': lambda f: f is None }})
    r"""The category you want to get top headlines for."""
    country: Optional[Country] = dataclasses.field(default=Country.US, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""The 2-letter ISO 3166-1 code of the country you want to get headlines
    for. You can't mix this with the sources parameter.
    """
    domains: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domains'), 'exclude': lambda f: f is None }})
    r"""A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com,
    engadget.com) to restrict the search to.
    """
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""A date and optional time for the newest article allowed. This should
    be in ISO 8601 format.
    """
    exclude_domains: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exclude_domains'), 'exclude': lambda f: f is None }})
    r"""A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com,
    engadget.com) to remove from the results.
    """
    language: Optional[Language] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language'), 'exclude': lambda f: f is None }})
    r"""The 2-letter ISO-639-1 code of the language you want to get headlines
    for. Possible options: ar de en es fr he it nl no pt ru se ud zh.
    """
    search_in: Optional[List[SearchIn]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_in'), 'exclude': lambda f: f is None }})
    r"""Where to apply search query. Possible values are: title, description,
    content.
    """
    search_query: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('search_query'), 'exclude': lambda f: f is None }})
    r"""Search query. See https://newsapi.org/docs/endpoints/everything for
    information.
    """
    sort_by: Optional[SortBy] = dataclasses.field(default=SortBy.PUBLISHED_AT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort_by'), 'exclude': lambda f: f is None }})
    r"""The order to sort the articles in. Possible options: relevancy,
    popularity, publishedAt.
    """
    SOURCE_TYPE: Final[NewsAPI] = dataclasses.field(default=NewsAPI.NEWS_API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    sources: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sources'), 'exclude': lambda f: f is None }})
    r"""Identifiers (maximum 20) for the news sources or blogs you want
    headlines from. Use the `/sources` endpoint to locate these
    programmatically or look at the sources index:
    https://newsapi.com/sources. Will override both country and category.
    """
    start_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""A date and optional time for the oldest article allowed. This should
    be in ISO 8601 format.
    """
    

