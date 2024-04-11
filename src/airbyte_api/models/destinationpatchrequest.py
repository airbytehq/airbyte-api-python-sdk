"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .destination_astra import DestinationAstra
from .destination_aws_datalake import DestinationAwsDatalake
from .destination_azure_blob_storage import DestinationAzureBlobStorage
from .destination_bigquery import DestinationBigquery
from .destination_clickhouse import DestinationClickhouse
from .destination_convex import DestinationConvex
from .destination_databricks import DestinationDatabricks
from .destination_dev_null import DestinationDevNull
from .destination_duckdb import DestinationDuckdb
from .destination_dynamodb import DestinationDynamodb
from .destination_elasticsearch import DestinationElasticsearch
from .destination_firestore import DestinationFirestore
from .destination_gcs import DestinationGcs
from .destination_google_sheets import DestinationGoogleSheets
from .destination_langchain import DestinationLangchain
from .destination_milvus import DestinationMilvus
from .destination_mongodb import DestinationMongodb
from .destination_mssql import DestinationMssql
from .destination_mysql import DestinationMysql
from .destination_oracle import DestinationOracle
from .destination_pinecone import DestinationPinecone
from .destination_postgres import DestinationPostgres
from .destination_pubsub import DestinationPubsub
from .destination_qdrant import DestinationQdrant
from .destination_redis import DestinationRedis
from .destination_redshift import DestinationRedshift
from .destination_s3 import DestinationS3
from .destination_s3_glue import DestinationS3Glue
from .destination_sftp_json import DestinationSftpJSON
from .destination_snowflake import DestinationSnowflake
from .destination_teradata import DestinationTeradata
from .destination_typesense import DestinationTypesense
from .destination_vectara import DestinationVectara
from .destination_weaviate import DestinationWeaviate
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationPatchRequest:
    configuration: Optional[Union[DestinationGoogleSheets, DestinationAstra, DestinationAwsDatalake, DestinationAzureBlobStorage, DestinationBigquery, DestinationClickhouse, DestinationConvex, DestinationDatabricks, DestinationDevNull, DestinationDuckdb, DestinationDynamodb, DestinationElasticsearch, DestinationFirestore, DestinationGcs, DestinationLangchain, DestinationMilvus, DestinationMongodb, DestinationMssql, DestinationMysql, DestinationOracle, DestinationPinecone, DestinationPostgres, DestinationPubsub, DestinationQdrant, DestinationRedis, DestinationRedshift, DestinationS3, DestinationS3Glue, DestinationSftpJSON, DestinationSnowflake, DestinationTeradata, DestinationTypesense, DestinationVectara, DestinationWeaviate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    r"""The values required to configure the destination."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    
