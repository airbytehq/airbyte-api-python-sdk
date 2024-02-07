<!-- Start SDK Example Usage [usage] -->
```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        basic_auth=shared.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

req = shared.ConnectionCreateRequest(
    destination_id='c669dd1e-3620-483e-afc8-55914e0a570f',
    source_id='6dd427d8-3a55-4584-b835-842325b6c7b3',
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                name='string',
                cursor_field=[
                    'string',
                ],
                primary_key=[
                    [
                        'string',
                    ],
                ],
            ),
        ],
    ),
    namespace_format='${SOURCE_NAMESPACE}',
    schedule=shared.ConnectionSchedule(
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->