# Sources
(*sources*)

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
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = shared.SourceCreateRequest(
    configuration=shared.SourceAha(
    api_key='string',
    url='https://complicated-seat.org',
),
    name='string',
    workspace_id='0f31f3dd-c984-48c3-8bdf-b109056aa6d6',
)

res = s.sources.create_source(req)

if res.source_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceCreateRequest](../../models/shared/sourcecreaterequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## delete_source

Delete a Source

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.DeleteSourceRequest(
    source_id='string',
)

res = s.sources.delete_source(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSourceRequest](../../models/operations/deletesourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSourceResponse](../../models/operations/deletesourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## get_source

Get Source details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.GetSourceRequest(
    source_id='string',
)

res = s.sources.get_source(req)

if res.source_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = shared.InitiateOauthRequest(
    o_auth_input_configuration=shared.OAuthInputConfiguration(),
    redirect_url='string',
    source_type=shared.OAuthActorNames.GITLAB,
    workspace_id='fd28130d-9919-4ffa-a67d-4e12eb099447',
)

res = s.sources.initiate_o_auth(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.InitiateOauthRequest](../../models/shared/initiateoauthrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.InitiateOAuthResponse](../../models/operations/initiateoauthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

## list_sources

List sources

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.ListSourcesRequest(
    workspace_ids=[
        '74dbbb77-f80b-457c-8540-0c5d47a64428',
    ],
)

res = s.sources.list_sources(req)

if res.sources_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListSourcesRequest](../../models/operations/listsourcesrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSourcesResponse](../../models/operations/listsourcesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.PatchSourceRequest(
    source_patch_request=shared.SourcePatchRequest(
        configuration=shared.SourceAha(
        api_key='string',
        url='http://apprehensive-visa.net',
    ),
        name='My source',
    ),
    source_id='string',
)

res = s.sources.patch_source(req)

if res.source_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.PatchSourceRequest](../../models/operations/patchsourcerequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.PatchSourceResponse](../../models/operations/patchsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |

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
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.PutSourceRequest(
    source_put_request=shared.SourcePutRequest(
        configuration=shared.SourceAha(
        api_key='string',
        url='http://alienated-traveler.name',
    ),
        name='string',
    ),
    source_id='string',
)

res = s.sources.put_source(req)

if res.source_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.PutSourceRequest](../../models/operations/putsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.PutSourceResponse](../../models/operations/putsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
