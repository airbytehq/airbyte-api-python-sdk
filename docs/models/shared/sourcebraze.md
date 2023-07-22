# SourceBraze

The values required to configure the source.


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `api_key`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API key                                                           |
| `source_type`                                                                | [SourceBrazeBraze](../../models/shared/sourcebrazebraze.md)                  | :heavy_check_mark:                                                           | N/A                                                                          |
| `start_date`                                                                 | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) | :heavy_check_mark:                                                           | Rows after this date will be synced                                          |
| `url`                                                                        | *str*                                                                        | :heavy_check_mark:                                                           | Braze REST API endpoint                                                      |