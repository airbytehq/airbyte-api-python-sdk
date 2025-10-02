# SourceDefinitions
(*source_definitions*)

## Overview

### Available Operations

* [create_source_definition](#create_source_definition) - Create a source definition.
* [delete_source_definition](#delete_source_definition) - Delete a source definition.
* [get_source_definition](#get_source_definition) - Get source definition details.
* [list_source_definitions](#list_source_definitions) - List source definitions.
* [update_source_definition](#update_source_definition) - Update source definition details.

## create_source_definition

Create a source definition.

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


res = s.source_definitions.create_source_definition(request=api.CreateSourceDefinitionRequest(
    create_definition_request=models.CreateDefinitionRequest(
        docker_image_tag='<value>',
        docker_repository='<value>',
        name='<value>',
    ),
    workspace_id='06dbde72-63a8-4326-8f4b-67eb708f9ad6',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.CreateSourceDefinitionRequest](../../api/createsourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |

### Response

**[api.CreateSourceDefinitionResponse](../../api/createsourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_source_definition

Delete a source definition.

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


res = s.source_definitions.delete_source_definition(request=api.DeleteSourceDefinitionRequest(
    definition_id='fddaf9d9-7e09-433e-8e25-895734ad8809',
    workspace_id='9789f575-f200-4155-b7ec-0750094af77f',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.DeleteSourceDefinitionRequest](../../api/deletesourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |

### Response

**[api.DeleteSourceDefinitionResponse](../../api/deletesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_source_definition

Get source definition details.

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


res = s.source_definitions.get_source_definition(request=api.GetSourceDefinitionRequest(
    definition_id='b6405f71-0930-4f13-a99b-6b1b0a882853',
    workspace_id='e76093e5-5cd8-4b87-ab32-c620a178a1c3',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [api.GetSourceDefinitionRequest](../../api/getsourcedefinitionrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |

### Response

**[api.GetSourceDefinitionResponse](../../api/getsourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_source_definitions

List source definitions.

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


res = s.source_definitions.list_source_definitions(request=api.ListSourceDefinitionsRequest(
    workspace_id='fb60a310-f38b-47cb-9633-01f0cf740c18',
))

if res.definitions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [api.ListSourceDefinitionsRequest](../../api/listsourcedefinitionsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |

### Response

**[api.ListSourceDefinitionsResponse](../../api/listsourcedefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_source_definition

Update source definition details.

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


res = s.source_definitions.update_source_definition(request=api.UpdateSourceDefinitionRequest(
    update_definition_request=models.UpdateDefinitionRequest(
        docker_image_tag='<value>',
        name='<value>',
    ),
    definition_id='6eaf6fbb-3e08-4f73-9ff1-de62553abd76',
    workspace_id='b6bd5c36-3814-4489-97fb-3e48c1e0fdea',
))

if res.definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [api.UpdateSourceDefinitionRequest](../../api/updatesourcedefinitionrequest.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |

### Response

**[api.UpdateSourceDefinitionResponse](../../api/updatesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |