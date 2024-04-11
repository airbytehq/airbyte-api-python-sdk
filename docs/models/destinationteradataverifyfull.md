# DestinationTeradataVerifyFull

Verify-full SSL mode.


## Fields

| Field                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ssl_ca_certificate`                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                            | :heavy_check_mark:                                                                                                                                                                                                                                                                               | Specifies the file name of a PEM file that contains Certificate Authority (CA) certificates for use with SSLMODE=verify-full.<br/> See more information - <a href="https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#URL_SSLCA"> in the docs</a>. |
| `mode`                                                                                                                                                                                                                                                                                           | [Optional[models.DestinationTeradataSchemasSSLModeSSLModes6Mode]](../models/destinationteradataschemassslmodesslmodes6mode.md)                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                                                                              |