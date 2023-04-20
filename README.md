<div align="center">
    <picture>
        <img src="https://user-images.githubusercontent.com/68016351/222853569-b35cc448-6481-4cf2-a237-bd5da47e94fd.png" width="500">
    </picture>
   <p>Programatically control Airbyte Cloud through an API.</p>
   <a href="https://reference.airbyte.com/reference/start"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
   <a href="https://github.com/airbytehq/airbyte-api-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte-api-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/airbytehq/airbyte-api-python-sdk/releases"><img src="https://img.shields.io/github/v/release/airbytehq/airbyte-api-python-sdk?sort=semver&style=for-the-badge" /></a>
</div>

## Authentication

Developers will need to create an API Key within your [Developer Portal](https://portal.airbyte.com/) to make API requests. You can use your existing Airbyte account to log in to the Developer Portal. Once you are in the Developer Portal, use the API Keys tab to create or remove API Keys. You can see a [walkthrough demo here](https://www.loom.com/share/7997a7c67cd642cc8d1c72ef0dfcc4bc)🎦

The Developer Portal UI can also be used to help build your integration by showing information about network requests in the Requests tab. API usage information is also available to you in the Usage tab.

***(Installation will not work until published to a package manager, please clone locally and run `pip install -e ../path/to/local/clone` to try out the artifact locally)***

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install airbyte
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    "distinctio",
                    "quibusdam",
                    "unde",
                ],
                name="Johnnie Stamm",
                primary_key=[
                    [
                        "iure",
                        "magnam",
                    ],
                    [
                        "ipsa",
                        "delectus",
                        "tempora",
                        "suscipit",
                    ],
                    [
                        "minus",
                        "placeat",
                    ],
                ],
                sync_mode="incremental_append",
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    "excepturi",
                    "nisi",
                ],
                name="Jake Bernier MD",
                primary_key=[
                    [
                        "repellendus",
                        "sapiente",
                    ],
                ],
                sync_mode="incremental_deduped_history",
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    "at",
                ],
                name="Emilio Krajcik",
                primary_key=[
                    [
                        "porro",
                        "dolorum",
                        "dicta",
                    ],
                    [
                        "officia",
                        "occaecati",
                        "fugit",
                    ],
                ],
                sync_mode="incremental_append",
            ),
        ],
    ),
    data_residency="eu",
    destination_id="c816742c-b739-4205-9293-96fea7596eb1",
    name="Lela Orn",
    namespace_definition="source",
    namespace_format="${SOURCE_NAMESPACE}",
    prefix="dolorem",
    schedule=shared.ConnectionScheduleCreate(
        cron_expression="corporis",
        schedule_type="manual",
    ),
    source_id="c5955907-aff1-4a3a-afa9-467739251aa5",
)
    
res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### connections

* `create_connection` - Create a connection
* `delete_connection` - Delete a Connection
* `get_connection` - Get Connection details
* `list_connections` - List connections

### destinations

* `create_destination` - Create a destination
* `delete_destination` - Delete a Destination
* `get_destination` - Get Destination details
* `list_destinations` - List destinations

### jobs

* `cancel_job` - Cancel a running Job
* `create_job` - Trigger a sync or reset job of a connection
* `get_job` - Get Job status and details
* `list_jobs` - List Jobs by sync type

### sources

* `create_source` - Create a source
* `delete_source` - Delete a Source
* `get_source` - Get Source details
* `initiate_o_auth` - Initiate OAuth for a source
* `list_sources` - List sources

### streams

* `get_stream_properties` - Get stream properties

### workspaces

* `create_or_update_workspace_o_auth_credentials` - Create OAuth override credentials for a workspace and source type.
* `create_workspace` - Create a workspace
* `get_workspace` - Get Workspace details
* `list_workspaces` - List workspaces
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
