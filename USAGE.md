<!-- Start SDK Example Usage [usage] -->
```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = models.ConnectionCreateRequest(
    destination_id='c669dd1e-3620-483e-afc8-55914e0a570f',
    source_id='6dd427d8-3a55-4584-b835-842325b6c7b3',
    namespace_format='${SOURCE_NAMESPACE}',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->