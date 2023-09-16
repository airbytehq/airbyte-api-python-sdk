# Sources

### Available Operations

* [create_source](#create_source) - Create a source
* [delete_source](#delete_source) - Delete a Source
* [get_source](#get_source) - Get Source details
* [initiate_o_auth](#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](#list_sources) - List sources
* [patch_source](#patch_source) - Update a Source
* [put_source](#put_source) - Update a Source and fully overwrite it

## create_source

Creates a source given a name, workspace id, and a json blob containing the configuration for the source.

### Example Usage

```python
import airbyte
import dateutil.parser
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceFileSecure(
        dataset_name='asperiores',
        format=shared.SourceFileSecureFileFormat.YAML,
        provider='modi',
        reader_options='{"sep": " "}',
        source_type=shared.SourceFileSecureFileSecure.FILE_SECURE,
        url='s3://gdelt-open-data/events/20190914.export.csv',
    ),
    name='Ervin McLaughlin',
    secret_id='delectus',
    workspace_id='48633323-f9b7-47f3-a410-0674ebf69280',
)

res = s.sources.create_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceCreateRequest](../../models/shared/sourcecreaterequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## delete_source

Delete a Source

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.DeleteSourceRequest(
    source_id='fugiat',
)

res = s.sources.delete_source(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSourceRequest](../../models/operations/deletesourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSourceResponse](../../models/operations/deletesourceresponse.md)**


## get_source

Get Source details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.GetSourceRequest(
    source_id='ab',
)

res = s.sources.get_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**


## initiate_o_auth

Given a source ID, workspace ID, and redirect URL, initiates OAuth for the source.

This returns a fully formed URL for performing user authentication against the relevant source identity provider (IdP). Once authentication has been completed, the IdP will redirect to an Airbyte endpoint which will save the access and refresh tokens off as a secret and return the secret ID to the redirect URL specified in the `secret_id` query string parameter.

That secret ID can be used to create a source with credentials in place of actual tokens.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = shared.InitiateOauthRequest(
    o_auth_input_configuration=shared.OAuthInputConfiguration(),
    redirect_url='soluta',
    source_type=shared.OAuthActorNames.SMARTSHEETS,
    workspace_id='77a89ebf-737a-4e42-83ce-5e6a95d8a0d4',
)

res = s.sources.initiate_o_auth(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InitiateOauthRequest](../../models/shared/initiateoauthrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.InitiateOAuthResponse](../../models/operations/initiateoauthresponse.md)**


## list_sources

List sources

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.ListSourcesRequest(
    include_deleted=False,
    limit=273542,
    offset=425451,
    workspace_ids=[
        'ce2af7a7-3cf3-4be4-93f8-70b326b5a734',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListSourcesRequest](../../models/operations/listsourcesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSourcesResponse](../../models/operations/listsourcesresponse.md)**


## patch_source

Update a Source

### Example Usage

```python
import airbyte
import dateutil.parser
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.PatchSourceRequest(
    source_patch_request=shared.SourcePatchRequest(
        configuration=shared.SourceDockerhub(
            docker_username='airbyte',
            source_type=shared.SourceDockerhubDockerhub.DOCKERHUB,
        ),
        name='My source',
        secret_id='cupiditate',
        workspace_id='cdb1a842-2bb6-479d-a322-715bf0cbb1e3',
    ),
    source_id='veritatis',
)

res = s.sources.patch_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchSourceRequest](../../models/operations/patchsourcerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchSourceResponse](../../models/operations/patchsourceresponse.md)**


## put_source

Update a Source and fully overwrite it

### Example Usage

```python
import airbyte
import dateutil.parser
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = operations.PutSourceRequest(
    source_put_request=shared.SourcePutRequest(
        configuration=shared.SourceSenseforce(
            access_token='quos',
            backend_url='https://galaxyapi.senseforce.io',
            dataset_id='8f418098-ca28-4df5-9498-0df9fe78eda7',
            slice_range=180,
            source_type=shared.SourceSenseforceSenseforce.SENSEFORCE,
            start_date=dateutil.parser.parse('2017-01-25').date(),
        ),
        name='Kevin Willms',
    ),
    source_id='labore',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PutSourceRequest](../../models/operations/putsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PutSourceResponse](../../models/operations/putsourceresponse.md)**

