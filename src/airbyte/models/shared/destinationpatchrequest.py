"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import destination_aws_datalake as shared_destination_aws_datalake
from ..shared import destination_azure_blob_storage as shared_destination_azure_blob_storage
from ..shared import destination_bigquery as shared_destination_bigquery
from ..shared import destination_bigquery_denormalized as shared_destination_bigquery_denormalized
from ..shared import destination_clickhouse as shared_destination_clickhouse
from ..shared import destination_convex as shared_destination_convex
from ..shared import destination_cumulio as shared_destination_cumulio
from ..shared import destination_databend as shared_destination_databend
from ..shared import destination_databricks as shared_destination_databricks
from ..shared import destination_dev_null as shared_destination_dev_null
from ..shared import destination_dynamodb as shared_destination_dynamodb
from ..shared import destination_elasticsearch as shared_destination_elasticsearch
from ..shared import destination_firebolt as shared_destination_firebolt
from ..shared import destination_firestore as shared_destination_firestore
from ..shared import destination_gcs as shared_destination_gcs
from ..shared import destination_google_sheets as shared_destination_google_sheets
from ..shared import destination_keen as shared_destination_keen
from ..shared import destination_kinesis as shared_destination_kinesis
from ..shared import destination_langchain as shared_destination_langchain
from ..shared import destination_milvus as shared_destination_milvus
from ..shared import destination_mongodb as shared_destination_mongodb
from ..shared import destination_mssql as shared_destination_mssql
from ..shared import destination_mysql as shared_destination_mysql
from ..shared import destination_oracle as shared_destination_oracle
from ..shared import destination_pinecone as shared_destination_pinecone
from ..shared import destination_postgres as shared_destination_postgres
from ..shared import destination_pubsub as shared_destination_pubsub
from ..shared import destination_redis as shared_destination_redis
from ..shared import destination_redshift as shared_destination_redshift
from ..shared import destination_s3 as shared_destination_s3
from ..shared import destination_s3_glue as shared_destination_s3_glue
from ..shared import destination_sftp_json as shared_destination_sftp_json
from ..shared import destination_snowflake as shared_destination_snowflake
from ..shared import destination_timeplus as shared_destination_timeplus
from ..shared import destination_typesense as shared_destination_typesense
from ..shared import destination_vertica as shared_destination_vertica
from ..shared import destination_xata as shared_destination_xata
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationPatchRequest:
    configuration: Optional[Union[shared_destination_aws_datalake.DestinationAwsDatalake, shared_destination_azure_blob_storage.DestinationAzureBlobStorage, shared_destination_bigquery.DestinationBigquery, shared_destination_bigquery_denormalized.DestinationBigqueryDenormalized, shared_destination_clickhouse.DestinationClickhouse, shared_destination_convex.DestinationConvex, shared_destination_cumulio.DestinationCumulio, shared_destination_databend.DestinationDatabend, shared_destination_databricks.DestinationDatabricks, shared_destination_dev_null.DestinationDevNull, shared_destination_dynamodb.DestinationDynamodb, shared_destination_elasticsearch.DestinationElasticsearch, shared_destination_firebolt.DestinationFirebolt, shared_destination_firestore.DestinationFirestore, shared_destination_gcs.DestinationGcs, shared_destination_google_sheets.DestinationGoogleSheets, shared_destination_keen.DestinationKeen, shared_destination_kinesis.DestinationKinesis, shared_destination_langchain.DestinationLangchain, shared_destination_milvus.DestinationMilvus, shared_destination_mongodb.DestinationMongodb, shared_destination_mssql.DestinationMssql, shared_destination_mysql.DestinationMysql, shared_destination_oracle.DestinationOracle, shared_destination_pinecone.DestinationPinecone, shared_destination_postgres.DestinationPostgres, shared_destination_pubsub.DestinationPubsub, shared_destination_redis.DestinationRedis, shared_destination_redshift.DestinationRedshift, shared_destination_s3.DestinationS3, shared_destination_s3_glue.DestinationS3Glue, shared_destination_sftp_json.DestinationSftpJSON, shared_destination_snowflake.DestinationSnowflake, shared_destination_timeplus.DestinationTimeplus, shared_destination_typesense.DestinationTypesense, shared_destination_vertica.DestinationVertica, shared_destination_xata.DestinationXata]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('configuration'), 'exclude': lambda f: f is None }})
    r"""The values required to configure the destination."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    

