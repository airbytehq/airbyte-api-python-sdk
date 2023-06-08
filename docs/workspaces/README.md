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
        configuration={
            "dolores": 'deserunt',
            "molestiae": 'accusantium',
            "porro": 'eum',
            "quas": 'praesentium',
        },
        name='Cassandra Considine',
    ),
    workspace_id='incidunt',
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
        bearer_auth="",
    ),
)

req = shared.WorkspaceCreateRequest(
    name='Roy Hansen',
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
        bearer_auth="",
    ),
)

req = operations.DeleteWorkspaceRequest(
    workspace_id='sapiente',
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
        bearer_auth="",
    ),
)

req = operations.GetWorkspaceRequest(
    workspace_id='consequuntur',
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
        bearer_auth="",
    ),
)

req = operations.ListWorkspacesRequest(
    include_deleted=False,
    limit=187131,
    offset=129412,
    workspace_ids=[
        '9817ee17-cbe6-41e6-b7b9-5bc0ab3c20c4',
        'f3789fd8-71f9-49dd-aefd-121aa6f1e674',
        'bdb04f15-7560-482d-a8ea-19f1d1705133',
        '9d08086a-1840-4394-8260-71f93f5f0642',
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
        bearer_auth="",
    ),
)

req = operations.UpdateWorkspaceRequest(
    workspace_update_request=shared.WorkspaceUpdateRequest(
        name='Luke Schoen',
    ),
    workspace_id='asperiores',
)

res = s.workspaces.update_workspace(req)

if res.workspace_response is not None:
    # handle response
```
