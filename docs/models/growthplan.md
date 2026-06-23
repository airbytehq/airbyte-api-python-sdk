# GrowthPlan


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `contacts_rate_limit`                                                   | *OptionalNullable[Literal[None]]*                                       | :heavy_minus_sign:                                                      | Maximum Rate in Limit/minute for contacts list endpoint in Growth Plan  |
| `general_rate_limit`                                                    | *OptionalNullable[Literal[None]]*                                       | :heavy_minus_sign:                                                      | General Maximum Rate in Limit/minute for other endpoints in Growth Plan |
| `plan_type`                                                             | [Optional[models.RateLimitPlanPlan]](../models/ratelimitplanplan.md)    | :heavy_minus_sign:                                                      | N/A                                                                     |
| `tickets_rate_limit`                                                    | *OptionalNullable[Literal[None]]*                                       | :heavy_minus_sign:                                                      | Maximum Rate in Limit/minute for tickets list endpoint in Growth Plan   |