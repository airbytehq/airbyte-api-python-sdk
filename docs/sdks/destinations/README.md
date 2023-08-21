# destinations

### Available Operations

* [create_destination](#create_destination) - Create a destination
* [delete_destination](#delete_destination) - Delete a Destination
* [get_destination](#get_destination) - Get Destination details
* [list_destinations](#list_destinations) - List destinations
* [patch_destination](#patch_destination) - Update a Destination
* [put_destination](#put_destination) - Update a Destination and fully overwrite it

## create_destination

Creates a destination given a name, workspace id, and a json blob containing the configuration for the source.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DestinationCreateRequest(
    configuration=shared.DestinationPostgres(
        database='deleniti',
        destination_type=shared.DestinationPostgresPostgres.POSTGRES,
        host='omnis',
        jdbc_url_params='necessitatibus',
        password='distinctio',
        port=5432,
        schema='public',
        ssl_mode=shared.DestinationPostgresSslModeVerifyFull(
            ca_certificate='nihil',
            client_certificate='ipsum',
            client_key='voluptate',
            client_key_password='id',
            mode=shared.DestinationPostgresSslModeVerifyFullMode.VERIFY_FULL,
        ),
        tunnel_method=shared.DestinationPostgresTunnelMethodPasswordAuthentication(
            tunnel_host='eius',
            tunnel_method=shared.DestinationPostgresTunnelMethodPasswordAuthenticationTunnelMethod.SSH_PASSWORD_AUTH,
            tunnel_port=22,
            tunnel_user='aspernatur',
            tunnel_user_password='perferendis',
        ),
        username='Daphne.Rosenbaum90',
    ),
    name='Rosie McKenzie',
    workspace_id='8a0d446c-e2af-47a7-bcf3-be453f870b32',
)

res = s.destinations.create_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationCreateRequest](../../models/shared/destinationcreaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**


## delete_destination

Delete a Destination

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteDestinationRequest(
    destination_id='vel',
)

res = s.destinations.delete_destination(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteDestinationRequest](../../models/operations/deletedestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteDestinationResponse](../../models/operations/deletedestinationresponse.md)**


## get_destination

Get Destination details

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDestinationRequest(
    destination_id='libero',
)

res = s.destinations.get_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**


## list_destinations

List destinations

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListDestinationsRequest(
    include_deleted=False,
    limit=374170,
    offset=646265,
    workspace_ids=[
        '3429cdb1-a842-42bb-a79d-2322715bf0cb',
        'b1e31b8b-90f3-4443-a110-8e0adcf4b921',
    ],
)

res = s.destinations.list_destinations(req)

if res.destinations_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDestinationsRequest](../../models/operations/listdestinationsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListDestinationsResponse](../../models/operations/listdestinationsresponse.md)**


## patch_destination

Update a Destination

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PatchDestinationRequest(
    destination_patch_request=shared.DestinationPatchRequest(
        configuration=shared.DestinationKinesis(
            access_key='odio',
            buffer_size=580447,
            destination_type=shared.DestinationKinesisKinesis.KINESIS,
            endpoint='kinesis.us‑west‑1.amazonaws.com',
            private_key='voluptatibus',
            region='us‑west‑1',
            shard_count=787542,
        ),
        name='Arturo Hauck',
    ),
    destination_id='voluptate',
)

res = s.destinations.patch_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.PatchDestinationRequest](../../models/operations/patchdestinationrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.PatchDestinationResponse](../../models/operations/patchdestinationresponse.md)**


## put_destination

Update a Destination and fully overwrite it

### Example Usage

```python
import airbyte
from airbyte.models import operations, shared

s = airbyte.Airbyte(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.PutDestinationRequest(
    destination_put_request=shared.DestinationPutRequest(
        configuration=shared.DestinationDatabricks(
            accept_terms=False,
            data_source=shared.DestinationDatabricksDataSourceAzureBlobStorage(
                azure_blob_storage_account_name='airbyte5storage',
                azure_blob_storage_container_name='airbytetestcontainername',
                azure_blob_storage_endpoint_domain_name='blob.core.windows.net',
                azure_blob_storage_sas_token='?sv=2016-05-31&ss=b&srt=sco&sp=rwdl&se=2018-06-27T10:05:50Z&st=2017-06-27T02:05:50Z&spr=https,http&sig=bgqQwoXwxzuD2GJfagRg7VOS8hzNr3QLT7rhS8OFRLQ%3D',
                data_source_type=shared.DestinationDatabricksDataSourceAzureBlobStorageDataSourceType.AZURE_BLOB_STORAGE,
            ),
            database='tenetur',
            databricks_http_path='sql/protocolvx/o/1234567489/0000-1111111-abcd90',
            databricks_personal_access_token='dapi0123456789abcdefghij0123456789AB',
            databricks_port='443',
            databricks_server_hostname='abc-12345678-wxyz.cloud.databricks.com',
            destination_type=shared.DestinationDatabricksDatabricks.DATABRICKS,
            enable_schema_evolution=False,
            purge_staging_data=False,
            schema='default',
        ),
        name='Darla Rau',
    ),
    destination_id='similique',
)

res = s.destinations.put_destination(req)

if res.destination_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PutDestinationRequest](../../models/operations/putdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutDestinationResponse](../../models/operations/putdestinationresponse.md)**

