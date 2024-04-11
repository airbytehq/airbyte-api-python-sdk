# Streams
(*streams*)

### Available Operations

* [get_stream_properties](#get_stream_properties) - Get stream properties

## get_stream_properties

Get stream properties

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI(
    security=airbyte_api.Security(
        basic_auth=airbyte_api.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = airbyte_api.GetStreamPropertiesRequest(
    destination_id='<value>',
    source_id='<value>',
)

res = s.streams.get_stream_properties(req)

if res.stream_properties_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.GetStreamPropertiesRequest](../../models/getstreampropertiesrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |


### Response

**[models.GetStreamPropertiesResponse](../../models/getstreampropertiesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
