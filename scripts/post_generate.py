"""Post-generation patch pipeline (no-op placeholder).

This script runs after Speakeasy code generation to apply any
Python SDK-specific patches. Currently no patches are needed.

Add patch functions here when durable fixes to generated code are required.
See the terraform-provider-airbyte repo for examples of post-generation patches.
"""


def main() -> None:
    print("post_generate: no patches to apply (no-op)")


if __name__ == "__main__":
    main()
