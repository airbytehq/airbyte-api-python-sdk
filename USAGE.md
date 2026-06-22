<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.connections.create_connection(request={
        "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
        "name": "Postgres-to-Bigquery",
        "namespace_format": "${SOURCE_NAMESPACE}",
        "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
    })

    assert res.connection_response is not None

    # Handle response
    print(res.connection_response)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from airbyte_api import AirbyteAPI, models
import asyncio

async def main():

    async with AirbyteAPI(
        security=models.Security(
            basic_auth=models.SchemeBasicAuth(
                password="",
                username="",
            ),
        ),
    ) as aa_client:

        res = await aa_client.connections.create_connection_async(request={
            "destination_id": "e478de0d-a3a0-475c-b019-25f7dd29e281",
            "name": "Postgres-to-Bigquery",
            "namespace_format": "${SOURCE_NAMESPACE}",
            "source_id": "95e66a59-8045-4307-9678-63bc3c9b8c93",
        })

        assert res.connection_response is not None

        # Handle response
        print(res.connection_response)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->