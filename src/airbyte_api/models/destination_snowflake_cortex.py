"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional, Union


class SnowflakeCortex(str, Enum):
    SNOWFLAKE_CORTEX = 'snowflake-cortex'


class DestinationSnowflakeCortexSchemasEmbeddingEmbedding5Mode(str, Enum):
    OPENAI_COMPATIBLE = 'openai_compatible'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexOpenAICompatible:
    r"""Use a service that's compatible with the OpenAI API to embed text."""
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    r"""The base URL for your OpenAI-compatible service"""
    dimensions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimensions') }})
    r"""The number of dimensions the embedding model is generating"""
    api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasEmbeddingEmbedding5Mode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasEmbeddingEmbedding5Mode.OPENAI_COMPATIBLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    model_name: Optional[str] = dataclasses.field(default='text-embedding-ada-002', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_name'), 'exclude': lambda f: f is None }})
    r"""The name of the model to use for embedding"""
    



class DestinationSnowflakeCortexSchemasEmbeddingEmbeddingMode(str, Enum):
    AZURE_OPENAI = 'azure_openai'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexAzureOpenAI:
    r"""Use the Azure-hosted OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    api_base: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_base') }})
    r"""The base URL for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    deployment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployment') }})
    r"""The deployment for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    r"""The API key for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasEmbeddingEmbeddingMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasEmbeddingEmbeddingMode.AZURE_OPENAI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationSnowflakeCortexSchemasEmbeddingMode(str, Enum):
    FAKE = 'fake'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexFake:
    r"""Use a fake embedding made out of random vectors with 1536 embedding dimensions. This is useful for testing the data pipeline without incurring any costs."""
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasEmbeddingMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasEmbeddingMode.FAKE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationSnowflakeCortexSchemasMode(str, Enum):
    COHERE = 'cohere'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexCohere:
    r"""Use the Cohere API to embed text."""
    cohere_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cohere_key') }})
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasMode.COHERE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationSnowflakeCortexMode(str, Enum):
    OPENAI = 'openai'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexOpenAI:
    r"""Use the OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    MODE: Final[Optional[DestinationSnowflakeCortexMode]] = dataclasses.field(default=DestinationSnowflakeCortexMode.OPENAI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


DestinationSnowflakeCortexEmbedding = Union['DestinationSnowflakeCortexOpenAI', 'DestinationSnowflakeCortexCohere', 'DestinationSnowflakeCortexFake', 'DestinationSnowflakeCortexAzureOpenAI', 'DestinationSnowflakeCortexOpenAICompatible']


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexCredentials:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Enter the password you want to use to access the database"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexIndexing:
    r"""Snowflake can be used to store vector data and retrieve embeddings."""
    credentials: DestinationSnowflakeCortexCredentials = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Enter the name of the database that you want to sync data into"""
    default_schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_schema') }})
    r"""Enter the name of the default schema"""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Enter the account name you want to use to access the database. This is usually the identifier before .snowflakecomputing.com"""
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""Enter the role that you want to use to access Snowflake"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Enter the name of the user you want to use to access the database"""
    warehouse: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warehouse') }})
    r"""Enter the name of the warehouse that you want to sync data into"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexFieldNameMappingConfigModel:
    from_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_field') }})
    r"""The field name in the source"""
    to_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_field') }})
    r"""The field name to use in the destination"""
    



class DestinationSnowflakeCortexLanguage(str, Enum):
    r"""Split code in suitable places based on the programming language"""
    CPP = 'cpp'
    GO = 'go'
    JAVA = 'java'
    JS = 'js'
    PHP = 'php'
    PROTO = 'proto'
    PYTHON = 'python'
    RST = 'rst'
    RUBY = 'ruby'
    RUST = 'rust'
    SCALA = 'scala'
    SWIFT = 'swift'
    MARKDOWN = 'markdown'
    LATEX = 'latex'
    HTML = 'html'
    SOL = 'sol'


class DestinationSnowflakeCortexSchemasProcessingTextSplitterTextSplitterMode(str, Enum):
    CODE = 'code'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexByProgrammingLanguage:
    r"""Split the text by suitable delimiters based on the programming language. This is useful for splitting code into chunks."""
    language: DestinationSnowflakeCortexLanguage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language') }})
    r"""Split code in suitable places based on the programming language"""
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasProcessingTextSplitterTextSplitterMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasProcessingTextSplitterTextSplitterMode.CODE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationSnowflakeCortexSchemasProcessingTextSplitterMode(str, Enum):
    MARKDOWN = 'markdown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexByMarkdownHeader:
    r"""Split the text by Markdown headers down to the specified header level. If the chunk size fits multiple sections, they will be combined into a single chunk."""
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasProcessingTextSplitterMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasProcessingTextSplitterMode.MARKDOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    split_level: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('split_level'), 'exclude': lambda f: f is None }})
    r"""Level of markdown headers to split text fields by. Headings down to the specified level will be used as split points"""
    



class DestinationSnowflakeCortexSchemasProcessingMode(str, Enum):
    SEPARATOR = 'separator'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexBySeparator:
    r"""Split the text by the list of separators until the chunk size is reached, using the earlier mentioned separators where possible. This is useful for splitting text fields by paragraphs, sentences, words, etc."""
    keep_separator: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keep_separator'), 'exclude': lambda f: f is None }})
    r"""Whether to keep the separator in the resulting chunks"""
    MODE: Final[Optional[DestinationSnowflakeCortexSchemasProcessingMode]] = dataclasses.field(default=DestinationSnowflakeCortexSchemasProcessingMode.SEPARATOR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    separators: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('separators'), 'exclude': lambda f: f is None }})
    r"""List of separator strings to split text fields by. The separator itself needs to be wrapped in double quotes, e.g. to split by the dot character, use \\".\\". To split by a newline, use \\"\n\\"."""
    


DestinationSnowflakeCortexTextSplitter = Union['DestinationSnowflakeCortexBySeparator', 'DestinationSnowflakeCortexByMarkdownHeader', 'DestinationSnowflakeCortexByProgrammingLanguage']


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortexProcessingConfigModel:
    chunk_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_size') }})
    r"""Size of chunks in tokens to store in vector store (make sure it is not too big for the context if your LLM)"""
    chunk_overlap: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_overlap'), 'exclude': lambda f: f is None }})
    r"""Size of overlap between chunks in tokens to store in vector store to better capture relevant context"""
    field_name_mappings: Optional[List[DestinationSnowflakeCortexFieldNameMappingConfigModel]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name_mappings'), 'exclude': lambda f: f is None }})
    r"""List of fields to rename. Not applicable for nested fields, but can be used to rename fields already flattened via dot notation."""
    metadata_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be stored as metadata. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered metadata fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array. When specifying nested paths, all matching values are flattened into an array set to a field named by the path."""
    text_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be used to calculate the embedding. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered text fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array."""
    text_splitter: Optional[DestinationSnowflakeCortexTextSplitter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_splitter'), 'exclude': lambda f: f is None }})
    r"""Split text fields into chunks based on the specified method."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationSnowflakeCortex:
    r"""The configuration model for the Vector DB based destinations. This model is used to generate the UI for the destination configuration,
    as well as to provide type safety for the configuration passed to the destination.

    The configuration model is composed of four parts:
    * Processing configuration
    * Embedding configuration
    * Indexing configuration
    * Advanced configuration

    Processing, embedding and advanced configuration are provided by this base class, while the indexing configuration is provided by the destination connector in the sub class.
    """
    embedding: DestinationSnowflakeCortexEmbedding = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('embedding') }})
    r"""Embedding configuration"""
    indexing: DestinationSnowflakeCortexIndexing = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    r"""Snowflake can be used to store vector data and retrieve embeddings."""
    processing: DestinationSnowflakeCortexProcessingConfigModel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing') }})
    DESTINATION_TYPE: Final[SnowflakeCortex] = dataclasses.field(default=SnowflakeCortex.SNOWFLAKE_CORTEX, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    omit_raw_text: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('omit_raw_text'), 'exclude': lambda f: f is None }})
    r"""Do not store the text that gets embedded along with the vector and the metadata in the destination. If set to true, only the vector and the metadata will be stored - in this case raw text for LLM use cases needs to be retrieved from another source."""
    

