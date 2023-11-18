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
    configuration=shared.DestinationGoogleSheets(
    credentials=shared.AuthenticationViaGoogleOAuth(
        client_id='string',
        client_secret='string',
        refresh_token='string',
    ),
    spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
),
    name='string',
    workspace_id='8360860a-d46e-48e6-af62-08e5ba5019ef',
)

res = s.destinations.create_destination(req)

if res.destination_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationCreateRequest](../../models/shared/destinationcreaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
    destination_id='string',
)

res = s.destinations.delete_destination(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteDestinationRequest](../../models/operations/deletedestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteDestinationResponse](../../models/operations/deletedestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
    destination_id='string',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
    workspace_ids=[
        'c2980b9a-8317-4202-845c-d26fb4455227',
    ],
)

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDestinationsRequest](../../models/operations/listdestinationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListDestinationsResponse](../../models/operations/listdestinationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
        configuration=shared.DestinationGoogleSheets(
        credentials=shared.AuthenticationViaGoogleOAuth(
            client_id='string',
            client_secret='string',
            refresh_token='string',
        ),
        spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
    ),
    ),
    destination_id='string',
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchDestinationRequest](../../models/operations/patchdestinationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchDestinationResponse](../../models/operations/patchdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
        configuration=shared.DestinationGoogleSheets(
        credentials=shared.AuthenticationViaGoogleOAuth(
            client_id='string',
            client_secret='string',
            refresh_token='string',
        ),
        spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
    ),
        name='string',
    ),
    destination_id='string',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PutDestinationRequest](../../models/operations/putdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutDestinationResponse](../../models/operations/putdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
