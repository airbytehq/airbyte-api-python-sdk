# SourceGoogleAnalyticsV4ServiceAccountOnlyServiceAccountKeyAuthentication


## Fields

| Field                                                                                                                                | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          | Example                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `credentials_json`                                                                                                                   | *str*                                                                                                                                | :heavy_check_mark:                                                                                                                   | The JSON key of the service account to use for authorization                                                                         | { "type": "service_account", "project_id": YOUR_PROJECT_ID, "private_key_id": YOUR_PRIVATE_KEY, ... }                                |
| `auth_type`                                                                                                                          | [Optional[models.SourceGoogleAnalyticsV4ServiceAccountOnlyAuthType]](../models/sourcegoogleanalyticsv4serviceaccountonlyauthtype.md) | :heavy_minus_sign:                                                                                                                   | N/A                                                                                                                                  |                                                                                                                                      |