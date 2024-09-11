"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class NamespaceDefinitionEnum(str, Enum):
    r"""Define the location where the data will be stored in the destination"""
    SOURCE = 'source'
    DESTINATION = 'destination'
    CUSTOM_FORMAT = 'custom_format'
