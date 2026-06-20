---
title: "BrowserVersion function"
source_id: 8337
source_url: https://wiki.genexus.com/commwiki/wiki?8337
genexus_version: "18"
---

# BrowserVersion function

Returns a browser’s description.

### [Syntax](#Syntax)

**BrowserVersion()**  
  
**Type returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The BrowserVersion function returns the description corresponding to the browser’s version (or agent). If the browser used is not recognized (the function BrowserId returned 0), it returns an empty string.

**Note**: It can be used in any GeneXus object. The result makes sense only if the object was called directly or indirectly by a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or if executed in a Web environment.

### [See Also](#See+Also)

[BrowserId Function](https://wiki.genexus.com/commwiki/wiki?8336)


|  |
| --- |
| **Backlinks** |
| [BrowserId function](https://wiki.genexus.com/commwiki/wiki?8336) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |

---
