# FreePlan


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `contacts_rate_limit`                                                 | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum Rate in Limit/minute for contacts list endpoint in Free Plan  |
| `general_rate_limit`                                                  | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | General Maximum Rate in Limit/minute for other endpoints in Free Plan |
| `plan_type`                                                           | [Optional[models.Plan]](../models/plan.md)                            | :heavy_minus_sign:                                                    | N/A                                                                   |
| `tickets_rate_limit`                                                  | *Optional[int]*                                                       | :heavy_minus_sign:                                                    | Maximum Rate in Limit/minute for tickets list endpoint in Free Plan   |