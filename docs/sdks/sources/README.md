# sources

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
        bearer_auth="",
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourcePipedrive(
        authorization=shared.SourcePipedriveAPIKeyAuthentication(
            api_token='dolorum',
            auth_type=shared.SourcePipedriveAPIKeyAuthenticationAuthType.TOKEN,
        ),
        replication_start_date=dateutil.parser.isoparse('2017-01-25T00:00:00Z'),
        source_type=shared.SourcePipedrivePipedrive.PIPEDRIVE,
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
        bearer_auth="",
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
        bearer_auth="",
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
        bearer_auth="",
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
        bearer_auth="",
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
        bearer_auth="",
    ),
)

req = operations.PatchSourceRequest(
    source_patch_request=shared.SourcePatchRequest(
        configuration=shared.SourceDixa(
            api_token='cupiditate',
            batch_size=31,
            source_type=shared.SourceDixaDixa.DIXA,
            start_date='YYYY-MM-DD',
        ),
        name='My source',
        secret_id='pariatur',
        workspace_id='b1a8422b-b679-4d23-a271-5bf0cbb1e31b',
    ),
    source_id='quos',
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
        bearer_auth="",
    ),
)

req = operations.PutSourceRequest(
    source_put_request=shared.SourcePutRequest(
        configuration=shared.SourceSalesloft(
            credentials=shared.SourceSalesloftCredentialsAuthenticateViaAPIKey(
                api_key='aperiam',
                auth_type=shared.SourceSalesloftCredentialsAuthenticateViaAPIKeyAuthType.API_KEY,
            ),
            source_type=shared.SourceSalesloftSalesloft.SALESLOFT,
            start_date=dateutil.parser.isoparse('2020-11-16T00:00:00Z'),
        ),
        name='Mike Greenholt',
    ),
    source_id='dolorum',
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

