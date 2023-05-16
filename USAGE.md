<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
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
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_APPEND,
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
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_DEDUPED_HISTORY,
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
                sync_mode=shared.ConnectionSyncModeEnumEnum.INCREMENTAL_APPEND,
            ),
        ],
    ),
    data_residency=shared.GeographyEnumEnum.EU,
    destination_id='c816742c-b739-4205-9293-96fea7596eb1',
    name='Lela Orn',
    namespace_definition=shared.NamespaceDefinitionEnumEnum.SOURCE,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_schema_updates_behavior=shared.NonBreakingSchemaUpdatesBehaviorEnumEnum.IGNORE,
    prefix='corporis',
    schedule=shared.ConnectionScheduleCreate(
        cron_expression='explicabo',
        schedule_type=shared.ScheduleTypeEnumEnum.CRON,
    ),
    source_id='5955907a-ff1a-43a2-ba94-67739251aa52',
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->