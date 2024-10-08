"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import permissionsresponse as models_permissionsresponse
from typing import Optional


@dataclasses.dataclass
class ListPermissionsRequest:
    organization_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'organizationId', 'style': 'form', 'explode': True }})
    r"""This is required if you want to read someone else's permissions, and you should have organization admin or a higher role."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'userId', 'style': 'form', 'explode': True }})
    r"""User Id in permission."""
    



@dataclasses.dataclass
class ListPermissionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    permissions_response: Optional[models_permissionsresponse.PermissionsResponse] = dataclasses.field(default=None)
    r"""List Permissions."""
    

