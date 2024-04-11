# SourceTrello


## Fields

| Field                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                              | Example                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key`                                                                                                                                                                                                                                                                                                    | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Trello API key. See the <a href="https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth">docs</a> for instructions on how to generate it.                                                                                                                         |                                                                                                                                                                                                                                                                                                          |
| `start_date`                                                                                                                                                                                                                                                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated.                                                                                                                                                                                                  | 2021-03-01T00:00:00Z                                                                                                                                                                                                                                                                                     |
| `token`                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | Trello API token. See the <a href="https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#using-basic-oauth">docs</a> for instructions on how to generate it.                                                                                                                       |                                                                                                                                                                                                                                                                                                          |
| `board_ids`                                                                                                                                                                                                                                                                                              | List[*str*]                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                       | IDs of the boards to replicate data from. If left empty, data from all boards to which you have access will be replicated. Please note that this is not the 8-character ID in the board's shortLink (URL of the board). Rather, what is required here is the 24-character ID usually returned by the API |                                                                                                                                                                                                                                                                                                          |
| `source_type`                                                                                                                                                                                                                                                                                            | [models.Trello](../models/trello.md)                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                          |