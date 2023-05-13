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
    configuration=shared.DestinationAzureBlobStorage(
        azure_blob_storage_account_key='maiores',
        azure_blob_storage_account_name='quidem',
        azure_blob_storage_container_name='ipsam',
        azure_blob_storage_endpoint_domain_name='voluptate',
        azure_blob_storage_output_buffer_size=420075,
        azure_blob_storage_spill_size=722056,
        destination_type=shared.DestinationAzureBlobStorageAzureBlobStorageEnum.AZURE_BLOB_STORAGE,
        format=shared.DestinationAzureBlobStorageFormatCSVCommaSeparatedValues(
            flattening=shared.DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesNormalizationFlatteningEnum.ROOT_LEVEL_FLATTENING,
            format_type=shared.DestinationAzureBlobStorageFormatCSVCommaSeparatedValuesFormatTypeEnum.CSV,
        ),
    ),
    name='Camille Armstrong',
    workspace_id='0c5fbb25-8705-4320-ac73-d5fe9b90c289',
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
    destination_id='eaque',
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
    destination_id='occaecati',
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
    limit=699098,
    offset=237893,
    workspace_ids=[
        'e49a8d9c-bf48-4633-b23f-9b77f3a41006',
        '74ebf692-80d1-4ba7-ba89-ebf737ae4203',
        'ce5e6a95-d8a0-4d44-ace2-af7a73cf3be4',
        '53f870b3-26b5-4a73-829c-db1a8422bb67',
    ],
)

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
```
