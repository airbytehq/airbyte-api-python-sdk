# SourceZoom


## Fields

| Field                                                                                                                | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                         | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The account ID for your Zoom account. You can find this in the Zoom Marketplace under the "Manage" tab for your app. |
| `client_id`                                                                                                          | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The client ID for your Zoom app. You can find this in the Zoom Marketplace under the "Manage" tab for your app.      |
| `client_secret`                                                                                                      | *str*                                                                                                                | :heavy_check_mark:                                                                                                   | The client secret for your Zoom app. You can find this in the Zoom Marketplace under the "Manage" tab for your app.  |
| `authorization_endpoint`                                                                                             | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | N/A                                                                                                                  |
| `source_type`                                                                                                        | [models.Zoom](../models/zoom.md)                                                                                     | :heavy_check_mark:                                                                                                   | N/A                                                                                                                  |