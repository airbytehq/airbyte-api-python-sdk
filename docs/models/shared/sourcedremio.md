# SourceDremio

The values required to configure the source.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `api_key`                                                                            | *Optional[str]*                                                                      | :heavy_check_mark:                                                                   | API Key that is generated when you authenticate to Dremio API                        |
| `base_url`                                                                           | *Optional[str]*                                                                      | :heavy_minus_sign:                                                                   | URL of your Dremio instance                                                          |
| `source_type`                                                                        | [Optional[shared.SourceDremioDremio]](undefined/models/shared/sourcedremiodremio.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |