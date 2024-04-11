# DestinationRedshift


## Fields

| Field                                                                                                                                                                                                                                                                              | Type                                                                                                                                                                                                                                                                               | Required                                                                                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                        | Example                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `database`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | Name of the database.                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                    |
| `host`                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | Host Endpoint of the Redshift Cluster (must include the cluster-id, region and end with .redshift.amazonaws.com)                                                                                                                                                                   |                                                                                                                                                                                                                                                                                    |
| `password`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | Password associated with the username.                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                    |
| `username`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                                 | Username to use to access the database.                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                    |
| `destination_type`                                                                                                                                                                                                                                                                 | [models.Redshift](../models/redshift.md)                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                 | N/A                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                    |
| `disable_type_dedupe`                                                                                                                                                                                                                                                              | *Optional[bool]*                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Disable Writing Final Tables. WARNING! The data format in _airbyte_data is likely stable but there are no guarantees that other metadata columns will remain the same in future versions                                                                                           |                                                                                                                                                                                                                                                                                    |
| `enable_incremental_final_table_updates`                                                                                                                                                                                                                                           | *Optional[bool]*                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | When enabled your data will load into your final tables incrementally while your data is still being synced. When Disabled (the default), your data loads into your final tables once at the end of a sync. Note that this option only applies if you elect to create Final tables |                                                                                                                                                                                                                                                                                    |
| `jdbc_url_params`                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3).                                                                                   |                                                                                                                                                                                                                                                                                    |
| `port`                                                                                                                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Port of the database.                                                                                                                                                                                                                                                              | 5439                                                                                                                                                                                                                                                                               |
| `raw_data_schema`                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The schema to write raw tables into                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                    |
| `schema`                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The default schema tables are written to if the source does not specify a namespace. Unless specifically configured, the usual value for this field is "public".                                                                                                                   | public                                                                                                                                                                                                                                                                             |
| `tunnel_method`                                                                                                                                                                                                                                                                    | [Optional[Union[models.DestinationRedshiftNoTunnel, models.DestinationRedshiftSSHKeyAuthentication, models.DestinationRedshiftPasswordAuthentication]]](../models/destinationredshiftsshtunnelmethod.md)                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.                                                                                                                                                               |                                                                                                                                                                                                                                                                                    |
| `uploading_method`                                                                                                                                                                                                                                                                 | [Optional[Union[models.AWSS3Staging, models.Standard]]](../models/uploadingmethod.md)                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                 | The way data will be uploaded to Redshift.                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                    |