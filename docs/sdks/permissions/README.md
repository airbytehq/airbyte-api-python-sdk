# Permissions

## Overview

### Available Operations

* [create_permission](#create_permission) - Create a permission
* [delete_permission](#delete_permission) - Delete a Permission
* [get_permission](#get_permission) - Get Permission details
* [list_permissions](#list_permissions) - List Permissions by user id
* [update_permission](#update_permission) - Update a permission

## create_permission

Create a permission

### Example Usage: Permission Creation Request Example

<!-- UsageSnippet language="python" operationID="createPermission" method="post" path="/permissions" example="Permission Creation Request Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.create_permission(request={
        "permission_type": models.PublicPermissionType.WORKSPACE_ADMIN,
        "user_id": "7d08fd6c-531e-4a00-937e-3d355f253e63",
        "workspace_id": "9924bcd0-99be-453d-ba47-c2c9766f7da5",
    })

    assert res.permission_response is not None

    # Handle response
    print(res.permission_response)

```
### Example Usage: Permission Creation Response Example

<!-- UsageSnippet language="python" operationID="createPermission" method="post" path="/permissions" example="Permission Creation Response Example" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.create_permission(request={
        "permission_type": models.PublicPermissionType.WORKSPACE_READER,
        "user_id": "dc1309ac-0e0a-43cf-80a3-b39dea83440d",
    })

    assert res.permission_response is not None

    # Handle response
    print(res.permission_response)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.PermissionCreateRequest](../../models/permissioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[api.CreatePermissionResponse](../../api/createpermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_permission

Delete a Permission

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePermission" method="delete" path="/permissions/{permissionId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.delete_permission(request={
        "permission_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeletePermissionRequest](../../api/deletepermissionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.DeletePermissionResponse](../../api/deletepermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_permission

Get Permission details

### Example Usage

<!-- UsageSnippet language="python" operationID="getPermission" method="get" path="/permissions/{permissionId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.get_permission(request={
        "permission_id": "<value>",
    })

    assert res.permission_response is not None

    # Handle response
    print(res.permission_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.GetPermissionRequest](../../api/getpermissionrequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.GetPermissionResponse](../../api/getpermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_permissions

List Permissions by user id

### Example Usage

<!-- UsageSnippet language="python" operationID="listPermissions" method="get" path="/permissions" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.list_permissions(request={})

    assert res.permissions_response is not None

    # Handle response
    print(res.permissions_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.ListPermissionsRequest](../../api/listpermissionsrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListPermissionsResponse](../../api/listpermissionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_permission

Update a permission

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePermission" method="patch" path="/permissions/{permissionId}" -->
```python
from airbyte_api import AirbyteAPI, models


with AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
) as aa_client:

    res = aa_client.permissions.update_permission(request={
        "permission_id": "<value>",
        "permission_update_request": {
            "permission_type": models.PermissionType.ORGANIZATION_READER,
        },
    })

    assert res.permission_response is not None

    # Handle response
    print(res.permission_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.UpdatePermissionRequest](../../api/updatepermissionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.UpdatePermissionResponse](../../api/updatepermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |