"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional, Union


class SourceJotformSchemasAPIEndpoint(str, Enum):
    ENTERPRISE = 'enterprise'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Enterprise:
    enterprise_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enterprise_url') }})
    r"""Upgrade to Enterprise to make your API url your-domain.com/API or subdomain.jotform.com/API instead of api.jotform.com"""
    API_ENDPOINT: Final[Optional[SourceJotformSchemasAPIEndpoint]] = dataclasses.field(default=SourceJotformSchemasAPIEndpoint.ENTERPRISE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_endpoint'), 'exclude': lambda f: f is None }})
    



class SourceJotformAPIEndpoint(str, Enum):
    BASIC = 'basic'


class BaseURLPrefix(str, Enum):
    r"""You can access our API through the following URLs - Standard API Usage (Use the default API URL - https://api.jotform.com), For EU (Use the EU API URL - https://eu-api.jotform.com), For HIPAA (Use the HIPAA API URL - https://hipaa-api.jotform.com)"""
    STANDARD = 'Standard'
    EU = 'EU'
    HIPAA = 'HIPAA'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Basic:
    API_ENDPOINT: Final[Optional[SourceJotformAPIEndpoint]] = dataclasses.field(default=SourceJotformAPIEndpoint.BASIC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_endpoint'), 'exclude': lambda f: f is None }})
    url_prefix: Optional[BaseURLPrefix] = dataclasses.field(default=BaseURLPrefix.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url_prefix'), 'exclude': lambda f: f is None }})
    r"""You can access our API through the following URLs - Standard API Usage (Use the default API URL - https://api.jotform.com), For EU (Use the EU API URL - https://eu-api.jotform.com), For HIPAA (Use the HIPAA API URL - https://hipaa-api.jotform.com)"""
    



class Jotform(str, Enum):
    JOTFORM = 'jotform'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceJotform:
    api_endpoint: APIEndpoint = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_endpoint') }})
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    end_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    SOURCE_TYPE: Final[Jotform] = dataclasses.field(default=Jotform.JOTFORM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    


APIEndpoint = Union[Basic, Enterprise]
