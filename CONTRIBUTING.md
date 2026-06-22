# Contributing to This Repository

## Important: This is a Generated Codebase

> **Note:** This repository contains predominantly generated code. We do not accept direct changes to generated files. Report issues on GitHub or submit fixes to the upstream OpenAPI spec in [airbyte-platform](https://github.com/airbytehq/airbyte-platform).

## Code Generation Lineage

The Python SDK is generated through a multi-step pipeline:

```
┌──────────────────────────────────────────┐
│  1. Upstream OpenAPI Spec                │
│  (airbyte-platform / api_sdk.yaml)       │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│  2. Speakeasy Overlay (optional)         │
│  (overlays/python_speakeasy.yaml)        │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│  3. Speakeasy Code Generation            │
│  (src/airbyte_api/)                      │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│  4. Post-Generation Patches              │
│  (scripts/post_generate.py)              │
└──────────────────┬───────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────┐
│  5. Package Build & Publish              │
│  (pyproject.toml → PyPI)                 │
└──────────────────────────────────────────┘
```

### Step-by-step details

1. **Upstream OpenAPI Spec** — The source-of-truth API definition lives in `airbyte-platform`:
   [`airbyte-api/server-api/src/main/openapi/api_sdk.yaml`](https://github.com/airbytehq/airbyte-platform/blob/main/airbyte-api/server-api/src/main/openapi/api_sdk.yaml)

2. **Speakeasy Overlay** — Python SDK-specific customizations applied on top of the upstream spec before code generation (currently a no-op placeholder):
   [`overlays/python_speakeasy.yaml`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/overlays/python_speakeasy.yaml)

3. **Speakeasy Code Generation** — Speakeasy consumes the spec (+ overlay if enabled) and generates the Python SDK in `src/airbyte_api/`. These files should never be edited by hand.

4. **Post-Generation Patches** — A Python script applies any SDK-specific patches after generation (currently a no-op placeholder):
   [`scripts/post_generate.py`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/scripts/post_generate.py)

5. **Package Build & Publish** — The generated SDK is built with `uv build` and published to PyPI via OIDC trusted publishing.

> **Tip:** If you need to change SDK behavior, determine which layer is appropriate:
> - **API changes** → submit to the [upstream OpenAPI spec](https://github.com/airbytehq/airbyte-platform/blob/main/airbyte-api/server-api/src/main/openapi/api_sdk.yaml)
> - **Python SDK-specific schema tweaks** → modify the [overlay](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/overlays/python_speakeasy.yaml)
> - **Post-generation fixes** → modify the [post-generate script](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/scripts/post_generate.py)
> - Then trigger regeneration (see below)

## For Maintainers

### Regenerating the SDK

Use the GitHub Actions workflow: [Actions > Generate SDK](https://github.com/airbytehq/airbyte-api-python-sdk/actions/workflows/generate-command.yml) > Run workflow

Or comment `/generate` on any PR to regenerate and push results to the PR branch.

### Release Process

Releases use a draft-based workflow:

1. The `release-drafter.yml` workflow runs on every push to main, creating/updating a draft release
2. Review the draft at [Releases](https://github.com/airbytehq/airbyte-api-python-sdk/releases)
3. Edit the draft version if needed
4. Click "Publish release" — this triggers PyPI publication via OIDC

### Pre-Release Process

Pre-releases let you publish an SDK version for testing without making it the default on PyPI.

**Two ways to trigger a pre-release:**

1. **Slash command on a PR** (recommended for PR-based work):
   ```
   /pre-release version=1.0.0rc1
   ```
   This builds from the PR's head branch.

2. **Manual workflow dispatch** (from the [Actions tab](https://github.com/airbytehq/airbyte-api-python-sdk/actions/workflows/pre-release-command.yml)):
   - **version** (required): e.g. `1.0.0rc1`, `1.0.0a1`. Must be valid PEP 440 with a pre-release suffix.
   - **ref** (optional, default: `main`): branch, tag, or commit SHA to build from.

**Using a pre-release:**

```bash
pip install airbyte-api==1.0.0rc1
```

### Debugging Generation Drift Failures

When the zero-diff CI check fails, it means the committed code doesn't match what the generation pipeline produces. To debug:

1. Download the generated artifacts from the failed CI run:
   ```bash
   gh run download <RUN_ID> --name generated_sdk_code --dir /tmp/generated_from_ci
   ```

2. Compare against committed code:
   ```bash
   diff -rq src/ /tmp/generated_from_ci/src/
   ```

3. Fix the root cause at the appropriate layer (overlay, post-generate script, or upstream spec), then comment `/generate` on the PR.

## Speakeasy CLI Version

The Speakeasy CLI version is pinned in [`.github/speakeasy/dummy-compose.yml`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/.github/speakeasy/dummy-compose.yml) and bumped by Dependabot's `docker-compose` ecosystem. The `.speakeasy/workflow.yaml` uses `speakeasyVersion: pinned` to consume whatever version is installed.

## Build Tasks

Build tasks are defined in [`poe_tasks.toml`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/main/poe_tasks.toml) and run via [poethepoet](https://poethepoet.natn.io/):

```bash
uvx --from=poethepoet poe generate-code   # Generate SDK from spec
uvx --from=poethepoet poe post-generate    # Run post-generation patches
uvx --from=poethepoet poe generate-full    # Full pipeline (generate + patches)
uvx --from=poethepoet poe lint             # Run linting checks
uvx --from=poethepoet poe fix              # Auto-fix lint/formatting
uvx --from=poethepoet poe test             # Run tests
uvx --from=poethepoet poe typecheck        # Run type checking
```

## How to Report Issues

If you encounter bugs or have suggestions, please [open an issue](https://github.com/airbytehq/airbyte-api-python-sdk/issues/new). Include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected and actual behavior
- Any relevant logs or error messages
- SDK version and Python version
