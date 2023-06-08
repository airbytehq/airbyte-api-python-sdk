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
        configuration=shared.DestinationConvex(
            access_key='neque',
            deployment_url='https://murky-swan-635.convex.cloud',
            destination_type=shared.DestinationConvexConvex.CONVEX,
        ),
        name='Courtney Cassin',
    ),
    destination_id='hic',
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
```

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
        configuration=shared.DestinationAwsDatalake(
            aws_account_id='111111111111',
            bucket_name='cumque',
            bucket_prefix='soluta',
            credentials=shared.DestinationAwsDatalakeCredentialsIAMUser(
                aws_access_key_id='et',
                aws_secret_access_key='saepe',
                credentials_title=shared.DestinationAwsDatalakeCredentialsIAMUserCredentialsTitle.IAM_USER,
            ),
            destination_type=shared.DestinationAwsDatalakeAwsDatalake.AWS_DATALAKE,
            format=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSON(
                compression_codec=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONCompressionCodecOptional.UNCOMPRESSED,
                format_type=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONFormatTypeWildcard.JSONL,
            ),
            glue_catalog_float_as_decimal=False,
            lakeformation_database_default_tag_key='pii_level',
            lakeformation_database_default_tag_values='private,public',
            lakeformation_database_name='nobis',
            lakeformation_governed_tables=False,
            partitioning=shared.DestinationAwsDatalakeChooseHowToPartitionData.MONTH,
            region=shared.DestinationAwsDatalakeS3BucketRegion.EU_WEST_1,
        ),
        name='Kevin Willms',
    ),
    destination_id='labore',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
```
