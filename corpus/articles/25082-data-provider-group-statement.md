---
title: "Data Provider Group statement"
source_id: 25082
source_url: https://wiki.genexus.com/commwiki/wiki?25082
genexus_version: "18"
---

# Data Provider Group statement

It is one of the three main components of the [Data Provider output-based declarative language](https://wiki.genexus.com/commwiki/wiki?5309).

It sorts a set of subordinate Elements or other Groups. It may or may not be a collection. GeneXus is intelligent enough to figure out when the Group is a repetitive one and when it is not. With repetitive groups, a group is like a for each, with many of its clauses being valid.

## [Syntax](#Syntax)

```
<GroupName>
  [<GroupProperties>]       
  [From <BaseTrn1>|<BaseTrn.Level1>,...,<BaseTrnN>|<BaseTrn.LevelN>]
  [<Order1>,...,<OrderN>]
  [unique <Att1>,...,<AttN>]...
  [using <DataSelectorName>([<parm1>,...,<parmN>])]...
  [<Input>]
  [<Condition1>,...,<ConditionN>]
  '{'
  <variableStatement> | <elementStatement> | <subgroupElementInsertion> | <groupStatement>...
  '}'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*GroupName*  
           Name of the group in the output, i.e, name of an element of the output SDT o BC.

*GroupProperties*  
Designed to have better control of the Output. It can take one of the following values: [Default](https://wiki.genexus.com/commwiki/wiki?25407), [NoOutput](https://wiki.genexus.com/commwiki/wiki?25408), [OutputIfDetail](https://wiki.genexus.com/commwiki/wiki?25409), [Paging](https://wiki.genexus.com/commwiki/wiki?25410), or [One](https://wiki.genexus.com/commwiki/wiki?25411).

*BaseTrn1|BaseTrn.Level1, ..., BaseTrnN|BaseTrn.LevelN*  
Is a Transaction or Transaction.Level name (or several separated by commas) to be used as the base table to be navigated. Read more in [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418).

[*Order*](https://wiki.genexus.com/commwiki/wiki?6075)*1,...,OrderN*  
         Allows indicating the order in which the query will be returned. As the syntax indicates, you can write many conditional order clauses.

[*unique*](https://wiki.genexus.com/commwiki/wiki?24592)  
          Returns only those records where the set of values of the referred attributes is unique.

*Att1*,...,*AttN*  
It is a list of attributes separated by a comma.

[*using*](https://wiki.genexus.com/commwiki/wiki?5312)  
Allows ordering and filtering according to the criteria set out in the Data selector specified by its name *DataSelectorName.*

*DataSelectorName*  
     Is the name of the [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271).

*parm1, …, parmN*  
     Are variables defined in the called object or attributes.

*Input*  
         When a scan through a collection/array/matrix variable is needed, in order to do something with each item values (from a source other than Database) inside the group body. See [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) for *ForIter* and *ForIn* syntax, and further information.

*Condition1,...,ConditionN*  
Specifies any valid logical expression that conditions the data retrieval. It can be a compound condition, using 'and', 'or' and 'not' logical operators.

*[variableStatement](https://wiki.genexus.com/commwiki/wiki?25413)*  
         They are locally declared variables that can be used to do internal calculations.

*[elementStatement](https://wiki.genexus.com/commwiki/wiki?25103)*An Element is an atomic value in the Data Provider Output which may also be of a SDT data type.

*subgroupElementInsertion*  
 It can be defined as follows: *<SubGroupName>***.Insert(**[*<parm1*>, *<parm2*>, ...] **) .**   
Where *SubGroupName*should be declared as a subgroup, by means of a [Data Provider Subgroup statement](https://wiki.genexus.com/commwiki/wiki?25412).

**Note:** The [Defined By Clause](https://wiki.genexus.com/commwiki/wiki?8358,,) from previous versions of GeneXus (located after *Condition1,...,ConditionN* in syntax), although allowed, becomes meaningless against the [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
   CustomerId
   CustomerName
   CustomerAddress
   CustomerPhone
   CustomerEmail
   CustomerBalance
}
```

And the following [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021):

`[imagen omitida: wiki id 55433]`

The following Data Provider navigates the Customer [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) filtering those customers whose CustomerBalance > 1000. It loads and returns a collection of customers that fulfills the condition:

```
SDTCustomers From Customer
where CustomerBalance > 1000
{
    SDTCustomersItem        
   {
         Code = CustomerId
         Name = CustomerName
   }
}
```

Another sample code is:

```
SDTCustomers From Customer order CustomerName unique CustomerName
using DataSelector1()
{
    SDTCustomersItem    
    {
        Id = CustomerId
        Name = CustomerName
    }
}
```

**Notes:**

* **Order** and **Where** clauses apply to Input attributes, not to SDT Elements. For example: 'Order CustomerName' is valid but 'Order Name' is not. In fact, the order will cause access to the Database.
* The behavior is the same as in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744). This includes the way to determine the base table, and the fact that conditional [order clauses](https://wiki.genexus.com/commwiki/wiki?6075) as well as conditional where clauses are valid. The same happens with the 'USING' [Data Selector](https://wiki.genexus.com/commwiki/wiki?5312) clause and the 'IN' operator used in a where clause (that is, Data Selectors can also be used in a Data Provider group, in the same way, same syntax, as in a For each. See some [Data Selectors in Data Providers examples](https://wiki.genexus.com/commwiki/wiki?6501)).


|  |
| --- |
| **Backlinks** |
| [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) | [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103) |
| [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) | [Data Provider Subgroup statement](https://wiki.genexus.com/commwiki/wiki?25412) | [Data Provider Variable statement](https://wiki.genexus.com/commwiki/wiki?25413) | [Default clause](https://wiki.genexus.com/commwiki/wiki?25407) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) | [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) | [NoOutput clause](https://wiki.genexus.com/commwiki/wiki?25408) |
| [Order clause](https://wiki.genexus.com/commwiki/wiki?6075) | [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) | [Order None clause](https://wiki.genexus.com/commwiki/wiki?8619) | [OutputIfDetail clause](https://wiki.genexus.com/commwiki/wiki?25409) |
| [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) | [Unique clause in Data Providers](https://wiki.genexus.com/commwiki/wiki?24594) | [Use Read Replica property](https://wiki.genexus.com/commwiki/wiki?54189) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) |
| [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
