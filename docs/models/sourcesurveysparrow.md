# SourceSurveySparrow


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                      | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Your access token. See <a href="https://developers.surveysparrow.com/rest-apis#authentication">here</a>. The key is case sensitive. |
| `region`                                                                                                                            | [Optional[Union[models.EUBasedAccount, models.GlobalAccount]]](../models/baseurl.md)                                                | :heavy_minus_sign:                                                                                                                  | Is your account location is EU based? If yes, the base url to retrieve data will be different.                                      |
| `source_type`                                                                                                                       | [models.SurveySparrow](../models/surveysparrow.md)                                                                                  | :heavy_check_mark:                                                                                                                  | N/A                                                                                                                                 |
| `survey_id`                                                                                                                         | List[*Any*]                                                                                                                         | :heavy_minus_sign:                                                                                                                  | A List of your survey ids for survey-specific stream                                                                                |