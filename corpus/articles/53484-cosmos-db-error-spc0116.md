---
title: "Cosmos DB error spc0116"
source_id: 53484
source_url: https://wiki.genexus.com/commwiki/wiki?53484
genexus_version: "18"
---

# Cosmos DB error spc0116

Azure CosmosDB does not support ordering unless an index is defined for the properties of the index.

Taken from [Azure CosmosDB documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/index-overview#types-of-indexes):

**Note**

  An ORDER BY clause that orders by a single property always needs a range index and will fail if the path it references doesn't have one.  
  Similarly, an ORDER BY query which orders by multiple properties always needs a composite index.

If the dataview associated with the transaction you are navigating does not have an appropriate index defined, the following specification error is thrown.

```
error spc0116: Group cannot be ordered by <> in group starting at line.
```

### [Solution](#Solution)

Define an index at the dataview definition, according to the order needed.

The index definition must have the Datastore of type Service in all cases.

`[imagen omitida: wiki id 53535]`

**Note**: GeneXus infers an ordering based on what is explained [here](https://wiki.genexus.com/commwiki/wiki?6075).


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) | [Cosmos DB indexes](https://wiki.genexus.com/commwiki/wiki?55180) | [Cosmos DB Inspector](https://wiki.genexus.com/commwiki/wiki?53475) |

---
