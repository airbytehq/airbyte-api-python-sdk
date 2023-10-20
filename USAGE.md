<!-- Start SDK Example Usage -->


```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'violet',
                ],
                name='Account',
                primary_key=[
                    [
                        'BMW',
                    ],
                ],
            ),
        ],
    ),
    destination_id='e362083e-afc8-4559-94e0-a570f6dd427d',
    namespace_format='${SOURCE_NAMESPACE}',
    schedule=shared.ConnectionSchedule(
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='3a555847-8358-4423-a5b6-c7b3fd2fd307',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->