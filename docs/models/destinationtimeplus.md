# ~~DestinationTimeplus~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'destinationType' key instead..


## Fields

| Field                                         | Type                                          | Required                                      | Description                                   | Example                                       |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| `apikey`                                      | *str*                                         | :heavy_check_mark:                            | Personal API key                              |                                               |
| `destination_type`                            | [models.Timeplus](../models/timeplus.md)      | :heavy_check_mark:                            | N/A                                           |                                               |
| `endpoint`                                    | *Optional[str]*                               | :heavy_minus_sign:                            | Timeplus workspace endpoint                   | https://us-west-2.timeplus.cloud/workspace_id |