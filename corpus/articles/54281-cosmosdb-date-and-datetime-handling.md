---
title: "CosmosDB date and datetime handling"
source_id: 54281
source_url: https://wiki.genexus.com/commwiki/wiki?54281
genexus_version: "18"
---

# CosmosDB date and datetime handling

## [Date and Datetime values](#Date+and+Datetime+values)

In [Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329), date and datetime values are stored in yyyy-MM-ddTHH:mm:ss.fffZ format, which follows the ISO 8601 UTC standard.

The [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) is ignored, as it **always** uses UTC format. In that regard, the conversion to the local Timezone is always done automatically on the client side.

For external programs that update the datetime values of the database, it is recommended to store the values using the same format.

### [Date and datetime filters](#Date+and+datetime+filters)

Dates and datetimes in JSON are represented as strings. So, for filtering (and ordering) on the server side (filters executed by the database engine), the comparison is done using strings.  
On the server side, the comparison by equal will work only for dates stored in the yyyy-MM-ddTHH:mm:ss.fffZ format.

#### [Java Generator](#Java+Generator)

In the Java generator, when retrieving date values, the following formats are also recognized as dates. This could be useful if external applications stored the data in a different format.

            "yyyy-MM-dd",  
            "MM/dd/yyyy",  
            "EEE, dd MMM yyyy",  
            "EEEE, dd MMMM yyyy",  
            "Month D, Yr",  
            "Yr, Month D",  
            "D Month, Yr",  
            "M/D/YY",  
            "YY/M/D",  
            "Mon-DD-YYYY",  
            "DD-Mon-YYYY",  
            "YYYYY-Mon-DD",  
            "Mon DD, YYYY",  
            "DD Mon, YYYY",  
            "YYYY, Mon DD"

Other date formats are not recognized for retrieving data, and the date will be returned as a null date value.  
Nevertheless, as explained above, take into account that the comparison on the server will only work for the ISO 8601 formatted strings.


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) | [What is Azure Cosmos DB?](https://wiki.genexus.com/commwiki/wiki?53307) |

---
