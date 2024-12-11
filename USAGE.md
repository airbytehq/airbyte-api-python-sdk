<!-- Start SDK Example Usage [usage] -->
```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.connections.create_connection(request=models.ConnectionCreateRequest(
    destination_id='e478de0d-a3a0-475c-b019-25f7dd29e281',
    source_id='95e66a59-8045-4307-9678-63bc3c9b8c93',
    name='Postgres-to-Bigquery',
    namespace_format='${SOURCE_NAMESPACE}',
))

if res.connection_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->