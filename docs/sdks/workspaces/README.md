# workspaces

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
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.CreateOrUpdateWorkspaceOAuthCredentialsRequest(
    workspace_o_auth_credentials_request=shared.WorkspaceOAuthCredentialsRequest(
        actor_type=shared.ActorTypeEnum.SOURCE,
        configuration=shared.FacebookMarketing(
            client_id='voluptas',
            client_secret='voluptas',
        ),
        name=shared.OAuthActorNames.INSTAGRAM,
    ),
    workspace_id='minima',
)

res = s.workspaces.create_or_update_workspace_o_auth_credentials(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.CreateOrUpdateWorkspaceOAuthCredentialsRequest](../../models/operations/createorupdateworkspaceoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.CreateOrUpdateWorkspaceOAuthCredentialsResponse](../../models/operations/createorupdateworkspaceoauthcredentialsresponse.md)**


## create_workspace

Create a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.WorkspaceCreateRequest(
    name='Wilbur Ferry',
)

res = s.workspaces.create_workspace(req)

if res.workspace_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceCreateRequest](../../models/shared/workspacecreaterequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateWorkspaceResponse](../../models/operations/createworkspaceresponse.md)**


## delete_workspace

Delete a Workspace

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteWorkspaceRequest(
    workspace_id='blanditiis',
)

res = s.workspaces.delete_workspace(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeleteWorkspaceRequest](../../models/operations/deleteworkspacerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeleteWorkspaceResponse](../../models/operations/deleteworkspaceresponse.md)**


## get_workspace

Get Workspace details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkspaceRequest(
    workspace_id='in',
)

res = s.workspaces.get_workspace(req)

if res.workspace_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetWorkspaceRequest](../../models/operations/getworkspacerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetWorkspaceResponse](../../models/operations/getworkspaceresponse.md)**


## list_workspaces

List workspaces

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListWorkspacesRequest(
    include_deleted=False,
    limit=296242,
    offset=304468,
    workspace_ids=[
        'd53b88f3-a8d8-4f5c-8b2f-2fb7b194a276',
        'b26916fe-1f08-4f42-94e3-698f447f603e',
        '8b445e80-ca55-4efd-a0e4-57e1858b6a89',
        'fbe3a5aa-8e48-424d-8ab4-075088e51862',
    ],
)

res = s.workspaces.list_workspaces(req)

if res.workspaces_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.ListWorkspacesRequest](../../models/operations/listworkspacesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ListWorkspacesResponse](../../models/operations/listworkspacesresponse.md)**


## update_workspace

Update a workspace

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateWorkspaceRequest(
    workspace_update_request=shared.WorkspaceUpdateRequest(
        name='Gina Heathcote',
    ),
    workspace_id='consequatur',
)

res = s.workspaces.update_workspace(req)

if res.workspace_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateWorkspaceRequest](../../models/operations/updateworkspacerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateWorkspaceResponse](../../models/operations/updateworkspaceresponse.md)**

