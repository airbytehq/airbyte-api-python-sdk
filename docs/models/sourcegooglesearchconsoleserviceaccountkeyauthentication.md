# SourceGoogleSearchConsoleServiceAccountKeyAuthentication


## Fields

| Field                                                                                                                                                                | Type                                                                                                                                                                 | Required                                                                                                                                                             | Description                                                                                                                                                          | Example                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `email`                                                                                                                                                              | *str*                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                   | The email of the user which has permissions to access the Google Workspace Admin APIs.                                                                               |                                                                                                                                                                      |
| `service_account_info`                                                                                                                                               | *str*                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                   | The JSON key of the service account to use for authorization. Read more <a href="https://cloud.google.com/iam/docs/creating-managing-service-account-keys">here</a>. | { "type": "service_account", "project_id": YOUR_PROJECT_ID, "private_key_id": YOUR_PRIVATE_KEY, ... }                                                                |
| `auth_type`                                                                                                                                                          | [models.SourceGoogleSearchConsoleSchemasAuthType](../models/sourcegooglesearchconsoleschemasauthtype.md)                                                             | :heavy_check_mark:                                                                                                                                                   | N/A                                                                                                                                                                  |                                                                                                                                                                      |