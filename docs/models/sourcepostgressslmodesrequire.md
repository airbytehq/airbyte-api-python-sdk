# SourcePostgresSSLModesRequire

Always require encryption. If the source database server does not support encryption, connection will fail.


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `__pydantic_extra__`                                                                         | Dict[str, *Any*]                                                                             | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `mode`                                                                                       | [models.SourcePostgresSSLModesSSLMode4Mode](../models/sourcepostgressslmodessslmode4mode.md) | :heavy_check_mark:                                                                           | N/A                                                                                          |