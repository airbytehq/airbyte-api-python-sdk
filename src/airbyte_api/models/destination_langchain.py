"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional, Union


class Langchain(str, Enum):
    LANGCHAIN = 'langchain'


class DestinationLangchainSchemasMode(str, Enum):
    FAKE = 'fake'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationLangchainFake:
    r"""Use a fake embedding made out of random vectors with 1536 embedding dimensions. This is useful for testing the data pipeline without incurring any costs."""
    MODE: Final[Optional[DestinationLangchainSchemasMode]] = dataclasses.field(default=DestinationLangchainSchemasMode.FAKE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationLangchainMode(str, Enum):
    OPENAI = 'openai'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationLangchainOpenAI:
    r"""Use the OpenAI API to embed text. This option is using the text-embedding-ada-002 model with 1536 embedding dimensions."""
    openai_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('openai_key') }})
    MODE: Final[Optional[DestinationLangchainMode]] = dataclasses.field(default=DestinationLangchainMode.OPENAI, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationLangchainSchemasIndexingIndexing3Mode(str, Enum):
    CHROMA_LOCAL = 'chroma_local'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChromaLocalPersistance:
    r"""Chroma is a popular vector store that can be used to store and retrieve embeddings. It will build its index in memory and persist it to disk by the end of the sync."""
    destination_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_path') }})
    r"""Path to the directory where chroma files will be written. The files will be placed inside that local mount."""
    collection_name: Optional[str] = dataclasses.field(default='langchain', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('collection_name'), 'exclude': lambda f: f is None }})
    r"""Name of the collection to use."""
    MODE: Final[Optional[DestinationLangchainSchemasIndexingIndexing3Mode]] = dataclasses.field(default=DestinationLangchainSchemasIndexingIndexing3Mode.CHROMA_LOCAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationLangchainSchemasIndexingIndexingMode(str, Enum):
    DOC_ARRAY_HNSW_SEARCH = 'DocArrayHnswSearch'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DocArrayHnswSearch:
    r"""DocArrayHnswSearch is a lightweight Document Index implementation provided by Docarray that runs fully locally and is best suited for small- to medium-sized datasets. It stores vectors on disk in hnswlib, and stores all other data in SQLite."""
    destination_path: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination_path') }})
    r"""Path to the directory where hnswlib and meta data files will be written. The files will be placed inside that local mount. All files in the specified destination directory will be deleted on each run."""
    MODE: Final[Optional[DestinationLangchainSchemasIndexingIndexingMode]] = dataclasses.field(default=DestinationLangchainSchemasIndexingIndexingMode.DOC_ARRAY_HNSW_SEARCH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



class DestinationLangchainSchemasIndexingMode(str, Enum):
    PINECONE = 'pinecone'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationLangchainPinecone:
    r"""Pinecone is a popular vector store that can be used to store and retrieve embeddings. It is a managed service and can also be queried from outside of langchain."""
    index: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('index') }})
    r"""Pinecone index to use"""
    pinecone_environment: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pinecone_environment') }})
    r"""Pinecone environment to use"""
    pinecone_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pinecone_key') }})
    MODE: Final[Optional[DestinationLangchainSchemasIndexingMode]] = dataclasses.field(default=DestinationLangchainSchemasIndexingMode.PINECONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('mode'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationLangchainProcessingConfigModel:
    chunk_size: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_size') }})
    r"""Size of chunks in tokens to store in vector store (make sure it is not too big for the context if your LLM)"""
    text_fields: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text_fields') }})
    r"""List of fields in the record that should be used to calculate the embedding. All other fields are passed along as meta fields. The field list is applied to all streams in the same way and non-existing fields are ignored. If none are defined, all fields are considered text fields. When specifying text fields, you can access nested fields in the record by using dot notation, e.g. `user.name` will access the `name` field in the `user` object. It's also possible to use wildcards to access all fields in an object, e.g. `users.*.name` will access all `names` fields in all entries of the `users` array."""
    chunk_overlap: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_overlap'), 'exclude': lambda f: f is None }})
    r"""Size of overlap between chunks in tokens to store in vector store to better capture relevant context"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationLangchain:
    embedding: DestinationLangchainEmbedding = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('embedding') }})
    r"""Embedding configuration"""
    indexing: DestinationLangchainIndexing = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('indexing') }})
    r"""Indexing configuration"""
    processing: DestinationLangchainProcessingConfigModel = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processing') }})
    DESTINATION_TYPE: Final[Langchain] = dataclasses.field(default=Langchain.LANGCHAIN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    


DestinationLangchainEmbedding = Union[DestinationLangchainOpenAI, DestinationLangchainFake]

DestinationLangchainIndexing = Union[DestinationLangchainPinecone, DocArrayHnswSearch, ChromaLocalPersistance]
