---
title: "Cosmos DB Functions to be evaluated at the database"
source_id: 53652
source_url: https://wiki.genexus.com/commwiki/wiki?53652
genexus_version: "18"
---

# Cosmos DB Functions to be evaluated at the database

When using functions as filters for your queries, functions evaluated at the server side (by the database) are more performant than those that have to be evaluated at the client side.

At present, the functions to be evaluated by the Cosmos DB engine are as follows:

|  |  |
| --- | --- |
| **CosmosDB function** | **GeneXus function** |
| CONTAINS | Contains |
| STARTSWITH | StartsWith |
| ENDSWITH | EndsWith |
| LENGTH | Length |
| LOWER | ToLower |
| UPPER | ToUpper |
| TRIM | Trim |
| IS\_NULL | IsNull |
| RTRIM | TrimEnd, RTrim |
| LTRIM | TrimStart, LTrim |
| StringToNumber | ToNumeric |

The navigation list gives you information about the filters that have to be evaluated at the client, and you should try to avoid.

`[imagen omitida: wiki id 53654]`

On the other hand, when being evaluated at the server side, you should also consider the index usage of the function you use.

For example, look at the [document](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/query/string-functions#functions) which gives information about the index usage of string functions.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

As since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) |

---
