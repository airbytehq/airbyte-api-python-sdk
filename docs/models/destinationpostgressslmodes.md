# DestinationPostgresSSLModes

SSL connection modes. 
 <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
 <b>allow</b> - Chose this mode to enable encryption only when required by the source database
 <b>prefer</b> - Chose this mode to allow unencrypted connection only if the source database does not support encryption
 <b>require</b> - Chose this mode to always require encryption. If the source database server does not support encryption, connection will fail
  <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the source database server has a valid SSL certificate
  <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the source database server
 See more information - <a href="https://jdbc.postgresql.org/documentation/head/ssl-client.html"> in the docs</a>.


## Supported Types

### `models.DestinationPostgresDisable`

```python
value: models.DestinationPostgresDisable = /* values here */
```

### `models.DestinationPostgresAllow`

```python
value: models.DestinationPostgresAllow = /* values here */
```

### `models.DestinationPostgresPrefer`

```python
value: models.DestinationPostgresPrefer = /* values here */
```

### `models.DestinationPostgresRequire`

```python
value: models.DestinationPostgresRequire = /* values here */
```

### `models.DestinationPostgresVerifyCa`

```python
value: models.DestinationPostgresVerifyCa = /* values here */
```

### `models.DestinationPostgresVerifyFull`

```python
value: models.DestinationPostgresVerifyFull = /* values here */
```

