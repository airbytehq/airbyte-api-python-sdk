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
            "error": 'sint',
            "pariatur": 'possimus',
            "quia": 'eveniet',
            "asperiores": 'facere',
        },
        name='Marilyn Botsford',
    ),
    workspace_id='aliquid',
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
    name='Scott Wehner',
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
    workspace_id='eius',
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
    workspace_id='libero',
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
    limit=849039,
    offset=742238,
    workspace_ids=[
        '4f157560-82d6-48ea-99f1-d17051339d08',
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
        name='Marsha Keebler IV',
    ),
    workspace_id='non',
)

res = s.workspaces.update_workspace(req)

if res.workspace_response is not None:
    # handle response
```
