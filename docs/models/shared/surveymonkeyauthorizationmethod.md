# SurveyMonkeyAuthorizationMethod

The authorization method to use to retrieve data from SurveyMonkey


## Fields

| Field                                                                                                                                                                             | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                                    | *str*                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                | Access Token for making authenticated requests. See the <a href="https://docs.airbyte.io/integrations/sources/surveymonkey">docs</a> for information on how to generate this key. |
| `auth_method`                                                                                                                                                                     | [shared.SourceSurveymonkeyAuthMethod](../../models/shared/sourcesurveymonkeyauthmethod.md)                                                                                        | :heavy_check_mark:                                                                                                                                                                | N/A                                                                                                                                                                               |
| `client_id`                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | The Client ID of the SurveyMonkey developer application.                                                                                                                          |
| `client_secret`                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                | The Client Secret of the SurveyMonkey developer application.                                                                                                                      |