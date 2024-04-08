# Health
(*health*)

### Available Operations

* [get_health_check](#get_health_check) - Health Check

## get_health_check

Health Check

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()


res = s.health.get_health_check()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `server_url`                   | *Optional[str]*                | :heavy_minus_sign:             | An optional server URL to use. |


### Response

**[models.GetHealthCheckResponse](../../models/gethealthcheckresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
