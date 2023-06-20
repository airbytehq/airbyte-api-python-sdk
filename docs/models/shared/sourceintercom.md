# SourceIntercom

The values required to configure the source.


## Fields

| Field                                                                                                                                                                                                          | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    | Example                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                                                                                                 | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | Access token for making authenticated requests. See the <a href="https://developers.intercom.com/building-apps/docs/authentication-types#how-to-get-your-access-token">Intercom docs</a> for more information. |                                                                                                                                                                                                                |
| `source_type`                                                                                                                                                                                                  | [SourceIntercomIntercom](../../models/shared/sourceintercomintercom.md)                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                             | N/A                                                                                                                                                                                                            |                                                                                                                                                                                                                |
| `start_date`                                                                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                             | UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated.                                                                                                        | 2020-11-16T00:00:00Z                                                                                                                                                                                           |