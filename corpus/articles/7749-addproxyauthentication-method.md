---
title: "AddProxyAuthentication method"
source_id: 7749
source_url: https://wiki.genexus.com/commwiki/wiki?7749
genexus_version: "18"
---

# AddProxyAuthentication method

Authenticates proxy when required.

### [Syntax](#Syntax)

**&**DataType**.AddProxyAuthentication(***Method***,** *Realm***,** *User***,** *Password***)**  
  
**Where:**  
*Method*  
    Must be numeric:

* &DataType.Basic for Basic Authentication.format to Where / Scope
* &DataType.Digest for Digest Authentication.
* 2 for NTLM Authentication.
* 3 for Kerberos Authentication.

*Realm*  
    Name of the realm. It must be string.

* In
  [Java](https://wiki.genexus.com/commwiki/wiki?12258) the realm value is mandatory.
* If [NTLM authentication](https://wiki.genexus.com/commwiki/wiki?11486,,) is used, the realm name is usually the network domain.

*User*  
    Name of the user to authenticate. It must be string.  
  
*Password*  
    User password. It must be string.

### [Scope](#Scope)

**Extended data types:** [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
Ruby (up to GeneXus X Evolution 3),
Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932)


|  |
| --- |
| **Backlinks** |
| [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |

---
