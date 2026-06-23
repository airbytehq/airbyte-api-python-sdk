# ~~SourceZohoInvoice~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `client_id`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `client_refresh_token`                                                 | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `client_secret`                                                        | *str*                                                                  | :heavy_check_mark:                                                     | N/A                                                                    |
| `organization_id`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | To be provided if a user belongs to multiple organizations             |
| `region`                                                               | [models.SourceZohoInvoiceRegion](../models/sourcezohoinvoiceregion.md) | :heavy_check_mark:                                                     | N/A                                                                    |
| `source_type`                                                          | [models.ZohoInvoice](../models/zohoinvoice.md)                         | :heavy_check_mark:                                                     | N/A                                                                    |