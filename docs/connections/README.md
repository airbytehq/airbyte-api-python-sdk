# connections

### Available Operations

* [create_connection](#create_connection) - Create a connection
* [delete_connection](#delete_connection) - Delete a Connection
* [get_connection](#get_connection) - Get Connection details
* [list_connections](#list_connections) - List connections

## create_connection

Create a connection

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'sequi',
                    'tenetur',
                    'ipsam',
                    'id',
                ],
                name='Richard Boyer',
                primary_key=[
                    [
                        'reiciendis',
                    ],
                    [
                        'vero',
                        'nihil',
                        'praesentium',
                        'voluptatibus',
                    ],
                    [
                        'omnis',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnumEnum.FULL_REFRESH_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnumEnum.EU,
    destination_id='0074f154-71b5-4e6e-93b9-9d488e1e91e4',
    name='Elizabeth Orn',
    namespace_definition=shared.ConnectionCreateRequestNamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    prefix='distinctio',
    schedule=shared.ConnectionScheduleCreate(
        cron_expression='quibusdam',
        schedule_type=shared.ScheduleTypeEnumEnum.MANUAL,
    ),
    source_id='4269802d-502a-494b-b4f6-3c969e9a3efa',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```

## delete_connection

Delete a Connection

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteConnectionRequest(
    connection_id='in',
)

res = s.connections.delete_connection(req)

if res.status_code == 200:
    # handle response
```

## get_connection

Get Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetConnectionRequest(
    connection_id='in',
)

res = s.connections.get_connection(req)

if res.connection_response is not None:
    # handle response
```

## list_connections

List connections

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListConnectionsRequest(
    include_deleted=False,
    limit=846409,
    offset=978571,
    workspace_ids=[
        '14cd66ae-395e-4fb9-ba88-f3a66997074b',
        'a4469b6e-2141-4959-890a-fa563e2516fe',
        '4c8b711e-5b7f-4d2e-9028-921cddc69260',
    ],
)

res = s.connections.list_connections(req)

if res.connections_response is not None:
    # handle response
```
