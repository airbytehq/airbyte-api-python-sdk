# SourcePlausible


## Fields

| Field                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                            | Plausible API Key. See the <a href="https://plausible.io/docs/stats-api">docs</a> for information on how to generate this key.                                                                                                |                                                                                                                                                                                                                               |
| `site_id`                                                                                                                                                                                                                     | *str*                                                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                                                            | The domain of the site you want to retrieve data for. Enter the name of your site as configured on Plausible, i.e., excluding "https://" and "www". Can be retrieved from the 'domain' field in your Plausible site settings. | airbyte.com                                                                                                                                                                                                                   |
| `api_url`                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                            | The API URL of your plausible instance. Change this if you self-host plausible. The default is https://plausible.io/api/v1/stats                                                                                              | https://plausible.example.com/api/v1/stats                                                                                                                                                                                    |
| `source_type`                                                                                                                                                                                                                 | [models.Plausible](../models/plausible.md)                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                           |                                                                                                                                                                                                                               |
| `start_date`                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                            | Start date for data to retrieve, in ISO-8601 format.                                                                                                                                                                          | YYYY-MM-DD                                                                                                                                                                                                                    |