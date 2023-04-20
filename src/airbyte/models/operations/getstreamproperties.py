"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import streamproperties as shared_streamproperties
from typing import Optional


@dataclasses.dataclass
class GetStreamPropertiesRequest:
    
    destination_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'destinationId', 'style': 'form', 'explode': True }})
    r"""ID of the destination"""  
    source_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'sourceId', 'style': 'form', 'explode': True }})
    r"""ID of the source"""  
    

@dataclasses.dataclass
class GetStreamPropertiesResponse:
    
    content_type: str = dataclasses.field()  
    status_code: int = dataclasses.field()  
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)  
    stream_properties: Optional[shared_streamproperties.StreamProperties] = dataclasses.field(default=None)
    r"""Get the available streams properties for a source/destination pair."""  
    