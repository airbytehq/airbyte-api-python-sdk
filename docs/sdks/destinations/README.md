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
    configuration=shared.DestinationKeen(
        api_key='ABCDEFGHIJKLMNOPRSTUWXYZ',
        destination_type=shared.DestinationKeenKeen.KEEN,
        infer_timestamp=False,
        project_id='58b4acc22ba938934e888322e',
    ),
    name='Mrs. Emilio Price',
    workspace_id='d66ae395-efb9-4ba8-8f3a-66997074ba44',
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
    destination_id='suscipit',
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
    destination_id='natus',
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
    limit=749170,
    offset=428769,
    workspace_ids=[
        'e2141959-890a-4fa5-a3e2-516fe4c8b711',
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
        configuration=shared.DestinationTypesense(
            api_key='ullam',
            batch_size=714242,
            destination_type=shared.DestinationTypesenseTypesense.TYPESENSE,
            host='nihil',
            port='repellat',
            protocol='quibusdam',
        ),
        name='Mr. Jenna Stroman',
    ),
    destination_id='natus',
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
        configuration=shared.DestinationCumulio(
            api_host='sunt',
            api_key='quo',
            api_token='illum',
            destination_type=shared.DestinationCumulioCumulio.CUMULIO,
        ),
        name='Simon Jenkins',
    ),
    destination_id='ea',
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

