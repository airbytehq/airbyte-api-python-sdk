# SourceZonkaFeedback


## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `auth_token`                                                                                                        | *str*                                                                                                               | :heavy_check_mark:                                                                                                  | Auth token to use. Generate it by navigating to Company Settings > Developers > API in your Zonka Feedback account. |
| `datacenter`                                                                                                        | [models.DataCenterID](../models/datacenterid.md)                                                                    | :heavy_check_mark:                                                                                                  | The identifier for the data center, such as 'us1' or 'e' for EU.                                                    |
| `source_type`                                                                                                       | [models.ZonkaFeedback](../models/zonkafeedback.md)                                                                  | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |