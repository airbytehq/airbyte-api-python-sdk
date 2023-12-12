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
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'string',
                ],
                name='string',
                primary_key=[
                    [
                        'string',
                    ],
                ],
            ),
        ],
    ),
    destination_id='c669dd1e-3620-483e-afc8-55914e0a570f',
    namespace_format='${SOURCE_NAMESPACE}',
    schedule=shared.ConnectionSchedule(
        schedule_type=shared.ScheduleTypeEnum.MANUAL,
    ),
    source_id='dd427d83-a555-4847-8358-42325b6c7b3f',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->