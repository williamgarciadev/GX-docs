---
title: "RGB function"
source_id: 8347
source_url: https://wiki.genexus.com/commwiki/wiki?8347
genexus_version: "18"
---

# RGB function

Returns a number representing an RGB color value.

### [Syntax](#Syntax)

**RGB(***Numeric-expression1*, *Numeric-expression2*, *Numeric-expression3***)**

**Where:**  
  
*Numeric-expression1*  
   Number in the range from 0 to 255, inclusively, representing the red component of the color.

*Numeric-expression2*  
   Number in the range from 0 to 255, inclusively, representing the green component of the color.

*Numeric-expression3*  
   Number in the range from 0 to 255, inclusively, representing the blue component of the color.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol, [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Controls that accept a color specification, expecting it to be a number representing an RGB color value. An RGB color value specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

The value of any argument to RGB exceeding 255 is assumed to be 255.

The following table lists a number of standard colors, and the red, green, and blue values they include:

|  |  |  |  |
| --- | --- | --- | --- |
| **Color** | **Red Value** | **Green Value** | **Blue Value** |
| **Black** | **0** | **0** | **0** |
| **Blue** | **0** | **0** | **255** |
| **Green** | **0** | **255** | **0** |
| **Cyan** | **0** | **255** | **255** |
| **Red** | **255** | **0** | **0** |
| **Magenta** | **255** | **0** | **255** |
| **Yellow** | **255** | **255** | **0** |
| **White** | **255** | **255** | **255** |

### [Samples](#Samples)

```
ProdDesc.Backcolor = RGB(255,255,255)
```

ProdDesc is an Edit control and its backcolor is white.

### [See Also](#See+Also)

[Color function](https://wiki.genexus.com/commwiki/wiki?8345)


|  |
| --- |
| **Backlinks** |
| [Color function](https://wiki.genexus.com/commwiki/wiki?8345) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
