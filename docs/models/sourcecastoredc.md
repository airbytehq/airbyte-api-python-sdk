# ~~SourceCastorEdc~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `client_id`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Visit `https://YOUR_REGION.castoredc.com/account/settings`           |
| `client_secret`                                                      | *str*                                                                | :heavy_check_mark:                                                   | Visit `https://YOUR_REGION.castoredc.com/account/settings`           |
| `source_type`                                                        | [models.CastorEdc](../models/castoredc.md)                           | :heavy_check_mark:                                                   | N/A                                                                  |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `url_region`                                                         | [Optional[models.URLRegion]](../models/urlregion.md)                 | :heavy_minus_sign:                                                   | The url region given at time of registration                         |