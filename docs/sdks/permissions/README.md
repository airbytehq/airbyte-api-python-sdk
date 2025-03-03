# Permissions
(*permissions*)

## Overview

### Available Operations

* [create_permission](#create_permission) - Create a permission
* [delete_permission](#delete_permission) - Delete a Permission
* [get_permission](#get_permission) - Get Permission details
* [list_permissions](#list_permissions) - List Permissions by user id
* [update_permission](#update_permission) - Update a permission

## create_permission

Create a permission

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password='',
            username='',
        ),
    ),
)


res = s.permissions.create_permission(request=models.PermissionCreateRequest(
    permission_type=models.PublicPermissionType.WORKSPACE_ADMIN,
    user_id='7d08fd6c-531e-4a00-937e-3d355f253e63',
    workspace_id='9924bcd0-99be-453d-ba47-c2c9766f7da5',
))

if res.permission_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.PermissionCreateRequest](../../models/permissioncreaterequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |

### Response

**[api.CreatePermissionResponse](../../api/createpermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_permission

Delete a Permission

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


res = s.permissions.delete_permission(request=api.DeletePermissionRequest(
    permission_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.DeletePermissionRequest](../../api/deletepermissionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |

### Response

**[api.DeletePermissionResponse](../../api/deletepermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_permission

Get Permission details

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


res = s.permissions.get_permission(request=api.GetPermissionRequest(
    permission_id='<value>',
))

if res.permission_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                     | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `request`                                                     | [api.GetPermissionRequest](../../api/getpermissionrequest.md) | :heavy_check_mark:                                            | The request object to use for the request.                    |

### Response

**[api.GetPermissionResponse](../../api/getpermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_permissions

List Permissions by user id

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


res = s.permissions.list_permissions(request=api.ListPermissionsRequest())

if res.permissions_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `request`                                                         | [api.ListPermissionsRequest](../../api/listpermissionsrequest.md) | :heavy_check_mark:                                                | The request object to use for the request.                        |

### Response

**[api.ListPermissionsResponse](../../api/listpermissionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_permission

Update a permission

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


res = s.permissions.update_permission(request=api.UpdatePermissionRequest(
    permission_update_request=models.PermissionUpdateRequest(
        permission_type=models.PermissionType.WORKSPACE_OWNER,
    ),
    permission_id='<value>',
))

if res.permission_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [api.UpdatePermissionRequest](../../api/updatepermissionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |

### Response

**[api.UpdatePermissionResponse](../../api/updatepermissionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |