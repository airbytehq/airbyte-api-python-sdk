# SourceDefinitions

## Overview

### Available Operations

* [create_source_definition](#create_source_definition) - Create a source definition.
* [delete_source_definition](#delete_source_definition) - Delete a source definition.
* [get_source_definition](#get_source_definition) - Get source definition details.
* [list_source_definitions](#list_source_definitions) - List source definitions.
* [update_source_definition](#update_source_definition) - Update source definition details.

## create_source_definition

Create a source definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="createSourceDefinition" method="post" path="/workspaces/{workspaceId}/definitions/sources" -->
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

    res = aa_client.source_definitions.create_source_definition(request={
        "workspace_id": "8198a6e0-f056-42f7-8427-5ff6e06d6b3c",
        "create_definition_request": {
            "docker_image_tag": "<value>",
            "docker_repository": "<value>",
            "name": "<value>",
        },
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.CreateSourceDefinitionRequest](../../api/createsourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[api.CreateSourceDefinitionResponse](../../api/createsourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_source_definition

Delete a source definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSourceDefinition" method="delete" path="/workspaces/{workspaceId}/definitions/sources/{definitionId}" -->
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

    res = aa_client.source_definitions.delete_source_definition(request={
        "workspace_id": "674a8870-5757-45f8-89f2-a765895d7bcc",
        "definition_id": "21000375-129d-49b4-8099-23a142e25559",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.DeleteSourceDefinitionRequest](../../api/deletesourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[api.DeleteSourceDefinitionResponse](../../api/deletesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_source_definition

Get source definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="getSourceDefinition" method="get" path="/workspaces/{workspaceId}/definitions/sources/{definitionId}" -->
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

    res = aa_client.source_definitions.get_source_definition(request={
        "workspace_id": "ea535916-6a24-4a05-b039-7da73c74b7c5",
        "definition_id": "ccda715b-b5a9-4c56-9c95-7285878c622f",
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [api.GetSourceDefinitionRequest](../../api/getsourcedefinitionrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[api.GetSourceDefinitionResponse](../../api/getsourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_source_definitions

List source definitions.

### Example Usage

<!-- UsageSnippet language="python" operationID="listSourceDefinitions" method="get" path="/workspaces/{workspaceId}/definitions/sources" -->
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

    res = aa_client.source_definitions.list_source_definitions(request={
        "workspace_id": "d85ea6af-c9b0-461e-8a87-d7d38bfb62a3",
    })

    assert res.definitions_response is not None

    # Handle response
    print(res.definitions_response)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [api.ListSourceDefinitionsRequest](../../api/listsourcedefinitionsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[api.ListSourceDefinitionsResponse](../../api/listsourcedefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_source_definition

Update source definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSourceDefinition" method="put" path="/workspaces/{workspaceId}/definitions/sources/{definitionId}" -->
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

    res = aa_client.source_definitions.update_source_definition(request={
        "workspace_id": "d00d0938-69b2-48ac-878f-e92689d1c3b8",
        "definition_id": "d83c1bd9-0e8c-47a0-ba61-d9fff4bea47c",
        "update_definition_request": {
            "docker_image_tag": "<value>",
            "name": "<value>",
        },
    })

    assert res.definition_response is not None

    # Handle response
    print(res.definition_response)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.UpdateSourceDefinitionRequest](../../api/updatesourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[api.UpdateSourceDefinitionResponse](../../api/updatesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |