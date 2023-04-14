<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.ConnectionCreateRequest(
    destination_id="89bd9d8d-69a6-474e-8f46-7cc8796ed151",
    geography="us",
    name="Roberta Sipes",
    schedule=shared.ConnectionScheduleCreate(
        cron_expression="odit",
        schedule_type="cron",
    ),
    source_id="df7cc78c-a1ba-4928-bc81-6742cb739205",
)
    
res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->