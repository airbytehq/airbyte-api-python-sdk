# destinations

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
        bearer_auth="",
    ),
)

req = shared.DestinationCreateRequest(
    configuration=shared.DestinationPubsub(
        batching_delay_threshold=536579,
        batching_element_count_threshold=607045,
        batching_enabled=False,
        batching_request_bytes_threshold=896672,
        credentials_json='distinctio',
        destination_type=shared.DestinationPubsubPubsub.PUBSUB,
        ordering_enabled=False,
        project_id='asperiores',
        topic_id='nihil',
    ),
    name='Tamara Ondricka',
    workspace_id='203ce5e6-a95d-48a0-9446-ce2af7a73cf3',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDestinationRequest(
    destination_id='tempore',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDestinationRequest(
    destination_id='accusamus',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListDestinationsRequest(
    include_deleted=False,
    limit=253941,
    offset=313692,
    workspace_ids=[
        'f870b326-b5a7-4342-9cdb-1a8422bb679d',
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
        bearer_auth="",
    ),
)

req = operations.PatchDestinationRequest(
    destination_patch_request=shared.DestinationPatchRequest(
        configuration=shared.DestinationCumulio(
            api_host='neque',
            api_key='fugit',
            api_token='magni',
            destination_type=shared.DestinationCumulioCumulio.CUMULIO,
        ),
        name='Ashley Hermiston',
    ),
    destination_id='voluptatem',
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
        bearer_auth="",
    ),
)

req = operations.PutDestinationRequest(
    destination_put_request=shared.DestinationPutRequest(
        configuration=shared.DestinationS3(
            access_key_id='A012345678910EXAMPLE',
            destination_type=shared.DestinationS3S3.S3,
            file_name_pattern='{part_number}',
            format=shared.DestinationS3FormatJSONLinesNewlineDelimitedJSON(
                compression=shared.DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompression(
                    compression_type=shared.DestinationS3FormatJSONLinesNewlineDelimitedJSONCompressionNoCompressionCompressionType.NO_COMPRESSION,
                ),
                flattening=shared.DestinationS3FormatJSONLinesNewlineDelimitedJSONFlattening.ROOT_LEVEL_FLATTENING,
                format_type=shared.DestinationS3FormatJSONLinesNewlineDelimitedJSONFormatType.JSONL,
            ),
            s3_bucket_name='airbyte_sync',
            s3_bucket_path='data_sync/test',
            s3_bucket_region=shared.DestinationS3S3BucketRegion.AF_SOUTH_1,
            s3_endpoint='http://localhost:9000',
            s3_path_format='${NAMESPACE}/${STREAM_NAME}/${YEAR}_${MONTH}_${DAY}_${EPOCH}_',
            secret_access_key='a012345678910ABCDEFGH/AbCdEfGhEXAMPLEKEY',
        ),
        name='Gayle Lueilwitz',
    ),
    destination_id='aperiam',
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

