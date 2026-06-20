---
title: "GXMLines function"
source_id: 8408
source_url: https://wiki.genexus.com/commwiki/wiki?8408
genexus_version: "18"
---

# GXMLines function

Returns the number of lines occupied by a field, considering a numeric value.

### [Syntax](#Syntax)

**GXMLines(***Character* **,** *Constant***)**

**Where:**  
  
*Character*  
    Specifies a long varchar, varchar or char field.

*Constant*  
    Specifies a numeric constant.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Considering constant as the number of characters per line, it returns the number of lines occupied by the character field.  
  
**Notes:**

* The font used to display the fields must be non-proportional.
* In order to use these functions the Knowledge Base “Functions” Property must be set with the value “Allows non-standard functions on saving”.

### [Samples](#Samples)

The following example shows how to print  the attribute attchar splited in lines of 40 characters each.

```
&nlin = GXMLines(attchar,40)

For &i = 1 to &nlin
    &txt = GXGetMLi(attchar,&i,40)
    Print txtLines // (print block that prints &txt)
EndFor
```

### [See Also](#See+Also)

[Knowledge Base Preferences](https://wiki.genexus.com/commwiki/wiki?7109)  
[Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412)  
[GXGetMLi function](https://wiki.genexus.com/commwiki/wiki?8407)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412) |
| [GXGetMLi function](https://wiki.genexus.com/commwiki/wiki?8407) |

---
