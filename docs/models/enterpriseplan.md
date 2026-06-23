# EnterprisePlan


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `contacts_rate_limit`                                                       | *OptionalNullable[Literal[None]]*                                           | :heavy_minus_sign:                                                          | Maximum Rate in Limit/minute for contacts list endpoint in Enterprise Plan  |
| `general_rate_limit`                                                        | *OptionalNullable[Literal[None]]*                                           | :heavy_minus_sign:                                                          | General Maximum Rate in Limit/minute for other endpoints in Enterprise Plan |
| `plan_type`                                                                 | [Optional[models.PlanEnterprise]](../models/planenterprise.md)              | :heavy_minus_sign:                                                          | N/A                                                                         |
| `tickets_rate_limit`                                                        | *OptionalNullable[Literal[None]]*                                           | :heavy_minus_sign:                                                          | Maximum Rate in Limit/minute for tickets list endpoint in Enterprise Plan   |