# Connections
(*connections*)

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

req = models.ConnectionCreateRequest(
    destination_id='c669dd1e-3620-483e-afc8-55914e0a570f',
    source_id='6dd427d8-3a55-4584-b835-842325b6c7b3',
    namespace_format='${SOURCE_NAMESPACE}',
)

res = s.connections.create_connection(req)

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

req = api.DeleteConnectionRequest(
    connection_id='<value>',
)

res = s.connections.delete_connection(req)

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

req = api.GetConnectionRequest(
    connection_id='<value>',
)

res = s.connections.get_connection(req)

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

req = api.ListConnectionsRequest()

res = s.connections.list_connections(req)

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

req = api.PatchConnectionRequest(
    connection_patch_request=models.ConnectionPatchRequest(
        namespace_format='${SOURCE_NAMESPACE}',
    ),
    connection_id='<value>',
)

res = s.connections.patch_connection(req)

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
