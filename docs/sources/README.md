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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceFaker(
        count=961571,
        parallelism=455169,
        records_per_slice=231701,
        records_per_sync=878870,
        seed=949319,
        source_type=shared.SourceFakerFakerEnum.FAKER,
    ),
    name='Darla Rau',
    secret_id='similique',
    workspace_id='bd74dd39-c0f5-4d2c-bf7c-70a45626d436',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteSourceRequest(
    source_id='laudantium',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetSourceRequest(
    source_id='dicta',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.InitiateOauthRequest(
    name='Elisa Boyle',
    o_auth_input_configuration={
        "voluptatibus": 'nostrum',
        "sapiente": 'quisquam',
        "saepe": 'ea',
    },
    redirect_url='impedit',
    workspace_id='556146c3-e250-4fb0-88c4-2e141aac366c',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListSourcesRequest(
    include_deleted=False,
    limit=557369,
    offset=829603,
    workspace_ids=[
        '6b144290-7474-4778-a7bd-466d28c10ab3',
        'cdca4251-904e-4523-87e0-bc7178e4796f',
        '2a70c688-282a-4a48-a562-f222e9817ee1',
        '7cbe61e6-b7b9-45bc-8ab3-c20c4f3789fd',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
```
