"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class SourceStripeStripe(str, Enum):
    STRIPE = 'stripe'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceStripe:
    r"""The values required to configure the source."""
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Your Stripe account ID (starts with 'acct_', find yours <a href=\\"https://dashboard.stripe.com/settings/account\\">here</a>)."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Stripe API key (usually starts with 'sk_live_'; find yours <a href=\\"https://dashboard.stripe.com/apikeys\\">here</a>)."""
    SOURCE_TYPE: Final[SourceStripeStripe] = dataclasses.field(default=SourceStripeStripe.STRIPE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    lookback_window_days: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window_days'), 'exclude': lambda f: f is None }})
    r"""When set, the connector will always re-export data from the past N days, where N is the value set here. This is useful if your data is frequently updated after creation. Applies only to streams that do not support event-based incremental syncs: CheckoutSessionLineItems,  Events, SetupAttempts, ShippingRates, BalanceTransactions, Files, FileLinks. More info <a href=\\"https://docs.airbyte.com/integrations/sources/stripe#requirements\\">here</a>"""
    slice_range: Optional[int] = dataclasses.field(default=365, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slice_range'), 'exclude': lambda f: f is None }})
    r"""The time increment used by the connector when requesting data from the Stripe API. The bigger the value is, the less requests will be made and faster the sync will be. On the other hand, the more seldom the state is persisted."""
    start_date: Optional[datetime] = dataclasses.field(default=dateutil.parser.isoparse('2017-01-25T00:00:00Z'), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Only data generated after this date will be replicated."""
    

