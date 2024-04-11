"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional, Union

class Astra(str, Enum):
    ASTRA = 'astra'

class DestinationAstraSchemasEmbeddingEmbeddingMode(str, Enum):
    OPENAI_COMPATIBLE = 'openai_compatible'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpenAICompatible:
    r"""Use a service that's compatible with the OpenAI API to embed text."""
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    r"""The base URL for your OpenAI-compatible service"""
    dimensions: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dimensions') }})
    r"""The number of dimensions the embedding model is generating"""
    api_key: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    MODE: Final[Optional[DestinationAstraSchemasEmbeddingEmbeddingMode]] = dataclasses.field(default=DestinationAstraSchemasEmbeddingEmbeddingMode.OPENAI_COMPATIBLE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    model_name: Optional[str] = dataclasses.field(default='text-embedding-ada-002', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_name'), 'exclude': lambda f: f is None }})
    r"""The name of the model to use for embedding"""
    


class DestinationAstraSchemasEmbeddingMode(str, Enum):
    AZURE_OPENAI = 'azure_openai'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AzureOpenAI:
    r"""Use the Azure-hosted OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    api_base: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_base') }})
    r"""The base URL for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    deployment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('deployment') }})
    r"""The deployment for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    r"""The API key for your Azure OpenAI resource.  You can find this in the Azure portal under your Azure OpenAI resource"""
    MODE: Final[Optional[DestinationAstraSchemasEmbeddingMode]] = dataclasses.field(default=DestinationAstraSchemasEmbeddingMode.AZURE_OPENAI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationAstraSchemasMode(str, Enum):
    FAKE = 'fake'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Fake:
    r"""Use a fake embedding made out of random vectors with 1536 embedding dimensions. This is useful for testing the data pipeline without incurring any costs."""
    MODE: Final[Optional[DestinationAstraSchemasMode]] = dataclasses.field(default=DestinationAstraSchemasMode.FAKE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationAstraMode(str, Enum):
    COHERE = 'cohere'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cohere:
    r"""Use the Cohere API to embed text."""
    cohere_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cohere_key') }})
    MODE: Final[Optional[DestinationAstraMode]] = dataclasses.field(default=DestinationAstraMode.COHERE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationAstraSchemasEmbeddingEmbedding1Mode(str, Enum):
    OPENAI = 'openai'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpenAI:
    r"""Use the OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    MODE: Final[Optional[DestinationAstraSchemasEmbeddingEmbedding1Mode]] = dataclasses.field(default=DestinationAstraSchemasEmbeddingEmbedding1Mode.OPENAI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Indexing:
    r"""Astra DB gives developers the APIs, real-time data and ecosystem integrations to put accurate RAG and Gen AI apps with fewer hallucinations in production."""
    astra_db_app_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('astra_db_app_token') }})
    r"""The application token authorizes a user to connect to a specific Astra DB database. It is created when the user clicks the Generate Token button on the Overview tab of the Database page in the Astra UI."""
    astra_db_endpoint: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('astra_db_endpoint') }})
    r"""The endpoint specifies which Astra DB database queries are sent to. It can be copied from the Database Details section of the Overview tab of the Database page in the Astra UI."""
    astra_db_keyspace: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('astra_db_keyspace') }})
    r"""Keyspaces (or Namespaces) serve as containers for organizing data within a database. You can create a new keyspace uisng the Data Explorer tab in the Astra UI. The keyspace default_keyspace is created for you when you create a Vector Database in Astra DB."""
    collection: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection') }})
    r"""Collections hold data. They are analagous to tables in traditional Cassandra terminology. This tool will create the collection with the provided name automatically if it does not already exist. Alternatively, you can create one thorugh the Data Explorer tab in the Astra UI."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FieldNameMappingConfigModel:
    from_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_field') }})
    r"""The field name in the source"""
    to_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_field') }})
    r"""The field name to use in the destination"""
    


class DestinationAstraLanguage(str, Enum):
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

class DestinationAstraSchemasProcessingTextSplitterTextSplitterMode(str, Enum):
    CODE = 'code'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ByProgrammingLanguage:
    r"""Split the text by suitable delimiters based on the programming language. This is useful for splitting code into chunks."""
    language: DestinationAstraLanguage = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('language') }})
    r"""Split code in suitable places based on the programming language"""
    MODE: Final[Optional[DestinationAstraSchemasProcessingTextSplitterTextSplitterMode]] = dataclasses.field(default=DestinationAstraSchemasProcessingTextSplitterTextSplitterMode.CODE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    


class DestinationAstraSchemasProcessingTextSplitterMode(str, Enum):
    MARKDOWN = 'markdown'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ByMarkdownHeader:
    r"""Split the text by Markdown headers down to the specified header level. If the chunk size fits multiple sections, they will be combined into a single chunk."""
    MODE: Final[Optional[DestinationAstraSchemasProcessingTextSplitterMode]] = dataclasses.field(default=DestinationAstraSchemasProcessingTextSplitterMode.MARKDOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    split_level: Optional[int] = dataclasses.field(default=1, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('split_level'), 'exclude': lambda f: f is None }})
    r"""Level of markdown headers to split text fields by. Headings down to the specified level will be used as split points"""
    


class DestinationAstraSchemasProcessingMode(str, Enum):
    SEPARATOR = 'separator'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BySeparator:
    r"""Split the text by the list of separators until the chunk size is reached, using the earlier mentioned separators where possible. This is useful for splitting text fields by paragraphs, sentences, words, etc."""
    keep_separator: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('keep_separator'), 'exclude': lambda f: f is None }})
    r"""Whether to keep the separator in the resulting chunks"""
    MODE: Final[Optional[DestinationAstraSchemasProcessingMode]] = dataclasses.field(default=DestinationAstraSchemasProcessingMode.SEPARATOR, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    separators: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('separators'), 'exclude': lambda f: f is None }})
    r"""List of separator strings to split text fields by. The separator itself needs to be wrapped in double quotes, e.g. to split by the dot character, use \\".\\". To split by a newline, use \\"\n\\"."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProcessingConfigModel:
    chunk_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_size') }})
    r"""Size of chunks in tokens to store in vector store (make sure it is not too big for the context if your LLM)"""
    chunk_overlap: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_overlap'), 'exclude': lambda f: f is None }})
    r"""Size of overlap between chunks in tokens to store in vector store to better capture relevant context"""
    field_name_mappings: Optional[List[FieldNameMappingConfigModel]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('field_name_mappings'), 'exclude': lambda f: f is None }})
    r"""List of fields to rename. Not applicable for nested fields, but can be used to rename fields already flattened via dot notation."""
    metadata_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be stored as metadata. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered metadata fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array. When specifying nested paths, all matching values are flattened into an array set to a field named by the path."""
    text_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_fields'), 'exclude': lambda f: f is None }})
    r"""List of fields in the record that should be used to calculate the embedding. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered text fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array."""
    text_splitter: Optional[Union[BySeparator, ByMarkdownHeader, ByProgrammingLanguage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_splitter'), 'exclude': lambda f: f is None }})
    r"""Split text fields into chunks based on the specified method."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationAstra:
    r"""The configuration model for the Vector DB based destinations. This model is used to generate the UI for the destination configuration,
    as well as to provide type safety for the configuration passed to the destination.

    The configuration model is composed of four parts:
    * Processing configuration
    * Embedding configuration
    * Indexing configuration
    * Advanced configuration

    Processing, embedding and advanced configuration are provided by this base class, while the indexing configuration is provided by the destination connector in the sub class.
    """
    embedding: Union[OpenAI, Cohere, Fake, AzureOpenAI, OpenAICompatible] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('embedding') }})
    r"""Embedding configuration"""
    indexing: Indexing = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    r"""Astra DB gives developers the APIs, real-time data and ecosystem integrations to put accurate RAG and Gen AI apps with fewer hallucinations in production."""
    processing: ProcessingConfigModel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing') }})
    DESTINATION_TYPE: Final[Astra] = dataclasses.field(default=Astra.ASTRA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    omit_raw_text: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('omit_raw_text'), 'exclude': lambda f: f is None }})
    r"""Do not store the text that gets embedded along with the vector and the metadata in the destination. If set to true, only the vector and the metadata will be stored - in this case raw text for LLM use cases needs to be retrieved from another source."""
    

