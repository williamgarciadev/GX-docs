---
title: "SearchResultItem Data Type"
source_id: 7729
source_url: https://wiki.genexus.com/commwiki/wiki?7729
genexus_version: "18"
---

# SearchResultItem Data Type

To store data related to a result hit in a search

### [Syntax](#Syntax)

```
&SearchResultItem.Id
```

### [Properties](#Properties)

|  |  |
| --- | --- |
| Id | Identifier for the document in the index |
| Score | Relevance for the item, given a query. It is greater than 0 and less than or equal to 1, it indicates how closely the document matched the query. Search results are ordered by their score by default. |
| TimeStamp | TimeStamp of the last document indexing. |
| Title | Description Attribute value of the Transaction where the item was found. |
| Type | Document type identifier (for example: "client", "Invoice"). |
| Viewer | URL used to display a retrieval result |

### [Methods](#Methods)

None

### [Scope](#Scope)

**Objects:** Procedures, Reports, Transactions, Web Panels  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3)


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |

---
