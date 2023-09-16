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
                    'iure',
                ],
                name='Dr. Rickey Boyle',
                primary_key=[
                    [
                        'mollitia',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.AUTO,
    destination_id='352c5955-907a-4ff1-a3a2-fa9467739251',
    name='Matt Hamill',
    namespace_definition=shared.NamespaceDefinitionEnum.SOURCE,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.PROPAGATE_FULLY,
    prefix='ipsam',
    schedule=shared.ConnectionSchedule(
        cron_expression='id',
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='019da1ff-e78f-4097-b007-4f15471b5e6e',
    status=shared.ConnectionStatusEnum.ACTIVE,
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
    connection_id='ipsum',
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
    connection_id='quidem',
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
    limit=565189,
    offset=566602,
    workspace_ids=[
        'd488e1e9-1e45-40ad-aabd-44269802d502',
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
                        'dolorum',
                    ],
                    name='Eddie Prosacco',
                    primary_key=[
                        [
                            'delectus',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_APPEND,
                ),
            ],
        ),
        data_residency=shared.GeographyEnumNoDefault.AUTO,
        name='Sergio Hyatt',
        namespace_definition=shared.NamespaceDefinitionEnumNoDefault.DESTINATION,
        namespace_format='${SOURCE_NAMESPACE}',
        non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumNoDefault.PROPAGATE_COLUMNS,
        prefix='dolor',
        schedule=shared.ConnectionSchedule(
            cron_expression='debitis',
            schedule_type=shared.ScheduleTypeEnum.CRON,
        ),
        status=shared.ConnectionStatusEnum.DEPRECATED,
    ),
    connection_id='in',
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

