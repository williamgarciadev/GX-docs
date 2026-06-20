---
title: "Connection Options FTPS"
source_id: 45278
source_url: https://wiki.genexus.com/commwiki/wiki?45278
genexus_version: "18"
---

# Connection Options FTPS

**Note**: These Options are part of the [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274) that implements the File Transfer Protocol over SSL/TLS  - FTPS.

## [SDT FtpsOptions](#SDT+FtpsOptions+)

### [Properties](#Properties)

* **Host**- Character(100): Domain name or IP of the SFTP server.
* **Port**- Numeric(9.0): Port number  - Default value: 21.
* **User**- Character(100): Registered server user for authentication.
* **Password**- Character(100): Registered user's password.
* **ForceEncryption** - Boolean: Keeps the connection encrypted after login. Default value: true
* **ConnectionMode** - FtpConnectionMode Domain; Sets passive or active connection for file transfer. Default value: PASSIVE
* **EncryptionMode**- FtpEncryptionMode Domain: Defines if Implicit or Explicit mode is used. Default value: EXPLICIT
* **Encoding**- FtpEncoding Domain: Defines the mode for file transfer. Default value: BINARY
* **TrustStorePath** - VarChar(256): Trust store or certificate (PKCS12 format) absolute path.
* **TrustStorePassword** - Character(100): Trust Store or pkcs12 certificate password
* **Protocol** - FtpsProtocol Domain: Defines SSL protocol to be used. Default value: TLS1\_2
* **WhiteList** - [ExtensionsWhiteList](https://wiki.genexus.com/commwiki/wiki?45554) SecurityAPICommons object.

### [Implementation details](#Implementation+details)

* If TrustStorePath is empty, it will accept any certificate without validation.
* A PKCS12 formatted certificate or keystore is expected for the trust store. Allowed file extensions for TrustStorePath are: pfx, p12, pkcs12 or jks for Java. [More information about extensions](https://wiki.genexus.com/commwiki/wiki?43918)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
