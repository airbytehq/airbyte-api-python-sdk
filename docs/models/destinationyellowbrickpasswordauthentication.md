# DestinationYellowbrickPasswordAuthentication


## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        | Example                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `tunnel_host`                                                                                                                      | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | Hostname of the jump server host that allows inbound ssh tunnel.                                                                   |                                                                                                                                    |
| `tunnel_user`                                                                                                                      | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | OS-level username for logging into the jump server host                                                                            |                                                                                                                                    |
| `tunnel_user_password`                                                                                                             | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | OS-level password for logging into the jump server host                                                                            |                                                                                                                                    |
| `tunnel_method`                                                                                                                    | [models.DestinationYellowbrickSchemasTunnelMethodTunnelMethod](../models/destinationyellowbrickschemastunnelmethodtunnelmethod.md) | :heavy_check_mark:                                                                                                                 | Connect through a jump server tunnel host using username and password authentication                                               |                                                                                                                                    |
| `tunnel_port`                                                                                                                      | *Optional[int]*                                                                                                                    | :heavy_minus_sign:                                                                                                                 | Port on the proxy/jump server that accepts inbound ssh connections.                                                                | 22                                                                                                                                 |