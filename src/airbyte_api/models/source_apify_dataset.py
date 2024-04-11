"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class ApifyDataset(str, Enum):
    APIFY_DATASET = 'apify-dataset'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceApifyDataset:
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id') }})
    r"""ID of the dataset you would like to load to Airbyte. In Apify Console, you can view your datasets in the <a href=\\"https://console.apify.com/storage/datasets\\">Storage section under the Datasets tab</a> after you login. See the <a href=\\"https://docs.apify.com/platform/storage/dataset\\">Apify Docs</a> for more information."""
    token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Personal API token of your Apify account. In Apify Console, you can find your API token in the <a href=\\"https://console.apify.com/account/integrations\\">Settings section under the Integrations tab</a> after you login. See the <a href=\\"https://docs.apify.com/platform/integrations/api#api-token\\">Apify Docs</a> for more information."""
    SOURCE_TYPE: Final[ApifyDataset] = dataclasses.field(default=ApifyDataset.APIFY_DATASET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

