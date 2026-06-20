---
title: "Connection Options SFTP"
source_id: 44967
source_url: https://wiki.genexus.com/commwiki/wiki?44967
genexus_version: "18"
---

# Connection Options SFTP

**Note**: These Options are part of [GeneXus SFTP Module](https://wiki.genexus.com/commwiki/wiki?44965) which implements the SSH File Transfer Protocol  - SFTP.

## [SDT SftpOptions](#SDT+SftpOptions+)

### [Properties](#Properties)

* **Host**- Character(100): domain name or IP of the SFTP server.
* **Port**- Numeric(9.0): port number  - Default value: 22.
* **User**- Character(100): registered server user for authentication (without @domain).
* **Password**- Character(100): registered user's password for user/password authentication method.
* **KeyPath**- VarChar(256): absolute local path to the registered private key used to establish the connection.
* **KeyPassword****-**Character(100): password of the encrypted key file indicated on KeyPath property.
* **AllowHostKeyChecking** - Boolean: True if the server's fingerprint will be checked against a known\_hosts file. - Default value: true.
* **KnownHostsPath**- VarChar(256): absolute path of the known\_host file.
* **WhiteList** - [ExtensionsWhiteList](https://wiki.genexus.com/commwiki/wiki?45554) SecurityAPICommons object (Available since GeneXus v16 Upgrade 9)

### [Implementation details](#Implementation+details)

* If a KeyPath is configured, it will automatically try to establish a connection using the private key even when a password is also configured.
* known\_hosts file format must be the OpenSSH defined format. [More information here.](https://www.freebsd.org/cgi/man.cgi?sshd(8)#SSH_KNOWN_HOSTS%09FILE_FORMAT)
* The User is needed when using a private key authentication method.
* If AllowHostKeyChecking is false, it will not check the server identity even if KnownHostsPath is configured. This configuration is not recommended because it allows man-in-the-middle attacks. Use for tests only.
* If AllowHostKeyChecking is true it will not establish a connection to the server if KnownHostsPath is not configured, known\_hosts has an invalid format, or the server fingerprint does not match any of the registered hosts in the mentioned file.
* KeyPath's referenced private keys are base64 encoded files. It is expected to use an Encrypted private key, and use the KeyPassword property to set the key's encryption password. Allowed file extensions: none, .pem, and .key.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
