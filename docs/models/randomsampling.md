# RandomSampling

For each stream, randomly log a percentage of the entries with a maximum cap.


## Fields

| Field                                                                                                                                   | Type                                                                                                                                    | Required                                                                                                                                | Description                                                                                                                             | Example                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_properties`                                                                                                                 | Dict[str, *Any*]                                                                                                                        | :heavy_minus_sign:                                                                                                                      | N/A                                                                                                                                     |                                                                                                                                         |
| `logging_type`                                                                                                                          | [Optional[models.DestinationDevNullSchemasLoggingType]](../models/destinationdevnullschemasloggingtype.md)                              | :heavy_minus_sign:                                                                                                                      | N/A                                                                                                                                     |                                                                                                                                         |
| `max_entry_count`                                                                                                                       | *Optional[float]*                                                                                                                       | :heavy_minus_sign:                                                                                                                      | Number of entries to log. This destination is for testing only. So it won't make sense to log infinitely. The maximum is 1,000 entries. | 100                                                                                                                                     |
| `sampling_ratio`                                                                                                                        | *Optional[float]*                                                                                                                       | :heavy_minus_sign:                                                                                                                      | A positive floating number smaller than 1.                                                                                              | 0.001                                                                                                                                   |
| `seed`                                                                                                                                  | *Optional[float]*                                                                                                                       | :heavy_minus_sign:                                                                                                                      | When the seed is unspecified, the current time millis will be used as the seed.                                                         | 1900                                                                                                                                    |