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
                sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.AUTO,
    destination_id='083eafc8-5591-44e0-a570-f6dd427d83a5',
    name='mesh interactive',
    namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.IGNORE,
    prefix='port Idaho',
    schedule=shared.ConnectionSchedule(
        cron_expression='productivity',
        schedule_type=shared.ScheduleTypeEnum.MANUAL,
    ),
    source_id='b3fd2fd3-07d6-40cb-97ea-6dfc635b80f2',
    status=shared.ConnectionStatusEnum.INACTIVE,
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->