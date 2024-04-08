# OAuth
(*o_auth*)

### Available Operations

* [oauth_callback](#oauth_callback) - Receive OAuth callbacks

## oauth_callback

Redirected to by identity providers after authentication.

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()

req = airbyte_api.OauthCallbackRequest()

res = s.o_auth.oauth_callback(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.OauthCallbackRequest](../../models/oauthcallbackrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |


### Response

**[models.OauthCallbackResponse](../../models/oauthcallbackresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
