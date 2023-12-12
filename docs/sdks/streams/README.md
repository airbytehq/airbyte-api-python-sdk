# Streams
(*streams*)

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
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = operations.GetStreamPropertiesRequest(
    destination_id='string',
    source_id='string',
)

res = s.streams.get_stream_properties(req)

if res.stream_properties_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetStreamPropertiesRequest](../../models/operations/getstreampropertiesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetStreamPropertiesResponse](../../models/operations/getstreampropertiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 400-600         | */*             |
