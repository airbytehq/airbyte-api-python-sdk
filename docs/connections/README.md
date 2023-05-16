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
                    'tenetur',
                ],
                name='Mr. Alberta Schuster',
                primary_key=[
                    [
                        'quasi',
                        'reiciendis',
                        'voluptatibus',
                    ],
                    [
                        'nihil',
                        'praesentium',
                        'voluptatibus',
                        'ipsa',
                    ],
                    [
                        'voluptate',
                        'cum',
                        'perferendis',
                    ],
                    [
                        'reprehenderit',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnumEnum.FULL_REFRESH_APPEND,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'dicta',
                    'corporis',
                    'dolore',
                    'iusto',
                ],
                name='Maryann Hamill',
                primary_key=[
                    [
                        'ipsum',
                    ],
                    [
                        'molestias',
                        'excepturi',
                        'pariatur',
                    ],
                    [
                        'praesentium',
                        'rem',
                    ],
                    [
                        'quasi',
                        'repudiandae',
                        'sint',
                        'veritatis',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_DEDUPED_HISTORY,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'enim',
                    'consequatur',
                ],
                name='Taylor Cole',
                primary_key=[
                    [
                        'modi',
                        'qui',
                    ],
                    [
                        'cupiditate',
                        'quos',
                    ],
                    [
                        'magni',
                    ],
                    [
                        'ipsam',
                        'alias',
                        'fugit',
                        'dolorum',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_APPEND,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'facilis',
                    'tempore',
                ],
                name='Lucia Kemmer',
                primary_key=[
                    [
                        'provident',
                        'necessitatibus',
                    ],
                    [
                        'officia',
                        'dolor',
                        'debitis',
                    ],
                    [
                        'dolorum',
                        'in',
                        'in',
                        'illum',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_DEDUPED_HISTORY,
            ),
        ],
    ),
    data_residency=shared.GeographyEnumEnum.EU,
    destination_id='14cd66ae-395e-4fb9-ba88-f3a66997074b',
    name='Leroy Greenfelder',
    namespace_definition=shared.NamespaceDefinitionEnumEnum.CUSTOM_FORMAT,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumEnum.IGNORE,
    prefix='vero',
    schedule=shared.ConnectionScheduleCreate(
        cron_expression='aspernatur',
        schedule_type=shared.ScheduleTypeEnumEnum.MANUAL,
    ),
    source_id='41959890-afa5-463e-a516-fe4c8b711e5b',
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
    connection_id='nihil',
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
    connection_id='repellat',
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
    limit=841140,
    offset=149448,
    workspace_ids=[
        'd028921c-ddc6-4926-81fb-576b0d5f0d30',
        'c5fbb258-7053-4202-873d-5fe9b90c2890',
        '9b3fe49a-8d9c-4bf4-8633-323f9b77f3a4',
        '100674eb-f692-480d-9ba7-7a89ebf737ae',
    ],
)

res = s.connections.list_connections(req)

if res.connections_response is not None:
    # handle response
```
