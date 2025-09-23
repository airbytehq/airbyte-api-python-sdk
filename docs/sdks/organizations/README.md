# Organizations
(*organizations*)

## Overview

### Available Operations

* [create_or_update_organization_o_auth_credentials](#create_or_update_organization_o_auth_credentials) - Create OAuth override credentials for an organization and source type.
* [list_organizations_for_user](#list_organizations_for_user) - List all organizations for a user

## create_or_update_organization_o_auth_credentials

Create/update a set of OAuth credentials to override the Airbyte-provided OAuth credentials used for source/destination OAuth.
In order to determine what the credential configuration needs to be, please see the connector specification of the relevant source/destination.

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


res = s.organizations.create_or_update_organization_o_auth_credentials(request=api.CreateOrUpdateOrganizationOAuthCredentialsRequest(
    organization_o_auth_credentials_request=models.OrganizationOAuthCredentialsRequest(
        actor_type=models.ActorTypeEnum.SOURCE,
        configuration=models.Airtable(),
        name='<value>',
    ),
    organization_id='<value>',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                               | [api.CreateOrUpdateOrganizationOAuthCredentialsRequest](../../api/createorupdateorganizationoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                      | The request object to use for the request.                                                                              |

### Response

**[api.CreateOrUpdateOrganizationOAuthCredentialsResponse](../../api/createorupdateorganizationoauthcredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_organizations_for_user

Lists users organizations.

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


res = s.organizations.list_organizations_for_user()

if res.organizations_response is not None:
    # handle response
    pass

```

### Response

**[api.ListOrganizationsForUserResponse](../../api/listorganizationsforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |