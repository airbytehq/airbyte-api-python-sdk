"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import connectionsresponse as models_connectionsresponse
from typing import List, Optional


@dataclasses.dataclass
class ListConnectionsRequest:
    include_deleted: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'includeDeleted', 'style': 'form', 'explode': True }})
    r"""Include deleted connections in the returned results."""
    limit: Optional[int] = dataclasses.field(default=20, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Set the limit on the number of Connections returned. The default is 20."""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Set the offset to start at when returning Connections. The default is 0"""
    workspace_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceIds', 'style': 'form', 'explode': True }})
    r"""The UUIDs of the workspaces you wish to list connections for. Empty list will retrieve all allowed workspaces."""
    



@dataclasses.dataclass
class ListConnectionsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    connections_response: Optional[models_connectionsresponse.ConnectionsResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    

