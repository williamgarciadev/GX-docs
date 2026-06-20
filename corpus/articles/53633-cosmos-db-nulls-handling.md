---
title: "Cosmos DB nulls handling"
source_id: 53633
source_url: https://wiki.genexus.com/commwiki/wiki?53633
genexus_version: "18"
---

# Cosmos DB nulls handling

The way to represent the null value in cosmos DB is by using null (the null value is a supported value for the JSON format) or not instantiating in the JSON (see [here](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/query/working-with-json?source=recommendations#difference-between-null-and-undefined) for more information).  
The second alternative (the undefined value) cannot be modeled in GeneXus.

Therefore, for handling nulls, you should use the [SetNull method](https://wiki.genexus.com/commwiki/wiki?12730) before inserting or updating data. As a result, the value will be inserted as a null JSON value.

**Note**: The [Nullable property](https://wiki.genexus.com/commwiki/wiki?7642) of the attribute must be set to Yes to allow storing null values.

### [Sample](#Sample)

```
new
    MagazineId = "Travel+Leisure"
    magazineTech = false
    MagazineName.SetNull()
endnew
```

`[imagen omitida: wiki id 53634]`

The [IsNull function](https://wiki.genexus.com/commwiki/wiki?2357) evaluated in the database will return only the records with a null value.

```
for each Magazines
where MagazineName.IsNull()

endfor
```

Evaluated on the client (that is, executing an if sentence inside the For Each loop), the [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) will also return true when it finds the null value because GeneXus cannot distinguish one from the other.

## [Handling empty values](#Handling+empty+values)

By using the [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646), the empty value is saved (according to the data type of the attribute).

```
new
    MagazineId = "Food&Wine"
    magazineTech = false
    MagazineName.SetEmpty()
endnew
```

Asking for IsNULL on the client also returns the ​empty values.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

As since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853).


|  |
| --- |
| **Backlinks** |
| [Toc:Cosmos DB](https://wiki.genexus.com/commwiki/wiki?53329) |

---
