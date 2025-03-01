# Tags
(*tags*)

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


res = s.tags.create_tag(request=models.TagCreateRequest(
    color='blue',
    name='<value>',
    workspace_id='5f85d5ab-c889-4273-91d7-c22bac981db2',
))

if res.tag_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                   | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `request`                                                   | [models.TagCreateRequest](../../models/tagcreaterequest.md) | :heavy_check_mark:                                          | The request object to use for the request.                  |

### Response

**[api.CreateTagResponse](../../api/createtagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_tag

Delete a tag

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


res = s.tags.delete_tag(request=api.DeleteTagRequest(
    tag_id='da1c4fd4-2786-4b27-8b72-2335c85a5af8',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.DeleteTagRequest](../../api/deletetagrequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |

### Response

**[api.DeleteTagResponse](../../api/deletetagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_tag

Get a tag

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


res = s.tags.get_tag(request=api.GetTagRequest(
    tag_id='808ab48f-5790-47fe-aa1e-3073281a0300',
))

if res.tag_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                       | Type                                            | Required                                        | Description                                     |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `request`                                       | [api.GetTagRequest](../../api/gettagrequest.md) | :heavy_check_mark:                              | The request object to use for the request.      |

### Response

**[api.GetTagResponse](../../api/gettagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_tags

Lists all tags

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


res = s.tags.list_tags(request=api.ListTagsRequest())

if res.tags_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                           | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `request`                                           | [api.ListTagsRequest](../../api/listtagsrequest.md) | :heavy_check_mark:                                  | The request object to use for the request.          |

### Response

**[api.ListTagsResponse](../../api/listtagsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_tag

Update a tag

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


res = s.tags.update_tag(request=api.UpdateTagRequest(
    tag_patch_request=models.TagPatchRequest(
        color='turquoise',
        name='<value>',
    ),
    tag_id='3043493e-7596-4d2b-8ee9-859838c615f6',
))

if res.tag_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.UpdateTagRequest](../../api/updatetagrequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |

### Response

**[api.UpdateTagResponse](../../api/updatetagresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |