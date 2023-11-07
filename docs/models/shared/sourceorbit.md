# SourceOrbit

The values required to configure the source.


## Fields

| Field                                                                                       | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `api_token`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | Authorizes you to work with Orbit workspaces associated with the token.                     |
| `source_type`                                                                               | [shared.Orbit](../../models/shared/orbit.md)                                                | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `start_date`                                                                                | *Optional[str]*                                                                             | :heavy_minus_sign:                                                                          | Date in the format 2022-06-26. Only load members whose last activities are after this date. |
| `workspace`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | The unique name of the workspace that your API token is associated with.                    |