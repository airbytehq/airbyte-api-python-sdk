"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class ConnectionSyncModeEnum(str, Enum):
    FULL_REFRESH_OVERWRITE = 'full_refresh_overwrite'
    FULL_REFRESH_APPEND = 'full_refresh_append'
    INCREMENTAL_APPEND = 'incremental_append'
    INCREMENTAL_DEDUPED_HISTORY = 'incremental_deduped_history'
