---
title: "Return command"
source_id: 31353
source_url: https://wiki.genexus.com/commwiki/wiki?31353
genexus_version: "18"
---

# Return command

Ends the execution and returns to the caller program.

### [Syntax](#Syntax)

**Return**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [WorkWith](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This command forces the running program to stop and return to the caller.

When the Return command is used within a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), you must consider that the database updates are not made when the assignment is performed, but immediately before the Endfor.

Consider the generic code given below:

```
For each
    att = value
    If <condition_is_true>
        Return    //consider that if you define this, att is not updated in the database yet
    Endif
EndFor
```

When the condition is satisfied and the Return command is executed, the attribute is not modified in the database yet (because the database update is performed just before the Endfor).

Below is a particular example to solve this scenario.

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Supplier
{
    SupplierId*
    SupplierName
    SupplierPhone
    SupplierEmail
    SupplierReviewed
}
```

And the following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293):

```
CheckSupplier Procedure
Rule: Parm(in:&SupplierId, out:&Flag);

Source:

&Flag = 0
For each Supplier
    where SupplierId = &SupplierId
          SupplierReviewed = 'Y'
          &Flag = 1       
EndFor
If &Flag = 1
    Return
EndIf
```

### [See Also](#See+Also)

[HowTo: Return from a Panel to the caller Panel in Native Mobile Apps](https://wiki.genexus.com/commwiki/wiki?59817)


|  |
| --- |
| **Backlinks** |
| [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [Composite examples](https://wiki.genexus.com/commwiki/wiki?15551) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853) |
| [For In Array/Collection command](https://wiki.genexus.com/commwiki/wiki?8585) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) | [HowTo: Return from a Panel to the caller Panel in Native Mobile Apps](https://wiki.genexus.com/commwiki/wiki?59817) |

---
