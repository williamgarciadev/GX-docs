---
title: "Null function"
source_id: 8421
source_url: https://wiki.genexus.com/commwiki/wiki?8421
genexus_version: "18"
---

# Null function

Returns True if the value of a given attribute or variable is empty.

### [Syntax](#Syntax)

**Null(***Attribute* | *&Variable***)**

**Where:**  
  
*Attribute*Is an[Attribute](https://wiki.genexus.com/commwiki/wiki?7240) that should be able to be evaluated in the context where the function is used (it must belong to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the current [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), it must be instantiated, etc.).

*&Variable*Is aVariable defined in the object where the function is used.

**Type Returned:**  
Boolean (True or False)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generatos:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol, [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns True if the value of the attribute or variable is empty.

### [Samples](#Samples)

Consider the following Transaction:

```
Customer
{
 CustomerId*
 CustomerName
 CustomerAddress
 }
```

Suppose you are asked to query the customers stored with null address. The following [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) solve the requirement:

```
For each Customer
    where Null(CustomerAddress)
          Print Customer      /* The printblock contains the attributes: CustomerId, CustomerName*/
Endfor
```

### [See Also](#See+Also)

[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)  
[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)  
[IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [IsNull function](https://wiki.genexus.com/commwiki/wiki?2357) | [IsNull method](https://wiki.genexus.com/commwiki/wiki?12735) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226) | [SetNull method](https://wiki.genexus.com/commwiki/wiki?12730) |

---
