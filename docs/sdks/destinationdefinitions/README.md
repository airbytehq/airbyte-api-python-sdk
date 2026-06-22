# DestinationDefinitions

## Overview

### Available Operations

* [create_destination_definition](#create_destination_definition) - Create a destination definition.
* [delete_destination_definition](#delete_destination_definition) - Delete a destination definition.
* [get_destination_definition](#get_destination_definition) - Get destination definition details.
* [list_destination_definitions](#list_destination_definitions) - List destination definitions.
* [update_destination_definition](#update_destination_definition) - Update destination definition details.

## create_destination_definition

Create a destination definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDestinationDefinition" method="post" path="/workspaces/{workspaceId}/definitions/destinations" -->
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

    res = aa_client.destination_definitions.create_destination_definition(request={
        "create_definition_request": {
            "docker_image_tag": "<value>",
            "docker_repository": "<value>",
            "name": "<value>",
        },
        "workspace_id": "20a22858-a8c3-4a9c-af3e-691931b55938",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.CreateDestinationDefinitionRequest](../../api/createdestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[api.CreateDestinationDefinitionResponse](../../api/createdestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_destination_definition

Delete a destination definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDestinationDefinition" method="delete" path="/workspaces/{workspaceId}/definitions/destinations/{definitionId}" -->
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

    res = aa_client.destination_definitions.delete_destination_definition(request={
        "definition_id": "1f3ace88-4e9e-4438-8667-c98520825c79",
        "workspace_id": "b1b184d8-4def-4e2d-8e9d-7caadc80e180",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.DeleteDestinationDefinitionRequest](../../api/deletedestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[api.DeleteDestinationDefinitionResponse](../../api/deletedestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_destination_definition

Get destination definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDestinationDefinition" method="get" path="/workspaces/{workspaceId}/definitions/destinations/{definitionId}" -->
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

    res = aa_client.destination_definitions.get_destination_definition(request={
        "definition_id": "83a7ce8a-1507-42c5-84a3-1b95932f919f",
        "workspace_id": "443f2bd2-d502-4aec-b86f-c4e3d5675ae9",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [api.GetDestinationDefinitionRequest](../../api/getdestinationdefinitionrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[api.GetDestinationDefinitionResponse](../../api/getdestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_destination_definitions

List destination definitions.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDestinationDefinitions" method="get" path="/workspaces/{workspaceId}/definitions/destinations" -->
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

    res = aa_client.destination_definitions.list_destination_definitions(request={
        "workspace_id": "aed43ac9-470c-4cba-8489-c73f9e881f94",
    })

    assert res.definitions_response is not None

    # Handle response
    print(res.definitions_response)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [api.ListDestinationDefinitionsRequest](../../api/listdestinationdefinitionsrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[api.ListDestinationDefinitionsResponse](../../api/listdestinationdefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_destination_definition

Update destination definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDestinationDefinition" method="put" path="/workspaces/{workspaceId}/definitions/destinations/{definitionId}" -->
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

    res = aa_client.destination_definitions.update_destination_definition(request={
        "update_definition_request": {
            "docker_image_tag": "<value>",
            "name": "<value>",
        },
        "definition_id": "43c71f97-6486-49c7-9f26-4de603fa3bb2",
        "workspace_id": "29dd981b-57da-413b-b1f4-012b1a97afc4",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.UpdateDestinationDefinitionRequest](../../api/updatedestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[api.UpdateDestinationDefinitionResponse](../../api/updatedestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |