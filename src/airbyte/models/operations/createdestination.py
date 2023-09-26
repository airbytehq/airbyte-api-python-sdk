"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationresponse as shared_destinationresponse
from typing import Optional



@dataclasses.dataclass
class CreateDestinationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    destination_response: Optional[shared_destinationresponse.DestinationResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

