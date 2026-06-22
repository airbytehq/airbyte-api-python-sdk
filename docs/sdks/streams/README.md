# Streams

## Overview

### Available Operations

* [get_stream_properties](#get_stream_properties) - Get stream properties

## get_stream_properties

Get stream properties

### Example Usage

<!-- UsageSnippet language="python" operationID="getStreamProperties" method="get" path="/streams" -->
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

    res = aa_client.streams.get_stream_properties(request={
        "source_id": "<value>",
    })

    assert res.stream_properties_response is not None

    # Handle response
    print(res.stream_properties_response)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [api.GetStreamPropertiesRequest](../../api/getstreampropertiesrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[api.GetStreamPropertiesResponse](../../api/getstreampropertiesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |