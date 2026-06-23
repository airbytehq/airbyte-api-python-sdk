# BatchedStandardInserts

Direct loading using batched SQL INSERT statements. This method uses the BigQuery driver to convert large INSERT statements into file uploads automatically.


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `__pydantic_extra__`                                                                                 | Dict[str, *Any*]                                                                                     | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |
| `method`                                                                                             | [Optional[models.DestinationBigqueryMethodStandard]](../models/destinationbigquerymethodstandard.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |