# workspaces

### Available Operations

* [create_or_update_workspace_o_auth_credentials](#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_workspace](#create_workspace) - Create a workspace
* [get_workspace](#get_workspace) - Get Workspace details
* [list_workspaces](#list_workspaces) - List workspaces

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
        actor_type=shared.WorkspaceOAuthCredentialsRequestActorTypeEnum.SOURCE,
        configuration={
            "laborum": 'placeat',
            "velit": 'eum',
            "autem": 'nobis',
        },
        name='Mack Stoltenberg',
    ),
    workspace_id='quasi',
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
    name='Carrie Cole IV',
)

res = s.workspaces.create_workspace(req)

if res.workspace_response is not None:
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
    workspace_id='magnam',
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
    limit=487935,
    offset=262118,
    workspace_ids=[
        '78a7bd46-6d28-4c10-ab3c-dca4251904e5',
        '23c7e0bc-7178-4e47-96f2-a70c688282aa',
    ],
)

res = s.workspaces.list_workspaces(req)

if res.workspaces_response is not None:
    # handle response
```
