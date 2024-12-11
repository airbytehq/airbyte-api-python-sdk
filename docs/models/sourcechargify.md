# SourceChargify


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `api_key`                                                          | *str*                                                              | :heavy_check_mark:                                                 | Maxio Advanced Billing/Chargify API Key.                           |
| `domain`                                                           | *str*                                                              | :heavy_check_mark:                                                 | Chargify domain. Normally this domain follows the following format |
| `username`                                                         | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `password`                                                         | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `source_type`                                                      | [models.Chargify](../models/chargify.md)                           | :heavy_check_mark:                                                 | N/A                                                                |