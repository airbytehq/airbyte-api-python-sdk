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
        actor_type=shared.ActorTypeEnum.DESTINATION,
        configuration=shared.Mailchimp(
            credentials=shared.MailchimpCredentials(
                client_id='accusantium',
                client_secret='porro',
            ),
        ),
        source_type=shared.OAuthActorNames.LEVER_HIRING,
    ),
    workspace_id='quas',
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
    name='Eugene Leuschke',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteWorkspaceRequest(
    workspace_id='mollitia',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetWorkspaceRequest(
    workspace_id='incidunt',
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
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListWorkspacesRequest(
    include_deleted=False,
    limit=539224,
    offset=128860,
    workspace_ids=[
        '62f222e9-817e-4e17-8be6-1e6b7b95bc0a',
        'b3c20c4f-3789-4fd8-b1f9-9dd2efd121aa',
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
        name='Mandy Berge',
    ),
    workspace_id='in',
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

