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


res = s.sources.create_source(request=models.SourceCreateRequest(
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


res = s.sources.delete_source(request=api.DeleteSourceRequest(
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


res = s.sources.get_source(request=api.GetSourceRequest(
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


res = s.sources.initiate_o_auth(request=models.InitiateOauthRequest(
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


res = s.sources.list_sources(request=api.ListSourcesRequest(
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


res = s.sources.patch_source(request=api.PatchSourceRequest(
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


res = s.sources.put_source(request=api.PutSourceRequest(
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
