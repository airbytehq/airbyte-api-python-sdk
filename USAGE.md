<!-- Start SDK Example Usage -->
```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.ConnectionCreateRequest(
    configurations=shared.StreamConfigurations(
        streams=[
            shared.StreamConfiguration(
                cursor_field=[
                    "distinctio",
                    "quibusdam",
                    "unde",
                ],
                name="Johnnie Stamm",
                primary_key=[
                    [
                        "iure",
                        "magnam",
                    ],
                    [
                        "ipsa",
                        "delectus",
                        "tempora",
                        "suscipit",
                    ],
                    [
                        "minus",
                        "placeat",
                    ],
                ],
                sync_mode="incremental_append",
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    "excepturi",
                    "nisi",
                ],
                name="Jake Bernier MD",
                primary_key=[
                    [
                        "repellendus",
                        "sapiente",
                    ],
                ],
                sync_mode="incremental_deduped_history",
            ),
            shared.StreamConfiguration(
                cursor_field=[
                    "at",
                ],
                name="Emilio Krajcik",
                primary_key=[
                    [
                        "porro",
                        "dolorum",
                        "dicta",
                    ],
                    [
                        "officia",
                        "occaecati",
                        "fugit",
                    ],
                ],
                sync_mode="incremental_append",
            ),
        ],
    ),
    data_residency="eu",
    destination_id="c816742c-b739-4205-9293-96fea7596eb1",
    name="Lela Orn",
    namespace_definition="source",
    namespace_format="${SOURCE_NAMESPACE}",
    prefix="dolorem",
    schedule=shared.ConnectionScheduleCreate(
        cron_expression="corporis",
        schedule_type="manual",
    ),
    source_id="c5955907-aff1-4a3a-afa9-467739251aa5",
)

res = s.connections.create_connection(req)

if res.connection_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->