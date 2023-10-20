# GetStreamPropertiesRequest


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `destination_id`                                                                     | *str*                                                                                | :heavy_check_mark:                                                                   | ID of the destination                                                                |
| `ignore_cache`                                                                       | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | If true pull the latest schema from the source, else pull from cache (default false) |
| `source_id`                                                                          | *str*                                                                                | :heavy_check_mark:                                                                   | ID of the source                                                                     |