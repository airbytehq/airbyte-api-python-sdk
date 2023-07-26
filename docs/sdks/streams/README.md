# streams

### Available Operations

* [get_stream_properties](#get_stream_properties) - Get stream properties

## get_stream_properties

Get stream properties

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetStreamPropertiesRequest(
    destination_id='eligendi',
    ignore_cache=False,
    source_id='sit',
)

res = s.streams.get_stream_properties(req)

if res.stream_properties_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetStreamPropertiesRequest](../../models/operations/getstreampropertiesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetStreamPropertiesResponse](../../models/operations/getstreampropertiesresponse.md)**

