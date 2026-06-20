---
title: "GXGetMLi function"
source_id: 8407
source_url: https://wiki.genexus.com/commwiki/wiki?8407
genexus_version: "18"
---

# GXGetMLi function

Considers a constantas the number of characters per line and the current line*.* It returns the next line of characters.

### [Syntax](#Syntax)

**GXGetMLi(***character***,** *line* **,** *constant***)**  
  
**Where:**

*Character*  
Specifies a long varchar, varchar or char field.

*Lline*  
Line number.

*Constant*  
Specifies the number of characters per *line*.

**Type Returned:**  
Character(Constant)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Considering constant as the number of characters per line, it is able to return the next line of the character field.  
  
**Notes:**

* The font used to display the fields must be non-proportional.
* In order to use these functions, the Knowledge Base “Functions” Property must be set with the value “Allows non-standard functions on saving”.

### [Samples](#Samples)

The following example shows how to print  the attribute attchar splited in lines of 40 characters each.

```
  &nlin = GXMLines(attchar,40)
  &i = 1
  Do While &i <= &nlin
     &txt = GXGetMLi(attchar,&i,40)
     Print txtLines // (print block that prints &txt)
     &i += 1
  EndDo
```

### [See Also](#See+Also)

[Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412)  
[Knowledge Base Preferences](https://wiki.genexus.com/commwiki/wiki?7109)  
[GXMLines function](https://wiki.genexus.com/commwiki/wiki?8408)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Functions that Manage LongVarchar Fields](https://wiki.genexus.com/commwiki/wiki?8412) |
| [GXMLines function](https://wiki.genexus.com/commwiki/wiki?8408) |

---
