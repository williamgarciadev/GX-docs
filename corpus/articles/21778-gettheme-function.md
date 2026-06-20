---
title: "GetTheme function"
source_id: 21778
source_url: https://wiki.genexus.com/commwiki/wiki?21778
genexus_version: "18"
---

# GetTheme function

Returns the name (not description) of the currently active Theme object.

### [Syntax](#Syntax)

**GetTheme()**

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The most common usage is to set a variable of your own with the currently selected Theme as in the following example.

### [Samples](#Samples)

```
Event Start
    &MyTheme = GetTheme()
    ...
EndEvent
```

Variable &MyTheme holds the value of the currently active Theme. It is also shown as a Combo Box on the screen, letting you select any other Theme available.

### [See Also](#See+Also)

[SetTheme function for Web](https://wiki.genexus.com/commwiki/wiki?21777)


|  |
| --- |
| **Backlinks** |
| [SetTheme function for Web](https://wiki.genexus.com/commwiki/wiki?21777) |

---
