"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Any, Optional

class SourceS3FormatJsonlFiletypeEnum(str, Enum):
    JSONL = 'jsonl'

class SourceS3FormatJsonlUnexpectedFieldBehaviorEnum(str, Enum):
    r"""How JSON fields outside of explicit_schema (if given) are treated. Check <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.json.ParseOptions.html\\" target=\\"_blank\\">PyArrow documentation</a> for details"""
    IGNORE = 'ignore'
    INFER = 'infer'
    ERROR = 'error'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatJsonl:
    r"""This connector uses <a href=\\"https://arrow.apache.org/docs/python/json.html\\" target=\\"_blank\\">PyArrow</a> for JSON Lines (jsonl) file parsing."""
    
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    r"""The chunk size in bytes to process at a time in memory from each file. If your data is particularly wide and failing during schema detection, increasing this should solve it. Beware of raising this too high as you could hit OOM errors."""  
    filetype: Optional[SourceS3FormatJsonlFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})  
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    r"""Whether newline characters are allowed in JSON values. Turning this on may affect performance. Leave blank to default to False."""  
    unexpected_field_behavior: Optional[SourceS3FormatJsonlUnexpectedFieldBehaviorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unexpected_field_behavior'), 'exclude': lambda f: f is None }})
    r"""How JSON fields outside of explicit_schema (if given) are treated. Check <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.json.ParseOptions.html\\" target=\\"_blank\\">PyArrow documentation</a> for details"""  
    
class SourceS3FormatAvroFiletypeEnum(str, Enum):
    AVRO = 'avro'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatAvro:
    r"""This connector utilises <a href=\\"https://fastavro.readthedocs.io/en/latest/\\" target=\\"_blank\\">fastavro</a> for Avro parsing."""
    
    filetype: Optional[SourceS3FormatAvroFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})  
    
class SourceS3FormatParquetFiletypeEnum(str, Enum):
    PARQUET = 'parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatParquet:
    r"""This connector utilises <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.parquet.ParquetFile.html\\" target=\\"_blank\\">PyArrow (Apache Arrow)</a> for Parquet parsing."""
    
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    r"""Maximum number of records per batch read from the input files. Batches may be smaller if there aren’t enough rows in the file. This option can help avoid out-of-memory errors if your data is particularly wide."""  
    buffer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('buffer_size'), 'exclude': lambda f: f is None }})
    r"""Perform read buffering when deserializing individual column chunks. By default every group column will be loaded fully to memory. This option can help avoid out-of-memory errors if your data is particularly wide."""  
    columns: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns'), 'exclude': lambda f: f is None }})
    r"""If you only want to sync a subset of the columns from the file(s), add the columns you want here as a comma-delimited list. Leave it empty to sync all columns."""  
    filetype: Optional[SourceS3FormatParquetFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})  
    
class SourceS3FormatCSVFiletypeEnum(str, Enum):
    CSV = 'csv'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3FormatCSV:
    r"""This connector utilises <a href=\\"https: // arrow.apache.org/docs/python/generated/pyarrow.csv.open_csv.html\\" target=\\"_blank\\">PyArrow (Apache Arrow)</a> for CSV parsing."""
    
    additional_reader_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('additional_reader_options'), 'exclude': lambda f: f is None }})
    r"""Optionally add a valid JSON string here to provide additional options to the csv reader. Mappings must correspond to options <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.csv.ConvertOptions.html#pyarrow.csv.ConvertOptions\\" target=\\"_blank\\">detailed here</a>. 'column_types' is used internally to handle schema so overriding that would likely cause problems."""  
    advanced_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advanced_options'), 'exclude': lambda f: f is None }})
    r"""Optionally add a valid JSON string here to provide additional <a href=\\"https://arrow.apache.org/docs/python/generated/pyarrow.csv.ReadOptions.html#pyarrow.csv.ReadOptions\\" target=\\"_blank\\">Pyarrow ReadOptions</a>. Specify 'column_names' here if your CSV doesn't have header, or if you want to use custom column names. 'block_size' and 'encoding' are already used above, specify them again here will override the values above."""  
    block_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('block_size'), 'exclude': lambda f: f is None }})
    r"""The chunk size in bytes to process at a time in memory from each file. If your data is particularly wide and failing during schema detection, increasing this should solve it. Beware of raising this too high as you could hit OOM errors."""  
    delimiter: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    r"""The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\t'."""  
    double_quote: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    r"""Whether two quotes in a quoted CSV value denote a single quote in the data."""  
    encoding: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    r"""The character encoding of the CSV data. Leave blank to default to <strong>UTF8</strong>. See <a href=\\"https://docs.python.org/3/library/codecs.html#standard-encodings\\" target=\\"_blank\\">list of python encodings</a> for allowable options."""  
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    r"""The character used for escaping special characters. To disallow escaping, leave this field blank."""  
    filetype: Optional[SourceS3FormatCSVFiletypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})  
    infer_datatypes: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('infer_datatypes'), 'exclude': lambda f: f is None }})
    r"""Configures whether a schema for the source should be inferred from the current data or not. If set to false and a custom schema is set, then the manually enforced schema is used. If a schema is not manually set, and this is set to false, then all fields will be read as strings"""  
    newlines_in_values: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('newlines_in_values'), 'exclude': lambda f: f is None }})
    r"""Whether newline characters are allowed in CSV values. Turning this on may affect performance. Leave blank to default to False."""  
    quote_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    r"""The character used for quoting CSV values. To disallow quoting, make this field blank."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3S3AmazonWebServices:
    r"""Use this to load files from S3 or S3-compatible services"""
    
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""Name of the S3 bucket where the file(s) exist."""  
    aws_access_key_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key_id'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""  
    aws_secret_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_access_key'), 'exclude': lambda f: f is None }})
    r"""In order to access private Buckets stored on AWS S3, this connector requires credentials with the proper permissions. If accessing publicly available data, this field is not necessary."""  
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint'), 'exclude': lambda f: f is None }})
    r"""Endpoint to an S3 compatible service. Leave empty to use AWS."""  
    path_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_prefix'), 'exclude': lambda f: f is None }})
    r"""By providing a path-like prefix (e.g. myFolder/thisTable/) under which all the relevant files sit, we can optimize finding these in S3. This is optional but recommended if your bucket contains many folders/files which you don't need to replicate."""  
    
class SourceS3S3Enum(str, Enum):
    S3 = 's3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceS3:
    r"""The values required to configure the source."""
    
    dataset: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset') }})
    r"""The name of the stream you would like this source to output. Can contain letters, numbers, or underscores."""  
    path_pattern: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path_pattern') }})
    r"""A regular expression which tells the connector which files to replicate. All files which match this pattern will be replicated. Use | to separate multiple patterns. See <a href=\\"https://facelessuser.github.io/wcmatch/glob/\\" target=\\"_blank\\">this page</a> to understand pattern syntax (GLOBSTAR and SPLIT flags are enabled). Use pattern <strong>**</strong> to pick up all files."""  
    provider: SourceS3S3AmazonWebServices = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider') }})
    r"""Use this to load files from S3 or S3-compatible services"""  
    source_type: SourceS3S3Enum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    format: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    r"""The format of the files you'd like to replicate"""  
    schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""Optionally provide a schema to enforce, as a valid JSON string. Ensure this is a mapping of <strong>{ \\"column\\" : \\"type\\" }</strong>, where types are valid <a href=\\"https://json-schema.org/understanding-json-schema/reference/type.html\\" target=\\"_blank\\">JSON Schema datatypes</a>. Leave as {} to auto-infer the schema."""  
    