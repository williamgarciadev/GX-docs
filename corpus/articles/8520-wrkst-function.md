---
title: "WrkSt function"
source_id: 8520
source_url: https://wiki.genexus.com/commwiki/wiki?8520
genexus_version: "18"
---

# WrkSt function

Returns the current Work Station Identification.

### [Syntax](#Syntax)

**WrkSt()**  
  
**Type Returned:**   
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG

### [Description](#Description)

Returns the current Work Station identification. In a PC environment, it returns the name of the machine (using API Windows functions) when the PSTATION environment variable is not set. Otherwise, this variable's value is used. This is the expected behavior whether there is network support or not.

**Note**: In Client Server generator,if the variable PSTATION is not set, the machine identification is considered.

### [See Also](#See+Also)

[UserId function](https://wiki.genexus.com/commwiki/wiki?8518)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [UserId function](https://wiki.genexus.com/commwiki/wiki?8518) |

---
