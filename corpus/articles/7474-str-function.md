---
title: "Str function"
source_id: 7474
source_url: https://wiki.genexus.com/commwiki/wiki?7474
genexus_version: "18"
---

# Str function

Converts a numeric expression into a string.

### [Syntax](#Syntax)

**Str(***Value* [ **,** *Length* [ **,** *Decimals* ] ] **)**  
  
**Where:**  
  
*Value*  
   Is the Numeric [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) to be converted into a string.  
  
*Length*  
   Is a Numeric [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that indicates the total length of the*Value* parameter, including numeric sign and decimal point. If you don't complete this parameter, the default value is 10.  
  
*Decimals*  
   Is a Numeric [expression](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?51320,,) that indicates the number of decimal places you want to convert. If you don't complete this parameter, the default value is 0.

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)

### [Description](#Description)

Returns a character string, aligned to the right, which represents the *Value* in string format.

If you specify fewer decimal places (*Decimal* parameter) than those in the *Value* parameter, the value is rounded.

Constraints:  
0 <= *Length* <= 18

In COBOL the limit for *Decimals* is 2.

**Note**: Insignificant zeros are truncated.

### [Samples](#Samples)

```
Str(1.25) = " 1"
```

Note the blank spaces due to the right alignment.

```
Str(-1.25,10,2) = " -1.25"
```

Note the blank spaces due to the right alignment.

```
Str(-1.25,2,1) = "-1"
```

```
Str(-1.25,5,1) = " -1.3"
```

Note the blank space due to the right alignment.

```
Str(-1.25,5,2) = "-1.25"
```

```
Str(12345678901234.12,13,2) = "*************"
```

```
Str(1234.4,5,1) = " 1234"
```

Here 1234.4 is rounded and the decimal is discarded because it ends up having a zero value.

### [See Also](#See+Also)

[Concat function](https://wiki.genexus.com/commwiki/wiki?8352)  
[Substr function](https://wiki.genexus.com/commwiki/wiki?8527)  
[Val function](https://wiki.genexus.com/commwiki/wiki?8528)


|  |
| --- |
| **Backlinks** |
| [Concat function](https://wiki.genexus.com/commwiki/wiki?8352) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |
| [Substr function](https://wiki.genexus.com/commwiki/wiki?8527) | [Substring method](https://wiki.genexus.com/commwiki/wiki?12713) | [ToNumeric method](https://wiki.genexus.com/commwiki/wiki?12717) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |
| [Val function](https://wiki.genexus.com/commwiki/wiki?8528) |

---
