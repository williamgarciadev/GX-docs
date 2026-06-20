---
title: "When clause"
source_id: 8629
source_url: https://wiki.genexus.com/commwiki/wiki?8629
genexus_version: "18"
---

# When clause

Specifies when the condition for data retrieval or the order in which data is displayed should be used.

### [Syntax](#Syntax)

*condition* | *order\_attributes…*[ **when** *constraint* ]  
  
**Where:**  
*condition*  
    Any valid logical expression that conditionally filters the data during retrieval.

*order\_attributes*  
    A list of attributes (separated by spaces or commas) that defines the navigation order.

*constraint*  
    Enables the condition or order to be applied.

### [Description](#Description)

The When clause can be specified to restrict a condition for data retrieval or the order in which data is displayed. It may be used in the [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) and in the [Order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,) of the [For each command](https://wiki.genexus.com/commwiki/wiki?24744), [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596) and [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601).  It also applies to [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) conditions and [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) orders.

### [Notes](#Notes)

* Conditional filter conditions are combined using AND. If all corresponding conditions are false, no constraint is applied.
* They only apply to generators that use SQL to access the database.
* To generate a conditional constraint, a Client/Server architecture must be used, and the DBMS must be capable of evaluating the Condition. For example: GeneXus must know how to write the Condition in the language of the DBMS used.
* If it cannot be generated as such—either because the target generator doesn't support it or the condition cannot be written in the DBMS language—it will be converted into a standard filter, replacing WHEN with OR.
* If the constraint includes attributes, they are considered instantiated. For example, the constraint is evaluated before navigation begins and does not change during navigation.
* If none of the constraints are true, and there is no unconditional Order (that is, no When Clause), the navigation order is undefined. In this context, undefined means that no order is indicated. Therefore, the order to be applied may vary across DBMSs, even between executions.
* If more than one constraint is true, the first defined ORDER clause is used. For this reason, that order should be the preferred one for queries.
* Conditional orders are not supported when using Breaks.

### [Examples](#Examples)

#### [Example of a conditional filter:](#Example+of+a+conditional+filter%3A)

```
CustomerName LIKE &CustomerName
       WHEN NOT null(&CustomerName);
```

```
CustomerIDCard >= &CustomerIDCard
       WHEN NOT null(&CustomerIDCard);
```

The previous code is interpreted as follows:

If the &CustomerName variable has a value, GeneXus will apply the filter CustomerName LIKE &CustomerName.  
If the &CustomerIDCard variable also has a value, the filter CustomerIDCard >= &CustomerIDCard will be applied as well, using an AND relationship with the other filters.  
If no variable has a value, no filter will be applied.

#### [Example with orders:](#Example+with+orders%3A)

```
For each CustomerName WHEN NOT null(&CustomerName)
       Order CustomerIDCard WHEN NOT null(&CustomerIDCard)
       ...
EndFor
```

In this For each, navigation will be ordered by CustomerName if the &CustomerName variable has a value.  
If it doesn't, and the &CustomerIDCard variable has a value, the order will be by CustomerIDCard.  
If neither condition is met, navigation will be performed in an undefined order.

```
For each CustomerName WHEN NOT null(&CustomerName)
       Order CustomerIDCard WHEN NOT null(&CustomerIDCard)
       Order CustomerId
       ...
EndFor
```

In the For each from the example, the navigation orders are the same as in the previous one. However, if none of the Conditions are met because an unconditional Order is defined, the navigation will follow the unconditional CustomerId Order.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Commands** | [For each command](https://wiki.genexus.com/commwiki/wiki?24744), [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596), [Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601) |
| **Controls** | [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) |
| **Objects** | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Query object](https://wiki.genexus.com/commwiki/wiki?9026) |
| **Operators** | [Like operator](https://wiki.genexus.com/commwiki/wiki?9991) |
|  |  |

### [See also](#See+also)

[For each command](https://wiki.genexus.com/commwiki/wiki?24744)  
[Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596)  
[Xfor First command](https://wiki.genexus.com/commwiki/wiki?8601)  
[Like operator](https://wiki.genexus.com/commwiki/wiki?9991)


|  |
| --- |
| **Backlinks** |
| [For each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Like operator](https://wiki.genexus.com/commwiki/wiki?9991) | [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
