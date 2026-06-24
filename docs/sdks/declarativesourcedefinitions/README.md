# DeclarativeSourceDefinitions

## Overview

### Available Operations

* [create_declarative_source_definition](#create_declarative_source_definition) - Create a declarative source definition.
* [delete_declarative_source_definition](#delete_declarative_source_definition) - Delete a declarative source definition.
* [get_declarative_source_definition](#get_declarative_source_definition) - Get declarative source definition details.
* [list_declarative_source_definitions](#list_declarative_source_definitions) - List declarative source definitions.
* [update_declarative_source_definition](#update_declarative_source_definition) - Update declarative source definition details.

## create_declarative_source_definition

Create a declarative source definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="createDeclarativeSourceDefinition" method="post" path="/workspaces/{workspaceId}/definitions/declarative_sources" -->
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

    res = aa_client.declarative_source_definitions.create_declarative_source_definition(request={
        "workspace_id": "9f09326e-38fd-40ea-8871-6aaf7655a237",
        "create_declarative_source_definition_request": {
            "manifest": "<value>",
            "name": "<value>",
        },
    })

    assert res.declarative_source_definition_response is not None

    # Handle response
    print(res.declarative_source_definition_response)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.CreateDeclarativeSourceDefinitionRequest](../../api/createdeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[api.CreateDeclarativeSourceDefinitionResponse](../../api/createdeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_declarative_source_definition

Delete a declarative source definition.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteDeclarativeSourceDefinition" method="delete" path="/workspaces/{workspaceId}/definitions/declarative_sources/{definitionId}" -->
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

    res = aa_client.declarative_source_definitions.delete_declarative_source_definition(request={
        "workspace_id": "5bed2604-75d1-40cf-a858-64e430840198",
        "definition_id": "0cf3a1f6-1af6-4ae7-ae77-4bd1b32041f4",
    })

    assert res.declarative_source_definition_response is not None

    # Handle response
    print(res.declarative_source_definition_response)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.DeleteDeclarativeSourceDefinitionRequest](../../api/deletedeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[api.DeleteDeclarativeSourceDefinitionResponse](../../api/deletedeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_declarative_source_definition

Get declarative source definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="getDeclarativeSourceDefinition" method="get" path="/workspaces/{workspaceId}/definitions/declarative_sources/{definitionId}" -->
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

    res = aa_client.declarative_source_definitions.get_declarative_source_definition(request={
        "workspace_id": "2a50feae-cf51-42e9-b777-b8d52ea2704e",
        "definition_id": "ce3288f2-b43c-40d0-ae8e-864c7a844485",
    })

    assert res.declarative_source_definition_response is not None

    # Handle response
    print(res.declarative_source_definition_response)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [api.GetDeclarativeSourceDefinitionRequest](../../api/getdeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[api.GetDeclarativeSourceDefinitionResponse](../../api/getdeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_declarative_source_definitions

List declarative source definitions.

### Example Usage

<!-- UsageSnippet language="python" operationID="listDeclarativeSourceDefinitions" method="get" path="/workspaces/{workspaceId}/definitions/declarative_sources" -->
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

    res = aa_client.declarative_source_definitions.list_declarative_source_definitions(request={
        "workspace_id": "76222ecd-532e-4ab1-94e3-b96d1abd686e",
    })

    assert res.declarative_source_definitions_response is not None

    # Handle response
    print(res.declarative_source_definitions_response)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [api.ListDeclarativeSourceDefinitionsRequest](../../api/listdeclarativesourcedefinitionsrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[api.ListDeclarativeSourceDefinitionsResponse](../../api/listdeclarativesourcedefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_declarative_source_definition

Update declarative source definition details.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateDeclarativeSourceDefinition" method="put" path="/workspaces/{workspaceId}/definitions/declarative_sources/{definitionId}" -->
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

    res = aa_client.declarative_source_definitions.update_declarative_source_definition(request={
        "workspace_id": "38cb8d27-592a-4438-be38-823abf06a84e",
        "definition_id": "c97eb9ab-47b5-4609-8d65-0a62f74ca843",
        "update_declarative_source_definition_request": {
            "manifest": "<value>",
        },
    })

    assert res.declarative_source_definition_response is not None

    # Handle response
    print(res.declarative_source_definition_response)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.UpdateDeclarativeSourceDefinitionRequest](../../api/updatedeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[api.UpdateDeclarativeSourceDefinitionResponse](../../api/updatedeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |