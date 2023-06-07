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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.PatchDestinationRequest(
    destination_patch_request=shared.DestinationPatchRequest(
        configuration=shared.DestinationConvex(
            access_key='neque',
            deployment_url='fugit',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.PutDestinationRequest(
    destination_put_request=shared.DestinationPutRequest(
        configuration=shared.DestinationAwsDatalake(
            aws_account_id='cumque',
            bucket_name='soluta',
            bucket_prefix='nobis',
            credentials=shared.DestinationAwsDatalakeCredentialsIAMRole(
                credentials_title=shared.DestinationAwsDatalakeCredentialsIAMRoleCredentialsTitle.IAM_ROLE,
                role_arn='saepe',
            ),
            destination_type=shared.DestinationAwsDatalakeAwsDatalake.AWS_DATALAKE,
            format=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSON(
                compression_codec=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONCompressionCodecOptional.UNCOMPRESSED,
                format_type=shared.DestinationAwsDatalakeFormatJSONLinesNewlineDelimitedJSONFormatTypeWildcard.JSONL,
            ),
            glue_catalog_float_as_decimal=False,
            lakeformation_database_default_tag_key='nobis',
            lakeformation_database_default_tag_values='quos',
            lakeformation_database_name='tempore',
            lakeformation_governed_tables=False,
            partitioning=shared.DestinationAwsDatalakeChooseHowToPartitionData.DAY,
            region=shared.DestinationAwsDatalakeS3BucketRegion.US_EAST_1,
        ),
        name='Mike Greenholt',
    ),
    destination_id='dolorum',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
```
