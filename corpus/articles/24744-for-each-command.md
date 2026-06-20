---
title: "For each command"
source_id: 24744
source_url: https://wiki.genexus.com/commwiki/wiki?24744
genexus_version: "18"
---

# For each command

Retrieves a dataset from the database. When used in Procedure objects, besides reading the database, it can also be used to update it.

### [Syntax](#Syntax)

```
For each [BaseTrn1|BaseTrn.Level1,...,BaseTrnN|BaseTrn.LevelN]
         [SKIP NumericExpression COUNT NumericExpression]
         [order Att1,...,AttN [when Condition]]...
         [order none [when Condition]]...
         [using DataSelectorName([parm1,...,parmN])]...
         [unique Att1,...,AttN]...
         [where Condition [when Constraint]]...
         [where [not] Att in DataSelectorName([parm1,...,parmN])]...
         [blocking NumericExpression]
                   MainCode
         [When duplicate
                   [CodeWhenDuplicate]]
         [When none
                   [CodeWhenNone]]
Endfor
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**  
  
*BaseTrn1|BaseTrn.Level1, ..., BaseTrnN|BaseTrn.LevelN*  
Is a Transaction or Transaction.Level name (or several separated by commas) to be used as the base table for the For Each navigation. See more on [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418).

*SKIP*  
Determines the number of records omitted from the output. Skip takes positive values.

*NumericExpression  
S*pecifies the number of records in each block.

*COUNT*  
Determines the number of records that will go to the output. If Count takes the value 0 or less, it means no limit.

[order](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,)  
Allows indicating the order in which the query will be returned. As the syntax indicates, you can write many conditional order clauses.

*Att1,...,AttN*  
It is a list of attributes separated by a comma. Each mentioned attribute must be a knowledge base attribute that may be written with or without round brackets. When an order attribute appears between round brackets, it indicates a descending order for this attribute.

*[when](https://wiki.genexus.com/commwiki/wiki?8629)*  
Specifies when the condition for data retrieval or the order of data displayed will be used.

*Condition*  
Specifies any valid logical expression that conditions the data retrieval. It can be a compound condition, using 'and', 'or' and 'not' logical operators.

*[Order None clause](https://wiki.genexus.com/commwiki/wiki?8619)*  
For cases in which you are not interested in a particular order and want it to remain undefined.

*[using](https://wiki.genexus.com/commwiki/wiki?5312)*  
Allows ordering and filtering according to the criteria set out in the [Data selector](https://wiki.genexus.com/commwiki/wiki?5312) specified by its name *DataSelectorName.*

*DataSelectorName*  
Is the name of the Data Selector.

*parm1, …, parmN*  
Are variables defined in the called object or attributes.

*[Unique](https://wiki.genexus.com/commwiki/wiki?24592)*  
Returns only those records where the set of values of the referred attributes is unique.

*[where](https://wiki.genexus.com/commwiki/wiki?8578)*  
Allows indicating a list of conditions that must be matched by the data in order to be processed within the For each (inside the *MainCode*). The conditions are boolean expressions, simple ones or very complex nested ones.

*Constraint*  
Is a condition that specifies when the where clause will apply.

*Att*  
It is an attribute that must belong to the extended table of the Data Selector base table.

*[blocking](https://wiki.genexus.com/commwiki/wiki?4837)*  
Available in Procedures (when updating/deleting). It indicates the number of records that will constitute a database block, when you are updating or deleting, in order to reduce the number of roundtrips to the DBMS.

*MainCode*  
It is the list of commands.

*CodeWhenDuplicate*  
Available in Procedures, when inside *MainCode* certain attribute is updated (overwritten) and there exists a unique index for it. When you intend to overwrite the record with a previously existing value, this code will be executed instead of *MainCode* for that record. See more on [When duplicate clause](https://wiki.genexus.com/commwiki/wiki?24843).

*CodeWhenNone*  
When there is no data meeting the filter conditions, the *MainCode* commands will not be executed; the *CodeWhenNone* commands will be executed instead. See more on [When None Clause](https://wiki.genexus.com/commwiki/wiki?8603).

**Note**: Even though the [Defined By Clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8358,,) from previous versions of GeneXus (located between *ConditionList* and *BlockingGroup* in syntax) is allowed, it becomes meaningless against the [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418).

### [Description](#Description)

Throughout any application, you may need to retrieve information from the database in a [procedural](http://en.wikipedia.org/wiki/Imperative_programming) way.

For this, GeneXus offers the **For each command** to be used to get a dataset from the database. When used in Procedures, besides reading the database, it can also be used in order to update it.

You can define For each commands in:

* [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664)s
* [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panels](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7387,,) or [Panels](https://wiki.genexus.com/commwiki/wiki?24829) Events
* [Subroutines](https://wiki.genexus.com/commwiki/wiki?24767)

Within a For each command you can define the information you want to read (also write if inside a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerAddress
   CustomerPhone
   CustomerEmail
   CountryId
   CountryName   
}

Country
{
   CountryId*
   CountryName
}
```

