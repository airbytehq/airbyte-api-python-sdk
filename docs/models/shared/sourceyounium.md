# SourceYounium

The values required to configure the source.


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `legal_entity`                                                                      | *str*                                                                               | :heavy_check_mark:                                                                  | Legal Entity that data should be pulled from                                        |
| `password`                                                                          | *str*                                                                               | :heavy_check_mark:                                                                  | Account password for younium account API key                                        |
| `playground`                                                                        | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Property defining if connector is used against playground or production environment |
| `source_type`                                                                       | [shared.Younium](../../models/shared/younium.md)                                    | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `username`                                                                          | *str*                                                                               | :heavy_check_mark:                                                                  | Username for Younium account                                                        |