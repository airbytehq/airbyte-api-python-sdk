# Destinations

### Available Operations

* [create_destination](#create_destination) - Create a destination
* [delete_destination](#delete_destination) - Delete a Destination
* [get_destination](#get_destination) - Get Destination details
* [list_destinations](#list_destinations) - List destinations
* [patch_destination](#patch_destination) - Update a Destination
* [put_destination](#put_destination) - Update a Destination and fully overwrite it

## create_destination

Creates a destination given a name, workspace id, and a json blob containing the configuration for the source.

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

req = shared.DestinationCreateRequest(
    configuration=shared.DestinationAzureBlobStorage(
        azure_blob_storage_account_key='Z8ZkZpteggFx394vm+PJHnGTvdRncaYS+JhLKdj789YNmD+iyGTnG+PV+POiuYNhBg/ACS+LKjd%4FG3FHGN12Nd==',
        azure_blob_storage_account_name='airbyte5storage',
        azure_blob_storage_container_name='airbytetescontainername',
        azure_blob_storage_endpoint_domain_name='blob.core.windows.net',
        azure_blob_storage_output_buffer_size=5,
        azure_blob_storage_spill_size=500,
        destination_type=shared.DestinationAzureBlobStorageAzureBlobStorage.AZURE_BLOB_STORAGE,
        format='consequuntur',
    ),
    name='Miss Nick Cummerata',
    workspace_id='dc692601-fb57-46b0-95f0-d30c5fbb2587',
)

res = s.destinations.create_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationCreateRequest](../../models/shared/destinationcreaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**


## delete_destination

Delete a Destination

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

req = operations.DeleteDestinationRequest(
    destination_id='eaque',
)

res = s.destinations.delete_destination(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteDestinationRequest](../../models/operations/deletedestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteDestinationResponse](../../models/operations/deletedestinationresponse.md)**


## get_destination

Get Destination details

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

req = operations.GetDestinationRequest(
    destination_id='quis',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**


## list_destinations

List destinations

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

req = operations.ListDestinationsRequest(
    include_deleted=False,
    limit=199996,
    offset=179490,
    workspace_ids=[
        '02c73d5f-e9b9-40c2-8909-b3fe49a8d9cb',
    ],
)

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDestinationsRequest](../../models/operations/listdestinationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListDestinationsResponse](../../models/operations/listdestinationsresponse.md)**


## patch_destination

Update a Destination

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

req = operations.PatchDestinationRequest(
    destination_patch_request=shared.DestinationPatchRequest(
        configuration=shared.DestinationVertica(
            database='quaerat',
            destination_type=shared.DestinationVerticaVertica.VERTICA,
            host='quos',
            jdbc_url_params='aliquid',
            password='dolorem',
            port=5433,
            schema='dolorem',
            tunnel_method='dolor',
            username='Christy_Erdman73',
        ),
        name='Marian Wisozk',
    ),
    destination_id='numquam',
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchDestinationRequest](../../models/operations/patchdestinationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchDestinationResponse](../../models/operations/patchdestinationresponse.md)**


## put_destination

Update a Destination and fully overwrite it

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

req = operations.PutDestinationRequest(
    destination_put_request=shared.DestinationPutRequest(
        configuration=shared.DestinationBigqueryDenormalized(
            big_query_client_buffer_size_mb=15,
            credentials_json='ipsa',
            dataset_id='ipsa',
            dataset_location=shared.DestinationBigqueryDenormalizedDatasetLocation.EUROPE_WEST1,
            destination_type=shared.DestinationBigqueryDenormalizedBigqueryDenormalized.BIGQUERY_DENORMALIZED,
            loading_method=shared.DestinationBigqueryDenormalizedGCSStaging(
                credential='odio',
                file_buffer_count=10,
                gcs_bucket_name='airbyte_sync',
                gcs_bucket_path='data_sync/test',
                keep_files_in_gcs_bucket=shared.DestinationBigqueryDenormalizedGCSStagingGCSTmpFilesAfterwardProcessing.DELETE_ALL_TMP_FILES_FROM_GCS,
                method=shared.DestinationBigqueryDenormalizedGCSStagingMethod.GCS_STAGING,
            ),
            project_id='accusamus',
        ),
        name='Jan Hodkiewicz',
    ),
    destination_id='atque',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PutDestinationRequest](../../models/operations/putdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutDestinationResponse](../../models/operations/putdestinationresponse.md)**

