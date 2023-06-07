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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceSmartengage(
        api_key='doloribus',
        source_type=shared.SourceSmartengageSmartengage.SMARTENGAGE,
    ),
    name='Olivia McGlynn IV',
    secret_id='odio',
    workspace_id='9fce953f-73ef-47fb-87ab-d74dd39c0f5d',
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
    source_id='fugit',
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
    source_id='porro',
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
    name='Domingo Kris',
    o_auth_input_configuration={
        "officia": 'tempora',
    },
    redirect_url='ipsam',
    workspace_id='626d4368-13f1-46d9-b5fc-e6c556146c3e',
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
    limit=132487,
    offset=325310,
    workspace_ids=[
        'fb008c42-e141-4aac-b66c-8dd6b1442907',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.PatchSourceRequest(
    source_patch_request=shared.SourcePatchRequest(
        configuration=shared.SourceGooglePagespeedInsights(
            api_key='odio',
            categories=[
                shared.SourceGooglePagespeedInsightsCategories.PERFORMANCE,
                shared.SourceGooglePagespeedInsightsCategories.PERFORMANCE,
            ],
            source_type=shared.SourceGooglePagespeedInsightsGooglePagespeedInsights.GOOGLE_PAGESPEED_INSIGHTS,
            strategies=[
                shared.SourceGooglePagespeedInsightsStrategies.MOBILE,
                shared.SourceGooglePagespeedInsightsStrategies.DESKTOP,
                shared.SourceGooglePagespeedInsightsStrategies.MOBILE,
            ],
            urls=[
                'ut',
                'eum',
                'suscipit',
                'assumenda',
            ],
        ),
        name='My source',
        secret_id='eos',
        workspace_id='8c10ab3c-dca4-4251-904e-523c7e0bc717',
    ),
    source_id='totam',
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
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.PutSourceRequest(
    source_put_request=shared.SourcePutRequest(
        configuration=shared.SourceTwilioTaskrouter(
            account_sid='aliquam',
            auth_token='odio',
            source_type=shared.SourceTwilioTaskrouterTwilioTaskrouter.TWILIO_TASKROUTER,
        ),
        name='Leslie Williamson',
    ),
    source_id='molestiae',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
```
