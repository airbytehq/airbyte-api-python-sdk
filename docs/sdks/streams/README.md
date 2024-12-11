# Streams
(*streams*)

## Overview

### Available Operations

* [get_stream_properties](#get_stream_properties) - Get stream properties

## get_stream_properties

Get stream properties

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


res = s.streams.get_stream_properties(request=api.GetStreamPropertiesRequest(
    source_id='<value>',
))

if res.stream_properties_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [api.GetStreamPropertiesRequest](../../api/getstreampropertiesrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |

### Response

**[api.GetStreamPropertiesResponse](../../api/getstreampropertiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |