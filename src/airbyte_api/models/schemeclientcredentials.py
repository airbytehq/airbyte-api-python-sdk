"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class SchemeClientCredentials:
    client_id: str = dataclasses.field(metadata={'security': { 'field_name': 'clientID' }})
    client_secret: str = dataclasses.field(metadata={'security': { 'field_name': 'clientSecret' }})
    token_url: str = dataclasses.field(default='/applications/token')
    

