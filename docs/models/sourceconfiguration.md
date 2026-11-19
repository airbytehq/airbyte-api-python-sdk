# SourceConfiguration

The values required to configure the source. Must include a `sourceType` string identifying the connector (e.g. 'postgres', 'github'). Additional properties depend on the connector type; the API validates the full schema server-side.


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `__pydantic_extra__`                                                               | Dict[str, *Any*]                                                                   | :heavy_minus_sign:                                                                 | N/A                                                                                | {<br/>"user": "charles",<br/>"sourceType": "postgres",<br/>"host": "localhost",<br/>"port": 5432<br/>} |
| `source_type`                                                                      | *str*                                                                              | :heavy_check_mark:                                                                 | The type of source connector.                                                      |                                                                                    |