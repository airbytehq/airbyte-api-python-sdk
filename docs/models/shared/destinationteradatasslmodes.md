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

### DestinationTeradataDisable

```python
destinationTeradataSSLModes: shared.DestinationTeradataDisable = /* values here */
```

### DestinationTeradataAllow

```python
destinationTeradataSSLModes: shared.DestinationTeradataAllow = /* values here */
```

### DestinationTeradataPrefer

```python
destinationTeradataSSLModes: shared.DestinationTeradataPrefer = /* values here */
```

### DestinationTeradataRequire

```python
destinationTeradataSSLModes: shared.DestinationTeradataRequire = /* values here */
```

### DestinationTeradataVerifyCa

```python
destinationTeradataSSLModes: shared.DestinationTeradataVerifyCa = /* values here */
```

### DestinationTeradataVerifyFull

```python
destinationTeradataSSLModes: shared.DestinationTeradataVerifyFull = /* values here */
```

