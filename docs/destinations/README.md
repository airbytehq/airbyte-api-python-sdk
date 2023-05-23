# destinations

### Available Operations

* [create_destination](#create_destination) - Create a destination
* [delete_destination](#delete_destination) - Delete a Destination
* [get_destination](#get_destination) - Get Destination details
* [list_destinations](#list_destinations) - List destinations

## create_destination

Creates a destination given a name, workspace id, and a json blob containing the configuration for the source.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.DestinationCreateRequest(
    configuration=shared.DestinationDatabricks(
        accept_terms=False,
        data_source=shared.DestinationDatabricksDataSourceRecommendedManagedTables(
            data_source_type=shared.DestinationDatabricksDataSourceRecommendedManagedTablesDataSourceType.MANAGED_TABLES_STORAGE,
        ),
        database='perferendis',
        databricks_http_path='amet',
        databricks_personal_access_token='optio',
        databricks_port='accusamus',
        databricks_server_hostname='ad',
        destination_type=shared.DestinationDatabricksDatabricks.DATABRICKS,
        purge_staging_data=False,
        schema='saepe',
    ),
    name='Rosie McKenzie',
    workspace_id='8a0d446c-e2af-47a7-bcf3-be453f870b32',
)

res = s.destinations.create_destination(req)

if res.destination_response is not None:
    # handle response
```

## delete_destination

Delete a Destination

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteDestinationRequest(
    destination_id='vel',
)

res = s.destinations.delete_destination(req)

if res.status_code == 200:
    # handle response
```

## get_destination

Get Destination details

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetDestinationRequest(
    destination_id='libero',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
```

## list_destinations

List destinations

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListDestinationsRequest(
    include_deleted=False,
    limit=374170,
    offset=646265,
    workspace_ids=[
        '3429cdb1-a842-42bb-a79d-2322715bf0cb',
        'b1e31b8b-90f3-4443-a110-8e0adcf4b921',
    ],
)

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
```
