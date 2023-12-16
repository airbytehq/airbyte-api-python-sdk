# DestinationSftpJSON


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             | Example                                                 |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `destination_type`                                      | [shared.SftpJSON](../../models/shared/sftpjson.md)      | :heavy_check_mark:                                      | N/A                                                     |                                                         |
| `destination_path`                                      | *str*                                                   | :heavy_check_mark:                                      | Path to the directory where json files will be written. | /json_data                                              |
| `host`                                                  | *str*                                                   | :heavy_check_mark:                                      | Hostname of the SFTP server.                            |                                                         |
| `password`                                              | *str*                                                   | :heavy_check_mark:                                      | Password associated with the username.                  |                                                         |
| `port`                                                  | *Optional[int]*                                         | :heavy_minus_sign:                                      | Port of the SFTP server.                                | 22                                                      |
| `username`                                              | *str*                                                   | :heavy_check_mark:                                      | Username to use to access the SFTP server.              |                                                         |