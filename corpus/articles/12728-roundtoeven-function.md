---
title: "RoundToEven function"
source_id: 12728
source_url: https://wiki.genexus.com/commwiki/wiki?12728
genexus_version: "18"
---

# RoundToEven function

Rounds to even the value of a given numeric expression.

### [Syntax](#Syntax)

**RoundToEven(***numeric-expression*, *nK***)**

**Where:**  
*numeric-expression*  
   Must be a numeric expression.  
  
*nK*   
   Must be a Numeric Constant

**Type Returned:**  
Numeric.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), .NET Mobile (up to GeneXus X Evolution 3)

### [Description](#Description)

This function is different from round. The return value is the number closest to the value of expression, with the appropriate number of decimal places. If expression is exactly halfway between two possible rounded values, the function returns the possible rounded value whose rightmost digit is an even number. (In a round function, also known as round to larger, a number that is halfway between two possible rounded values is always rounded to the larger number.)

**Notes**

* Round to even is a statistically more accurate rounding algorithm than round.
* The round to even is used to a better distribution of the global results in some calculations.
* The nk can be a negative number, the behaviour is the same as 0.

### [Samples](#Samples+)

```
RoundToEven(1.5, 0) = 2       (Round(1.5, 0) = 2) 
RoundToEven(2.5, 0) = 2       (Round(2.5, 0) = 3) 
RoundToEven(2.51, 0) = 3      (Round(2.51, 0) = 3) 
RoundToEven(1.25, 1) = 1.2    (Round(1.25, 1) = 1.3) 
RoundToEven(1.24, 1) = 1.2    (Round(1.24, 1) = 1.2) 
RoundToEven(125.11, -1) = 130 (Round(125.11, -1) = 130) 
RoundToEven(135.11, -1) = 140 (Round(135.11, -1) = 140)
```

### [See Also](#See+Also)

[RoundToEven method](https://wiki.genexus.com/commwiki/wiki?12729)  
[Round function](https://wiki.genexus.com/commwiki/wiki?8486)  
[Round method](https://wiki.genexus.com/commwiki/wiki?12726)


|  |
| --- |
| **Backlinks** |
| [RoundToEven method](https://wiki.genexus.com/commwiki/wiki?12729) |

---
