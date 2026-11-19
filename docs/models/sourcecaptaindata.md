# ~~SourceCaptainData~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `api_key`                                      | *str*                                          | :heavy_check_mark:                             | Your Captain Data project API key.             |
| `project_uid`                                  | *str*                                          | :heavy_check_mark:                             | Your Captain Data project uuid.                |
| `source_type`                                  | [models.CaptainData](../models/captaindata.md) | :heavy_check_mark:                             | N/A                                            |