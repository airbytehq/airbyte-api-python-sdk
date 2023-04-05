"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sdk import utils
from typing import Optional

class SourceAmazonSellerPartnerAuthTypeEnum(str, Enum):
    OAUTH2_0 = 'oauth2.0'

class SourceAmazonSellerPartnerAWSEnvironmentEnum(str, Enum):
    r"""An enumeration."""
    PRODUCTION = 'PRODUCTION'
    SANDBOX = 'SANDBOX'

class SourceAmazonSellerPartnerAWSRegionEnum(str, Enum):
    r"""An enumeration."""
    AE = 'AE'
    AU = 'AU'
    BE = 'BE'
    BR = 'BR'
    CA = 'CA'
    DE = 'DE'
    EG = 'EG'
    ES = 'ES'
    FR = 'FR'
    GB = 'GB'
    IN = 'IN'
    IT = 'IT'
    JP = 'JP'
    MX = 'MX'
    NL = 'NL'
    PL = 'PL'
    SA = 'SA'
    SE = 'SE'
    SG = 'SG'
    TR = 'TR'
    UK = 'UK'
    US = 'US'

class SourceAmazonSellerPartnerAmazonSellerPartnerEnum(str, Enum):
    AMAZON_SELLER_PARTNER = 'amazon-seller-partner'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAmazonSellerPartner:
    r"""The values required to configure the source."""
    
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id') }})
    r"""Your Amazon App ID"""  
    aws_environment: SourceAmazonSellerPartnerAWSEnvironmentEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_environment') }})
    r"""An enumeration."""  
    lwa_app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lwa_app_id') }})
    r"""Your Login with Amazon Client ID."""  
    lwa_client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lwa_client_secret') }})
    r"""Your Login with Amazon Client Secret."""  
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The Refresh Token obtained via OAuth flow authorization."""  
    region: SourceAmazonSellerPartnerAWSRegionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('region') }})
    r"""An enumeration."""  
    replication_start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_start_date') }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""  
    source_type: SourceAmazonSellerPartnerAmazonSellerPartnerEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})  
    auth_type: Optional[SourceAmazonSellerPartnerAuthTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})  
    aws_access_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_access_key'), 'exclude': lambda f: f is None }})
    r"""Specifies the AWS access key used as part of the credentials to authenticate the user."""  
    aws_secret_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_key'), 'exclude': lambda f: f is None }})
    r"""Specifies the AWS secret key used as part of the credentials to authenticate the user."""  
    max_wait_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_wait_seconds'), 'exclude': lambda f: f is None }})
    r"""Sometimes report can take up to 30 minutes to generate. This will set the limit for how long to wait for a successful report."""  
    period_in_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period_in_days'), 'exclude': lambda f: f is None }})
    r"""Will be used for stream slicing for initial full_refresh sync when no updated state is present for reports that support sliced incremental sync."""  
    replication_end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_end_date'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data after this date will not be replicated."""  
    report_options: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('report_options'), 'exclude': lambda f: f is None }})
    r"""Additional information passed to reports. This varies by report type. Must be a valid json string."""  
    role_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role_arn'), 'exclude': lambda f: f is None }})
    r"""Specifies the Amazon Resource Name (ARN) of an IAM role that you want to use to perform operations requested using this profile. (Needs permission to 'Assume Role' STS)."""  
    