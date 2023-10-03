# SourceSftpAuthenticationWildcardSSHKeyAuthentication

The server authentication method


## Fields

| Field                                                                                                               | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `auth_method`                                                                                                       | *Optional[str]*                                                                                                     | :heavy_check_mark:                                                                                                  | Connect through ssh key                                                                                             |
| `auth_ssh_key`                                                                                                      | *Optional[str]*                                                                                                     | :heavy_check_mark:                                                                                                  | OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa ) |