# SourceOutbrainAmplify


## Fields

| Field                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `credentials`                                                                                                                                                                                                                               | [Union[models.SourceOutbrainAmplifyAccessToken, models.SourceOutbrainAmplifyUsernamePassword]](../models/sourceoutbrainamplifyauthenticationmethod.md)                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                          | Credentials for making authenticated requests requires either username/password or access_token.                                                                                                                                            |
| `start_date`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                                                                          | Date in the format YYYY-MM-DD eg. 2017-01-25. Any data before this date will not be replicated.                                                                                                                                             |
| `end_date`                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                          | Date in the format YYYY-MM-DD.                                                                                                                                                                                                              |
| `geo_location_breakdown`                                                                                                                                                                                                                    | [Optional[models.GranularityForGeoLocationRegion]](../models/granularityforgeolocationregion.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                          | The granularity used for geo location data in reports.                                                                                                                                                                                      |
| `report_granularity`                                                                                                                                                                                                                        | [Optional[models.GranularityForPeriodicReports]](../models/granularityforperiodicreports.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                          | The granularity used for periodic data in reports. See <a href="https://amplifyv01.docs.apiary.io/#reference/performance-reporting/periodic/retrieve-performance-statistics-for-all-marketer-campaigns-by-periodic-breakdown">the docs</a>. |
| `source_type`                                                                                                                                                                                                                               | [models.OutbrainAmplify](../models/outbrainamplify.md)                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                                         |