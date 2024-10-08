"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import destinationresponse as models_destinationresponse
from typing import Optional


@dataclasses.dataclass
class GetDestinationRequest:
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetDestinationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    destination_response: Optional[models_destinationresponse.DestinationResponse] = dataclasses.field(default=None)
    r"""Get a Destination by the id in the path."""
    

