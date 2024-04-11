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

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.DestinationCreateRequest(
    configuration=airbyte_api.DestinationGoogleSheets(
        credentials=airbyte_api.AuthenticationViaGoogleOAuth(
            client_id='<value>',
            client_secret='<value>',
            refresh_token='<value>',
        ),
        spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
    ),
    name='<value>',
    workspace_id='8360860a-d46e-48e6-af62-08e5ba5019ef',
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

**[models.CreateDestinationResponse](../../models/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_destination

Delete a Destination

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.DeleteDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.delete_destination(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.DeleteDestinationRequest](../../models/deletedestinationrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |


### Response

**[models.DeleteDestinationResponse](../../models/deletedestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_destination

Get Destination details

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.GetDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.GetDestinationRequest](../../models/getdestinationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |


### Response

**[models.GetDestinationResponse](../../models/getdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_destinations

List destinations

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.ListDestinationsRequest()

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ListDestinationsRequest](../../models/listdestinationsrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[models.ListDestinationsResponse](../../models/listdestinationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## patch_destination

Update a Destination

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.PatchDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.PatchDestinationRequest](../../models/patchdestinationrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[models.PatchDestinationResponse](../../models/patchdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## put_destination

Update a Destination and fully overwrite it

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.PutDestinationRequest(
    destination_id='<value>',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.PutDestinationRequest](../../models/putdestinationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |


### Response

**[models.PutDestinationResponse](../../models/putdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
