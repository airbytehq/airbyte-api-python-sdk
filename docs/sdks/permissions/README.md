# Permissions
(*permissions*)

### Available Operations

* [create_permission](#create_permission) - Create a permission

## create_permission

Create a permission

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)

res = s.permissions.create_permission(request=models.PermissionCreateRequest(
    permission_type=models.PermissionType.WORKSPACE_ADMIN,
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

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
