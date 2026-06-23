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

airbyte-api: Programmatically control Airbyte Cloud, OSS & Enterprise.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [Authentication](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#authentication)
  * [SDK Installation](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#sdk-installation)
  * [IDE Support](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#ide-support)
  * [SDK Example Usage](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#sdk-example-usage)
  * [Available Resources and Operations](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#available-resources-and-operations)
  * [Retries](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#retries)
  * [Error Handling](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#error-handling)
  * [Server Selection](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#server-selection)
  * [Custom HTTP Client](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#custom-http-client)
  * [Authentication](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#authentication-1)
  * [Resource Management](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#resource-management)
  * [Debugging](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./#debugging)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add airbyte-api
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install airbyte-api
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add airbyte-api
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from airbyte-api python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "airbyte-api",
# ]
# ///

from airbyte_api import AirbyteAPI

sdk = AirbyteAPI(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from airbyte_api import AirbyteAPI, models
import asyncio

async def main():

    async with AirbyteAPI(
        security=models.Security(
            basic_auth=models.SchemeBasicAuth(
                password="",
                username="",
            ),
        ),
    ) as aa_client:

        res = await aa_client.connections.create_connection_async(request={
            "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
            "name": "Postgres-to-Bigquery",
            "namespace_format": "${SOURCE_NAMESPACE}",
            "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
        })

        assert res.connection_response is not None

        # Handle response
        print(res.connection_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Connections](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md)

* [create_connection](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md#create_connection) - Create a connection
* [delete_connection](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md#delete_connection) - Delete a Connection
* [get_connection](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md#get_connection) - Get Connection details
* [list_connections](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md#list_connections) - List connections
* [patch_connection](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/connections/README.md#patch_connection) - Update Connection details

### [DeclarativeSourceDefinitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md)

* [create_declarative_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md#create_declarative_source_definition) - Create a declarative source definition.
* [delete_declarative_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md#delete_declarative_source_definition) - Delete a declarative source definition.
* [get_declarative_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md#get_declarative_source_definition) - Get declarative source definition details.
* [list_declarative_source_definitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md#list_declarative_source_definitions) - List declarative source definitions.
* [update_declarative_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/declarativesourcedefinitions/README.md#update_declarative_source_definition) - Update declarative source definition details.

### [DestinationDefinitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md)

* [create_destination_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md#create_destination_definition) - Create a destination definition.
* [delete_destination_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md#delete_destination_definition) - Delete a destination definition.
* [get_destination_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md#get_destination_definition) - Get destination definition details.
* [list_destination_definitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md#list_destination_definitions) - List destination definitions.
* [update_destination_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinationdefinitions/README.md#update_destination_definition) - Update destination definition details.

### [Destinations](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md)

* [create_destination](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#create_destination) - Create a destination
* [delete_destination](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#delete_destination) - Delete a Destination
* [get_destination](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#get_destination) - Get Destination details
* [list_destinations](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#list_destinations) - List destinations
* [patch_destination](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#patch_destination) - Update a Destination
* [put_destination](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/destinations/README.md#put_destination) - Update a Destination and fully overwrite it

### [Health](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/health/README.md)

* [get_health_check](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/health/README.md#get_health_check) - Health Check

### [Jobs](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/jobs/README.md)

* [cancel_job](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/jobs/README.md#cancel_job) - Cancel a running Job
* [create_job](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/jobs/README.md#create_job) - Trigger a sync or reset job of a connection
* [get_job](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/jobs/README.md#get_job) - Get Job status and details
* [list_jobs](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/jobs/README.md#list_jobs) - List Jobs by sync type

### [Organizations](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/organizations/README.md)

* [create_or_update_organization_o_auth_credentials](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/organizations/README.md#create_or_update_organization_o_auth_credentials) - Create OAuth override credentials for an organization and source type.
* [delete_organization_o_auth_credentials](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/organizations/README.md#delete_organization_o_auth_credentials) - Delete OAuth override credentials for an organization and source/destination type.
* [list_organizations_for_user](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/organizations/README.md#list_organizations_for_user) - List all organizations for a user

### [Permissions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md)

* [create_permission](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md#create_permission) - Create a permission
* [delete_permission](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md#delete_permission) - Delete a Permission
* [get_permission](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md#get_permission) - Get Permission details
* [list_permissions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md#list_permissions) - List Permissions by user id
* [update_permission](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/permissions/README.md#update_permission) - Update a permission

### [SourceDefinitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md)

* [create_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md#create_source_definition) - Create a source definition.
* [delete_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md#delete_source_definition) - Delete a source definition.
* [get_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md#get_source_definition) - Get source definition details.
* [list_source_definitions](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md#list_source_definitions) - List source definitions.
* [update_source_definition](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sourcedefinitions/README.md#update_source_definition) - Update source definition details.

### [Sources](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md)

* [create_source](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#create_source) - Create a source
* [delete_source](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#delete_source) - Delete a Source
* [get_source](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#get_source) - Get Source details
* [initiate_o_auth](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#list_sources) - List sources
* [patch_source](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#patch_source) - Update a Source
* [put_source](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/sources/README.md#put_source) - Update a Source and fully overwrite it

### [Streams](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/streams/README.md)

* [get_stream_properties](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/streams/README.md#get_stream_properties) - Get stream properties

### [Tags](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md)

* [create_tag](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md#create_tag) - Create a tag
* [delete_tag](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md#delete_tag) - Delete a tag
* [get_tag](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md#get_tag) - Get a tag
* [list_tags](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md#list_tags) - List all tags
* [update_tag](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/tags/README.md#update_tag) - Update a tag

### [Users](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/users/README.md)

* [list_users_within_an_organization](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/users/README.md#list_users_within_an_organization) - List all users within an organization

### [Workspaces](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md)

* [create_or_update_workspace_o_auth_credentials](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#create_workspace) - Create a workspace
* [delete_workspace](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#delete_workspace) - Delete a Workspace
* [delete_workspace_o_auth_credentials](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#delete_workspace_o_auth_credentials) - Delete OAuth override credentials for a workspace and source/destination type.
* [get_workspace](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#get_workspace) - Get Workspace details
* [list_workspaces](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#list_workspaces) - List workspaces
* [update_workspace](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/./docs/sdks/workspaces/README.md#update_workspace) - Update a workspace

</details>
<!-- End Available Resources and Operations [operations] -->







<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from airbyte_api import AirbyteAPI, models
from airbyte_api.utils import BackoffStrategy, RetryConfig


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    },
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from airbyte_api import AirbyteAPI, models
from airbyte_api.utils import BackoffStrategy, RetryConfig


with AirbyteAPI(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`AirbyteAPIError`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/././src/airbyte_api/errors/airbyteapierror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                            |
| ------------------ | ---------------- | ------------------------------------------------------ |
| `err.message`      | `str`            | Error message                                          |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                     |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                  |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned. |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                      |

### Example
```python
from airbyte_api import AirbyteAPI, errors, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:
    res = None
    try:

        res = aa_client.connections.create_connection(request={
            "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
            "name": "Postgres-to-Bigquery",
            "namespace_format": "${SOURCE_NAMESPACE}",
            "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
        })

        assert res.connection_response is not None

        # Handle response
        print(res.connection_response)


    except errors.AirbyteAPIError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

```

### Error Classes
**Primary error:**
* [`AirbyteAPIError`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/././src/airbyte_api/errors/airbyteapierror.py): The base class for HTTP error responses.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`AirbyteAPIError`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/././src/airbyte_api/errors/airbyteapierror.py)**:
* [`ResponseValidationError`](https://github.com/airbytehq/airbyte-api-python-sdk/blob/master/././src/airbyte_api/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    server_url="https://api.airbyte.com/v1",
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from airbyte_api import AirbyteAPI
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = AirbyteAPI(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from airbyte_api import AirbyteAPI
from airbyte_api.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = AirbyteAPI(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name                 | Type   | Scheme       |
| -------------------- | ------ | ------------ |
| `basic_auth`         | http   | HTTP Basic   |
| `bearer_auth`        | http   | HTTP Bearer  |
| `client_credentials` | oauth2 | OAuth2 token |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```
<!-- End Authentication [security] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `AirbyteAPI` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from airbyte_api import AirbyteAPI, models
def main():

    with AirbyteAPI(
        security=models.Security(
            basic_auth=models.SchemeBasicAuth(
                password="",
                username="",
            ),
        ),
    ) as aa_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with AirbyteAPI(
        security=models.Security(
            basic_auth=models.SchemeBasicAuth(
                password="",
                username="",
            ),
        ),
    ) as aa_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from airbyte_api import AirbyteAPI
import logging

logging.basicConfig(level=logging.DEBUG)
s = AirbyteAPI(debug_logger=logging.getLogger("airbyte_api"))
```
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
