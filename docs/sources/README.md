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
    configuration=shared.SourceRecruitee(
        api_key='repellendus',
        company_id=785153,
        source_type=shared.SourceRecruiteeRecruitee.RECRUITEE,
    ),
    name='Alexander Prosacco',
    secret_id='quae',
    workspace_id='879fce95-3f73-4ef7-bbc7-abd74dd39c0f',
)

res = s.sources.create_source(req)

if res.source_response is not None:
    # handle response
```

## delete_source

Delete a Source

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteSourceRequest(
    source_id='exercitationem',
)

res = s.sources.delete_source(req)

if res.status_code == 200:
    # handle response
```

## get_source

Get Source details

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSourceRequest(
    source_id='nulla',
)

res = s.sources.get_source(req)

if res.source_response is not None:
    # handle response
```

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
    name='Johnnie Wunsch',
    o_auth_input_configuration={
        "ducimus": 'alias',
        "officia": 'tempora',
        "ipsam": 'ea',
        "aspernatur": 'vel',
    },
    redirect_url='possimus',
    workspace_id='436813f1-6d9f-45fc-a6c5-56146c3e250f',
)

res = s.sources.initiate_o_auth(req)

if res.status_code == 200:
    # handle response
```

## list_sources

List sources

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListSourcesRequest(
    include_deleted=False,
    limit=725595,
    offset=13948,
    workspace_ids=[
        '8c42e141-aac3-466c-8dd6-b14429074747',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
```

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
        configuration=shared.SourceMarketo(
            client_id='rem',
            client_secret='fuga',
            domain_url='https://000-AAA-000.mktorest.com',
            source_type=shared.SourceMarketoMarketo.MARKETO,
            start_date=dateutil.parser.isoparse('2020-09-25T00:00:00Z'),
        ),
        name='My source',
        secret_id='reprehenderit',
        workspace_id='bd466d28-c10a-4b3c-9ca4-251904e523c7',
    ),
    source_id='recusandae',
)

res = s.sources.patch_source(req)

if res.source_response is not None:
    # handle response
```

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
        configuration=shared.SourceAsana(
            credentials=shared.SourceAsanaCredentialsAuthenticateWithPersonalAccessToken(
                option_title=shared.SourceAsanaCredentialsAuthenticateWithPersonalAccessTokenCredentialsTitle.PAT_CREDENTIALS,
                personal_access_token='quod',
            ),
            source_type=shared.SourceAsanaAsana.ASANA,
        ),
        name='Debra Kovacek',
    ),
    source_id='aliquam',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
```
