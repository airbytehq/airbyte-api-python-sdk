# SourceOracleNativeNetworkEncryptionNNE

The native network encryption gives you the ability to encrypt database connections, without the configuration overhead of TCP/IP and SSL/TLS and without the need to open and listen on different ports.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `encryption_algorithm`                                                                           | [Optional[models.SourceOracleEncryptionAlgorithm]](../models/sourceoracleencryptionalgorithm.md) | :heavy_minus_sign:                                                                               | This parameter defines what encryption algorithm is used.                                        |
| `encryption_method`                                                                              | [models.SourceOracleSchemasEncryptionMethod](../models/sourceoracleschemasencryptionmethod.md)   | :heavy_check_mark:                                                                               | N/A                                                                                              |