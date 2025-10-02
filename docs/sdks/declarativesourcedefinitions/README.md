# DeclarativeSourceDefinitions
(*declarative_source_definitions*)

## Overview

### Available Operations

* [create_declarative_source_definition](#create_declarative_source_definition) - Create a declarative source definition.
* [delete_declarative_source_definition](#delete_declarative_source_definition) - Delete a declarative source definition.
* [get_declarative_source_definition](#get_declarative_source_definition) - Get declarative source definition details.
* [list_declarative_source_definitions](#list_declarative_source_definitions) - List declarative source definitions.
* [update_declarative_source_definition](#update_declarative_source_definition) - Update declarative source definition details.

## create_declarative_source_definition

Create a declarative source definition.

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


res = s.declarative_source_definitions.create_declarative_source_definition(request=api.CreateDeclarativeSourceDefinitionRequest(
    create_declarative_source_definition_request=models.CreateDeclarativeSourceDefinitionRequest(
        manifest='<value>',
        name='<value>',
    ),
    workspace_id='2d054f48-a68c-4d16-b04d-bb444d47c285',
))

if res.declarative_source_definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.CreateDeclarativeSourceDefinitionRequest](../../api/createdeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |

### Response

**[api.CreateDeclarativeSourceDefinitionResponse](../../api/createdeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_declarative_source_definition

Delete a declarative source definition.

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


res = s.declarative_source_definitions.delete_declarative_source_definition(request=api.DeleteDeclarativeSourceDefinitionRequest(
    definition_id='26cd06ea-5caa-47b9-98a2-1d217049557d',
    workspace_id='f7cdc65f-5255-43d5-a6be-8fee673091f3',
))

if res.declarative_source_definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.DeleteDeclarativeSourceDefinitionRequest](../../api/deletedeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |

### Response

**[api.DeleteDeclarativeSourceDefinitionResponse](../../api/deletedeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_declarative_source_definition

Get declarative source definition details.

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


res = s.declarative_source_definitions.get_declarative_source_definition(request=api.GetDeclarativeSourceDefinitionRequest(
    definition_id='a003b7d3-efd4-4d7e-8ea6-469e9fe7871f',
    workspace_id='3855d0f6-8cfb-44c2-ac49-0c3965c034bd',
))

if res.declarative_source_definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [api.GetDeclarativeSourceDefinitionRequest](../../api/getdeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |

### Response

**[api.GetDeclarativeSourceDefinitionResponse](../../api/getdeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_declarative_source_definitions

List declarative source definitions.

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


res = s.declarative_source_definitions.list_declarative_source_definitions(request=api.ListDeclarativeSourceDefinitionsRequest(
    workspace_id='23bc0a4f-72b3-4d91-abe3-3f32d8a49dfc',
))

if res.declarative_source_definitions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [api.ListDeclarativeSourceDefinitionsRequest](../../api/listdeclarativesourcedefinitionsrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |

### Response

**[api.ListDeclarativeSourceDefinitionsResponse](../../api/listdeclarativesourcedefinitionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_declarative_source_definition

Update declarative source definition details.

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


res = s.declarative_source_definitions.update_declarative_source_definition(request=api.UpdateDeclarativeSourceDefinitionRequest(
    update_declarative_source_definition_request=models.UpdateDeclarativeSourceDefinitionRequest(
        manifest='<value>',
    ),
    definition_id='66066427-c293-4cbf-b72e-b31a72a46545',
    workspace_id='87f1ccdb-71b2-401c-8f60-cac1f2a2da80',
))

if res.declarative_source_definition_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [api.UpdateDeclarativeSourceDefinitionRequest](../../api/updatedeclarativesourcedefinitionrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |

### Response

**[api.UpdateDeclarativeSourceDefinitionResponse](../../api/updatedeclarativesourcedefinitionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |