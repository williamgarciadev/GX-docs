---
title: "FromString method"
source_id: 12694
source_url: https://wiki.genexus.com/commwiki/wiki?12694
genexus_version: "18"
---

# FromString method

Converts a character data type to the data type of the attribute or variable to which the method is applied.

### [Syntax](#Syntax)

*AttOrVar***.FromString(***character-expression***)**

**Where:**

*AttOrVar*Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375).

*character-expression*  
     Must be a character [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,).  
  
**Type Returned:**  
Data type of the attribute or variable to which the method is applied.

### [Scope](#Scope)

**Data Types:**[Blob](https://wiki.genexus.com/commwiki/wiki?6704), [Boolean](https://wiki.genexus.com/commwiki/wiki?4374), [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371), [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), [Geography](https://wiki.genexus.com/commwiki/wiki?32408), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361), [GUID](https://wiki.genexus.com/commwiki/wiki?31772), [Numeric](https://wiki.genexus.com/commwiki/wiki?6793)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Samples](#Samples)

```
If &GUID <> GUID.FromString("2ac61739-b024-438e-a6e5-e507d8be4667")
   msg("Bad Site Key")
EndIf
```

### [See Also](#See+Also)

[CtoD function](https://wiki.genexus.com/commwiki/wiki?7472)  
[CtoT function](https://wiki.genexus.com/commwiki/wiki?7473)  
[ToString method](https://wiki.genexus.com/commwiki/wiki?7090)


|  |
| --- |
| **Backlinks** |
| [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) | [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472) | [Floating Point Operation Precision property](https://wiki.genexus.com/commwiki/wiki?57658) |
| [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [Language domain](https://wiki.genexus.com/commwiki/wiki?40453) | [Locale domain](https://wiki.genexus.com/commwiki/wiki?40450) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) | [What is a static method](https://wiki.genexus.com/commwiki/wiki?39593) |

---
