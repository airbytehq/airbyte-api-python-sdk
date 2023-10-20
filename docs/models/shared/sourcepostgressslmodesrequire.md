# SourcePostgresSSLModesRequire

Always require encryption. If the source database server does not support encryption, connection will fail.


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                       | Dict[str, *Any*]                                                                              | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `mode`                                                                                        | [SourcePostgresSSLModesRequireMode](../../models/shared/sourcepostgressslmodesrequiremode.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |