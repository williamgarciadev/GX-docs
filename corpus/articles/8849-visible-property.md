---
title: "Visible property"
source_id: 8849
source_url: https://wiki.genexus.com/commwiki/wiki?8849
genexus_version: "18"
---

# Visible property

Determines whether a control is visible or hidden.

### [Syntax](#Syntax)

**control.** Visible

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [All](https://wiki.genexus.com/commwiki/wiki?5925)

### [Description](#Description)

To hide a control, set its **Visible property** to False or 0.

Once a control has been hidden (controlName.Visible = 0) it stays this way until you make it visible again (controlName.Visible = 1).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
   CustomerId*
   CustomerName
   CustomerAddress
   CustomerEmail
   CustomerPhoto
}
```

To show or hide the Customer’s photo, depending on the customer's category, you have to define the following rules:

```
CustomerPhoto.Visible = 0 if CategoryId = 2;
CustomerPhoto.Visible = 1 if CategoryId <> 2;
```


|  |
| --- |
| **Backlinks** |
| [Chronometer Control](https://wiki.genexus.com/commwiki/wiki?25058) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |
| [Invisible Mode property](https://wiki.genexus.com/commwiki/wiki?22743) | [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) | [Show Application Bars property](https://wiki.genexus.com/commwiki/wiki?23305) |

---
