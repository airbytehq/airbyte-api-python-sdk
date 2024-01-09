"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final

class ProductCatalog(str, Enum):
    r"""Product Catalog version of your Chargebee site. Instructions on how to find your version you may find <a href=\\"https://apidocs.chargebee.com/docs/api?prod_cat_ver=2\\">here</a> under `API Version` section."""
    ONE_0 = '1.0'
    TWO_0 = '2.0'

class Chargebee(str, Enum):
    CHARGEBEE = 'chargebee'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceChargebee:
    product_catalog: ProductCatalog = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_catalog') }})
    r"""Product Catalog version of your Chargebee site. Instructions on how to find your version you may find <a href=\\"https://apidocs.chargebee.com/docs/api?prod_cat_ver=2\\">here</a> under `API Version` section."""
    site: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site') }})
    r"""The site prefix for your Chargebee instance."""
    site_api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('site_api_key') }})
    r"""Chargebee API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/chargebee\\">docs</a> for more information on how to obtain this key."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2021-01-25T00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[Chargebee] = dataclasses.field(default=Chargebee.CHARGEBEE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

