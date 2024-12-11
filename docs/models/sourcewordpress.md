# SourceWordpress


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `domain`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | The domain of the WordPress site. Example: my-wordpress-website.host.com |
| `start_date`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)     | :heavy_check_mark:                                                       | Minimal Date to Retrieve Records when stream allow incremental.          |
| `password`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Placeholder for basic HTTP auth password - should be set to empty string |
| `source_type`                                                            | [models.Wordpress](../models/wordpress.md)                               | :heavy_check_mark:                                                       | N/A                                                                      |
| `username`                                                               | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Placeholder for basic HTTP auth username - should be set to empty string |