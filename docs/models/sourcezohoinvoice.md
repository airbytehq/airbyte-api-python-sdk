# SourceZohoInvoice


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `client_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `client_refresh_token`                                                 | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `client_secret`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `region`                                                               | [models.SourceZohoInvoiceRegion](../models/sourcezohoinvoiceregion.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | To be provided if a user belongs to multiple organizations             |
| `source_type`                                                          | [models.ZohoInvoice](../models/zohoinvoice.md)                         | :heavy_check_mark:                                                     | N/A                                                                    |