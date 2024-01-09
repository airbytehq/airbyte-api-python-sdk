# SSHTunnelMethod

Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use.


## Supported Types

### NoTunnel

```python
sshTunnelMethod: shared.NoTunnel = /* values here */
```

### SSHKeyAuthentication

```python
sshTunnelMethod: shared.SSHKeyAuthentication = /* values here */
```

### PasswordAuthentication

```python
sshTunnelMethod: shared.PasswordAuthentication = /* values here */
```

