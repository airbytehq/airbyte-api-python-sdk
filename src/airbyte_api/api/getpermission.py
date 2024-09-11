"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import permissionresponse as models_permissionresponse
from typing import Optional


@dataclasses.dataclass
class GetPermissionRequest:
    permission_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'permissionId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetPermissionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    permission_response: Optional[models_permissionresponse.PermissionResponse] = dataclasses.field(default=None)
    r"""Get a Permission by the id in the path."""
    

