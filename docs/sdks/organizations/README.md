# Organizations
(*organizations*)

## Overview

### Available Operations

* [list_organizations_for_user](#list_organizations_for_user) - List all organizations for a user

## list_organizations_for_user

Lists users organizations.

### Example Usage

```python
import airbyte_api
from airbyte_api import models

s = airbyte_api.AirbyteAPI(
    security=models.Security(
        basic_auth=models.SchemeBasicAuth(
            password="",
            username="",
        ),
    ),
)


res = s.organizations.list_organizations_for_user()

if res.organizations_response is not None:
    # handle response
    pass

```

### Response

**[api.ListOrganizationsForUserResponse](../../api/listorganizationsforuserresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
