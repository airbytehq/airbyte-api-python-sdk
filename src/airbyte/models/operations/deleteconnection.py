"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class DeleteConnectionRequest:
    
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})

    

@dataclasses.dataclass
class DeleteConnectionResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    