<div align="center">
        <img src="https://user-images.githubusercontent.com/68016351/222853569-b35cc448-6481-4cf2-a237-bd5da47e94fd.png" width="500">
   <p>Programatically control Airbyte Cloud through an API.</p>
   <a href="https://reference.airbyte.com/reference/start"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
   <a href="https://github.com/airbytehq/airbyte-api-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/airbytehq/airbyte-api-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/airbytehq/airbyte-api-python-sdk/releases"><img src="https://img.shields.io/github/v/release/airbytehq/airbyte-api-python-sdk?sort=semver&style=for-the-badge" /></a>
</div>

## Authentication

Developers will need to create an API Key within your [Developer Portal](https://portal.airbyte.com/) to make API requests. You can use your existing Airbyte account to log in to the Developer Portal. Once you are in the Developer Portal, use the API Keys tab to create or remove API Keys. You can see a [walkthrough demo here](https://www.loom.com/share/7997a7c67cd642cc8d1c72ef0dfcc4bc)🎦

The Developer Portal UI can also be used to help build your integration by showing information about network requests in the Requests tab. API usage information is also available to you in the Usage tab.

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install airbyte-api
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'distinctio',
                    'quibusdam',
                    'unde',
                ],
                name='Johnnie Stamm',
                primary_key=[
                    [
                        'iure',
                        'magnam',
                    ],
                    [
                        'ipsa',
                        'delectus',
                        'tempora',
                        'suscipit',
                    ],
                    [
                        'minus',
                        'placeat',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'excepturi',
                    'nisi',
                ],
                name='Jake Bernier MD',
                primary_key=[
                    [
                        'repellendus',
                        'sapiente',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'at',
                ],
                name='Emilio Krajcik',
                primary_key=[
                    [
                        'porro',
                        'dolorum',
                        'dicta',
                    ],
                    [
                        'officia',
                        'occaecati',
                        'fugit',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.EU,
    destination_id='c816742c-b739-4205-9293-96fea7596eb1',
    name='Lela Orn',
    namespace_definition=shared.NamespaceDefinitionEnum.SOURCE,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.IGNORE,
    prefix='corporis',
    schedule=shared.ConnectionScheduleCreate(
        cron_expression='explicabo',
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='5955907a-ff1a-43a2-ba94-67739251aa52',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [connections](docs/connections/README.md)

* [create_connection](docs/connections/README.md#create_connection) - Create a connection
* [delete_connection](docs/connections/README.md#delete_connection) - Delete a Connection
* [get_connection](docs/connections/README.md#get_connection) - Get Connection details
* [list_connections](docs/connections/README.md#list_connections) - List connections

### [destinations](docs/destinations/README.md)

* [create_destination](docs/destinations/README.md#create_destination) - Create a destination
* [delete_destination](docs/destinations/README.md#delete_destination) - Delete a Destination
* [get_destination](docs/destinations/README.md#get_destination) - Get Destination details
* [list_destinations](docs/destinations/README.md#list_destinations) - List destinations

### [jobs](docs/jobs/README.md)

* [cancel_job](docs/jobs/README.md#cancel_job) - Cancel a running Job
* [create_job](docs/jobs/README.md#create_job) - Trigger a sync or reset job of a connection
* [get_job](docs/jobs/README.md#get_job) - Get Job status and details
* [list_jobs](docs/jobs/README.md#list_jobs) - List Jobs by sync type

### [sources](docs/sources/README.md)

* [create_source](docs/sources/README.md#create_source) - Create a source
* [delete_source](docs/sources/README.md#delete_source) - Delete a Source
* [get_source](docs/sources/README.md#get_source) - Get Source details
* [initiate_o_auth](docs/sources/README.md#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](docs/sources/README.md#list_sources) - List sources

### [streams](docs/streams/README.md)

* [get_stream_properties](docs/streams/README.md#get_stream_properties) - Get stream properties

### [workspaces](docs/workspaces/README.md)

* [create_or_update_workspace_o_auth_credentials](docs/workspaces/README.md#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](docs/workspaces/README.md#create_workspace) - Create a workspace
* [delete_workspace](docs/workspaces/README.md#delete_workspace) - Delete a Workspace
* [get_workspace](docs/workspaces/README.md#get_workspace) - Get Workspace details
* [list_workspaces](docs/workspaces/README.md#list_workspaces) - List workspaces
* [update_workspace](docs/workspaces/README.md#update_workspace) - Update a workspace
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
