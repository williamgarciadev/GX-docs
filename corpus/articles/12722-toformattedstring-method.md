---
title: "ToFormattedString method"
source_id: 12722
source_url: https://wiki.genexus.com/commwiki/wiki?12722
genexus_version: "18"
---

# ToFormattedString method

Returns a string that results from applying an [attribute, variable](https://wiki.genexus.com/commwiki/wiki?6911), [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) [picture](https://wiki.genexus.com/commwiki/wiki?36522) to its value.

### [Syntax](#Syntax)

**&***V**ar***.ToFormattedString()**  
  
**Type Returned:**  
Character

### [Scope](#Scope)

**Objects**: [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911), [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021)  
**Generators**:
[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
[Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This method returns a string that results from applying the [Picture property](https://wiki.genexus.com/commwiki/wiki?36522) to its value.

The method may be applied to [Numeric](https://wiki.genexus.com/commwiki/wiki?6793), [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), [Character](https://wiki.genexus.com/commwiki/wiki?6777), and [VarChar](https://wiki.genexus.com/commwiki/wiki?6778) data types. In the case of [Date](https://wiki.genexus.com/commwiki/wiki?7373) and [DateTime](https://wiki.genexus.com/commwiki/wiki?7370) data types, the date and time format returned will also depend on the [Date format](https://wiki.genexus.com/commwiki/wiki?39441) and [Time format](https://wiki.genexus.com/commwiki/wiki?9227) properties (they both depend on the language set in the KB).

### [Samples](#Samples)

If you have a variable &Total(10, 2) with Picture "Z,ZZZ,ZZ9.99" and the value is 4395.35, the **&Total****.ToFormattedString()** function will return the "4,395.35" string.

### [See Also](#See+Also)

[ToFormattedString function](https://wiki.genexus.com/commwiki/wiki?8515)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [ToFormattedString function](https://wiki.genexus.com/commwiki/wiki?8515) |

---
