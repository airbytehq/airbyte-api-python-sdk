# Users

## Overview

### Available Operations

* [list_users_within_an_organization](#list_users_within_an_organization) - List all users within an organization

## list_users_within_an_organization

Organization Admin user can list all users within the same organization. Also provide filtering on a list of user IDs or/and a list of user emails.

### Example Usage

<!-- UsageSnippet language="python" operationID="listUsersWithinAnOrganization" method="get" path="/users" -->
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

    res = aa_client.users.list_users_within_an_organization(request={
        "organization_id": "<value>",
    })

    assert res.users_response is not None

    # Handle response
    print(res.users_response)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [api.ListUsersWithinAnOrganizationRequest](../../api/listuserswithinanorganizationrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[api.ListUsersWithinAnOrganizationResponse](../../api/listuserswithinanorganizationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |