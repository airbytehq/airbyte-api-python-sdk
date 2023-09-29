# SourceGithubAuthenticationPersonalAccessToken

Choose how to authenticate to GitHub


## Fields

| Field                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                        | Required                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `option_title`                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                          | N/A                                                                                                                                                                                                                         |
| `personal_access_token`                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                          | Log into GitHub and then generate a <a href="https://github.com/settings/tokens">personal access token</a>. To load balance your API quota consumption across multiple API tokens, input multiple tokens separated with "," |