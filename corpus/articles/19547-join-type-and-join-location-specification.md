---
title: "Join Type and Join Location Specification"
source_id: 19547
source_url: https://wiki.genexus.com/commwiki/wiki?19547
genexus_version: "18"
---

# Join Type and Join Location Specification

When there is a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) (or grid, etc.) that involves a join between several tables, GeneXus automatically determines the Join Type, that is to say, how this Join will be implemented between them ([natural](http://en.wikipedia.org/wiki/Join_%28SQL%29#Natural_join) or [outer](http://en.wikipedia.org/wiki/Join_%28SQL%29#Outer_joins)). In addition, it indicates if it can be solved in the database server or the application server (Join Location).

### [Join Type](#Join+Type)

The type of join is set based on the [nullability of the attributes](https://wiki.genexus.com/commwiki/wiki?7642) that make up a Foreign Key. If the foreign key can be null, an outer (or left) join will be made; otherwise, a natural (or inner) join will be used.

Navigation reports show the "=" symbol for natural joins and the "" symbol for outer joins (see examples below).

#### [Notes](#Notes)

* If the Join Location is solved in the application server, the Join Type will always be Outer.
* For compatibility reasons, exists the [Join Type property](https://wiki.genexus.com/commwiki/wiki?8984,,).

### [Join Location](#Join+Location)

Joins involved in a For Each command (or grid, etc.) can be "solved" in the database server (DBMS) or in the client (Application Server) according to the logic of the generated object. This is what we see in the navigation report as **Join Location: client | server**.

In general, it tries to solve it in the server for performance reasons but there are some exceptions, for instance:

* When the tables that take part in the navigation belong to different Data Stores
* When there is a For Each command that performs an update of an attribute that belongs to the extended table, the join is done on the client-side for all DBMS except SQLserver.

In case multiple tables are joined, Join location will be server if at least two tables are joined in the database server.

Example

Considering the following Transactions:

```
City
{
    CityId*
    CityName
}
```

```
Customer
{
    CustomerId*
    CustomerName
    CityId  (Nullable = No)
}
```

If we have a For Each that joins the two tables:

```
For Each CustomerName  CityName

...

Endfor
```

The detailed navigation will be as follows:

`[imagen omitida: wiki id 19549]`

Note the icon when reading the City table (natural join).

If, instead, it has been set that a Client may not have an assigned city (the CityId foreign key in Customer has the Nullable property set to Yes), the join between the tables will be an outer join:

`[imagen omitida: wiki id 19550]`

As we can see, in both cases the join is performed in the server.


|  |
| --- |
| **Backlinks** |
| [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) |

---
