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
    name="perferendis",
    schedule=shared.ConnectionScheduleCreate(
        cron_expression="ipsam",
        schedule_type="cron",
    ),
    source_id="fc2ddf7c-c78c-4a1b-a928-fc816742cb73",
)
    
res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->