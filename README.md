# public-api

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/airbytehq/airbyte-api-python-sdk.git
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
    destination_id="89bd9d8d-69a6-474e-8f46-7cc8796ed151",
    geography="us",
    name="perferendis",
    schedule=shared.ConnectionScheduleCreate(
        cron_expression="ipsam",
        schedule_type="cron",
    ),
    source_id="fc2ddf7c-c78c-4a1b-a928-fc816742cb73",
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
* `get_connection` - Get Connection details
* `list_connections` - List connections

### destinations

* `create_destination` - Create a destination
* `get_destination` - Get Destination details
* `list_destinations` - List destinations

### jobs

* `cancel_job` - Cancel a running Job
* `create_job` - Trigger a sync or reset job of a connection
* `get_job` - Get Job status and details
* `list_jobs` - List Jobs by sync type

### sources

* `create_source` - Create a source
* `get_source` - Get Source details
* `list_sources` - List sources

### workspaces

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
