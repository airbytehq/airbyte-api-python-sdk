"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class SourceGooglePagespeedInsightsCategories(str, Enum):
    ACCESSIBILITY = 'accessibility'
    BEST_PRACTICES = 'best-practices'
    PERFORMANCE = 'performance'
    PWA = 'pwa'
    SEO = 'seo'

class SourceGooglePagespeedInsightsGooglePagespeedInsights(str, Enum):
    GOOGLE_PAGESPEED_INSIGHTS = 'google-pagespeed-insights'

class SourceGooglePagespeedInsightsStrategies(str, Enum):
    DESKTOP = 'desktop'
    MOBILE = 'mobile'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGooglePagespeedInsights:
    r"""The values required to configure the source."""
    
    categories: list[SourceGooglePagespeedInsightsCategories] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('categories') }})
    r"""Defines which Lighthouse category to run. One or many of: \\"accessibility\\", \\"best-practices\\", \\"performance\\", \\"pwa\\", \\"seo\\"."""
    source_type: SourceGooglePagespeedInsightsGooglePagespeedInsights = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    strategies: list[SourceGooglePagespeedInsightsStrategies] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strategies') }})
    r"""The analyses strategy to use. Either \\"desktop\\" or \\"mobile\\"."""
    urls: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('urls') }})
    r"""The URLs to retrieve pagespeed information from. The connector will attempt to sync PageSpeed reports for all the defined URLs. Format: https://(www.)url.domain"""
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    r"""Google PageSpeed API Key. See <a href=\\"https://developers.google.com/speed/docs/insights/v5/get-started#APIKey\\">here</a>. The key is optional - however the API is heavily rate limited when using without API Key. Creating and using the API key therefore is recommended. The key is case sensitive."""
    