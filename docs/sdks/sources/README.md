# Sources

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

### Example Usage: Source Creation Request Example

<!-- UsageSnippet language="python" operationID="createSource" method="post" path="/sources" example="Source Creation Request Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.create_source(request=models.SourceCreateRequest(
        configuration=models.SourceConfiguration(
            source_type="onepagecrm",
            **{
                "airbyte_source_name": "google-ads",
                "conversion_window_days": 14,
                "customer_id": "1234567890",
                "start_date": 1672531200000,
                "end_date": 1704067200000,
            },
        ),
        name="My Source",
        workspace_id="744cc0ed-7f05-4949-9e60-2a814f90c035",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```
### Example Usage: Source Creation Response Example

<!-- UsageSnippet language="python" operationID="createSource" method="post" path="/sources" example="Source Creation Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.create_source(request=models.SourceCreateRequest(
        configuration=models.SourceConfiguration(
            source_type="postgres",
            **{
                "user": "charles",
                "host": "localhost",
                "port": 5432,
            },
        ),
        name="<value>",
        workspace_id="5923d04d-a31f-43ea-8396-170b96449103",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SourceCreateRequest](../../models/sourcecreaterequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.CreateSourceResponse](../../api/createsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_source

Delete a Source

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSource" method="delete" path="/sources/{sourceId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.delete_source(request={
        "source_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteSourceRequest](../../api/deletesourcerequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.DeleteSourceResponse](../../api/deletesourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_source

Get Source details

### Example Usage

<!-- UsageSnippet language="python" operationID="getSource" method="get" path="/sources/{sourceId}" example="Source Get Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.get_source(request={
        "source_id": "<value>",
    })

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetSourceRequest](../../api/getsourcerequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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

<!-- UsageSnippet language="python" operationID="initiateOAuth" method="post" path="/sources/initiateOAuth" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.initiate_o_auth(request={
        "redirect_url": "https://cloud.airbyte.io/v1/api/oauth/callback",
        "source_type": "intercom",
        "workspace_id": "871d9b60-11d1-44cb-8c92-c246d53bf87e",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.InitiateOauthRequest](../../models/initiateoauthrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.InitiateOAuthResponse](../../api/initiateoauthresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_sources

List sources

### Example Usage

<!-- UsageSnippet language="python" operationID="listSources" method="get" path="/sources" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.list_sources(request={
        "workspace_ids": [
            "d",
            "f",
            "0",
            "8",
            "f",
            "6",
            "b",
            "0",
            "-",
            "b",
            "3",
            "6",
            "4",
            "-",
            "4",
            "c",
            "c",
            "1",
            "-",
            "9",
            "b",
            "3",
            "f",
            "-",
            "9",
            "6",
            "f",
            "5",
            "d",
            "2",
            "f",
            "c",
            "c",
            "f",
            "b",
            "2",
            ",",
            "b",
            "0",
            "7",
            "9",
            "6",
            "7",
            "9",
            "7",
            "-",
            "d",
            "e",
            "2",
            "3",
            "-",
            "4",
            "f",
            "c",
            "7",
            "-",
            "a",
            "5",
            "e",
            "2",
            "-",
            "7",
            "e",
            "1",
            "3",
            "1",
            "3",
            "1",
            "4",
            "7",
            "1",
            "8",
            "c",
        ],
    })

    assert res.sources_response is not None

    # Handle response
    print(res.sources_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListSourcesRequest](../../api/listsourcesrequest.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListSourcesResponse](../../api/listsourcesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## patch_source

Update a Source

### Example Usage: Source Update Request Example

<!-- UsageSnippet language="python" operationID="patchSource" method="patch" path="/sources/{sourceId}" example="Source Update Request Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.patch_source(request=api.PatchSourceRequest(
        source_patch_request=models.SourcePatchRequest(
            configuration=models.SourceConfiguration(
                source_type="nutshell",
                **{
                    "airbyte_source_name": "google-ads",
                    "conversion_window_days": 14,
                    "customer_id": "1234567890",
                    "start_date": 1672531200000,
                    "end_date": 1704067200000,
                },
            ),
            name="My Source",
            workspace_id="744cc0ed-7f05-4949-9e60-2a814f90c035",
        ),
        source_id="<value>",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```
### Example Usage: Source Update Response Example

<!-- UsageSnippet language="python" operationID="patchSource" method="patch" path="/sources/{sourceId}" example="Source Update Response Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.patch_source(request=api.PatchSourceRequest(
        source_patch_request=models.SourcePatchRequest(
            configuration=models.SourceConfiguration(
                source_type="postgres",
                **{
                    "user": "charles",
                    "host": "localhost",
                    "port": 5432,
                },
            ),
            name="My source",
        ),
        source_id="<value>",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PatchSourceRequest](../../api/patchsourcerequest.md)           | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.PatchSourceResponse](../../api/patchsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## put_source

Update a Source and fully overwrite it

### Example Usage: Source Update Request Example

<!-- UsageSnippet language="python" operationID="putSource" method="put" path="/sources/{sourceId}" example="Source Update Request Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.put_source(request=api.PutSourceRequest(
        source_put_request=models.SourcePutRequest(
            configuration=models.SourceConfiguration(
                source_type="railz",
                **{
                    "airbyte_source_name": "google-ads",
                    "conversion_window_days": 14,
                    "customer_id": "1234567890",
                    "start_date": 1672531200000,
                    "end_date": 1704067200000,
                },
            ),
            name="My Source",
        ),
        source_id="<value>",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```
### Example Usage: Source Update Response Example

<!-- UsageSnippet language="python" operationID="putSource" method="put" path="/sources/{sourceId}" example="Source Update Response Example" -->
```python
from airbyte_api import AirbyteAPI, api, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.sources.put_source(request=api.PutSourceRequest(
        source_put_request=models.SourcePutRequest(
            configuration=models.SourceConfiguration(
                source_type="postgres",
                **{
                    "user": "charles",
                    "host": "localhost",
                    "port": 5432,
                },
            ),
            name="<value>",
        ),
        source_id="<value>",
    ))

    assert res.source_response is not None

    # Handle response
    print(res.source_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.PutSourceRequest](../../api/putsourcerequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.PutSourceResponse](../../api/putsourceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |