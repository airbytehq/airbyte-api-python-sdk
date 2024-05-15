"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional


class AwsCloudtrail(str, Enum):
    AWS_CLOUDTRAIL = 'aws-cloudtrail'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAwsCloudtrail:
    aws_key_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_key_id') }})
    r"""AWS CloudTrail Access Key ID. See the <a href=\\"https://docs.airbyte.com/integrations/sources/aws-cloudtrail\\">docs</a> for more information on how to obtain this key."""
    aws_region_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_region_name') }})
    r"""The default AWS Region to use, for example, us-west-1 or us-west-2. When specifying a Region inline during client initialization, this property is named region_name."""
    aws_secret_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aws_secret_key') }})
    r"""AWS CloudTrail Access Key ID. See the <a href=\\"https://docs.airbyte.com/integrations/sources/aws-cloudtrail\\">docs</a> for more information on how to obtain this key."""
    SOURCE_TYPE: Final[AwsCloudtrail] = dataclasses.field(default=AwsCloudtrail.AWS_CLOUDTRAIL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('1970-01-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date you would like to replicate data. Data in AWS CloudTrail is available for last 90 days only. Format: YYYY-MM-DD."""
    

