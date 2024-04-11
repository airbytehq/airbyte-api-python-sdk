# ServiceAccount


## Fields

| Field                                                                                                                                                                               | Type                                                                                                                                                                                | Required                                                                                                                                                                            | Description                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project_id`                                                                                                                                                                        | *int*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | Your project ID number. See the <a href="https://help.mixpanel.com/hc/en-us/articles/115004490503-Project-Settings#project-id">docs</a> for more information on how to obtain this. |
| `secret`                                                                                                                                                                            | *str*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | Mixpanel Service Account Secret. See the <a href="https://developer.mixpanel.com/reference/service-accounts">docs</a> for more information on how to obtain this.                   |
| `username`                                                                                                                                                                          | *str*                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                  | Mixpanel Service Account Username. See the <a href="https://developer.mixpanel.com/reference/service-accounts">docs</a> for more information on how to obtain this.                 |
| `option_title`                                                                                                                                                                      | [Optional[models.SourceMixpanelOptionTitle]](../models/sourcemixpaneloptiontitle.md)                                                                                                | :heavy_minus_sign:                                                                                                                                                                  | N/A                                                                                                                                                                                 |