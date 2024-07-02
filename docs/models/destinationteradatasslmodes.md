# DestinationTeradataSSLModes

SSL connection modes. 
 <b>disable</b> - Chose this mode to disable encryption of communication between Airbyte and destination database
 <b>allow</b> - Chose this mode to enable encryption only when required by the destination database
 <b>prefer</b> - Chose this mode to allow unencrypted connection only if the destination database does not support encryption
 <b>require</b> - Chose this mode to always require encryption. If the destination database server does not support encryption, connection will fail
  <b>verify-ca</b> - Chose this mode to always require encryption and to verify that the destination database server has a valid SSL certificate
  <b>verify-full</b> - This is the most secure mode. Chose this mode to always require encryption and to verify the identity of the destination database server
 See more information - <a href="https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#URL_SSLMODE"> in the docs</a>.


## Supported Types

### `models.DestinationTeradataDisable`

```python
value: models.DestinationTeradataDisable = /* values here */
```

### `models.DestinationTeradataAllow`

```python
value: models.DestinationTeradataAllow = /* values here */
```

### `models.DestinationTeradataPrefer`

```python
value: models.DestinationTeradataPrefer = /* values here */
```

### `models.DestinationTeradataRequire`

```python
value: models.DestinationTeradataRequire = /* values here */
```

### `models.DestinationTeradataVerifyCa`

```python
value: models.DestinationTeradataVerifyCa = /* values here */
```

### `models.DestinationTeradataVerifyFull`

```python
value: models.DestinationTeradataVerifyFull = /* values here */
```

