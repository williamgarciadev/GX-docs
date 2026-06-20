---
title: "Business Component Check method"
source_id: 23401
source_url: https://wiki.genexus.com/commwiki/wiki?23401
genexus_version: "18"
---

# Business Component Check method

Performs the same validations as the [Save method](https://wiki.genexus.com/commwiki/wiki?23229), but without updating the database. It is used when you want to validate data, mainly to get feedback, before actually updating the database.

### [Syntax](#Syntax)

**&***VarBasedOnBC***.Check()**

**Where:**  
*&VarBasedOnBC*  
     Is a variable defined in a GeneXus object, based on a Business Component.

### [Samples](#Samples)

**Specific case: Delete.Check**

In order to validate if a delete action can be performed, the [Allow non-standard functions property](https://wiki.genexus.com/commwiki/wiki?8565) must be set to True.

```
&Country.Load("uru")
&Country.Mode=TrnMode.Delete
&Country.Check()

if &Country.Success()
   msg("Delete check ok", status)
else
   msg("Delete check fails", status)
endif
```

### [See Also](#See+Also)

[Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) |
| [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) |

---
