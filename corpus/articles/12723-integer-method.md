---
title: "Integer method"
source_id: 12723
source_url: https://wiki.genexus.com/commwiki/wiki?12723
genexus_version: "18"
---

# Integer method

Returns the integer part of a Numeric-expression.

### [Syntax](#Syntax)

*Numeric-expression***.Integer(****)**  
  
**Type Returned:**  
Numeric  
  
**Where:**  
  
*Numeric-expression*   
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number the method will be applied to.

### [Scope](#Scope)

**Data Types:** [Numeric](https://wiki.genexus.com/commwiki/wiki?6793)

### [Description](#Description)

This function returns an integer value, representing the integer part of a received parameter.

### [Samples](#Samples)

```
&Val = 5/3
&IntVal = &Val.Integer() // Result &IntVal: 1

&Val = -1.75
&IntVal = &Val.Integer() // Result &IntVal: -1

&Val = 1.5
&IntVal = &Val.Integer() // Result &IntVal: 1
```

### [See Also](#See+Also)

[Int function](https://wiki.genexus.com/commwiki/wiki?8418)


|  |
| --- |
| **Backlinks** |
| [Int function](https://wiki.genexus.com/commwiki/wiki?8418) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
