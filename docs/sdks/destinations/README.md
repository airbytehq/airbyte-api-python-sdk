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
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = models.DestinationCreateRequest(
    configuration=models.DestinationGoogleSheets(
        credentials=models.AuthenticationViaGoogleOAuth(
            client_id='<value>',
            client_secret='<value>',
            refresh_token='<value>',
        ),
        spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
    ),
    name='Postgres',
    workspace_id='2155ae5a-de39-4808-af6a-16fe7b8b4ed2',
)

res = s.destinations.create_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.DestinationCreateRequest](../../models/destinationcreaterequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |


### Response

**[api.CreateDestinationResponse](../../api/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_destination

Delete a Destination

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.DeleteDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.delete_destination(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [api.DeleteDestinationRequest](../../api/deletedestinationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |


### Response

**[api.DeleteDestinationResponse](../../api/deletedestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_destination

Get Destination details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.GetDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [api.GetDestinationRequest](../../api/getdestinationrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[api.GetDestinationResponse](../../api/getdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_destinations

List destinations

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.ListDestinationsRequest()

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListDestinationsRequest](../../api/listdestinationsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.ListDestinationsResponse](../../api/listdestinationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_destination

Update a Destination

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.PatchDestinationRequest(
    destination_id='<value>',
    destination_patch_request=models.DestinationPatchRequest(
        configuration=models.DestinationGoogleSheets(
            credentials=models.AuthenticationViaGoogleOAuth(
                client_id='<value>',
                client_secret='<value>',
                refresh_token='<value>',
            ),
            spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
        ),
    ),
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PatchDestinationRequest](../../api/patchdestinationrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.PatchDestinationResponse](../../api/patchdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_destination

Update a Destination and fully overwrite it

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = api.PutDestinationRequest(
    destination_id='<value>',
    destination_put_request=models.DestinationPutRequest(
        configuration=models.DestinationGoogleSheets(
            credentials=models.AuthenticationViaGoogleOAuth(
                client_id='<value>',
                client_secret='<value>',
                refresh_token='<value>',
            ),
            spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
        ),
        name='<value>',
    ),
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [api.PutDestinationRequest](../../api/putdestinationrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[api.PutDestinationResponse](../../api/putdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
