# Connections

## Overview

### Available Operations

* [create_connection](#create_connection) - Create a connection
* [delete_connection](#delete_connection) - Delete a Connection
* [get_connection](#get_connection) - Get Connection details
* [list_connections](#list_connections) - List connections
* [patch_connection](#patch_connection) - Update Connection details

## create_connection

Create a connection

### Example Usage: Connection Creation Request Example

<!-- UsageSnippet language="python" operationID="createConnection" method="post" path="/connections" example="Connection Creation Request Example" -->
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
### Example Usage: Connection Creation Response Example

<!-- UsageSnippet language="python" operationID="createConnection" method="post" path="/connections" example="Connection Creation Response Example" -->
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
        "destination_id": "d446b90a-b83f-41d9-b1d6-eaa82f6b9713",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "a2bab3d3-7c90-4e49-ad1d-f4e1db27c748",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ConnectionCreateRequest](../../models/connectioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[api.CreateConnectionResponse](../../api/createconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_connection

Delete a Connection

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteConnection" method="delete" path="/connections/{connectionId}" -->
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

    res = aa_client.connections.delete_connection(request={
        "connection_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteConnectionRequest](../../api/deleteconnectionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.DeleteConnectionResponse](../../api/deleteconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_connection

Get Connection details

### Example Usage

<!-- UsageSnippet language="python" operationID="getConnection" method="get" path="/connections/{connectionId}" example="Connection Get Response Example" -->
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

    res = aa_client.connections.get_connection(request={
        "connection_id": "<value>",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetConnectionRequest](../../api/getconnectionrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetConnectionResponse](../../api/getconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_connections

List connections

### Example Usage

<!-- UsageSnippet language="python" operationID="listConnections" method="get" path="/connections" -->
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

    res = aa_client.connections.list_connections(request={})

    assert res.connections_response is not None

    # Handle response
    print(res.connections_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListConnectionsRequest](../../api/listconnectionsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListConnectionsResponse](../../api/listconnectionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_connection

Update Connection details

### Example Usage: Connection Get Response Example

<!-- UsageSnippet language="python" operationID="patchConnection" method="patch" path="/connections/{connectionId}" example="Connection Get Response Example" -->
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

    res = aa_client.connections.patch_connection(request={
        "connection_patch_request": {
            "namespace_format": "${SOURCE_NAMESPACE}",
        },
        "connection_id": "<value>",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```
### Example Usage: Connection Update Request Example

<!-- UsageSnippet language="python" operationID="patchConnection" method="patch" path="/connections/{connectionId}" example="Connection Update Request Example" -->
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

    res = aa_client.connections.patch_connection(request={
        "connection_patch_request": {
            "name": "Postgres-to-Bigquery",
            "namespace_format": "${SOURCE_NAMESPACE}",
        },
        "connection_id": "<value>",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PatchConnectionRequest](../../api/patchconnectionrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.PatchConnectionResponse](../../api/patchconnectionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |