# SourceSftpPasswordAuthentication

The server authentication method


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `auth_method`                                                              | [shared.SourceSftpAuthMethod](../../models/shared/sourcesftpauthmethod.md) | :heavy_check_mark:                                                         | Connect through password authentication                                    |
| `auth_user_password`                                                       | *str*                                                                      | :heavy_check_mark:                                                         | OS-level password for logging into the jump server host                    |