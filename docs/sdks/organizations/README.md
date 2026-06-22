# Organizations

## Overview

### Available Operations

* [create_or_update_organization_o_auth_credentials](#create_or_update_organization_o_auth_credentials) - Create OAuth override credentials for an organization and source type.
* [delete_organization_o_auth_credentials](#delete_organization_o_auth_credentials) - Delete OAuth override credentials for an organization and source/destination type.
* [list_organizations_for_user](#list_organizations_for_user) - List all organizations for a user

## create_or_update_organization_o_auth_credentials

Create/update a set of OAuth credentials to override the Airbyte-provided OAuth credentials used for source/destination OAuth.
In order to determine what the credential configuration needs to be, please see the connector specification of the relevant source/destination.

### Example Usage

<!-- UsageSnippet language="python" operationID="createOrUpdateOrganizationOAuthCredentials" method="put" path="/organizations/{organizationId}/oauthCredentials" -->
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

    res = aa_client.organizations.create_or_update_organization_o_auth_credentials(request={
        "organization_o_auth_credentials_request": {
            "actor_type": models.ActorTypeEnum.SOURCE,
            "configuration": {

            },
            "name": "<value>",
        },
        "organization_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                               | [api.CreateOrUpdateOrganizationOAuthCredentialsRequest](../../api/createorupdateorganizationoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                                      | The request object to use for the request.                                                                              |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[api.CreateOrUpdateOrganizationOAuthCredentialsResponse](../../api/createorupdateorganizationoauthcredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_organization_o_auth_credentials

Delete a set of OAuth credentials that overrides the Airbyte-provided OAuth credentials used for source/destination OAuth.

> 🚧 Warning
>
> Deleting an override that is actively used by existing sources or destinations will cause those connectors to fail on their next sync and require re-authentication.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteOrganizationOAuthCredentials" method="delete" path="/organizations/{organizationId}/oauthCredentials/{actorType}/{name}" -->
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

    res = aa_client.organizations.delete_organization_o_auth_credentials(request={
        "actor_type": models.ActorTypeEnum.SOURCE,
        "name": "<value>",
        "organization_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [api.DeleteOrganizationOAuthCredentialsRequest](../../api/deleteorganizationoauthcredentialsrequest.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[api.DeleteOrganizationOAuthCredentialsResponse](../../api/deleteorganizationoauthcredentialsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_organizations_for_user

Lists users organizations.

### Example Usage

<!-- UsageSnippet language="python" operationID="listOrganizationsForUser" method="get" path="/organizations" -->
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

    res = aa_client.organizations.list_organizations_for_user()

    assert res.organizations_response is not None

    # Handle response
    print(res.organizations_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[api.ListOrganizationsForUserResponse](../../api/listorganizationsforuserresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |