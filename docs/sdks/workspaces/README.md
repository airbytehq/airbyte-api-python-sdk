# Workspaces

## Overview

### Available Operations

* [create_or_update_workspace_o_auth_credentials](#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](#create_workspace) - Create a workspace
* [delete_workspace](#delete_workspace) - Delete a Workspace
* [delete_workspace_o_auth_credentials](#delete_workspace_o_auth_credentials) - Delete OAuth override credentials for a workspace and source/destination type.
* [get_workspace](#get_workspace) - Get Workspace details
* [list_workspaces](#list_workspaces) - List workspaces
* [update_workspace](#update_workspace) - Update a workspace

## create_or_update_workspace_o_auth_credentials

Create/update a set of OAuth credentials to override the Airbyte-provided OAuth credentials used for source/destination OAuth.
In order to determine what the credential configuration needs to be, please see the connector specification of the relevant source/destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOrUpdateWorkspaceOAuthCredentials" method="put" path="/workspaces/{workspaceId}/oauthCredentials" -->
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

    res = aa_client.workspaces.create_or_update_workspace_o_auth_credentials(request={
        "workspace_o_auth_credentials_request": {
            "actor_type": models.ActorTypeEnum.DESTINATION,
            "configuration": {

            },
            "name": "trello",
        },
        "workspace_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [api.CreateOrUpdateWorkspaceOAuthCredentialsRequest](../../api/createorupdateworkspaceoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[api.CreateOrUpdateWorkspaceOAuthCredentialsResponse](../../api/createorupdateworkspaceoauthcredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## create_workspace

Create a workspace

### Example Usage: Workspace Creation Request Example

<!-- UsageSnippet language="python" operationID="createWorkspace" method="post" path="/workspaces" example="Workspace Creation Request Example" -->
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

    res = aa_client.workspaces.create_workspace(request=models.WorkspaceCreateRequest(
        name="Company Workspace Name",
    ))

    assert res.workspace_response is not None

    # Handle response
    print(res.workspace_response)

```
### Example Usage: Workspace Creation Response Example

<!-- UsageSnippet language="python" operationID="createWorkspace" method="post" path="/workspaces" example="Workspace Creation Response Example" -->
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

    res = aa_client.workspaces.create_workspace(request=models.WorkspaceCreateRequest(
        name="<value>",
    ))

    assert res.workspace_response is not None

    # Handle response
    print(res.workspace_response)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.WorkspaceCreateRequest](../../models/workspacecreaterequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[api.CreateWorkspaceResponse](../../api/createworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_workspace

Delete a Workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWorkspace" method="delete" path="/workspaces/{workspaceId}" -->
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

    res = aa_client.workspaces.delete_workspace(request={
        "workspace_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteWorkspaceRequest](../../api/deleteworkspacerequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.DeleteWorkspaceResponse](../../api/deleteworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_workspace_o_auth_credentials

Delete a set of OAuth credentials that overrides the Airbyte-provided OAuth credentials used for source/destination OAuth.

> 🚧 Warning
>
> Deleting an override that is actively used by existing sources or destinations will cause those connectors to fail on their next sync and require re-authentication.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWorkspaceOAuthCredentials" method="delete" path="/workspaces/{workspaceId}/oauthCredentials/{actorType}/{name}" -->
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

    res = aa_client.workspaces.delete_workspace_o_auth_credentials(request={
        "actor_type": models.ActorTypeEnum.SOURCE,
        "name": "<value>",
        "workspace_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [api.DeleteWorkspaceOAuthCredentialsRequest](../../api/deleteworkspaceoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[api.DeleteWorkspaceOAuthCredentialsResponse](../../api/deleteworkspaceoauthcredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_workspace

Get Workspace details

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspace" method="get" path="/workspaces/{workspaceId}" example="Workspace Get Response Example" -->
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

    res = aa_client.workspaces.get_workspace(request={
        "workspace_id": "<value>",
    })

    assert res.workspace_response is not None

    # Handle response
    print(res.workspace_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetWorkspaceRequest](../../api/getworkspacerequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetWorkspaceResponse](../../api/getworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_workspaces

List workspaces

### Example Usage

<!-- UsageSnippet language="python" operationID="listWorkspaces" method="get" path="/workspaces" -->
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

    res = aa_client.workspaces.list_workspaces(request={})

    assert res.workspaces_response is not None

    # Handle response
    print(res.workspaces_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListWorkspacesRequest](../../api/listworkspacesrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListWorkspacesResponse](../../api/listworkspacesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_workspace

Update a workspace

### Example Usage: Workspace Update Request Example

<!-- UsageSnippet language="python" operationID="updateWorkspace" method="patch" path="/workspaces/{workspaceId}" example="Workspace Update Request Example" -->
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

    res = aa_client.workspaces.update_workspace(request=api.UpdateWorkspaceRequest(
        workspace_update_request=models.WorkspaceUpdateRequest(
            name="Company Workspace Name",
        ),
        workspace_id="<value>",
    ))

    assert res.workspace_response is not None

    # Handle response
    print(res.workspace_response)

```
### Example Usage: Workspace Update Response Example

<!-- UsageSnippet language="python" operationID="updateWorkspace" method="patch" path="/workspaces/{workspaceId}" example="Workspace Update Response Example" -->
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

    res = aa_client.workspaces.update_workspace(request=api.UpdateWorkspaceRequest(
        workspace_update_request=models.WorkspaceUpdateRequest(),
        workspace_id="<value>",
    ))

    assert res.workspace_response is not None

    # Handle response
    print(res.workspace_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.UpdateWorkspaceRequest](../../api/updateworkspacerequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.UpdateWorkspaceResponse](../../api/updateworkspaceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |