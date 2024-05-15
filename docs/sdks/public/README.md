# Public
(*public*)

### Available Operations

* [cancel_job](#cancel_job) - Cancel a running Job
* [create_connection](#create_connection) - Create a connection
* [create_destination](#create_destination) - Create a destination
* [create_job](#create_job) - Trigger a sync or reset job of a connection
* [create_or_update_workspace_o_auth_credentials](#create_or_update_workspace_o_auth_credentials) - Create OAuth override credentials for a workspace and source type.
* [create_permission](#create_permission) - Create a permission
* [create_source](#create_source) - Create a source
* [create_workspace](#create_workspace) - Create a workspace
* [delete_connection](#delete_connection) - Delete a Connection
* [delete_destination](#delete_destination) - Delete a Destination
* [delete_source](#delete_source) - Delete a Source
* [delete_workspace](#delete_workspace) - Delete a Workspace
* [get_connection](#get_connection) - Get Connection details
* [get_destination](#get_destination) - Get Destination details
* [get_job](#get_job) - Get Job status and details
* [get_source](#get_source) - Get Source details
* [get_stream_properties](#get_stream_properties) - Get stream properties
* [get_workspace](#get_workspace) - Get Workspace details
* [initiate_o_auth](#initiate_o_auth) - Initiate OAuth for a source
* [list_connections](#list_connections) - List connections
* [list_destinations](#list_destinations) - List destinations
* [list_jobs](#list_jobs) - List Jobs by sync type
* [list_sources](#list_sources) - List sources
* [list_workspaces](#list_workspaces) - List workspaces
* [patch_connection](#patch_connection) - Update Connection details
* [patch_destination](#patch_destination) - Update a Destination
* [patch_source](#patch_source) - Update a Source
* [put_destination](#put_destination) - Update a Destination and fully overwrite it
* [put_source](#put_source) - Update a Source and fully overwrite it
* [update_workspace](#update_workspace) - Update a workspace

## cancel_job

Cancel a running Job

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

res = s.public.cancel_job(request=api.CancelJobRequest(
    job_id=801771,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.CancelJobRequest](../../api/canceljobrequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[api.CancelJobResponse](../../api/canceljobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_connection

Create a connection

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

res = s.public.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.ConnectionCreateRequest](../../models/connectioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[api.CreateConnectionResponse](../../api/createconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_destination

Creates a destination given a name, workspace id, and a json blob containing the configuration for the source.

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

res = s.public.create_destination(request=models.DestinationCreateRequest(
    configuration=models.DestinationGoogleSheets(
        credentials=models.AuthenticationViaGoogleOAuth(
            client_id='<value>',
            client_secret='<value>',
            refresh_token='<value>',
        ),
        spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
    ),
    name='Postgres',
    workspace_id='2155ae5a-de39-4808-af6a-16fe7b8b4ed2',
))

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.DestinationCreateRequest](../../models/destinationcreaterequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |


### Response

**[api.CreateDestinationResponse](../../api/createdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_job

Trigger a sync or reset job of a connection

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

res = s.public.create_job(request=models.JobCreateRequest(
    connection_id='e735894a-e773-4938-969f-45f53957b75b',
    job_type=models.JobTypeEnum.SYNC,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.JobCreateRequest](../../models/jobcreaterequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[api.CreateJobResponse](../../api/createjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

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

res = s.public.create_or_update_workspace_o_auth_credentials(request=api.CreateOrUpdateWorkspaceOAuthCredentialsRequest(
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

## create_permission

Create a permission

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

res = s.public.create_permission(request=models.PermissionCreateRequest(
    permission_type=models.PermissionType.WORKSPACE_ADMIN,
    user_id='7d08fd6c-531e-4a00-937e-3d355f253e63',
    workspace_id='9924bcd0-99be-453d-ba47-c2c9766f7da5',
))

if res.permission_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.PermissionCreateRequest](../../models/permissioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[api.CreatePermissionResponse](../../api/createpermissionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_source

Creates a source given a name, workspace id, and a json blob containing the configuration for the source.

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

res = s.public.create_source(request=models.SourceCreateRequest(
    configuration=models.SourceAha(
        api_key='<value>',
        url='https://complicated-seat.org',
    ),
    name='My Source',
    workspace_id='744cc0ed-7f05-4949-9e60-2a814f90c035',
))

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [models.SourceCreateRequest](../../models/sourcecreaterequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.CreateSourceResponse](../../api/createsourceresponse.md)**
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

res = s.public.create_workspace(request=models.WorkspaceCreateRequest(
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

## delete_connection

Delete a Connection

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

res = s.public.delete_connection(request=api.DeleteConnectionRequest(
    connection_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteConnectionRequest](../../api/deleteconnectionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.DeleteConnectionResponse](../../api/deleteconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_destination

Delete a Destination

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

res = s.public.delete_destination(request=api.DeleteDestinationRequest(
    destination_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [api.DeleteDestinationRequest](../../api/deletedestinationrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |


### Response

**[api.DeleteDestinationResponse](../../api/deletedestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_source

Delete a Source

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

res = s.public.delete_source(request=api.DeleteSourceRequest(
    source_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [api.DeleteSourceRequest](../../api/deletesourcerequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |


### Response

**[api.DeleteSourceResponse](../../api/deletesourceresponse.md)**
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

res = s.public.delete_workspace(request=api.DeleteWorkspaceRequest(
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

## get_connection

Get Connection details

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

res = s.public.get_connection(request=api.GetConnectionRequest(
    connection_id='<value>',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `request`                                                     | [api.GetConnectionRequest](../../api/getconnectionrequest.md) | :heavy_check_mark:                                            | The request object to use for the request.                    |


### Response

**[api.GetConnectionResponse](../../api/getconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_destination

Get Destination details

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

res = s.public.get_destination(request=api.GetDestinationRequest(
    destination_id='<value>',
))

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [api.GetDestinationRequest](../../api/getdestinationrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[api.GetDestinationResponse](../../api/getdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_job

Get Job status and details

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

res = s.public.get_job(request=api.GetJobRequest(
    job_id=131101,
))

if res.job_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `request`                                       | [api.GetJobRequest](../../api/getjobrequest.md) | :heavy_check_mark:                              | The request object to use for the request.      |


### Response

**[api.GetJobResponse](../../api/getjobresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_source

Get Source details

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

res = s.public.get_source(request=api.GetSourceRequest(
    source_id='<value>',
))

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.GetSourceRequest](../../api/getsourcerequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[api.GetSourceResponse](../../api/getsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_stream_properties

Get stream properties

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

res = s.public.get_stream_properties(request=api.GetStreamPropertiesRequest(
    source_id='<value>',
))

if res.stream_properties_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [api.GetStreamPropertiesRequest](../../api/getstreampropertiesrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |


### Response

**[api.GetStreamPropertiesResponse](../../api/getstreampropertiesresponse.md)**
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

res = s.public.get_workspace(request=api.GetWorkspaceRequest(
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

## initiate_o_auth

Given a source ID, workspace ID, and redirect URL, initiates OAuth for the source.

This returns a fully formed URL for performing user authentication against the relevant source identity provider (IdP). Once authentication has been completed, the IdP will redirect to an Airbyte endpoint which will save the access and refresh tokens off as a secret and return the secret ID to the redirect URL specified in the `secret_id` query string parameter.

That secret ID can be used to create a source with credentials in place of actual tokens.

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

res = s.public.initiate_o_auth(request=models.InitiateOauthRequest(
    redirect_url='https://cloud.airbyte.io/v1/api/oauth/callback',
    source_type=models.OAuthActorNames.GITLAB,
    workspace_id='871d9b60-11d1-44cb-8c92-c246d53bf87e',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.InitiateOauthRequest](../../models/initiateoauthrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.InitiateOAuthResponse](../../api/initiateoauthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_connections

List connections

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

res = s.public.list_connections(request=api.ListConnectionsRequest())

if res.connections_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.ListConnectionsRequest](../../api/listconnectionsrequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.ListConnectionsResponse](../../api/listconnectionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_destinations

List destinations

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

res = s.public.list_destinations(request=api.ListDestinationsRequest())

if res.destinations_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListDestinationsRequest](../../api/listdestinationsrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.ListDestinationsResponse](../../api/listdestinationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_jobs

List Jobs by sync type

### Example Usage

```python
import airbyte_api
import dateutil.parser
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.public.list_jobs(request=api.ListJobsRequest(
    created_at_end=dateutil.parser.isoparse('1687450500000'),
    created_at_start=dateutil.parser.isoparse('1687450500000'),
    order_by='updatedAt|DESC',
    updated_at_end=dateutil.parser.isoparse('1687450500000'),
    updated_at_start=dateutil.parser.isoparse('1687450500000'),
))

if res.jobs_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                           | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `request`                                           | [api.ListJobsRequest](../../api/listjobsrequest.md) | :heavy_check_mark:                                  | The request object to use for the request.          |


### Response

**[api.ListJobsResponse](../../api/listjobsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_sources

List sources

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

res = s.public.list_sources(request=api.ListSourcesRequest(
    workspace_ids=[
        'd',
        'f',
        '0',
        '8',
        'f',
        '6',
        'b',
        '0',
        '-',
        'b',
        '3',
        '6',
        '4',
        '-',
        '4',
        'c',
        'c',
        '1',
        '-',
        '9',
        'b',
        '3',
        'f',
        '-',
        '9',
        '6',
        'f',
        '5',
        'd',
        '2',
        'f',
        'c',
        'c',
        'f',
        'b',
        '2',
        ',',
        'b',
        '0',
        '7',
        '9',
        '6',
        '7',
        '9',
        '7',
        '-',
        'd',
        'e',
        '2',
        '3',
        '-',
        '4',
        'f',
        'c',
        '7',
        '-',
        'a',
        '5',
        'e',
        '2',
        '-',
        '7',
        'e',
        '1',
        '3',
        '1',
        '3',
        '1',
        '4',
        '7',
        '1',
        '8',
        'c',
    ],
))

if res.sources_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                 | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `request`                                                 | [api.ListSourcesRequest](../../api/listsourcesrequest.md) | :heavy_check_mark:                                        | The request object to use for the request.                |


### Response

**[api.ListSourcesResponse](../../api/listsourcesresponse.md)**
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

res = s.public.list_workspaces(request=api.ListWorkspacesRequest())

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

## patch_connection

Update Connection details

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

res = s.public.patch_connection(request=api.PatchConnectionRequest(
    connection_patch_request=models.ConnectionPatchRequest(
        namespace_format='${SOURCE_NAMESPACE}',
    ),
    connection_id='<value>',
))

if res.connection_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.PatchConnectionRequest](../../api/patchconnectionrequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |


### Response

**[api.PatchConnectionResponse](../../api/patchconnectionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_destination

Update a Destination

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

res = s.public.patch_destination(request=api.PatchDestinationRequest(
    destination_id='<value>',
    destination_patch_request=models.DestinationPatchRequest(
        configuration=models.DestinationGoogleSheets(
            credentials=models.AuthenticationViaGoogleOAuth(
                client_id='<value>',
                client_secret='<value>',
                refresh_token='<value>',
            ),
            spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
        ),
    ),
))

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PatchDestinationRequest](../../api/patchdestinationrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[api.PatchDestinationResponse](../../api/patchdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## patch_source

Update a Source

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

res = s.public.patch_source(request=api.PatchSourceRequest(
    source_id='<value>',
    source_patch_request=models.SourcePatchRequest(
        configuration=models.SourceAha(
            api_key='<value>',
            url='http://apprehensive-visa.net',
        ),
        name='My source',
    ),
))

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                 | Type                                                      | Required                                                  | Description                                               |
| --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------- |
| `request`                                                 | [api.PatchSourceRequest](../../api/patchsourcerequest.md) | :heavy_check_mark:                                        | The request object to use for the request.                |


### Response

**[api.PatchSourceResponse](../../api/patchsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_destination

Update a Destination and fully overwrite it

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

res = s.public.put_destination(request=api.PutDestinationRequest(
    destination_id='<value>',
    destination_put_request=models.DestinationPutRequest(
        configuration=models.DestinationGoogleSheets(
            credentials=models.AuthenticationViaGoogleOAuth(
                client_id='<value>',
                client_secret='<value>',
                refresh_token='<value>',
            ),
            spreadsheet_id='https://docs.google.com/spreadsheets/d/1hLd9Qqti3UyLXZB2aFfUWDT7BG/edit',
        ),
        name='<value>',
    ),
))

if res.destination_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `request`                                                       | [api.PutDestinationRequest](../../api/putdestinationrequest.md) | :heavy_check_mark:                                              | The request object to use for the request.                      |


### Response

**[api.PutDestinationResponse](../../api/putdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_source

Update a Source and fully overwrite it

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

res = s.public.put_source(request=api.PutSourceRequest(
    source_id='<value>',
    source_put_request=models.SourcePutRequest(
        configuration=models.SourceAha(
            api_key='<value>',
            url='http://alienated-traveler.name',
        ),
        name='<value>',
    ),
))

if res.source_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.PutSourceRequest](../../api/putsourcerequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[api.PutSourceResponse](../../api/putsourceresponse.md)**
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

res = s.public.update_workspace(request=api.UpdateWorkspaceRequest(
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
