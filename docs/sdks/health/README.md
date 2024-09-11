# Health
(*health*)

## Overview

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

### Response

**[api.GetHealthCheckResponse](../../api/gethealthcheckresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
