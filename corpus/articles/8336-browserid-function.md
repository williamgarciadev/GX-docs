---
title: "BrowserId function"
source_id: 8336
source_url: https://wiki.genexus.com/commwiki/wiki?8336
genexus_version: "18"
---

# BrowserId function

Returns a browser’s identifier.

### [Syntax](#Syntax)

**BrowserId()**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:**   [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The BrowserId function returns a browser identifier:

|  |  |
| --- | --- |
| **Id** | **Description** |
| 0 | Unknown Agent |
| 1 | Internet Explorer |
| 2 | Netscape |
| 3 | Opera |
| 6 | Mozilla Firefox |
| 7 | Chrome |
| 8 | Safari |
| 9 | Edge |

**Note**: The result makes sense only if the object was called directly or indirectly by a Web Panel, or if executing in a Web environment.

### 

### [See Also](#See+Also)

[BrowserVersion function](https://wiki.genexus.com/commwiki/wiki?8337)


|  |
| --- |
| **Backlinks** |
| [BrowserVersion function](https://wiki.genexus.com/commwiki/wiki?8337) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
