"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Final, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceBigquery:
    r"""The values required to configure the source."""
    credentials_json: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials_json') }})
    r"""The contents of your Service Account Key JSON file. See the <a href=\\"https://docs.airbyte.com/integrations/sources/bigquery#setup-the-bigquery-source-in-airbyte\\">docs</a> for more information on how to obtain this key."""
    project_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project_id') }})
    r"""The GCP project ID for the project containing the target BigQuery dataset."""
    SOURCE_TYPE: Final[str] = dataclasses.field(default='bigquery', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    dataset_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_id'), 'exclude': lambda f: f is None }})
    r"""The dataset ID to search for tables and views. If you are only loading data from one dataset, setting this option could result in much faster schema discovery."""
    

