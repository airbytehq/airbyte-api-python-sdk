# SourceSnowflakeKeyPairAuthentication


## Fields

| Field                                                                                                                                                                                                       | Type                                                                                                                                                                                                        | Required                                                                                                                                                                                                    | Description                                                                                                                                                                                                 | Example                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `private_key`                                                                                                                                                                                               | *str*                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                          | RSA Private key to use for Snowflake connection. See the <a href="https://docs.airbyte.com/integrations/sources/snowflake#key-pair-authentication">docs</a> for more information on how to obtain this key. |                                                                                                                                                                                                             |
| `username`                                                                                                                                                                                                  | *str*                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                          | The username you created to allow Airbyte to access the database.                                                                                                                                           | AIRBYTE_USER                                                                                                                                                                                                |
| `auth_type`                                                                                                                                                                                                 | [Optional[models.SourceSnowflakeSchemasAuthType]](../models/sourcesnowflakeschemasauthtype.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |                                                                                                                                                                                                             |
| `private_key_password`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | Passphrase for private key                                                                                                                                                                                  |                                                                                                                                                                                                             |