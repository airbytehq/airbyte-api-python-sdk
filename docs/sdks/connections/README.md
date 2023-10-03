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
                    'violet',
                ],
                name='at BMW',
                primary_key=[
                    [
                        'pfft',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.AUTO,
    destination_id='083eafc8-5591-44e0-a570-f6dd427d83a5',
    name='mesh interactive',
    namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.IGNORE,
    prefix='port Idaho',
    schedule=shared.ConnectionSchedule(
        cron_expression='productivity',
        schedule_type=shared.ScheduleTypeEnum.MANUAL,
    ),
    source_id='b3fd2fd3-07d6-40cb-97ea-6dfc635b80f2',
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
    connection_id='Tesla Administrator Southeast',
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
    connection_id='silver rigid Southeast',
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
    limit=726733,
    offset=907316,
    workspace_ids=[
        'd8f6e532-a55f-479c-ab30-682edc879612',
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
                        'Northeast',
                    ],
                    name='Folk Wooden Officer',
                    primary_key=[
                        [
                            'Clothing',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
                ),
            ],
        ),
        data_residency=shared.GeographyEnumNoDefault.US,
        name='Customizable Dinar Bike',
        namespace_definition=shared.NamespaceDefinitionEnumNoDefault.SOURCE,
        namespace_format='${SOURCE_NAMESPACE}',
        non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumNoDefault.PROPAGATE_COLUMNS,
        prefix='override',
        schedule=shared.ConnectionSchedule(
            cron_expression='Serbia Indio microchip',
            schedule_type=shared.ScheduleTypeEnum.MANUAL,
        ),
        status=shared.ConnectionStatusEnum.ACTIVE,
    ),
    connection_id='Lead shyly port',
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

