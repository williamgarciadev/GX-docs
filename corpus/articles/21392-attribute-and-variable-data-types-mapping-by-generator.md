---
title: "Attribute and Variable Data types mapping by Generator"
source_id: 21392
source_url: https://wiki.genexus.com/commwiki/wiki?21392
genexus_version: "18"
---

# Attribute and Variable Data types mapping by Generator

The mapping between GeneXus data types and the target language data type are the following:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **GeneXus Type** | **Condition** | **C#** | **Java** | **Ruby** | **Wsdl** | **Swift** |
| Numeric(X,0) | X <= 2 | short | byte | byte | byte | Int |
| Numeric(X,0) | X <= 4 | short | short | short | short | Int |
| Numeric(X,0) | X <= 9 | int | int | int | int | Int |
| Numeric(X,0) | X <= 19 | long | long | long | long | Int64 |
| Numeric(X,Y) | Y>0 | decimal | java.math.BigDecimal  double1 | double | double | NSDecimal |
| Character(X) |  | string | String | String | string | String |
| datetime |  | DateTime | java.util.Date | GX::Date | datetime | NSDate |
| date |  | DateTime | java.util.Date | GX::Date | date | NSDate |
| boolean |  | boolean | boolean | boolean | boolean | Bool |
| varchar |  | string | String | String | string | String |
| longvarchar |  | string | String | String | string | String |
| bits |  | string | String | String | string | String |
| audio |  | string | String | String | string | String |
| video |  | string | String | String | string | String |
| GUID |  | Guid | java.util.UUID | GX::UUID |  | GXUUID |

1 - when the [Use decimal arithmetic property](https://wiki.genexus.com/commwiki/wiki?10324) is disabled

### [See Also](#See+Also)

* [Blob mapping](https://wiki.genexus.com/commwiki/wiki?4232)
* [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297)


|  |
| --- |
| **Backlinks** |
| [Calling a GeneXus generated program from other Environments](https://wiki.genexus.com/commwiki/wiki?21387) | [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297) | [What is Azure Cosmos DB?](https://wiki.genexus.com/commwiki/wiki?53307) |

---
