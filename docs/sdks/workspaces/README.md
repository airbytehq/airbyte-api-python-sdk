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

s = airbyte_api.AirbyteAPI()

req = airbyte_api.CreateOrUpdateWorkspaceOAuthCredentialsRequest(
    workspace_o_auth_credentials_request=airbyte_api.WorkspaceOAuthCredentialsRequest(
        actor_type=airbyte_api.ActorTypeEnum.DESTINATION,
        configuration=airbyte_api.OAuthCredentialsConfiguration(),
        name='<value>',
    ),
    workspace_id='<value>',
)

res = s.workspaces.create_or_update_workspace_o_auth_credentials(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                               | [models.CreateOrUpdateWorkspaceOAuthCredentialsRequest](../../models/createorupdateworkspaceoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                      | The request object to use for the request.                                                                              |


### Response

**[models.CreateOrUpdateWorkspaceOAuthCredentialsResponse](../../models/createorupdateworkspaceoauthcredentialsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create_workspace

Create a workspace

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.WorkspaceCreateRequest(
    name='<value>',
)

res = s.workspaces.create_workspace(req)

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.WorkspaceCreateRequest](../../models/workspacecreaterequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |


### Response

**[models.CreateWorkspaceResponse](../../models/createworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## delete_workspace

Delete a Workspace

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.DeleteWorkspaceRequest(
    workspace_id='<value>',
)

res = s.workspaces.delete_workspace(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.DeleteWorkspaceRequest](../../models/deleteworkspacerequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |


### Response

**[models.DeleteWorkspaceResponse](../../models/deleteworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_workspace

Get Workspace details

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.GetWorkspaceRequest(
    workspace_id='<value>',
)

res = s.workspaces.get_workspace(req)

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [models.GetWorkspaceRequest](../../models/getworkspacerequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[models.GetWorkspaceResponse](../../models/getworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## list_workspaces

List workspaces

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.ListWorkspacesRequest()

res = s.workspaces.list_workspaces(req)

if res.workspaces_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ListWorkspacesRequest](../../models/listworkspacesrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |


### Response

**[models.ListWorkspacesResponse](../../models/listworkspacesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## update_workspace

Update a workspace

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.UpdateWorkspaceRequest(
    workspace_update_request=airbyte_api.WorkspaceUpdateRequest(
        name='<value>',
    ),
    workspace_id='<value>',
)

res = s.workspaces.update_workspace(req)

if res.workspace_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UpdateWorkspaceRequest](../../models/updateworkspacerequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |


### Response

**[models.UpdateWorkspaceResponse](../../models/updateworkspaceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
