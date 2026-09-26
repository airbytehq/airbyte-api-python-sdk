# ~~SourceGmail~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'sourceType' key instead..


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `client_id`                                                                    | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `client_refresh_token`                                                         | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `client_secret`                                                                | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `include_spam_and_trash`                                                       | *Optional[bool]*                                                               | :heavy_minus_sign:                                                             | Include drafts/messages from SPAM and TRASH in the results. Defaults to false. |
| `source_type`                                                                  | [models.Gmail](../models/gmail.md)                                             | :heavy_check_mark:                                                             | N/A                                                                            |