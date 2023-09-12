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
                    'corrupti',
                ],
                name='Kelvin Sporer',
                primary_key=[
                    [
                        'corrupti',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.US,
    destination_id='9a674e0f-467c-4c87-96ed-151a05dfc2dd',
    name='Javier Schmidt',
    namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.PROPAGATE_FULLY,
    prefix='dolorum',
    schedule=shared.ConnectionSchedule(
        cron_expression='dicta',
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='a928fc81-6742-4cb7-b920-5929396fea75',
    status=shared.ConnectionStatusEnum.INACTIVE,
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->