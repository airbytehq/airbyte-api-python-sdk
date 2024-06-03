# Workspaces
(*workspaces*)

### Available Operations

* [create_or_update_workspace_o_auth_credentials](#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](#create_workspace) - Create a workspace
* [delete_workspace](#delete_workspace) - Delete a Workspace
* [get_workspace](#get_workspace) - Get Workspace details
* [list_workspaces](#list_workspaces) - List workspaces
* [update_workspace](#update_workspace) - Update a workspace

## create_or_update_workspace_o_auth_credentials

Create/update a set of OAuth credentials to override the Airbyte-provided OAuth credentials used for source/destination OAuth.
In order to determine what the credential configuration needs to be, please see the connector specification of the relevant  source/destination.

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


res = s.workspaces.create_or_update_workspace_o_auth_credentials(request=api.CreateOrUpdateWorkspaceOAuthCredentialsRequest(
    workspace_o_auth_credentials_request=models.WorkspaceOAuthCredentialsRequest(
        actor_type=models.ActorTypeEnum.DESTINATION,
        configuration=models.Airtable(),
        name=models.OAuthActorNames.AMAZON_ADS,
    ),
    workspace_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [api.CreateOrUpdateWorkspaceOAuthCredentialsRequest](../../api/createorupdateworkspaceoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |


### Response

**[api.CreateOrUpdateWorkspaceOAuthCredentialsResponse](../../api/createorupdateworkspaceoauthcredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_workspace

Create a workspace

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


res = s.workspaces.create_workspace(request=models.WorkspaceCreateRequest(
    name='Company Workspace Name',
))

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.WorkspaceCreateRequest](../../models/workspacecreaterequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |


### Response

**[api.CreateWorkspaceResponse](../../api/createworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_workspace

Delete a Workspace

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


res = s.workspaces.delete_workspace(request=api.DeleteWorkspaceRequest(
    workspace_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.DeleteWorkspaceRequest](../../api/deleteworkspacerequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.DeleteWorkspaceResponse](../../api/deleteworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_workspace

Get Workspace details

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


res = s.workspaces.get_workspace(request=api.GetWorkspaceRequest(
    workspace_id='<value>',
))

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [api.GetWorkspaceRequest](../../api/getworkspacerequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[api.GetWorkspaceResponse](../../api/getworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_workspaces

List workspaces

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


res = s.workspaces.list_workspaces(request=api.ListWorkspacesRequest())

if res.workspaces_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [api.ListWorkspacesRequest](../../api/listworkspacesrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[api.ListWorkspacesResponse](../../api/listworkspacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_workspace

Update a workspace

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


res = s.workspaces.update_workspace(request=api.UpdateWorkspaceRequest(
    workspace_update_request=models.WorkspaceUpdateRequest(
        name='<value>',
    ),
    workspace_id='<value>',
))

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.UpdateWorkspaceRequest](../../api/updateworkspacerequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.UpdateWorkspaceResponse](../../api/updateworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
