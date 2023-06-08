# streams

### Available Operations

* [get_stream_properties](#get_stream_properties) - Get stream properties

## get_stream_properties

Get stream properties

### Example Usage

```python
import airbyte
from airbyte.models import operations

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetStreamPropertiesRequest(
    destination_id='odio',
    ignore_cache=False,
    source_id='occaecati',
)

res = s.streams.get_stream_properties(req)

if res.stream_properties_response is not None:
    # handle response
```
