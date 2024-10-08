"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional


class AzureTable(str, Enum):
    AZURE_TABLE = 'azure-table'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAzureTable:
    storage_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_access_key') }})
    r"""Azure Table Storage Access Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/azure-table\\">docs</a> for more information on how to obtain this key."""
    storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_account_name') }})
    r"""The name of your storage account."""
    SOURCE_TYPE: Final[AzureTable] = dataclasses.field(default=AzureTable.AZURE_TABLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    storage_endpoint_suffix: Optional[str] = dataclasses.field(default='core.windows.net', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_endpoint_suffix'), 'exclude': lambda f: f is None }})
    r"""Azure Table Storage service account URL suffix. See the <a href=\\"https://docs.airbyte.com/integrations/sources/azure-table\\">docs</a> for more information on how to obtain endpoint suffix"""
    

