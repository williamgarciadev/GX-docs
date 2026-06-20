---
title: "AuthenticationMethod property (for mails data types)"
source_id: 50349
source_url: https://wiki.genexus.com/commwiki/wiki?50349
genexus_version: "18"
---

# AuthenticationMethod property (for mails data types)

Indicates the authentication type used for verifying the identity with the mail server.

## [Scope](#Scope)

**Level:**Variables based on [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) or [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Syntax](#Syntax)

*&VariableBasedOnPOP3SessionOrSMTPSessionDataType*.**AuthenticationMethod** = Value

## [Values](#Values)

|  |  |
| --- | --- |
| **"XOAUTH2"** | OAuth 2.0 Autentication |
| **"****" (empty string)** | Basic Authentication |

## [Description](#Description)

Indicates the authentication type used for verifying the identity with the mail server. This property is taken into account just when [Authentication](https://wiki.genexus.com/commwiki/wiki?6982) is set to 1. For both values allowed, the secret identity value must be passed in the [Password property](https://wiki.genexus.com/commwiki/wiki?6994) (i.e., the access token for OAuth 2.0, or the password in case of Basic Authentication).

## [Sample](#Sample+)

Consider a &Mail variable based on the [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937).

Then you can set its **AuthenticationMethod property**as shown:

```
Event Start
   &Mail.Authentication = 1
   &Mail.AuthenticationMethod = !"XOAUTH2"
EndEvent
​​​​​
```

## [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at run-time.

## [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,).

## [See Also](#See+Also)

[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)  
[Password property](https://wiki.genexus.com/commwiki/wiki?6994)  
[Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982)


|  |
| --- |
| **Backlinks** |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
