"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..models import jobsresponse as models_jobsresponse
from ..models import jobstatusenum as models_jobstatusenum
from ..models import jobtypeenum as models_jobtypeenum
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class ListJobsRequest:
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'connectionId', 'style': 'form', 'explode': True }})
    r"""Filter the Jobs by connectionId."""
    created_at_end: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'createdAtEnd', 'style': 'form', 'explode': True }})
    r"""The end date to filter by"""
    created_at_start: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'createdAtStart', 'style': 'form', 'explode': True }})
    r"""The start date to filter by"""
    job_type: Optional[models_jobtypeenum.JobTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'jobType', 'style': 'form', 'explode': True }})
    r"""Filter the Jobs by jobType."""
    limit: Optional[int] = dataclasses.field(default=20, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Set the limit on the number of Jobs returned. The default is 20 Jobs."""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Set the offset to start at when returning Jobs. The default is 0."""
    order_by: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'orderBy', 'style': 'form', 'explode': True }})
    r"""The field and method to use for ordering. Currently allowed are createdAt and updatedAt."""
    status: Optional[models_jobstatusenum.JobStatusEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'status', 'style': 'form', 'explode': True }})
    r"""The Job status you want to filter by"""
    updated_at_end: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updatedAtEnd', 'style': 'form', 'explode': True }})
    r"""The end date to filter by"""
    updated_at_start: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'updatedAtStart', 'style': 'form', 'explode': True }})
    r"""The start date to filter by"""
    workspace_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceIds', 'style': 'form', 'explode': True }})
    r"""The UUIDs of the workspaces you wish to list jobs for. Empty list will retrieve all allowed workspaces."""
    



@dataclasses.dataclass
class ListJobsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    jobs_response: Optional[models_jobsresponse.JobsResponse] = dataclasses.field(default=None)
    r"""List all the Jobs by connectionId."""
    
