"""Runtime version and Speakeasy generation metadata.

__version__ is resolved from installed package metadata (set at build time
by uv-dynamic-versioning from the git tag).  The remaining constants are
Speakeasy generation metadata updated on each regeneration.
"""

import importlib.metadata

__title__: str = "airbyte-api"

try:
    __version__: str = importlib.metadata.version(__title__)
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"

__openapi_doc_version__: str = "1.0.0"
__gen_version__: str = "2.911.0"
__user_agent__: str = (
    f"speakeasy-sdk/python {__version__} {__gen_version__}"
    f" {__openapi_doc_version__} {__title__}"
)
