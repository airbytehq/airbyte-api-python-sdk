"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceExchangeRatesExchangeRates(str, Enum):
    EXCHANGE_RATES = 'exchange-rates'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceExchangeRates:
    r"""The values required to configure the source."""
    
    access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key') }})
    r"""Your API Key. See <a href=\\"https://apilayer.com/marketplace/exchangerates_data-api\\">here</a>. The key is case sensitive."""
    source_type: SourceExchangeRatesExchangeRates = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso') }})
    r"""Start getting data from that date."""
    base: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base'), 'exclude': lambda f: f is None }})
    r"""ISO reference currency. See <a href=\\"https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html\\">here</a>. Free plan doesn't support Source Currency Switching, default base currency is EUR"""
    ignore_weekends: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore_weekends'), 'exclude': lambda f: f is None }})
    r"""Ignore weekends? (Exchanges don't run on weekends)"""
    