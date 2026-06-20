---
title: "WebSessionTimeOut property in GAMSecurityPolicy EO"
source_id: 58396
source_url: https://wiki.genexus.com/commwiki/wiki?58396
genexus_version: "18"
---

# WebSessionTimeOut property in GAMSecurityPolicy EO

Configures the Web Session expiration timeout in minutes.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.**WebSessionTimeOut*** *= Number\_Minutes*

**Where:**

*&GAMSecurityPolicy*  Is a variable based on the GAMSecurityPolicy data type.

*Number\_Minutes*  
   Web Session expiration timeout in minutes.

### [Description](#Description)

By default, this property is set to 0. This means that the session will never expire.

The Web Session Timeout configured in the SecurityPolicy EO has to be less than or equal to the Session Timeout configured in the Web Server.

**Note**: When using the [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), this property is shown with the description "Web Session timeout (minutes)".

### [Samples](#Samples)

The following code is an example where the security policy is loaded and its session timeout is changed:

```
&GAMSecurityPolicy.Load(&Id)  //&Id belongs to GAMKeyNumLong domain
&GAMSecurityPolicy.WebSessionTimeOut = &WebSessionTimeOut //&WebSessionTimeOut is Numeric(4)
```

### [See Also](#See+Also)

[Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [Security Session Management in Applications using GAM](https://wiki.genexus.com/commwiki/wiki?16338) |

---
