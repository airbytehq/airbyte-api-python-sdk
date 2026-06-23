# ~~DestinationHubspot~~

> :warning: **DEPRECATED**: Typed connector configuration models are deprecated and will be removed in v1.1.0. Pass configuration as a plain dict with a required 'destinationType' key instead..


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `credentials`                                                                          | [models.DestinationHubspotCredentials](../models/destinationhubspotcredentials.md)     | :heavy_check_mark:                                                                     | Choose how to authenticate to HubSpot.                                                 |
| `destination_type`                                                                     | [models.DestinationHubspotHubspot](../models/destinationhubspothubspot.md)             | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `object_storage_config`                                                                | [Optional[models.ObjectStorageConfiguration]](../models/objectstorageconfiguration.md) | :heavy_minus_sign:                                                                     | N/A                                                                                    |