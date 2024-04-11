# SourceBraze


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `api_key`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API key                                                           |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Rows after this date will be synced                                          |
| `url`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API endpoint                                                      |
| `source_type`                                                                | [models.Braze](../models/braze.md)                                           | :heavy_check_mark:                                                           | N/A                                                                          |