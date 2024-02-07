# IAMRole


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `role_arn`                                                                   | *str*                                                                        | :heavy_check_mark:                                                           | Will assume this role to write data to s3                                    |
| `credentials_title`                                                          | [Optional[shared.CredentialsTitle]](../../models/shared/credentialstitle.md) | :heavy_minus_sign:                                                           | Name of the credentials                                                      |