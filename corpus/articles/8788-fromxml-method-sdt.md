---
title: "FromXml method - SDT"
source_id: 8788
source_url: https://wiki.genexus.com/commwiki/wiki?8788
genexus_version: "18"
---

# FromXml method - SDT

Receives an XML string from which the SDT is loaded.

### [Syntax](#Syntax)

*[&Boolean =] &SDT.**FromXml(**&String[,&Messages]**)***

**Where:**

*&String*  
    Attribute or variable string

*&SDT*  
    Variable based on an SDT

*&Messages*  
     Variable based on GeneXus's Messages data type. In case of an error, it contains the error information. This Parameter is optional.

**Type Returned:**  
Boolean.  
     It returns False in case of having an error, otherwise, it returns True.

**Note**: Assigning the return value is optional.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258).

### [Description](#Description)

It loads the &SDT structure from the &String variable content. This variable's XML format must be compatible with the SDT's structure.

### [See Also](#See+Also)

[ToXml Method](https://wiki.genexus.com/commwiki/wiki?8789)  
[Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)

####


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [A08:2021 - Software and data integrity failures](https://wiki.genexus.com/commwiki/wiki?50188) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
| [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) | [ToXml method - SDT](https://wiki.genexus.com/commwiki/wiki?8789) |

---
