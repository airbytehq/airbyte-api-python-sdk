"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import tagpatchrequest as models_tagpatchrequest
from ..models import tagresponse as models_tagresponse
from typing import Optional


@dataclasses.dataclass
class UpdateTagRequest:
    tag_patch_request: models_tagpatchrequest.TagPatchRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    tag_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tagId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateTagResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    tag_response: Optional[models_tagresponse.TagResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    

