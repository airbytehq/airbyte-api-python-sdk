# Destinations
(*destinations*)

## Overview

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.create_destination(request=models.DestinationCreateRequest(
    configuration=models.DestinationPinecone(
        embedding=models.DestinationPineconeFake(),
        indexing=models.DestinationPineconeIndexing(
            index='<value>',
            pinecone_environment='us-west1-gcp',
            pinecone_key='<value>',
        ),
        processing=models.DestinationPineconeProcessingConfigModel(
            chunk_size=834173,
            metadata_fields=[
                'user',
            ],
            text_fields=[
                'users.*.name',
            ],
        ),
    ),
    name='Postgres',
    workspace_id='2155ae5a-de39-4808-af6a-16fe7b8b4ed2',
))

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.delete_destination(request=api.DeleteDestinationRequest(
    destination_id='<value>',
))

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.get_destination(request=api.GetDestinationRequest(
    destination_id='<value>',
))

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.list_destinations(request=api.ListDestinationsRequest())

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.patch_destination(request=api.PatchDestinationRequest(
    destination_id='<value>',
    destination_patch_request=models.DestinationPatchRequest(
        configuration=models.DestinationDuckdb(
            destination_path='motherduck:',
            schema='main',
        ),
        name='My Destination',
    ),
))

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
            password="",
            username="",
        ),
    ),
)


res = s.destinations.put_destination(request=api.PutDestinationRequest(
    destination_id='<value>',
    destination_put_request=models.DestinationPutRequest(
        configuration=models.DestinationClickhouse(
            database='<value>',
            host='urban-receptor.org',
            username='Kaylie_Terry',
            port=8123,
            tunnel_method=models.SSHKeyAuthentication(
                ssh_key='<value>',
                tunnel_host='<value>',
                tunnel_user='<value>',
                tunnel_port=22,
            ),
        ),
        name='My Destination',
    ),
))

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
