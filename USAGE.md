<!-- Start SDK Example Usage -->


```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    'distinctio',
                    'quibusdam',
                    'unde',
                ],
                name='Johnnie Stamm',
                primary_key=[
                    [
                        'iure',
                        'magnam',
                    ],
                    [
                        'ipsa',
                        'delectus',
                        'tempora',
                        'suscipit',
                    ],
                    [
                        'minus',
                        'placeat',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'excepturi',
                    'nisi',
                ],
                name='Jake Bernier MD',
                primary_key=[
                    [
                        'repellendus',
                        'sapiente',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_DEDUPED_HISTORY,
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    'at',
                ],
                name='Emilio Krajcik',
                primary_key=[
                    [
                        'porro',
                        'dolorum',
                        'dicta',
                    ],
                    [
                        'officia',
                        'occaecati',
                        'fugit',
                    ],
                ],
                sync_mode=shared.ConnectionSyncModeEnum.INCREMENTAL_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnum.EU,
    destination_id='c816742c-b739-4205-9293-96fea7596eb1',
    name='Lela Orn',
    namespace_definition=shared.NamespaceDefinitionEnum.SOURCE,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnum.IGNORE,
    prefix='corporis',
    schedule=shared.ConnectionSchedule(
        cron_expression='explicabo',
        schedule_type=shared.ScheduleTypeEnum.CRON,
    ),
    source_id='5955907a-ff1a-43a2-ba94-67739251aa52',
    status=shared.ConnectionStatusEnum.DEPRECATED,
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->