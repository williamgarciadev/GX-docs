---
title: "Color function"
source_id: 8345
source_url: https://wiki.genexus.com/commwiki/wiki?8345
genexus_version: "18"
---

# Color function

Returns a number representing an RGB color value.

### [Syntax](#Syntax)

**Color(***gx\_color***)**  
  
**Where:**  
  
*gx\_color*  
     Must be a constant value. It cannot be an attribute or variable.

**Type returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The controls that accept a color specification, expect it to be a number representing an RGB color value. An RGB color value specifies the relative intensity of red, green, and blue, causing a specific color to be displayed.

This function is used instead of the [RGB Function](https://wiki.genexus.com/commwiki/wiki?8347) when the corresponding RGB (red, green, blue) values are not remembered. It converts a valid GeneXus color into an RGB value.

Color abbreviations:

|  |  |
| --- | --- |
| 'WHT' | white |
| 'BLK' | black |
| 'RED' | red |
| 'GRN' | green |
| 'BRW' | brown |
| 'MGN' | magenta |
| 'BLU' | blue |
| 'CYN' | cyan |
| 'YLW' | yellow |
| 'X' | 'no-display' |

### [Samples](#Samples)

```
ProdDesc.Backcolor = Color('BLU')
```

ProdDesc is an Edit control and you want its backcolor to be blue.

### [See Also](#See+Also)

[RGB function](https://wiki.genexus.com/commwiki/wiki?8347)  
[Color rule](https://wiki.genexus.com/commwiki/wiki?8348)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [RGB function](https://wiki.genexus.com/commwiki/wiki?8347) | [SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589) |

---
