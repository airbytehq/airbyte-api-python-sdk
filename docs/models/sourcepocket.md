# SourcePocket


## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `access_token`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | The user's Pocket access token.                                                                 |                                                                                                 |
| `consumer_key`                                                                                  | *str*                                                                                           | :heavy_check_mark:                                                                              | Your application's Consumer Key.                                                                |                                                                                                 |
| `content_type`                                                                                  | [Optional[models.ContentType]](../models/contenttype.md)                                        | :heavy_minus_sign:                                                                              | Select the content type of the items to retrieve.                                               |                                                                                                 |
| `detail_type`                                                                                   | [Optional[models.DetailType]](../models/detailtype.md)                                          | :heavy_minus_sign:                                                                              | Select the granularity of the information about each item.                                      |                                                                                                 |
| `domain`                                                                                        | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Only return items from a particular `domain`.                                                   |                                                                                                 |
| `favorite`                                                                                      | *Optional[bool]*                                                                                | :heavy_minus_sign:                                                                              | Retrieve only favorited items.                                                                  |                                                                                                 |
| `search`                                                                                        | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Only return items whose title or url contain the `search` string.                               |                                                                                                 |
| `since`                                                                                         | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Only return items modified since the given timestamp.                                           | 2022-10-20 14:14:14                                                                             |
| `sort`                                                                                          | [Optional[models.SourcePocketSortBy]](../models/sourcepocketsortby.md)                          | :heavy_minus_sign:                                                                              | Sort retrieved items by the given criteria.                                                     |                                                                                                 |
| `source_type`                                                                                   | [models.Pocket](../models/pocket.md)                                                            | :heavy_check_mark:                                                                              | N/A                                                                                             |                                                                                                 |
| `state`                                                                                         | [Optional[models.State]](../models/state.md)                                                    | :heavy_minus_sign:                                                                              | Select the state of the items to retrieve.                                                      |                                                                                                 |
| `tag`                                                                                           | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | Return only items tagged with this tag name. Use _untagged_ for retrieving only untagged items. |                                                                                                 |