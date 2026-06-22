# ReadChangesUsingChangeDataCaptureCDC

<i>Recommended</i> - Incrementally reads new inserts, updates, and deletes using change data capture feature. This must be enabled on your database.


## Fields

| Field                                                                                            | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `__pydantic_extra__`                                                                             | Dict[str, *Any*]                                                                                 | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `cursor_method`                                                                                  | [Optional[models.SourceDb2EnterpriseCursorMethod]](../models/sourcedb2enterprisecursormethod.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              |
| `initial_load_timeout_hours`                                                                     | *Optional[int]*                                                                                  | :heavy_minus_sign:                                                                               | The amount of time an initial load is allowed to continue for before catching up on CDC events.  |