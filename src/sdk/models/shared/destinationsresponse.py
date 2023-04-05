"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import destinationresponse as shared_destinationresponse
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationsResponse:
    r"""Successful operation"""
    
    data: list[shared_destinationresponse.DestinationResponse] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data') }})  
    next: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('next') }})  
    previous: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previous') }})  
    