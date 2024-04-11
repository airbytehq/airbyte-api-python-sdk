# SourceFacebookMarketingActionReportTime

Determines the report time of action stats. For example, if a person saw the ad on Jan 1st but converted on Jan 2nd, when you query the API with action_report_time=impression, you see a conversion on Jan 1st. When you query the API with action_report_time=conversion, you see a conversion on Jan 2nd.


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CONVERSION` | conversion   |
| `IMPRESSION` | impression   |
| `MIXED`      | mixed        |