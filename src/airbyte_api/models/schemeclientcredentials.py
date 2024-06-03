"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Final


@dataclasses.dataclass
class SchemeClientCredentials:
    client_id: str = dataclasses.field(metadata={'security': { 'field_name': 'clientID' }})
    client_secret: str = dataclasses.field(metadata={'security': { 'field_name': 'clientSecret' }})
    TOKEN_URL: Final[str] = dataclasses.field(default='/api/v1/applications/token')
    
