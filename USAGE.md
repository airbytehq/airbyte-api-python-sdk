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
                name='at BMW',
                primary_key=[
                    [
                        'pfft',
                    ],
                ],
            ),
        ],
    ),
    destination_id='62083eaf-c855-4914-a0a5-70f6dd427d83',
    namespace_format='${SOURCE_NAMESPACE}',
    schedule=shared.ConnectionSchedule(
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='55584783-5842-4325-b6c7-b3fd2fd307d6',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->