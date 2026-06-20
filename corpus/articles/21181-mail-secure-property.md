---
title: "Mail Secure Property"
source_id: 21181
source_url: https://wiki.genexus.com/commwiki/wiki?21181
genexus_version: "18"
---

# Mail Secure Property

Sets or gets if a [POP3](https://wiki.genexus.com/commwiki/wiki?6966) or [SMTP](https://wiki.genexus.com/commwiki/wiki?6937) connection is secure or not.

The supported protocols are: SSL and TLS.

When using [POP3](https://wiki.genexus.com/commwiki/wiki?6966) and the security property is enabled; the first try is to establish a SSL connection and then a TLS connection.

When using [SMTP](https://wiki.genexus.com/commwiki/wiki?6937) and the security property is enabled; the first try is to establish a TLS protocol; which can be IndirectTLS or DirectTLS. The program will try to connect via Indirect TLS otherwise it will try with a Direct TLS connection and the last option is to try with a SSL connection.

If a secure connection cannot be made an error is displayed.

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | Unsecure protocol is used. This is the default value. |
| **1** | Secure protocol is used. |

### [Example](#Example)

Set protocol to be secure.

```
&smtpSession.Secure = 1
```

### [Scope](#Scope)

**Extended Data Types:**[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) , [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
**Languages:** .NET, Java, Ruby(up to and including GeneXus X Evolution 3)

### [See Also](#See+Also)

[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
