# Users
(*users*)

## Overview

### Available Operations

* [list_users_within_an_organization](#list_users_within_an_organization) - List all users within an organization

## list_users_within_an_organization

Organization Admin user can list all users within the same organization. Also provide filtering on a list of user IDs or/and a list of user emails.

### Example Usage

```python
import airbyte_api
from airbyte_api import api, models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.users.list_users_within_an_organization(request=api.ListUsersWithinAnOrganizationRequest(
    organization_id='<value>',
))

if res.users_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [api.ListUsersWithinAnOrganizationRequest](../../api/listuserswithinanorganizationrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |

### Response

**[api.ListUsersWithinAnOrganizationResponse](../../api/listuserswithinanorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |