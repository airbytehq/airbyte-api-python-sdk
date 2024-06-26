# SourceTrustpilotAPIKey

The API key authentication method gives you access to only the streams which are part of the Public API. When you want to get streams available via the Consumer API (e.g. the private reviews) you need to use authentication method OAuth 2.0.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `client_id`                                                                                      | *str*                                                                                            | :heavy_check_mark:                                                                               | The API key of the Trustpilot API application.                                                   |
| `auth_type`                                                                                      | [Optional[models.SourceTrustpilotSchemasAuthType]](../models/sourcetrustpilotschemasauthtype.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |