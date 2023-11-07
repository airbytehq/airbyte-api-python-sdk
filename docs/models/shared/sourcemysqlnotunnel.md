# SourceMysqlNoTunnel

Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `tunnel_method`                                                                  | [shared.SourceMysqlTunnelMethod](../../models/shared/sourcemysqltunnelmethod.md) | :heavy_check_mark:                                                               | No ssh tunnel needed to connect to database                                      |