"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union


class DestinationIcebergSchemasCatalogConfigIcebergCatalogConfigCatalogType(str, Enum):
    GLUE = 'Glue'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GlueCatalog:
    r"""The GlueCatalog connects to a AWS Glue Catalog"""
    catalog_type: Optional[DestinationIcebergSchemasCatalogConfigIcebergCatalogConfigCatalogType] = dataclasses.field(default=DestinationIcebergSchemasCatalogConfigIcebergCatalogConfigCatalogType.GLUE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_type'), 'exclude': lambda f: f is None }})
    database: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    



class DestinationIcebergSchemasCatalogConfigCatalogType(str, Enum):
    REST = 'Rest'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RESTCatalog:
    r"""The RESTCatalog connects to a REST server at the specified URI"""
    rest_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rest_uri') }})
    catalog_type: Optional[DestinationIcebergSchemasCatalogConfigCatalogType] = dataclasses.field(default=DestinationIcebergSchemasCatalogConfigCatalogType.REST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_type'), 'exclude': lambda f: f is None }})
    rest_credential: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rest_credential'), 'exclude': lambda f: f is None }})
    rest_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rest_token'), 'exclude': lambda f: f is None }})
    



class DestinationIcebergSchemasCatalogType(str, Enum):
    JDBC = 'Jdbc'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JdbcCatalogUseRelationalDatabase:
    r"""Using a table in a relational database to manage Iceberg tables through JDBC. Read more <a href=\\"https://iceberg.apache.org/docs/latest/jdbc/\\">here</a>. Supporting: PostgreSQL"""
    catalog_schema: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_schema'), 'exclude': lambda f: f is None }})
    r"""Iceberg catalog metadata tables are written to catalog schema. The usual value for this field is \\"public\\"."""
    catalog_type: Optional[DestinationIcebergSchemasCatalogType] = dataclasses.field(default=DestinationIcebergSchemasCatalogType.JDBC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_type'), 'exclude': lambda f: f is None }})
    database: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. The usual value for this field is \\"public\\"."""
    jdbc_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url'), 'exclude': lambda f: f is None }})
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""Password associated with the username."""
    ssl: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl'), 'exclude': lambda f: f is None }})
    r"""Encrypt data using SSL. When activating SSL, please select one of the connection modes."""
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    r"""Username to use to access the database."""
    



class DestinationIcebergCatalogType(str, Enum):
    HADOOP = 'Hadoop'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HadoopCatalogUseHierarchicalFileSystemsAsSameAsStorageConfig:
    r"""A Hadoop catalog doesn’t need to connect to a Hive MetaStore, but can only be used with HDFS or similar file systems that support atomic rename."""
    catalog_type: Optional[DestinationIcebergCatalogType] = dataclasses.field(default=DestinationIcebergCatalogType.HADOOP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_type'), 'exclude': lambda f: f is None }})
    database: Optional[str] = dataclasses.field(default='default', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The default database tables are written to if the source does not specify a namespace. The usual value for this field is \\"default\\"."""
    



class CatalogType(str, Enum):
    HIVE = 'Hive'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HiveCatalogUseApacheHiveMetaStore:
    hive_thrift_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hive_thrift_uri') }})
    r"""Hive MetaStore thrift server uri of iceberg catalog."""
    catalog_type: Optional[CatalogType] = dataclasses.field(default=CatalogType.HIVE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_type'), 'exclude': lambda f: f is None }})
    database: Optional[str] = dataclasses.field(default='default', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database'), 'exclude': lambda f: f is None }})
    r"""The default database tables are written to if the source does not specify a namespace. The usual value for this field is \\"default\\"."""
    



class Iceberg(str, Enum):
    ICEBERG = 'iceberg'


class FileStorageFormat(str, Enum):
    PARQUET = 'Parquet'
    AVRO = 'Avro'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FileFormat:
    r"""File format of Iceberg storage."""
    auto_compact: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auto_compact'), 'exclude': lambda f: f is None }})
    r"""Auto compact data files when stream close"""
    compact_target_file_size_in_mb: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compact_target_file_size_in_mb'), 'exclude': lambda f: f is None }})
    r"""Specify the target size of Iceberg data file when performing a compaction action."""
    flush_batch_size: Optional[int] = dataclasses.field(default=10000, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flush_batch_size'), 'exclude': lambda f: f is None }})
    r"""Iceberg data file flush batch size. Incoming rows write to cache firstly; When cache size reaches this 'batch size', flush into real Iceberg data file."""
    format: Optional[FileStorageFormat] = dataclasses.field(default=FileStorageFormat.PARQUET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format'), 'exclude': lambda f: f is None }})
    



class DestinationIcebergStorageType(str, Enum):
    MANAGED = 'MANAGED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServerManaged:
    r"""Server-managed object storage"""
    managed_warehouse_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('managed_warehouse_name') }})
    r"""The name of the managed warehouse"""
    storage_type: Optional[DestinationIcebergStorageType] = dataclasses.field(default=DestinationIcebergStorageType.MANAGED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_type'), 'exclude': lambda f: f is None }})
    



class DestinationIcebergS3BucketRegion(str, Enum):
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    UNKNOWN = ''
    AF_SOUTH_1 = 'af-south-1'
    AP_EAST_1 = 'ap-east-1'
    AP_NORTHEAST_1 = 'ap-northeast-1'
    AP_NORTHEAST_2 = 'ap-northeast-2'
    AP_NORTHEAST_3 = 'ap-northeast-3'
    AP_SOUTH_1 = 'ap-south-1'
    AP_SOUTH_2 = 'ap-south-2'
    AP_SOUTHEAST_1 = 'ap-southeast-1'
    AP_SOUTHEAST_2 = 'ap-southeast-2'
    AP_SOUTHEAST_3 = 'ap-southeast-3'
    AP_SOUTHEAST_4 = 'ap-southeast-4'
    CA_CENTRAL_1 = 'ca-central-1'
    CA_WEST_1 = 'ca-west-1'
    CN_NORTH_1 = 'cn-north-1'
    CN_NORTHWEST_1 = 'cn-northwest-1'
    EU_CENTRAL_1 = 'eu-central-1'
    EU_CENTRAL_2 = 'eu-central-2'
    EU_NORTH_1 = 'eu-north-1'
    EU_SOUTH_1 = 'eu-south-1'
    EU_SOUTH_2 = 'eu-south-2'
    EU_WEST_1 = 'eu-west-1'
    EU_WEST_2 = 'eu-west-2'
    EU_WEST_3 = 'eu-west-3'
    IL_CENTRAL_1 = 'il-central-1'
    ME_CENTRAL_1 = 'me-central-1'
    ME_SOUTH_1 = 'me-south-1'
    SA_EAST_1 = 'sa-east-1'
    US_EAST_1 = 'us-east-1'
    US_EAST_2 = 'us-east-2'
    US_GOV_EAST_1 = 'us-gov-east-1'
    US_GOV_WEST_1 = 'us-gov-west-1'
    US_WEST_1 = 'us-west-1'
    US_WEST_2 = 'us-west-2'


class StorageType(str, Enum):
    S3 = 'S3'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationIcebergS3:
    r"""S3 object storage"""
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    r"""The access key ID to access the S3 bucket. Airbyte requires Read and Write permissions to the given bucket. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>."""
    s3_warehouse_uri: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_warehouse_uri') }})
    r"""The Warehouse Uri for Iceberg"""
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    r"""The corresponding secret to the access key ID. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">here</a>"""
    s3_bucket_region: Optional[DestinationIcebergS3BucketRegion] = dataclasses.field(default=DestinationIcebergS3BucketRegion.UNKNOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region'), 'exclude': lambda f: f is None }})
    r"""The region of the S3 bucket. See <a href=\\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions\\">here</a> for all region codes."""
    s3_endpoint: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_endpoint'), 'exclude': lambda f: f is None }})
    r"""Your S3 endpoint url. Read more <a href=\\"https://docs.aws.amazon.com/general/latest/gr/s3.html#:~:text=Service%20endpoints-,Amazon%20S3%20endpoints,-When%20you%20use\\">here</a>"""
    s3_path_style_access: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_path_style_access'), 'exclude': lambda f: f is None }})
    r"""Use path style access"""
    storage_type: Optional[StorageType] = dataclasses.field(default=StorageType.S3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationIceberg:
    catalog_config: IcebergCatalogConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('catalog_config') }})
    r"""Catalog config of Iceberg."""
    format_config: FileFormat = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format_config') }})
    r"""File format of Iceberg storage."""
    storage_config: StorageConfig = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage_config') }})
    r"""Storage config of Iceberg."""
    DESTINATION_TYPE: Final[Iceberg] = dataclasses.field(default=Iceberg.ICEBERG, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    


IcebergCatalogConfig = Union[HiveCatalogUseApacheHiveMetaStore, HadoopCatalogUseHierarchicalFileSystemsAsSameAsStorageConfig, JdbcCatalogUseRelationalDatabase, RESTCatalog, GlueCatalog]

StorageConfig = Union[DestinationIcebergS3, ServerManaged]