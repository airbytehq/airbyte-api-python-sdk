"""Post-generation patch pipeline.

Runs after Speakeasy code generation to apply durable fixes to generated code.
See the terraform-provider-airbyte repo for more examples of post-generation patches.
"""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = REPO_ROOT / "src" / "airbyte_api" / "_version.py"


def patch_version_file() -> None:
    """Replace the hardcoded `__version__` in `_version.py` with a dynamic lookup.

    Speakeasy generates a `_version.py` with a hardcoded `__version__` string
    and a static `__user_agent__`.  This patch rewrites both so that the
    installed package version (set at build time by `uv-dynamic-versioning`
    from the git tag) is used instead.  Generation metadata
    (`__openapi_doc_version__`, `__gen_version__`) is left intact.
    """
    text = VERSION_FILE.read_text()
    original = text

    # 1. Replace the hardcoded __version__ assignment with importlib.metadata lookup.
    #    Matches:  __version__: str = "1.0.0"  (any semver-ish string)
    text = re.sub(
        r'^__version__: str = ".*"$',
        "__version__: str = importlib.metadata.version(__title__)",
        text,
        count=1,
        flags=re.MULTILINE,
    )

    # 2. Replace the static __user_agent__ string with an f-string using the
    #    dynamic __version__.
    #    Matches:  __user_agent__: str = "speakeasy-sdk/python 1.0.0 2.911.0 1.0.0 airbyte-api"
    text = re.sub(
        r'^__user_agent__: str = "speakeasy-sdk/python .+"$',
        (
            "__user_agent__: str = (\n"
            '    f"speakeasy-sdk/python {__version__} {__gen_version__}"\n'
            '    f" {__openapi_doc_version__} {__title__}"\n'
            ")"
        ),
        text,
        count=1,
        flags=re.MULTILINE,
    )

    # 3. Remove the stale try/except block that attempted to override __version__
    #    at runtime (no longer needed since the assignment itself is now dynamic).
    text = re.sub(
        r"\ntry:\n    if __package__.*?\nexcept.*?\n    pass\n",
        "\n",
        text,
        count=1,
        flags=re.DOTALL,
    )

    if text == original:
        print("post_generate: _version.py already patched (no changes)")
        return

    VERSION_FILE.write_text(text)
    print("post_generate: patched _version.py (hardcoded __version__ → importlib.metadata)")


def main() -> None:
    patch_version_file()


if __name__ == "__main__":
    main()
