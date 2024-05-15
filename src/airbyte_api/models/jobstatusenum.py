"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class JobStatusEnum(str, Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    INCOMPLETE = 'incomplete'
    FAILED = 'failed'
    SUCCEEDED = 'succeeded'
    CANCELLED = 'cancelled'
