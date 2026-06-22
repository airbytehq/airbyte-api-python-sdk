# Destinations

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

### Example Usage: Destination Creation Request Example

<!-- UsageSnippet language="python" operationID="createDestination" method="post" path="/destinations" example="Destination Creation Request Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.create_destination(request=models.DestinationCreateRequest(
        configuration=models.DestinationElasticsearch(
            endpoint="<value>",
            upsert=True,
        ),
        name="Postgres",
        workspace_id="2155ae5a-de39-4808-af6a-16fe7b8b4ed2",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```
### Example Usage: Destination Creation Response Example

<!-- UsageSnippet language="python" operationID="createDestination" method="post" path="/destinations" example="Destination Creation Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.create_destination(request=models.DestinationCreateRequest(
        configuration=models.DestinationTimeplus(
            apikey="<value>",
            endpoint="https://us-west-2.timeplus.cloud/workspace_id",
        ),
        name="<value>",
        workspace_id="dc693cc0-960d-4c6c-9d1b-05e8bf0c96ba",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.DestinationCreateRequest](../../models/destinationcreaterequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[api.CreateDestinationResponse](../../api/createdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_destination

Delete a Destination

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDestination" method="delete" path="/destinations/{destinationId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.delete_destination(request={
        "destination_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [api.DeleteDestinationRequest](../../api/deletedestinationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[api.DeleteDestinationResponse](../../api/deletedestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_destination

Get Destination details

### Example Usage

<!-- UsageSnippet language="python" operationID="getDestination" method="get" path="/destinations/{destinationId}" example="Destination Get Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.get_destination(request={
        "destination_id": "<value>",
    })

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetDestinationRequest](../../api/getdestinationrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetDestinationResponse](../../api/getdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_destinations

List destinations

### Example Usage

<!-- UsageSnippet language="python" operationID="listDestinations" method="get" path="/destinations" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.list_destinations(request={})

    assert res.destinations_response is not None

    # Handle response
    print(res.destinations_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListDestinationsRequest](../../api/listdestinationsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListDestinationsResponse](../../api/listdestinationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_destination

Update a Destination

### Example Usage: Destination Update Request Example

<!-- UsageSnippet language="python" operationID="patchDestination" method="patch" path="/destinations/{destinationId}" example="Destination Update Request Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.patch_destination(request=api.PatchDestinationRequest(
        destination_patch_request=models.DestinationPatchRequest(
            configuration=models.DestinationDuckdb(
                destination_path="/local/destination.duckdb",
            ),
            name="My Destination",
        ),
        destination_id="<value>",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```
### Example Usage: Destination Update Response Example

<!-- UsageSnippet language="python" operationID="patchDestination" method="patch" path="/destinations/{destinationId}" example="Destination Update Response Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.patch_destination(request=api.PatchDestinationRequest(
        destination_patch_request=models.DestinationPatchRequest(
            configuration=models.DestinationHubspot(
                credentials=models.OAuth(
                    client_id="<id>",
                    client_secret="<value>",
                    refresh_token="<value>",
                    type=models.Type.O_AUTH,
                ),
            ),
        ),
        destination_id="<value>",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PatchDestinationRequest](../../api/patchdestinationrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.PatchDestinationResponse](../../api/patchdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## put_destination

Update a Destination and fully overwrite it

### Example Usage: Destination Update Request Example

<!-- UsageSnippet language="python" operationID="putDestination" method="put" path="/destinations/{destinationId}" example="Destination Update Request Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.put_destination(request=api.PutDestinationRequest(
        destination_put_request=models.DestinationPutRequest(
            configuration=models.DestinationSftpJSON(
                destination_path="/json_data",
                host="slight-consistency.info",
                password="TRmq8ozhIC5jwDd",
                port=22,
                username="Easton_Wilderman",
            ),
            name="My Destination",
        ),
        destination_id="<value>",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```
### Example Usage: Destination Update Response Example

<!-- UsageSnippet language="python" operationID="putDestination" method="put" path="/destinations/{destinationId}" example="Destination Update Response Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.destinations.put_destination(request=api.PutDestinationRequest(
        destination_put_request=models.DestinationPutRequest(
            configuration=models.DestinationSalesforce(
                client_id="<id>",
                client_secret="<value>",
                is_sandbox=False,
                refresh_token="<value>",
            ),
            name="<value>",
        ),
        destination_id="<value>",
    ))

    assert res.destination_response is not None

    # Handle response
    print(res.destination_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PutDestinationRequest](../../api/putdestinationrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.PutDestinationResponse](../../api/putdestinationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |