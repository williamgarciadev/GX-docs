---
title: "AuthenticationMethod Property"
source_id: 6990
source_url: https://wiki.genexus.com/commwiki/wiki?6990
genexus_version: "18"
---

# AuthenticationMethod Property

Indicates the server authentication method, if used.

### [Syntax](#Syntax)

**&***DataType***.AuthenticationMethod**  
  
**Type Returned:**   
Numeric

### [Values](#Values)

**0:** Basic authentication: the user and password are sent without encrypting them. This is the default value.  
**1:** Digest authentication: the user and password are sent encrypted.  
**2:** NTLM authentication: the user and password are sent using the NTLM protocol.  
**3:** Kerberos authentication: the user and password are sent using Kerberos specifications, the sucessor of NTLM protocol.

### [Description](#Description)

When you make a SOAP call using authentication, this property indicates which type of authentication will be used.

NTLM value is not implemented in Java generator.

### [Scope](#Scope)

**Extended Data Types:**[Location](https://wiki.genexus.com/commwiki/wiki?6981)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3),  Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Location Data Type](https://wiki.genexus.com/commwiki/wiki?6981)  
[Locations](https://wiki.genexus.com/commwiki/wiki?6981)  
[Authentication](https://wiki.genexus.com/commwiki/wiki?6982)


|  |
| --- |
| **Backlinks** |
| [Authentication Property](https://wiki.genexus.com/commwiki/wiki?6982) | [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) |

---
