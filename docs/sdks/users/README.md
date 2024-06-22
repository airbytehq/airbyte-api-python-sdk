# Users
(*users*)

### Available Operations

* [list_users](#list_users) - List users

## list_users

Lists users based on provided filters. You can filter on either a list of IDs or a list of emails, but not both. If no filters provided we will list all users by default.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="<YOUR_PASSWORD_HERE>",
            username="<YOUR_USERNAME_HERE>",
        ),
    ),
)


res = s.users.list_users(request=api.ListUsersRequest())

if res.users_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                             | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `request`                                             | [api.ListUsersRequest](../../api/listusersrequest.md) | :heavy_check_mark:                                    | The request object to use for the request.            |


### Response

**[api.ListUsersResponse](../../api/listusersresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
