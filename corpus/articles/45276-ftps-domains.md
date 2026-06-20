---
title: "FTPS Domains"
source_id: 45276
source_url: https://wiki.genexus.com/commwiki/wiki?45276
genexus_version: "18"
---

# FTPS Domains

**Note**: These domains are part of the [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274) that implements the File Transfer Protocol over SSL  - FTPS.

## [FtpConnectionMode](#FtpConnectionMode)

Available values:

```
ACTIVE, PASSIVE
```

## [FtpEncoding](#FtpEncoding)

Available values:

```
BINARY, ASCII
```

## [FtpEncryptionMode](#FtpEncryptionMode)

Available values:

```
IMPLICIT, EXPLICIT
```

* When using EXPLICIT mode the typically used port is 21.
* When using IMPLICIT mode the typically used port is 990 for the handshake and then changes to port 989 for data transfer.

## [FtpsProtocol](#FtpsProtocol)

Available values:

```
TLS1_0, TLS1_1, TLS1_2, SSLv2, SSLv3
```

* SSLv2 and SSLv3 are included for compatibility reasons but are legacy protocols. SSLv2 is deprecated since 2011 and SSLv3 is deprecated since 2015 for security reasons. These protocols are not secure and their use is not recommended.
* SSLv2 and SSLv3 are available only for Java applications. .Net applications will return the Error Code *FS0014, FS0015* Description *Deprecated protocol, not implemented for .Net.* Net libraries deprecated both protocols and have no implementations for them.
* TLSv1.0 and TLSv1.1 will be deprecated in March 2020. The security of these protocols depends on the cipher selection and client implementations; their use is not recommended.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
