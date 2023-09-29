# SourceMixpanelAuthenticationWildcardServiceAccount

Choose how to authenticate to Mixpanel


## Fields

| Field                                                                                                                                                               | Type                                                                                                                                                                | Required                                                                                                                                                            | Description                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `option_title`                                                                                                                                                      | *Optional[str]*                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                  | N/A                                                                                                                                                                 |
| `secret`                                                                                                                                                            | *Optional[str]*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                  | Mixpanel Service Account Secret. See the <a href="https://developer.mixpanel.com/reference/service-accounts">docs</a> for more information on how to obtain this.   |
| `username`                                                                                                                                                          | *Optional[str]*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                  | Mixpanel Service Account Username. See the <a href="https://developer.mixpanel.com/reference/service-accounts">docs</a> for more information on how to obtain this. |