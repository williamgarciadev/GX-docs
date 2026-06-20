---
title: "Floating Point Operation Precision property"
source_id: 57658
source_url: https://wiki.genexus.com/commwiki/wiki?57658
genexus_version: "18"
---

# Floating Point Operation Precision property

Sets the required precision in floating point operations.

### [Values](#Values)

|  |  |
| --- | --- |
| **Full Decimal Precision** | Uses a decimal floating-point implementation for numbers requiring higher precision than supported by JavaScript. This is the default value. |
| **Javascript Precision** | Uses JavaScript numeric types. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** Generator

### [Description](#Description)

When working with large or decimal numbers, it is important to consider the precision of arithmetic operations. Special cases are when methods such as the [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) are used to convert values and when comparisons between numbers are made.

By setting this property to 'Javascript Precision', you can handle the precision of numeric operations in JavaScript (to influence how floating point values are handled and how they are compared).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).
