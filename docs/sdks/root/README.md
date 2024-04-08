# Root
(*root*)

### Available Operations

* [get_documentation](#get_documentation) - Root path, currently returns a redirect to the documentation

## get_documentation

Root path, currently returns a redirect to the documentation

### Example Usage

```python
import airbyte_api

s = airbyte_api.AirbyteAPI()


res = s.root.get_documentation()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                      | Type                           | Required                       | Description                    |
| ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| `server_url`                   | *Optional[str]*                | :heavy_minus_sign:             | An optional server URL to use. |


### Response

**[models.GetDocumentationResponse](../../models/getdocumentationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
