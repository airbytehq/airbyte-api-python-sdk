# DetectChangesWithXminSystemColumn

<i>Recommended</i> - Incrementally reads new inserts and updates via Postgres <a href="https://docs.airbyte.com/integrations/sources/postgres/#xmin">Xmin system column</a>. Only recommended for tables up to 500GB.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `method`                                                                       | [models.SourcePostgresSchemasMethod](../models/sourcepostgresschemasmethod.md) | :heavy_check_mark:                                                             | N/A                                                                            |