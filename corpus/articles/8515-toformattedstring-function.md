---
title: "ToFormattedString function"
source_id: 8515
source_url: https://wiki.genexus.com/commwiki/wiki?8515
genexus_version: "18"
---

# ToFormattedString function

Returns a string that results from applying an attribute/variable picture to its value.

### [Syntax](#Syntax)

**ToFormattedString(** *att* | **&***var* **)**  
  
**Type Returned:**  
Character

### [Scope](#Scope)

**Objects**: [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators**: [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This function receives an attribute or variable as parameter and it returns a string that results from applying the attribute/variable picture to its value.

The function may be applied to attributes/variables of the Numeric, Date, DateTime, Char and VarChar type. In the case of attributes/variables of the Date and DateTime type, the date and hour format returned will depend also on the "Date Format" and "Time Format" property (both of them depend on the language established in the KB).

### [Samples](#Samples)

If you have a variable &Total(10, 2) with Picture "Z,ZZZ,ZZ9.99" and the value is 4395.35, the **ToFormattedString(&Total)** function will return the " 4,395.35" string.

### [See Also](#See+Also)

[ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [ToFormattedString method](https://wiki.genexus.com/commwiki/wiki?12722) |

---
