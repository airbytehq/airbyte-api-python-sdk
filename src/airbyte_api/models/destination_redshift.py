"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class Redshift(str, Enum):
    REDSHIFT = 'redshift'

class DestinationRedshiftSchemasTunnelMethodTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftPasswordAuthentication:
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[DestinationRedshiftSchemasTunnelMethodTunnelMethod] = dataclasses.field(default=DestinationRedshiftSchemasTunnelMethodTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class DestinationRedshiftSchemasTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftSSHKeyAuthentication:
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[DestinationRedshiftSchemasTunnelMethod] = dataclasses.field(default=DestinationRedshiftSchemasTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class DestinationRedshiftTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshiftNoTunnel:
    TUNNEL_METHOD: Final[DestinationRedshiftTunnelMethod] = dataclasses.field(default=DestinationRedshiftTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    


class DestinationRedshiftSchemasMethod(str, Enum):
    STANDARD = 'Standard'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Standard:
    r"""<i>(not recommended)</i> Direct loading using SQL INSERT statements. This method is extremely inefficient and provided only for quick testing. In all other cases, you should use S3 uploading."""
    METHOD: Final[DestinationRedshiftSchemasMethod] = dataclasses.field(default=DestinationRedshiftSchemasMethod.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    


class DestinationRedshiftEncryptionType(str, Enum):
    AES_CBC_ENVELOPE = 'aes_cbc_envelope'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AESCBCEnvelopeEncryption:
    r"""Staging data will be encrypted using AES-CBC envelope encryption."""
    ENCRYPTION_TYPE: Final[Optional[DestinationRedshiftEncryptionType]] = dataclasses.field(default=DestinationRedshiftEncryptionType.AES_CBC_ENVELOPE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type'), 'exclude': lambda f: f is None }})
    key_encrypting_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key_encrypting_key'), 'exclude': lambda f: f is None }})
    r"""The key, base64-encoded. Must be either 128, 192, or 256 bits. Leave blank to have Airbyte generate an ephemeral key for each sync."""
    


class EncryptionType(str, Enum):
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NoEncryption:
    r"""Staging data will be stored in plaintext."""
    ENCRYPTION_TYPE: Final[Optional[EncryptionType]] = dataclasses.field(default=EncryptionType.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption_type'), 'exclude': lambda f: f is None }})
    


class DestinationRedshiftMethod(str, Enum):
    S3_STAGING = 'S3 Staging'

class DestinationRedshiftS3BucketRegion(str, Enum):
    r"""The region of the S3 staging bucket."""
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AWSS3Staging:
    r"""<i>(recommended)</i> Uploads data to S3 and then uses a COPY to insert the data into Redshift. COPY is recommended for production workloads for better speed and scalability. See <a href=\\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html\\">AWS docs</a> for more details."""
    access_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_key_id') }})
    r"""This ID grants access to the above S3 staging bucket. Airbyte requires Read and Write permissions to the given bucket. See <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">AWS docs</a> on how to generate an access key ID and secret access key."""
    s3_bucket_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_name') }})
    r"""The name of the staging S3 bucket."""
    secret_access_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret_access_key') }})
    r"""The corresponding secret to the above access key id. See <a href=\\"https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys\\">AWS docs</a> on how to generate an access key ID and secret access key."""
    encryption: Optional[Union[NoEncryption, AESCBCEnvelopeEncryption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encryption'), 'exclude': lambda f: f is None }})
    r"""How to encrypt the staging data"""
    file_name_pattern: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name_pattern'), 'exclude': lambda f: f is None }})
    r"""The pattern allows you to set the file-name format for the S3 staging file(s)"""
    METHOD: Final[DestinationRedshiftMethod] = dataclasses.field(default=DestinationRedshiftMethod.S3_STAGING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    purge_staging_data: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purge_staging_data'), 'exclude': lambda f: f is None }})
    r"""Whether to delete the staging files from S3 after completing the sync. See <a href=\\"https://docs.airbyte.com/integrations/destinations/redshift/#:~:text=the%20root%20directory.-,Purge%20Staging%20Data,-Whether%20to%20delete\\"> docs</a> for details."""
    s3_bucket_path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_path'), 'exclude': lambda f: f is None }})
    r"""The directory under the S3 bucket where data will be written. If not provided, then defaults to the root directory. See <a href=\\"https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/faq.html#:~:text=be%20globally%20unique.-,For%20S3%20bucket%20paths,-%2C%20you%20can%20use\\">path's name recommendations</a> for more details."""
    s3_bucket_region: Optional[DestinationRedshiftS3BucketRegion] = dataclasses.field(default=DestinationRedshiftS3BucketRegion.UNKNOWN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('s3_bucket_region'), 'exclude': lambda f: f is None }})
    r"""The region of the S3 staging bucket."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationRedshift:
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Host Endpoint of the Redshift Cluster (must include the cluster-id, region and end with .redshift.amazonaws.com)"""
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password associated with the username."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    DESTINATION_TYPE: Final[Redshift] = dataclasses.field(default=Redshift.REDSHIFT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    disable_type_dedupe: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disable_type_dedupe'), 'exclude': lambda f: f is None }})
    r"""Disable Writing Final Tables. WARNING! The data format in _airbyte_data is likely stable but there are no guarantees that other metadata columns will remain the same in future versions"""
    enable_incremental_final_table_updates: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_incremental_final_table_updates'), 'exclude': lambda f: f is None }})
    r"""When enabled your data will load into your final tables incrementally while your data is still being synced. When Disabled (the default), your data loads into your final tables once at the end of a sync. Note that this option only applies if you elect to create Final tables"""
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    port: Optional[int] = dataclasses.field(default=5439, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the database."""
    raw_data_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw_data_schema'), 'exclude': lambda f: f is None }})
    r"""The schema to write raw tables into"""
    schema: Optional[str] = dataclasses.field(default='public', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema'), 'exclude': lambda f: f is None }})
    r"""The default schema tables are written to if the source does not specify a namespace. Unless specifically configured, the usual value for this field is \\"public\\"."""
    tunnel_method: Optional[Union[DestinationRedshiftNoTunnel, DestinationRedshiftSSHKeyAuthentication, DestinationRedshiftPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    uploading_method: Optional[Union[AWSS3Staging, Standard]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploading_method'), 'exclude': lambda f: f is None }})
    r"""The way data will be uploaded to Redshift."""
    
