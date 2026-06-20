---
title: "AddAuthentication method"
source_id: 7091
source_url: https://wiki.genexus.com/commwiki/wiki?7091
genexus_version: "18"
---

# AddAuthentication method

Authenticates one user to a domain, using an authentication type.

### [Syntax](#Syntax)

**&**DataType**.AddAuthentication(**Method**,** Realm**,** User**,** Password**)**  
  
**Where:**  
*Method*  
   Authentication type, properties Basic and Digest can be used. It must be numeric where 0 = Basic, 1 = Digest, 2 = NTLM and 3 = Kerberos.

**Note**: In Genexus 15, there's an enum domain (HttpAuthenticationType) that represents the possible values.

*Realm*  
   Name of the realm. It must be a string.  
  
*User*  
   Name of the user to be authenticated. It must be a string.  
  
*Password*  
   Password of the user. It must be a string.

### [Scope](#Scope)

**Extended data types:** [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453).

**Note**: Available for [Apple](https://wiki.genexus.com/commwiki/wiki?14917) since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,)

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) | [OpenAPI import tool](https://wiki.genexus.com/commwiki/wiki?31864) |
| [OpenAPI import tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54370) |

---
