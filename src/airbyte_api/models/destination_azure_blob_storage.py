"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class DestinationAzureBlobStorageAzureBlobStorage(str, Enum):
    AZURE_BLOB_STORAGE = 'azure-blob-storage'


class DestinationAzureBlobStorageFormatType(str, Enum):
    JSONL = 'JSONL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorageJSONLinesNewlineDelimitedJSON:
    file_extension: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_extension'), 'exclude': lambda f: f is None }})
    r"""Add file extensions to the output file."""
    FORMAT_TYPE: Final[DestinationAzureBlobStorageFormatType] = dataclasses.field(default=DestinationAzureBlobStorageFormatType.JSONL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    



class NormalizationFlattening(str, Enum):
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    NO_FLATTENING = 'No flattening'
    ROOT_LEVEL_FLATTENING = 'Root level flattening'


class FormatType(str, Enum):
    CSV = 'CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CSVCommaSeparatedValues:
    file_extension: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_extension'), 'exclude': lambda f: f is None }})
    r"""Add file extensions to the output file."""
    flattening: Optional[NormalizationFlattening] = dataclasses.field(default=NormalizationFlattening.NO_FLATTENING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flattening'), 'exclude': lambda f: f is None }})
    r"""Whether the input json data should be normalized (flattened) in the output CSV. Please refer to docs for details."""
    FORMAT_TYPE: Final[FormatType] = dataclasses.field(default=FormatType.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_type') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAzureBlobStorage:
    azure_blob_storage_account_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_key') }})
    r"""The Azure blob storage account key."""
    azure_blob_storage_account_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_account_name') }})
    r"""The account's name of the Azure Blob Storage."""
    format: OutputFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""Output data format"""
    azure_blob_storage_container_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_container_name'), 'exclude': lambda f: f is None }})
    r"""The name of the Azure blob storage container. If not exists - will be created automatically. May be empty, then will be created automatically airbytecontainer+timestamp"""
    azure_blob_storage_endpoint_domain_name: Optional[str] = dataclasses.field(default='blob.core.windows.net', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_endpoint_domain_name'), 'exclude': lambda f: f is None }})
    r"""This is Azure Blob Storage endpoint domain name. Leave default value (or leave it empty if run container from command line) to use Microsoft native from example."""
    azure_blob_storage_output_buffer_size: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_output_buffer_size'), 'exclude': lambda f: f is None }})
    r"""The amount of megabytes to buffer for the output stream to Azure. This will impact memory footprint on workers, but may need adjustment for performance and appropriate block size in Azure."""
    azure_blob_storage_spill_size: Optional[int] = dataclasses.field(default=500, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('azure_blob_storage_spill_size'), 'exclude': lambda f: f is None }})
    r"""The amount of megabytes after which the connector should spill the records in a new blob object. Make sure to configure size greater than individual records. Enter 0 if not applicable"""
    DESTINATION_TYPE: Final[DestinationAzureBlobStorageAzureBlobStorage] = dataclasses.field(default=DestinationAzureBlobStorageAzureBlobStorage.AZURE_BLOB_STORAGE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    


OutputFormat = Union[CSVCommaSeparatedValues, DestinationAzureBlobStorageJSONLinesNewlineDelimitedJSON]
