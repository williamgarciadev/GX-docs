---
title: "Nested For Each commands to implement a Cartesian Product"
source_id: 30876
source_url: https://wiki.genexus.com/commwiki/wiki?30876
genexus_version: "18"
---

# Nested For Each commands to implement a Cartesian Product

This article concerns to retrieve for each record of a table, all the records from another table.

Observe the following [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) structures, and below them, the [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) source:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerEmail
}

Attraction
{
    AttractionId*
    AttractionName
    CategoyId
    CategoryName
}

Category
{
   CategoryId*
   CategoryName
}

For each Attraction
    Print attraction {AttractionName, CategoryName}
    For each Customer
        Print customer {CustomerName, CustomerEMail}
    Endfor
Endfor
```

Given this definition, GeneXus determines that the [base tables](https://wiki.genexus.com/commwiki/wiki?6347) of each [For each](https://wiki.genexus.com/commwiki/wiki?24744) are different, and they haven't got an N-1 direct or indirect relation between them. So, the result obtained is a **Cartesian Product** of these tables: for each record of the main For Each base table, it retrieves all the records of the nested For Each base table.

As GeneXus does not find a 1-N direct or indirect relation between the tables, therefore it does not apply implicit filters to the nested For Each records; that is to say, it performs a Cartesian Product between the tables.

You can establish filters on the data to be retrieved, but they will not be implicit conditions inferred by GeneXus; they will be explicitly specified by you.
