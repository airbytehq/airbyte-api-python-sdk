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
    configuration=shared.SourceFaker(
        always_updated=False,
        count=730856,
        parallelism=880298,
        records_per_slice=253941,
        seed=313692,
        source_type=shared.SourceFakerFaker.FAKER,
    ),
    name='Jeannie Leannon MD',
    secret_id='neque',
    workspace_id='26b5a734-29cd-4b1a-8422-bb679d232271',
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
    source_id='ullam',
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
    source_id='nam',
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
    redirect_url='hic',
    source_type=shared.OAuthActorNames.AMAZON_ADS,
    workspace_id='cbb1e31b-8b90-4f34-83a1-108e0adcf4b9',
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
    limit=181631,
    offset=63955,
    workspace_ids=[
        '879fce95-3f73-4ef7-bbc7-abd74dd39c0f',
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
        configuration=shared.SourceGridly(
            api_key='nulla',
            grid_id='fugit',
            source_type=shared.SourceGridlyGridly.GRIDLY,
        ),
        name='My source',
        secret_id='porro',
        workspace_id='ff7c70a4-5626-4d43-a813-f16d9f5fce6c',
    ),
    source_id='corporis',
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
        configuration=shared.SourceGoogleWebfonts(
            alt='aliquid',
            api_key='inventore',
            pretty_print='magnam',
            sort='ea',
            source_type=shared.SourceGoogleWebfontsGoogleWebfonts.GOOGLE_WEBFONTS,
        ),
        name='Glenn Walter',
    ),
    source_id='eaque',
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

