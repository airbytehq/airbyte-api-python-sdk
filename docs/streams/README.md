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
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = operations.GetStreamPropertiesRequest(
    destination_id='inventore',
    source_id='non',
)

res = s.streams.get_stream_properties(req)

if res.stream_properties is not None:
    # handle response
```
