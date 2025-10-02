# DestinationDefinitions
(*destination_definitions*)

## Overview

### Available Operations

* [create_destination_definition](#create_destination_definition) - Create a destination definition.
* [delete_destination_definition](#delete_destination_definition) - Delete a destination definition.
* [get_destination_definition](#get_destination_definition) - Get destination definition details.
* [list_destination_definitions](#list_destination_definitions) - List destination definitions.
* [update_destination_definition](#update_destination_definition) - Update destination definition details.

## create_destination_definition

Create a destination definition.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.destination_definitions.create_destination_definition(request=api.CreateDestinationDefinitionRequest(
    create_definition_request=models.CreateDefinitionRequest(
        docker_image_tag='<value>',
        docker_repository='<value>',
        name='<value>',
    ),
    workspace_id='f49928fc-e1f7-4278-9366-b5b974ad2068',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.CreateDestinationDefinitionRequest](../../api/createdestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |

### Response

**[api.CreateDestinationDefinitionResponse](../../api/createdestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_destination_definition

Delete a destination definition.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.destination_definitions.delete_destination_definition(request=api.DeleteDestinationDefinitionRequest(
    definition_id='7a6d93e0-5a99-4e33-87ce-c0e739faf1e9',
    workspace_id='619cc567-a21d-4f39-90ab-7854d54c9c42',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.DeleteDestinationDefinitionRequest](../../api/deletedestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |

### Response

**[api.DeleteDestinationDefinitionResponse](../../api/deletedestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_destination_definition

Get destination definition details.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.destination_definitions.get_destination_definition(request=api.GetDestinationDefinitionRequest(
    definition_id='5ddd49a6-7aa1-469d-bd19-fa66e3586402',
    workspace_id='5a9c29a5-f169-496b-b3b1-ab05028ede0b',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [api.GetDestinationDefinitionRequest](../../api/getdestinationdefinitionrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |

### Response

**[api.GetDestinationDefinitionResponse](../../api/getdestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_destination_definitions

List destination definitions.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.destination_definitions.list_destination_definitions(request=api.ListDestinationDefinitionsRequest(
    workspace_id='f1f18267-b72b-4ea5-a29c-8742c80ceaf4',
))

if res.definitions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [api.ListDestinationDefinitionsRequest](../../api/listdestinationdefinitionsrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |

### Response

**[api.ListDestinationDefinitionsResponse](../../api/listdestinationdefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_destination_definition

Update destination definition details.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.destination_definitions.update_destination_definition(request=api.UpdateDestinationDefinitionRequest(
    update_definition_request=models.UpdateDefinitionRequest(
        docker_image_tag='<value>',
        name='<value>',
    ),
    definition_id='97416649-dabf-43f9-8715-c5c8279f7f23',
    workspace_id='98e0ed50-276f-49ae-ad18-43bc892bb109',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [api.UpdateDestinationDefinitionRequest](../../api/updatedestinationdefinitionrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |

### Response

**[api.UpdateDestinationDefinitionResponse](../../api/updatedestinationdefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |