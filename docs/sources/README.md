# sources

### Available Operations

* [create_source](#create_source) - Create a source
* [delete_source](#delete_source) - Delete a Source
* [get_source](#get_source) - Get Source details
* [initiate_o_auth](#initiate_o_auth) - Initiate OAuth for a source
* [list_sources](#list_sources) - List sources

## create_source

Creates a source given a name, workspace id, and a json blob containing the configuration for the source.

### Example Usage

```python
import airbyte
import dateutil.parser
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceInstagram(
        access_token='nam',
        source_type=shared.SourceInstagramInstagramEnum.INSTAGRAM,
        start_date=dateutil.parser.isoparse('2022-11-28T15:41:44.846Z'),
    ),
    name='Dr. Dominic Rohan',
    secret_id='veritatis',
    workspace_id='b8b90f34-43a1-4108-a0ad-cf4b921879fc',
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteSourceRequest(
    source_id='vero',
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetSourceRequest(
    source_id='omnis',
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.InitiateOauthRequest(
    name='Tiffany Willms',
    o_auth_input_configuration={
        "tenetur": 'dignissimos',
        "hic": 'distinctio',
        "quod": 'odio',
        "similique": 'facilis',
    },
    redirect_url='vero',
    workspace_id='74dd39c0-f5d2-4cff-bc70-a45626d43681',
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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListSourcesRequest(
    include_deleted=False,
    limit=224317,
    offset=980700,
    workspace_ids=[
        '6d9f5fce-6c55-4614-ac3e-250fb008c42e',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
```