Suppose you want to display some information about the customers. To do so, you can define the following [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664):

```
For each Customer   //Customer is the name of the Transaction. So, Customer is the Base Trn of the For each.
    Print Customers 
Endfor
```

"Customers" is the name of the following printBlock defined in the [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468):

`[imagen omitida: wiki id 6022]`

With this For each command (which contains a [Print command](https://wiki.genexus.com/commwiki/wiki?5479) to show customers data) you are indicating you want to query the Customer table as the **Base table** and its **Extended table** to display the code, name and country of each customer in the database.

Every time there is a For each command, you are specifying that you want to get some information from the database and for each record retrieved you want to do something with the associated information (for example: print it).

### [Base table](#Base+table)

So, all for each command by default will navigate one table, which is known as the For each **Base table**. It is the table associated to the Base Transaction. A special case arises when using [more than one base trn](https://wiki.genexus.com/commwiki/wiki?24456).

In the example above, the For each Base table to be navigated is CUSTOMER. And for each navigated customer, his/her country is obtained from the COUNTRY table.

`[imagen omitida: wiki id 24768]`

For any For each command, GeneXus will navigate a **Base table**, but can access all tables that belong to the **Extended table** of that base table, in order to get the necessary information. That is why in the example above the base table is CUSTOMER, but for each customer GeneXus can get its related country (because the COUNTRY table is included in the CUSTOMER's extended table).

### [Extended table](#Extended+table)

Although you can specify a Base Transaction starting point for the search (it is strongly recommended to do so), it is not mandatory:

* When a base Base Transaction is specified, the Base table is directly determined. All attributes mentioned within the For each command code (including the attributes mentioned within the invoked print blocks), will have to belong to the corresponding extended table. If not, warnings will be displayed for each attribute not reachable from the Base table through the Extended table ("Att is not instantiated in group...").

* When not: considering the attributes defined inside the For each (including those mentioned within the invoked print blocks), GeneXus will find out how to retrieve them. How? Finding the least extended table that has all of them, and the base table of that extended table is the one chosen by GeneXus as the For each base table. You don’t need to define which tables they must be obtained from, nor the indexes that must be used to access them. We define which attributes are needed and GeneXus will find out how to retrieve them.

Specifying the Base Transaction, however, it is easier for GeneXus to understand what you want (and make it faster), and for you to be sure you have been clear and on control.

### [Optimizations](#Optimizations)

The boolean expressions in the *where* clause constraint the obtained dataset. However, there is a great difference between a full scan table access and an index-optimized random access.

By applying some rules of logic, GeneXus determines whether the order clause (or the primary key order) is compatible with the *where* boolean expression(s), optimizing the access to the table by using indexes and not doing a full table scan.

This is obviously the desired behavior whenever possible.

See [Conditional Orders and Filters](https://wiki.genexus.com/commwiki/wiki?12566) for further information.

### [Native Mobile and Angular applications](#Native+Mobile+and+Angular+applications)

This command can be used when developing applications for [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451)s or Angular but with some considerations. It can only be used in [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) and [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) and only in the System [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042), this means [Start](https://wiki.genexus.com/commwiki/wiki?8043), [Refresh](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,) and [Load](https://wiki.genexus.com/commwiki/wiki?8188) events.

### [See Also](#See+Also)

[Nested For each commands](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?30865,,)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Lists and For each command to query the database](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/lists-and-for-each-command-to-query-the-database-6104762)


|  |
| --- |
| **Backlinks** |
| [API object - ListCustomers service definition and declaration](https://wiki.genexus.com/commwiki/wiki?50051) | [API object - ListCustomers service definition and declaration (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60073) | [Area method](https://wiki.genexus.com/commwiki/wiki?59377) |
| [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) | [Before connect property](https://wiki.genexus.com/commwiki/wiki?8997) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) |
| [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commit command](https://wiki.genexus.com/commwiki/wiki?7964) | [Comparing the .NET generator with the .NET Framework generator](https://wiki.genexus.com/commwiki/wiki?45778) | [Comparing the .NET generator with the .NET Framework generator (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58039) | [Data Provider Element](https://wiki.genexus.com/commwiki/wiki?25096) |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Category:Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501) |
| [Data Selectors in For each command](https://wiki.genexus.com/commwiki/wiki?5312) | [Category:Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826) | [Delete command](https://wiki.genexus.com/commwiki/wiki?6828) | [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807) |
| [Table of contents:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) | [DynamoDB Support in GeneXus](https://wiki.genexus.com/commwiki/wiki?50498) | [Exit command](https://wiki.genexus.com/commwiki/wiki?8590) |
| [For each Optimizations](https://wiki.genexus.com/commwiki/wiki?26286) | [For In Array/Collection command](https://wiki.genexus.com/commwiki/wiki?8585) | [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) |
| [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [Header command](https://wiki.genexus.com/commwiki/wiki?7994) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) |
| [IsNull function](https://wiki.genexus.com/commwiki/wiki?2357) | [IsNull method](https://wiki.genexus.com/commwiki/wiki?12735) | [Join management property](https://wiki.genexus.com/commwiki/wiki?7966) | [Join Type and Join Location Specification](https://wiki.genexus.com/commwiki/wiki?19547) |
| [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Locking in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45652) | [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) |
| [Maximum workFile lines property](https://wiki.genexus.com/commwiki/wiki?8966) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Multiple Base Transactions in a For each command](https://wiki.genexus.com/commwiki/wiki?24456) | [Nested For Each commands to implement a Cartesian Product](https://wiki.genexus.com/commwiki/wiki?30876) |
| [Nested For each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878) | [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062) | [New command](https://wiki.genexus.com/commwiki/wiki?6714) | [Null function](https://wiki.genexus.com/commwiki/wiki?8421) |
| [OnLineActivate event](https://wiki.genexus.com/commwiki/wiki?12223) | [Order clause (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59376) | [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) |
| [Order None clause](https://wiki.genexus.com/commwiki/wiki?8619) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) | [Order rule (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59581) |
| [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) | [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) | [Return command](https://wiki.genexus.com/commwiki/wiki?31353) |
| [Simple example with DynamoDB](https://wiki.genexus.com/commwiki/wiki?50607) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) |
| [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) | [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) | [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) | [Unique Clause (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?57977) |
| [Use Read Replica property](https://wiki.genexus.com/commwiki/wiki?54189) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) | [What is a subroutine?](https://wiki.genexus.com/commwiki/wiki?24767) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) |
| [When duplicate clause](https://wiki.genexus.com/commwiki/wiki?24843) | [When None Clause](https://wiki.genexus.com/commwiki/wiki?8603) | [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) | [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596) |

---
