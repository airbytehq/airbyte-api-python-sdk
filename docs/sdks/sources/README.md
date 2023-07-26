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
    configuration=shared.SourcePosthog(
        api_key='facilis',
        base_url='https://posthog.example.com',
        source_type=shared.SourcePosthogPosthog.POSTHOG,
        start_date=dateutil.parser.isoparse('2021-01-01T00:00:00Z'),
    ),
    name='Allan Greenholt',
    secret_id='sequi',
    workspace_id='9c0f5d2c-ff7c-470a-8562-6d436813f16d',
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
    source_id='excepturi',
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
    source_id='voluptatibus',
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
    name=shared.OAuthActorNames.HUBSPOT,
    o_auth_input_configuration=shared.OAuthInputConfiguration(),
    redirect_url='sapiente',
    workspace_id='ce6c5561-46c3-4e25-8fb0-08c42e141aac',
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
    limit=245367,
    offset=432148,
    workspace_ids=[
        'c8dd6b14-4290-4747-8778-a7bd466d28c1',
        '0ab3cdca-4251-4904-a523-c7e0bc7178e4',
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
        configuration=shared.SourceMicrosoftTeams(
            credentials=shared.SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoft(
                auth_type=shared.SourceMicrosoftTeamsCredentialsAuthenticateViaMicrosoftAuthType.TOKEN,
                client_id='commodi',
                client_secret='sapiente',
                tenant_id='dolores',
            ),
            period='D7',
            source_type=shared.SourceMicrosoftTeamsMicrosoftTeams.MICROSOFT_TEAMS,
        ),
        name='My source',
        secret_id='deserunt',
        workspace_id='70c68828-2aa4-4825-a2f2-22e9817ee17c',
    ),
    source_id='nam',
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
        configuration=shared.SourceTvmazeSchedule(
            domestic_schedule_country_code='US',
            end_date='quasi',
            source_type=shared.SourceTvmazeScheduleTvmazeSchedule.TVMAZE_SCHEDULE,
            start_date='saepe',
            web_schedule_country_code='GB',
        ),
        name='Javier Price',
    ),
    source_id='distinctio',
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

