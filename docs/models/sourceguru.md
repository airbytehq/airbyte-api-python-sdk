# SourceGuru


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `start_date`                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                    | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `username`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `password`                                                                              | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `search_cards_query`                                                                    | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Query for searching cards                                                               |
| `source_type`                                                                           | [models.Guru](../models/guru.md)                                                        | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `team_id`                                                                               | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | Team ID received through response of /teams streams, make sure about access to the team |