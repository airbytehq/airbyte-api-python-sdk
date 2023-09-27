# Destinations
(*destinations*)

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
    configuration=[],
    name='Kathryn Lang',
    workspace_id='1cddc692-601f-4b57-ab0d-5f0d30c5fbb2',
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
    destination_id='quis',
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
    destination_id='totam',
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
    limit=489549,
    offset=54338,
    workspace_ids=[
        '53202c73-d5fe-49b9-8c28-909b3fe49a8d',
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
        configuration=[],
        name='Loren Renner',
    ),
    destination_id='quos',
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
        configuration=[],
        name='Florence Ebert',
    ),
    destination_id='ipsum',
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

