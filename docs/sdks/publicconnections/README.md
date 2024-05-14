# PublicConnections
(*public_connections*)

### Available Operations

* [create_connection](#create_connection) - Create a connection
* [delete_connection](#delete_connection) - Delete a Connection
* [get_connection](#get_connection) - Get Connection details
* [list_connections](#list_connections) - List connections
* [patch_connection](#patch_connection) - Update Connection details

## create_connection

Create a connection

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public_connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ConnectionCreateRequest](../../models/connectioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[api.CreateConnectionResponse](../../api/createconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_connection

Delete a Connection

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public_connections.delete_connection(request=api.DeleteConnectionRequest(
    connection_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteConnectionRequest](../../api/deleteconnectionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.DeleteConnectionResponse](../../api/deleteconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_connection

Get Connection details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public_connections.get_connection(request=api.GetConnectionRequest(
    connection_id='<value>',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `request`                                                     | [api.GetConnectionRequest](../../api/getconnectionrequest.md) | :heavy_check_mark:                                            | The request object to use for the request.                    |


### Response

**[api.GetConnectionResponse](../../api/getconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_connections

List connections

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public_connections.list_connections(request=api.ListConnectionsRequest())

if res.connections_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.ListConnectionsRequest](../../api/listconnectionsrequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.ListConnectionsResponse](../../api/listconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_connection

Update Connection details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public_connections.patch_connection(request=api.PatchConnectionRequest(
    connection_patch_request=models.ConnectionPatchRequest(
        namespace_format='${SOURCE_NAMESPACE}',
    ),
    connection_id='<value>',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.PatchConnectionRequest](../../api/patchconnectionrequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.PatchConnectionResponse](../../api/patchconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
