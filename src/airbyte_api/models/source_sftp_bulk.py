"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional, Union


class SourceSftpBulkSchemasAuthType(str, Enum):
    PRIVATE_KEY = 'private_key'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaPrivateKey:
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    r"""The Private key"""
    AUTH_TYPE: Final[Optional[SourceSftpBulkSchemasAuthType]] = dataclasses.field(default=SourceSftpBulkSchemasAuthType.PRIVATE_KEY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkAuthType(str, Enum):
    PASSWORD = 'password'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AuthenticateViaPassword:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password"""
    AUTH_TYPE: Final[Optional[SourceSftpBulkAuthType]] = dataclasses.field(default=SourceSftpBulkAuthType.PASSWORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



class SftpBulk(str, Enum):
    SFTP_BULK = 'sftp-bulk'


class SourceSftpBulkSchemasStreamsFormatFormat6Filetype(str, Enum):
    EXCEL = 'excel'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkExcelFormat:
    FILETYPE: Final[Optional[SourceSftpBulkSchemasStreamsFormatFormat6Filetype]] = dataclasses.field(default=SourceSftpBulkSchemasStreamsFormatFormat6Filetype.EXCEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkSchemasStreamsFormatFormatFiletype(str, Enum):
    UNSTRUCTURED = 'unstructured'


class SourceSftpBulkSchemasMode(str, Enum):
    API = 'api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkAPIParameterConfigModel:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the unstructured API parameter to use"""
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    r"""The value of the parameter"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkViaAPI:
    r"""Process files via an API, using the `hi_res` mode. This option is useful for increased performance and accuracy, but requires an API key and a hosted instance of unstructured."""
    api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    r"""The API key to use matching the environment"""
    api_url: Optional[str] = dataclasses.field(default='https://api.unstructured.io', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_url'), 'exclude': lambda f: f is None }})
    r"""The URL of the unstructured API to use"""
    MODE: Final[Optional[SourceSftpBulkSchemasMode]] = dataclasses.field(default=SourceSftpBulkSchemasMode.API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    parameters: Optional[List[SourceSftpBulkAPIParameterConfigModel]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters'), 'exclude': lambda f: f is None }})
    r"""List of parameters send to the API"""
    



class SourceSftpBulkMode(str, Enum):
    LOCAL = 'local'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkLocal:
    r"""Process files locally, supporting `fast` and `ocr` modes. This is the default option."""
    MODE: Final[Optional[SourceSftpBulkMode]] = dataclasses.field(default=SourceSftpBulkMode.LOCAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkParsingStrategy(str, Enum):
    r"""The strategy used to parse documents. `fast` extracts text directly from the document which doesn't work for all files. `ocr_only` is more reliable, but slower. `hi_res` is the most reliable, but requires an API key and a hosted instance of unstructured and can't be used with local mode. See the unstructured.io documentation for more details: https://unstructured-io.github.io/unstructured/core/partition.html#partition-pdf"""
    AUTO = 'auto'
    FAST = 'fast'
    OCR_ONLY = 'ocr_only'
    HI_RES = 'hi_res'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkUnstructuredDocumentFormat:
    r"""Extract text from document formats (.pdf, .docx, .md, .pptx) and emit as one record per file."""
    FILETYPE: Final[Optional[SourceSftpBulkSchemasStreamsFormatFormatFiletype]] = dataclasses.field(default=SourceSftpBulkSchemasStreamsFormatFormatFiletype.UNSTRUCTURED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    processing: Optional[SourceSftpBulkProcessing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing'), 'exclude': lambda f: f is None }})
    r"""Processing configuration"""
    skip_unprocessable_files: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_unprocessable_files'), 'exclude': lambda f: f is None }})
    r"""If true, skip files that cannot be parsed and pass the error message along as the _ab_source_file_parse_error field. If false, fail the sync."""
    strategy: Optional[SourceSftpBulkParsingStrategy] = dataclasses.field(default=SourceSftpBulkParsingStrategy.AUTO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strategy'), 'exclude': lambda f: f is None }})
    r"""The strategy used to parse documents. `fast` extracts text directly from the document which doesn't work for all files. `ocr_only` is more reliable, but slower. `hi_res` is the most reliable, but requires an API key and a hosted instance of unstructured and can't be used with local mode. See the unstructured.io documentation for more details: https://unstructured-io.github.io/unstructured/core/partition.html#partition-pdf"""
    



class SourceSftpBulkSchemasStreamsFormatFiletype(str, Enum):
    PARQUET = 'parquet'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkParquetFormat:
    decimal_as_float: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('decimal_as_float'), 'exclude': lambda f: f is None }})
    r"""Whether to convert decimal fields to floats. There is a loss of precision when converting decimals to floats, so this is not recommended."""
    FILETYPE: Final[Optional[SourceSftpBulkSchemasStreamsFormatFiletype]] = dataclasses.field(default=SourceSftpBulkSchemasStreamsFormatFiletype.PARQUET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkSchemasStreamsFiletype(str, Enum):
    JSONL = 'jsonl'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkJsonlFormat:
    FILETYPE: Final[Optional[SourceSftpBulkSchemasStreamsFiletype]] = dataclasses.field(default=SourceSftpBulkSchemasStreamsFiletype.JSONL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkSchemasFiletype(str, Enum):
    CSV = 'csv'


class SourceSftpBulkSchemasStreamsHeaderDefinitionType(str, Enum):
    USER_PROVIDED = 'User Provided'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkUserProvided:
    column_names: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column_names') }})
    r"""The column names that will be used while emitting the CSV records"""
    HEADER_DEFINITION_TYPE: Final[Optional[SourceSftpBulkSchemasStreamsHeaderDefinitionType]] = dataclasses.field(default=SourceSftpBulkSchemasStreamsHeaderDefinitionType.USER_PROVIDED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkSchemasHeaderDefinitionType(str, Enum):
    AUTOGENERATED = 'Autogenerated'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkAutogenerated:
    HEADER_DEFINITION_TYPE: Final[Optional[SourceSftpBulkSchemasHeaderDefinitionType]] = dataclasses.field(default=SourceSftpBulkSchemasHeaderDefinitionType.AUTOGENERATED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkHeaderDefinitionType(str, Enum):
    FROM_CSV = 'From CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkFromCSV:
    HEADER_DEFINITION_TYPE: Final[Optional[SourceSftpBulkHeaderDefinitionType]] = dataclasses.field(default=SourceSftpBulkHeaderDefinitionType.FROM_CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkInferenceType(str, Enum):
    r"""How to infer the types of the columns. If none, inference default to strings."""
    NONE = 'None'
    PRIMITIVE_TYPES_ONLY = 'Primitive Types Only'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkCSVFormat:
    delimiter: Optional[str] = dataclasses.field(default=',', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    r"""The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\t'."""
    double_quote: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    r"""Whether two quotes in a quoted CSV value denote a single quote in the data."""
    encoding: Optional[str] = dataclasses.field(default='utf8', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    r"""The character encoding of the CSV data. Leave blank to default to <strong>UTF8</strong>. See <a href=\\"https://docs.python.org/3/library/codecs.html#standard-encodings\\" target=\\"_blank\\">list of python encodings</a> for allowable options."""
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    r"""The character used for escaping special characters. To disallow escaping, leave this field blank."""
    false_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('false_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as false values."""
    FILETYPE: Final[Optional[SourceSftpBulkSchemasFiletype]] = dataclasses.field(default=SourceSftpBulkSchemasFiletype.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    header_definition: Optional[SourceSftpBulkCSVHeaderDefinition] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition'), 'exclude': lambda f: f is None }})
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    ignore_errors_on_fields_mismatch: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ignore_errors_on_fields_mismatch'), 'exclude': lambda f: f is None }})
    r"""Whether to ignore errors that occur when the number of fields in the CSV does not match the number of columns in the schema."""
    inference_type: Optional[SourceSftpBulkInferenceType] = dataclasses.field(default=SourceSftpBulkInferenceType.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inference_type'), 'exclude': lambda f: f is None }})
    r"""How to infer the types of the columns. If none, inference default to strings."""
    null_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('null_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as null values. For example, if the value 'NA' should be interpreted as null, enter 'NA' in this field."""
    quote_char: Optional[str] = dataclasses.field(default='"', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    r"""The character used for quoting CSV values. To disallow quoting, make this field blank."""
    skip_rows_after_header: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_after_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip after the header row."""
    skip_rows_before_header: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_before_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip before the header row. For example, if the header row is on the 3rd row, enter 2 in this field."""
    strings_can_be_null: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strings_can_be_null'), 'exclude': lambda f: f is None }})
    r"""Whether strings can be interpreted as null values. If true, strings that match the null_values set will be interpreted as null. If false, strings that match the null_values set will be interpreted as the string itself."""
    true_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('true_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as true values."""
    



class SourceSftpBulkFiletype(str, Enum):
    AVRO = 'avro'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkAvroFormat:
    double_as_string: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_as_string'), 'exclude': lambda f: f is None }})
    r"""Whether to convert double fields to strings. This is recommended if you have decimal numbers with a high degree of precision because there can be a loss precision when handling floating point numbers."""
    FILETYPE: Final[Optional[SourceSftpBulkFiletype]] = dataclasses.field(default=SourceSftpBulkFiletype.AVRO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    



class SourceSftpBulkValidationPolicy(str, Enum):
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    EMIT_RECORD = 'Emit Record'
    SKIP_RECORD = 'Skip Record'
    WAIT_FOR_DISCOVER = 'Wait for Discover'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulkFileBasedStreamConfig:
    format: SourceSftpBulkFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the stream."""
    days_to_sync_if_history_is_full: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_to_sync_if_history_is_full'), 'exclude': lambda f: f is None }})
    r"""When the state history of the file store is full, syncs will only read files that were last modified in the provided day range."""
    globs: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('globs'), 'exclude': lambda f: f is None }})
    r"""The pattern used to specify which files should be selected from the file system. For more information on glob pattern matching look <a href=\\"https://en.wikipedia.org/wiki/Glob_(programming)\\">here</a>."""
    input_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input_schema'), 'exclude': lambda f: f is None }})
    r"""The schema that will be used to validate records extracted from the file. This will override the stream schema that is auto-detected from incoming files."""
    legacy_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy_prefix'), 'exclude': lambda f: f is None }})
    r"""The path prefix configured in v3 versions of the S3 connector. This option is deprecated in favor of a single glob."""
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_key'), 'exclude': lambda f: f is None }})
    r"""The column or columns (for a composite key) that serves as the unique identifier of a record. If empty, the primary key will default to the parser's default primary key."""
    recent_n_files_to_read_for_schema_discovery: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('recent_n_files_to_read_for_schema_discovery'), 'exclude': lambda f: f is None }})
    r"""The number of resent files which will be used to discover the schema for this stream."""
    schemaless: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaless'), 'exclude': lambda f: f is None }})
    r"""When enabled, syncs will not validate or structure records against the stream's schema."""
    validation_policy: Optional[SourceSftpBulkValidationPolicy] = dataclasses.field(default=SourceSftpBulkValidationPolicy.EMIT_RECORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_policy'), 'exclude': lambda f: f is None }})
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulk:
    r"""Used during spec; allows the developer to configure the cloud provider specific options
    that are needed when users configure a file-based source.
    """
    credentials: SourceSftpBulkAuthentication = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    r"""Credentials for connecting to the SFTP Server"""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The server host address"""
    streams: List[SourceSftpBulkFileBasedStreamConfig] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams') }})
    r"""Each instance of this configuration defines a <a href=\\"https://docs.airbyte.com/cloud/core-concepts#stream\\">stream</a>. Use this to define which files belong in the stream, their format, and how they should be parsed and validated. When sending data to warehouse destination such as Snowflake or BigQuery, each stream is a separate table."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The server user"""
    folder_path: Optional[str] = dataclasses.field(default='/', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path'), 'exclude': lambda f: f is None }})
    r"""The directory to search files for sync"""
    port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The server port"""
    SOURCE_TYPE: Final[SftpBulk] = dataclasses.field(default=SftpBulk.SFTP_BULK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00.000000Z. Any file modified before this date will not be replicated."""
    


SourceSftpBulkAuthentication = Union[AuthenticateViaPassword, AuthenticateViaPrivateKey]

SourceSftpBulkProcessing = Union[SourceSftpBulkLocal, SourceSftpBulkViaAPI]

SourceSftpBulkCSVHeaderDefinition = Union[SourceSftpBulkFromCSV, SourceSftpBulkAutogenerated, SourceSftpBulkUserProvided]

SourceSftpBulkFormat = Union[SourceSftpBulkAvroFormat, SourceSftpBulkCSVFormat, SourceSftpBulkJsonlFormat, SourceSftpBulkParquetFormat, SourceSftpBulkUnstructuredDocumentFormat, SourceSftpBulkExcelFormat]
