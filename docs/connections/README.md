# connections

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
        bearer_auth="",
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'ipsam',
                    'id',
                    'possimus',
                    'aut',
                ],
                name='Sabrina Smitham DVM',
                primary_key=[
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
                    [
                        'maiores',
                        'dicta',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.AUTO,
    destination_id='71b5e6e1-3b99-4d48-8e1e-91e450ad2abd',
    name='Pauline Deckow',
    namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.IGNORE,
    prefix='magni',
    schedule=shared.ConnectionSchedule(
        cron_expression='assumenda',
        schedule_type=shared.ScheduleTypeEnum.MANUAL,
    ),
    source_id='02a94bb4-f63c-4969-a9a3-efa77dfb14cd',
    status=shared.ConnectionStatusEnum.INACTIVE,
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
        bearer_auth="",
    ),
)

req = operations.DeleteConnectionRequest(
    connection_id='aliquid',
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
        bearer_auth="",
    ),
)

req = operations.GetConnectionRequest(
    connection_id='laborum',
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
        bearer_auth="",
    ),
)

req = operations.ListConnectionsRequest(
    include_deleted=False,
    limit=881104,
    offset=249796,
    workspace_ids=[
        '5efb9ba8-8f3a-4669-9707-4ba4469b6e21',
        '41959890-afa5-463e-a516-fe4c8b711e5b',
        '7fd2ed02-8921-4cdd-8692-601fb576b0d5',
    ],
)

res = s.connections.list_connections(req)

if res.connections_response is not None:
    # handle response
```

## patch_connection

Update Connection details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PatchConnectionRequest(
    connection_patch_request=shared.ConnectionPatchRequest(
        configurations=shared.StreamConfigurations(
            streams=[
                shared.StreamConfiguration(
                    cursor_field=[
                        'fugiat',
                    ],
                    name='Jennifer Runolfsdottir',
                    primary_key=[
                        [
                            'dolores',
                            'quis',
                            'totam',
                        ],
                        [
                            'eaque',
                            'quis',
                        ],
                        [
                            'eos',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_OVERWRITE,
                ),
                shared.StreamConfiguration(
                    cursor_field=[
                        'minus',
                    ],
                    name='Rosa Swift',
                    primary_key=[
                        [
                            'facilis',
                            'perspiciatis',
                            'voluptatem',
                        ],
                        [
                            'consequuntur',
                            'blanditiis',
                            'error',
                            'eaque',
                        ],
                        [
                            'rerum',
                            'adipisci',
                            'asperiores',
                        ],
                        [
                            'modi',
                            'iste',
                            'dolorum',
                            'deleniti',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
                ),
                shared.StreamConfiguration(
                    cursor_field=[
                        'nobis',
                        'libero',
                        'delectus',
                    ],
                    name='Billie Jacobi',
                    primary_key=[
                        [
                            'ipsum',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
                ),
                shared.StreamConfiguration(
                    cursor_field=[
                        'cum',
                        'voluptate',
                        'dignissimos',
                    ],
                    name='Allen Parisian Jr.',
                    primary_key=[
                        [
                            'odio',
                            'quaerat',
                        ],
                    ],
                    sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
                ),
            ],
        ),
        data_residency=shared.GeographyEnumNoDefault.EU,
        name='Hector Mosciski',
        namespace_definition=shared.NamespaceDefinitionEnumNoDefault.SOURCE,
        namespace_format='${SOURCE_NAMESPACE}',
        non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumNoDefault.DISABLE_CONNECTION,
        prefix='ab',
        schedule=shared.ConnectionSchedule(
            cron_expression='soluta',
            schedule_type=shared.ScheduleTypeEnum.CRON,
        ),
        status=shared.ConnectionStatusEnum.INACTIVE,
    ),
    connection_id='voluptate',
)

res = s.connections.patch_connection(req)

if res.connection_response is not None:
    # handle response
```
