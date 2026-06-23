# Tags

## Overview

### Available Operations

* [create_tag](#create_tag) - Create a tag
* [delete_tag](#delete_tag) - Delete a tag
* [get_tag](#get_tag) - Get a tag
* [list_tags](#list_tags) - List all tags
* [update_tag](#update_tag) - Update a tag

## create_tag

Create a tag

### Example Usage

<!-- UsageSnippet language="python" operationID="createTag" method="post" path="/tags" -->
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

    res = aa_client.tags.create_tag(request={
        "color": "mint green",
        "name": "<value>",
        "workspace_id": "fb9b459f-ba25-4500-ab48-74bb184a25d8",
    })

    assert res.tag_response is not None

    # Handle response
    print(res.tag_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TagCreateRequest](../../models/tagcreaterequest.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.CreateTagResponse](../../api/createtagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_tag

Delete a tag

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTag" method="delete" path="/tags/{tagId}" -->
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

    res = aa_client.tags.delete_tag(request={
        "tag_id": "a7b6d3f2-0b68-410f-9d8b-570413d4925b",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeleteTagRequest](../../api/deletetagrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.DeleteTagResponse](../../api/deletetagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_tag

Get a tag

### Example Usage

<!-- UsageSnippet language="python" operationID="getTag" method="get" path="/tags/{tagId}" -->
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

    res = aa_client.tags.get_tag(request={
        "tag_id": "0e4206b6-0672-45f2-82cb-05850f1907ba",
    })

    assert res.tag_response is not None

    # Handle response
    print(res.tag_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetTagRequest](../../api/gettagrequest.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetTagResponse](../../api/gettagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_tags

Lists all tags

### Example Usage

<!-- UsageSnippet language="python" operationID="listTags" method="get" path="/tags" -->
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

    res = aa_client.tags.list_tags(request={})

    assert res.tags_response is not None

    # Handle response
    print(res.tags_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListTagsRequest](../../api/listtagsrequest.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListTagsResponse](../../api/listtagsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_tag

Update a tag

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTag" method="patch" path="/tags/{tagId}" -->
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

    res = aa_client.tags.update_tag(request={
        "tag_id": "80469d11-8074-4b50-ac85-fa8ba37ca92a",
        "tag_patch_request": {
            "color": "red",
            "name": "<value>",
        },
    })

    assert res.tag_response is not None

    # Handle response
    print(res.tag_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.UpdateTagRequest](../../api/updatetagrequest.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.UpdateTagResponse](../../api/updatetagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |