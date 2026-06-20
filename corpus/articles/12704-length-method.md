---
title: "Length method"
source_id: 12704
source_url: https://wiki.genexus.com/commwiki/wiki?12704
genexus_version: "18"
---

# Length method

Returns the number of characters in a character expression.

### [Syntax](#Syntax)

String**.Length()**

**Where:**  
  
*String*  
   Is an attribute or variable based on the Character/VarChar/LongVarChar data type.  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:** [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),  RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The Length method returns the number of characters in a character expression.

### [Samples](#Samples)

```
&Text = "Length method test"
&Nbr = &Text.Length()        //&Nbr value is: 18
```

```
&Text = " Length method test " 
&Nbr = &Text.Length()        //&Nbr value is: 20
```

```
&Nbr = CustomerName.Length() //&Nbr value will be the number of characters corresponding to the CustomerName attribute content.
```

### [See Also](#See+Also)

[Len function](https://wiki.genexus.com/commwiki/wiki?8436)


|  |
| --- |
| **Backlinks** |
| [ControlValueChanging event](https://wiki.genexus.com/commwiki/wiki?35768) | [Len function](https://wiki.genexus.com/commwiki/wiki?8436) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
