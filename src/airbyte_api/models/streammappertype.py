"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class StreamMapperType(str, Enum):
    HASHING = 'hashing'
    FIELD_RENAMING = 'field-renaming'
    ROW_FILTERING = 'row-filtering'
    ENCRYPTION = 'encryption'