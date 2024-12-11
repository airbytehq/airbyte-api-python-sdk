# SourceMux


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `start_date`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `username`                                                           | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `password`                                                           | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | N/A                                                                  |
| `playback_id`                                                        | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The playback id for your video asset shown in website details        |
| `source_type`                                                        | [models.Mux](../models/mux.md)                                       | :heavy_check_mark:                                                   | N/A                                                                  |