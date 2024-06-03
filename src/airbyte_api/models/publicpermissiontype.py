"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PublicPermissionType(str, Enum):
    r"""Subset of `PermissionType` (removing `instance_admin`), could be used in public-api."""
    ORGANIZATION_ADMIN = 'organization_admin'
    ORGANIZATION_EDITOR = 'organization_editor'
    ORGANIZATION_READER = 'organization_reader'
    ORGANIZATION_MEMBER = 'organization_member'
    WORKSPACE_ADMIN = 'workspace_admin'
    WORKSPACE_EDITOR = 'workspace_editor'
    WORKSPACE_READER = 'workspace_reader'