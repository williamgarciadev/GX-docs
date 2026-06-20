---
title: "OutputIfDetail clause"
source_id: 25409
source_url: https://wiki.genexus.com/commwiki/wiki?25409
genexus_version: "18"
---

# OutputIfDetail clause

To solve the typical situation when you need a collection as output related to a [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082), when each member structure has a header and some lines, that is, a subgroup/child (i.e. all documents with headers and lines, but only for those documents which have lines).

### [Syntax](#Syntax)

```
'['OutputIfDetail']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

### [Samples](#Samples)

```
Documents
{ 
   DocumentHeader [OutputIfDetail]
   {
      DocId
      DocDate
      DocLines
      {
         DocLineId
         DocLineDetail
         DocLineQuantity
      }
   }
}
```


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) |

---
