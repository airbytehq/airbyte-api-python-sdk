# SourceNewsdataIo


## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                                                                                                                          | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `start_date`                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                               | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |
| `categories`                                                                                                                       | List[*Any*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Search the news articles for a specific category. You can add up to 5 categories in a single query.                                |
| `countries`                                                                                                                        | List[*Any*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Search the news articles from a specific country. You can add up to 5 countries in a single query. Example: au, jp, br             |
| `domains`                                                                                                                          | List[*Any*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Search the news articles for specific domains or news sources. You can add up to 5 domains in a single query.                      |
| `end_date`                                                                                                                         | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                       | :heavy_minus_sign:                                                                                                                 | Choose an end date. Now UTC is default value                                                                                       |
| `languages`                                                                                                                        | List[*Any*]                                                                                                                        | :heavy_minus_sign:                                                                                                                 | Search the news articles for a specific language. You can add up to 5 languages in a single query.                                 |
| `search_query`                                                                                                                     | *Optional[str]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Search news articles for specific keywords or phrases present in the news title, content, URL, meta keywords and meta description. |
| `source_type`                                                                                                                      | [models.NewsdataIo](../models/newsdataio.md)                                                                                       | :heavy_check_mark:                                                                                                                 | N/A                                                                                                                                |