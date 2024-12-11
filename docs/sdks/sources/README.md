# Sources
(*sources*)

## Overview

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
import dateutil.parser
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.sources.create_source(request=models.SourceCreateRequest(
    configuration=models.SourcePosthog(
        api_key='<value>',
        start_date=dateutil.parser.isoparse('2021-01-01T00:00:00Z'),
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_source

Delete a Source

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_source

Get Source details

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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
            password='',
            username='',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_sources

List sources

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.sources.list_sources(request=api.ListSourcesRequest(
    workspace_ids=[
        'df08f6b0-b364-4cc1-9b3f-96f5d2fccfb2,b0796797-de23-4fc7-a5e2-7e131314718c',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_source

Update a Source

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.sources.patch_source(request=api.PatchSourceRequest(
    source_id='<value>',
    source_patch_request=models.SourcePatchRequest(
        configuration=models.SourceEventzilla(
            x_api_key='<value>',
        ),
        name='My Source',
        workspace_id='744cc0ed-7f05-4949-9e60-2a814f90c035',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## put_source

Update a Source and fully overwrite it

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.sources.put_source(request=api.PutSourceRequest(
    source_id='<value>',
    source_put_request=models.SourcePutRequest(
        configuration=models.SourceGridly(
            api_key='<value>',
            grid_id='<id>',
        ),
        name='My Source',
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |