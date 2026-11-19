# ~~SourceMyHours~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `email`                                               | *str*                                                 | :heavy_check_mark:                                    | Your My Hours username                                | john@doe.com                                          |
| `logs_batch_size`                                     | *Optional[int]*                                       | :heavy_minus_sign:                                    | Pagination size used for retrieving logs in days      | 30                                                    |
| `password`                                            | *str*                                                 | :heavy_check_mark:                                    | The password associated to the username               |                                                       |
| `source_type`                                         | [models.MyHours](../models/myhours.md)                | :heavy_check_mark:                                    | N/A                                                   |                                                       |
| `start_date`                                          | *str*                                                 | :heavy_check_mark:                                    | Start date for collecting time logs                   | **Example 1:** %Y-%m-%d<br/>**Example 2:** 2016-01-01 |