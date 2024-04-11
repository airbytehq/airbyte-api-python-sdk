"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte_api import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final

class Marketo(str, Enum):
    MARKETO = 'marketo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMarketo:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Marketo developer application. See <a href=\\"https://docs.airbyte.com/integrations/sources/marketo\\"> the docs </a> for info on how to obtain this."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Marketo developer application. See <a href=\\"https://docs.airbyte.com/integrations/sources/marketo\\"> the docs </a> for info on how to obtain this."""
    domain_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain_url') }})
    r"""Your Marketo Base URL. See <a href=\\"https://docs.airbyte.com/integrations/sources/marketo\\"> the docs </a> for info on how to obtain this."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[Marketo] = dataclasses.field(default=Marketo.MARKETO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    
