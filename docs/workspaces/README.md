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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateOrUpdateWorkspaceOAuthCredentialsRequest(
    workspace_o_auth_credentials_request=shared.WorkspaceOAuthCredentialsRequest(
        actor_type=shared.ActorTypeEnum.SOURCE,
        configuration={
            "praesentium": 'consequuntur',
            "deleniti": 'fugit',
            "fuga": 'mollitia',
        },
        name='Leah Champlin',
    ),
    workspace_id='fugit',
)

res = s.workspaces.create_or_update_workspace_o_auth_credentials(req)

if res.status_code == 200:
    # handle response
```

## create_workspace

Create a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.WorkspaceCreateRequest(
    name='Eugene Dibbert',
)

res = s.workspaces.create_workspace(req)

if res.workspace_response is not None:
    # handle response
```

## delete_workspace

Delete a Workspace

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteWorkspaceRequest(
    workspace_id='occaecati',
)

res = s.workspaces.delete_workspace(req)

if res.status_code == 200:
    # handle response
```

## get_workspace

Get Workspace details

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetWorkspaceRequest(
    workspace_id='atque',
)

res = s.workspaces.get_workspace(req)

if res.workspace_response is not None:
    # handle response
```

## list_workspaces

List workspaces

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListWorkspacesRequest(
    include_deleted=False,
    limit=92260,
    offset=456911,
    workspace_ids=[
        'e17cbe61-e6b7-4b95-bc0a-b3c20c4f3789',
        'fd871f99-dd2e-4fd1-a1aa-6f1e674bdb04',
        'f1575608-2d68-4ea1-9f1d-17051339d080',
        '86a18403-94c2-4607-9f93-f5f0642dac7a',
    ],
)

res = s.workspaces.list_workspaces(req)

if res.workspaces_response is not None:
    # handle response
```

## update_workspace

Update a workspace

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateWorkspaceRequest(
    workspace_update_request=shared.WorkspaceUpdateRequest(
        name='Vernon Bergnaum',
    ),
    workspace_id='quod',
)

res = s.workspaces.update_workspace(req)

if res.workspace_response is not None:
    # handle response
```
