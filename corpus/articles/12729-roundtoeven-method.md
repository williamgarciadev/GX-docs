---
title: "RoundToEven method"
source_id: 12729
source_url: https://wiki.genexus.com/commwiki/wiki?12729
genexus_version: "18"
---

# RoundToEven method

Rounds the value of a given numeric expression to an even number.

### [Syntax](#Syntax)

*Numeric-expression****.*RoundToEven(***nK***)**

**Where:**  
  
*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number the method will be applied to.  
  
*nK*   
   Must be a numeric constant

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:**

[Numeric](https://wiki.genexus.com/commwiki/wiki?6793)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This function is different from the [Round function](https://wiki.genexus.com/commwiki/wiki?8486), as its return value is the number closest to the value of expression, with the appropriate number of decimal places. If the numeric expression is exactly halfway between two possible rounded values, the function returns the possible rounded value whose rightmost digit is an even number. (In a round function, also known as round to larger, a number that is halfway between two possible rounded values is always rounded to the larger number).

If *nK* is a negative number, the RoundToEven method is applied to the integer part of the number.  
  
**Notes:**

* Round to even is a statistically more accurate rounding algorithm than round.
* This method is used for getting a better distribution of the global results in some calculations.

### [Samples](#Samples+)

```
&Val = 1.5
&Val.RoundToEven(0) = 2     // (Round(1.5, 0) = 2) 

&Val = 2.5
&Val.RoundToEven(0) = 2     // (Round(2.5, 0) = 3) 

&Val = 2.51
&Val.RoundToEven(0) = 3     // (Round(2.51, 0) = 3) 

&Val = 1.25
&Val.RoundToEven(1) = 1.2   // (Round(1.25, 1) = 1.3) 

&Val = 1.24
&Val.RoundToEven(1) = 1.2   // (Round(1.24, 1) = 1.2) 

&Val = 125.11
&Val.RoundToEven(-1) = 120  // (Round(125.11, -1) = 130) 

&Val = 135.11
&Val.RoundToEven(-1) = 140  // (Round(135.11, -1) = 140)
```

### [See Also](#See+Also)

[RoundToEven function](https://wiki.genexus.com/commwiki/wiki?12728)  
[Round function](https://wiki.genexus.com/commwiki/wiki?8486)  
[Round method](https://wiki.genexus.com/commwiki/wiki?12726)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [RoundToEven function](https://wiki.genexus.com/commwiki/wiki?12728) |

---
