"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import connectionresponse as models_connectionresponse
from typing import Optional


@dataclasses.dataclass
class GetConnectionRequest:
    connection_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'connectionId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetConnectionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connection_response: Optional[models_connectionresponse.ConnectionResponse] = dataclasses.field(default=None)
    r"""Get a Connection by the id in the path."""
    

