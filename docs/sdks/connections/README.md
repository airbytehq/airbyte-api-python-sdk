# Connections

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
            password="",
            username="",
        ),
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'ipsum',
                ],
                name='Virgil Mante',
                primary_key=[
                    [
                        'praesentium',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.EU,
    destination_id='1e91e450-ad2a-4bd4-8269-802d502a94bb',
    name='Lucia Kemmer',
    namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.DISABLE_CONNECTION,
    prefix='provident',
    schedule=shared.ConnectionSchedule(
        cron_expression='necessitatibus',
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='a3efa77d-fb14-4cd6-aae3-95efb9ba88f3',
    status=shared.ConnectionStatusEnum.INACTIVE,
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionCreateRequest](../../models/shared/connectioncreaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.CreateConnectionResponse](../../models/operations/createconnectionresponse.md)**


## delete_connection

Delete a Connection

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.DeleteConnectionRequest(
    connection_id='nisi',
)

res = s.connections.delete_connection(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteConnectionRequest](../../models/operations/deleteconnectionrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteConnectionResponse](../../models/operations/deleteconnectionresponse.md)**


## get_connection

Get Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.GetConnectionRequest(
    connection_id='vel',
)

res = s.connections.get_connection(req)

if res.connection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetConnectionRequest](../../models/operations/getconnectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetConnectionResponse](../../models/operations/getconnectionresponse.md)**


## list_connections

List connections

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.ListConnectionsRequest(
    include_deleted=False,
    limit=618809,
    offset=606393,
    workspace_ids=[
        '7074ba44-69b6-4e21-8195-9890afa563e2',
    ],
)

res = s.connections.list_connections(req)

if res.connections_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListConnectionsRequest](../../models/operations/listconnectionsrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListConnectionsResponse](../../models/operations/listconnectionsresponse.md)**


## patch_connection

Update Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.PatchConnectionRequest(
    connection_patch_request=shared.ConnectionPatchRequest(
        configurations=shared.StreamConfigurations(
            streams=[
                shared.StreamConfiguration(
                    cursor_field=[
                        'nemo',
                    ],
                    name='Vera Wyman',
                    primary_key=[
                        [
                            'maxime',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
                ),
            ],
        ),
        data_residency=shared.GeographyEnumNoDefault.EU,
        name='Alice Bradtke',
        namespace_definition=shared.NamespaceDefinitionEnumNoDefault.CUSTOM_FORMAT,
        namespace_format='${SOURCE_NAMESPACE}',
        non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumNoDefault.DISABLE_CONNECTION,
        prefix='repellat',
        schedule=shared.ConnectionSchedule(
            cron_expression='quibusdam',
            schedule_type=shared.ScheduleTypeEnum.MANUAL,
        ),
        status=shared.ConnectionStatusEnum.DEPRECATED,
    ),
    connection_id='pariatur',
)

res = s.connections.patch_connection(req)

if res.connection_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.PatchConnectionRequest](../../models/operations/patchconnectionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.PatchConnectionResponse](../../models/operations/patchconnectionresponse.md)**

