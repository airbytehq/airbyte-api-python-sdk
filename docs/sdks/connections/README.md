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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'string',
                ],
                name='string',
                primary_key=[
                    [
                        'string',
                    ],
                ],
            ),
        ],
    ),
    destination_id='c669dd1e-3620-483e-afc8-55914e0a570f',
    namespace_format='${SOURCE_NAMESPACE}',
    schedule=shared.ConnectionSchedule(
        schedule_type=shared.ScheduleTypeEnum.MANUAL,
    ),
    source_id='dd427d83-a555-4847-8358-42325b6c7b3f',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionCreateRequest](../../models/shared/connectioncreaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateConnectionResponse](../../models/operations/createconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_connection

Delete a Connection

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.DeleteConnectionRequest(
    connection_id='string',
)

res = s.connections.delete_connection(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteConnectionRequest](../../models/operations/deleteconnectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteConnectionResponse](../../models/operations/deleteconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_connection

Get Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.GetConnectionRequest(
    connection_id='string',
)

res = s.connections.get_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetConnectionRequest](../../models/operations/getconnectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_connections

List connections

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.ListConnectionsRequest(
    workspace_ids=[
        'bed8f6e5-32a5-45f7-9c2b-30682edc8796',
    ],
)

res = s.connections.list_connections(req)

if res.connections_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListConnectionsRequest](../../models/operations/listconnectionsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListConnectionsResponse](../../models/operations/listconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## patch_connection

Update Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.PatchConnectionRequest(
    connection_patch_request=shared.ConnectionPatchRequest(
        configurations=shared.StreamConfigurations(
            streams=[
                shared.StreamConfiguration(
                    cursor_field=[
                        'string',
                    ],
                    name='string',
                    primary_key=[
                        [
                            'string',
                        ],
                    ],
                ),
            ],
        ),
        namespace_format='${SOURCE_NAMESPACE}',
        schedule=shared.ConnectionSchedule(
            schedule_type=shared.ScheduleTypeEnum.MANUAL,
        ),
    ),
    connection_id='string',
)

res = s.connections.patch_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchConnectionRequest](../../models/operations/patchconnectionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchConnectionResponse](../../models/operations/patchconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
