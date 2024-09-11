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

<!-- Start Summary [summary] -->
## Summary

airbyte-api: Programatically control Airbyte Cloud, OSS & Enterprise.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed using the *pip* package manager, with dependencies and metadata stored in the `setup.py` file.

```bash
pip install airbyte-api
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [connections](docs/sdks/connections/README.md)

* [create_connection](docs/sdks/connections/README.md#create_connection) - Create a connection
* [delete_connection](docs/sdks/connections/README.md#delete_connection) - Delete a Connection
* [get_connection](docs/sdks/connections/README.md#get_connection) - Get Connection details
* [list_connections](docs/sdks/connections/README.md#list_connections) - List connections
* [patch_connection](docs/sdks/connections/README.md#patch_connection) - Update Connection details

### [destinations](docs/sdks/destinations/README.md)

* [create_destination](docs/sdks/destinations/README.md#create_destination) - Create a destination
* [delete_destination](docs/sdks/destinations/README.md#delete_destination) - Delete a Destination
* [get_destination](docs/sdks/destinations/README.md#get_destination) - Get Destination details
* [list_destinations](docs/sdks/destinations/README.md#list_destinations) - List destinations
* [patch_destination](docs/sdks/destinations/README.md#patch_destination) - Update a Destination
* [put_destination](docs/sdks/destinations/README.md#put_destination) - Update a Destination and fully overwrite it

### [health](docs/sdks/health/README.md)

* [get_health_check](docs/sdks/health/README.md#get_health_check) - Health Check

### [jobs](docs/sdks/jobs/README.md)

* [cancel_job](docs/sdks/jobs/README.md#cancel_job) - Cancel a running Job
* [create_job](docs/sdks/jobs/README.md#create_job) - Trigger a sync or reset job of a connection
* [get_job](docs/sdks/jobs/README.md#get_job) - Get Job status and details
* [list_jobs](docs/sdks/jobs/README.md#list_jobs) - List Jobs by sync type

### [organizations](docs/sdks/organizations/README.md)

* [list_organizations_for_user](docs/sdks/organizations/README.md#list_organizations_for_user) - List all organizations for a user

### [permissions](docs/sdks/permissions/README.md)

* [create_permission](docs/sdks/permissions/README.md#create_permission) - Create a permission
* [delete_permission](docs/sdks/permissions/README.md#delete_permission) - Delete a Permission
* [get_permission](docs/sdks/permissions/README.md#get_permission) - Get Permission details
* [list_permissions](docs/sdks/permissions/README.md#list_permissions) - List Permissions by user id
* [update_permission](docs/sdks/permissions/README.md#update_permission) - Update a permission

### [sources](docs/sdks/sources/README.md)

* [create_source](docs/sdks/sources/README.md#create_source) - Create a source
* [delete_source](docs/sdks/sources/README.md#delete_source) - Delete a Source
* [get_source](docs/sdks/sources/README.md#get_source) - Get Source details
* [initiate_o_auth](docs/sdks/sources/README.md#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](docs/sdks/sources/README.md#list_sources) - List sources
* [patch_source](docs/sdks/sources/README.md#patch_source) - Update a Source
* [put_source](docs/sdks/sources/README.md#put_source) - Update a Source and fully overwrite it

### [streams](docs/sdks/streams/README.md)

* [get_stream_properties](docs/sdks/streams/README.md#get_stream_properties) - Get stream properties

### [users](docs/sdks/users/README.md)

* [list_users_within_an_organization](docs/sdks/users/README.md#list_users_within_an_organization) - List all users within an organization

### [workspaces](docs/sdks/workspaces/README.md)

* [create_or_update_workspace_o_auth_credentials](docs/sdks/workspaces/README.md#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](docs/sdks/workspaces/README.md#create_workspace) - Create a workspace
* [delete_workspace](docs/sdks/workspaces/README.md#delete_workspace) - Delete a Workspace
* [get_workspace](docs/sdks/workspaces/README.md#get_workspace) - Get Workspace details
* [list_workspaces](docs/sdks/workspaces/README.md#list_workspaces) - List workspaces
* [update_workspace](docs/sdks/workspaces/README.md#update_workspace) - Update a workspace
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

### Example

```python
import airbyte_api
from airbyte_api import errors, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

res = None
try:
    res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

except errors.SDKError as e:
    # handle exception
    raise(e)

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.airbyte.com/v1` | None |

#### Example

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    server_idx=0,
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    server_url="https://api.airbyte.com/v1",
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import airbyte_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = airbyte_api.AirbyteAPI(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                 | Type                 | Scheme               |
| -------------------- | -------------------- | -------------------- |
| `basic_auth`         | http                 | HTTP Basic           |
| `bearer_auth`        | http                 | HTTP Bearer          |
| `client_credentials` | oauth2               | OAuth2 token         |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
