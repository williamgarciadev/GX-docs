---
title: "Sum, Count, Average formulas"
source_id: 6500
source_url: https://wiki.genexus.com/commwiki/wiki?6500
genexus_version: "18"
---

# Sum, Count, Average formulas

Sum, Count and Average are [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868).

### [Syntax](#Syntax)

{**Sum** | **Count** | **Average**}**(** <*aggregateExpression*>, <*aggregateCondition*>, <*defaultValue*> **)** [**if** <triggeringCondition>]

**Where:**

<*aggregateExpression*>

Is the expression to be aggregated, that is to say, the expression to be summed up, or averaged. It may contain attributes (even formula attributes), constants and variables (variables only are allowed in [inline formulas](https://wiki.genexus.com/commwiki/wiki?6441)).  
  
For Sum and Average, the <aggregateExpression> result data type must be numeric. For Count, the first parameter must be an attribute (not an expression) that belongs to the table in which you need to count records (\*).

<*aggregateCondition*>

Is a combination of a search condition with a [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271) invocation. Both parts are optional:

[<*SearchCondition*>] [**USING** <*DataSelector*> '(' <*Parameter*>1, <*Parameter*>2, <*Parameter*>*n* ')']

<*SearchCondition*>

Is the condition that records must verify to be considered in the aggregation. It may contain attributes, constants and variables (user variables are allowed only in [inline formulas](https://wiki.genexus.com/commwiki/wiki?6441), GeneXus standard variables in [global formulas](https://wiki.genexus.com/commwiki/wiki?6440) and inline formulas).

<defaultValue>

Is the returned value when no records match the <*aggregateCondition*>. It is a constant and it is optional.

<*triggeringCondition*>

Is the condition that determines if the formula must be triggered or not. It is optional. The only attributes allowed are those belonging to the contextual table (that the formula attribute would belong to if it were stored) and its extended.

**Note:** Return value is rounded according to the definition of the attribute or variable which is assigned with the aggregate expression.  
For instance, if you assign AttributeB=Average(AttributeA) having 3 records of AttributeA with values 1, 3 and 1,

* if AttributeB is defined as N(10.5), will have value 1,66667
* if AttributeB is defined as N(7.2), will have value 1,67

(\*) All records are count, even those where the mentioned attribute is null.

### [Samples](#Samples)

Consider the following Transactions:

```
Flight
{
   FlightId*
   FlightDescription
   FlightPrice
   FlightInstanceAveragePrice = Average(FlightInstancePrice, FlightInstanceDate = Today(), 0);
   FlightInstanceTotalPrice = Sum(FlightInstancePrice);
   FlightInstanceCountDate = Count(FlightInstanceNumber) if FlightPrice > 100;
}

FlightInstance
{
   FlightInstanceNumber*
   FlightId
   FlightDescription
   FlightPrice
   FlightInstanceDate
   FlightInstanceNumberOfPassengers
   FlightInstancePrice = FlightPrice if FlightInstanceNumberOfPassengers <= 100;
        FlightPrice * 0.9  if  FlightInstanceNumberOfPassengers > 100 and FlightInstanceNumberOfPassengers < 200;
        FlightPrice * 0.8  otherwise;
FlightInstanceNumberOfPassengers = Count(PassengerName,PassengerName = "Smith",0);
   {
       PassengerId*
       PassengerName
   }
}
```

The above example shows several Aggregate [global formulas](https://wiki.genexus.com/commwiki/wiki?6440) with their associated definitions (note that all the defined formulas are Aggregate formulas except for the FlightInstancePrice formula).


|  |
| --- |
| **Backlinks** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Compound Formulas](https://wiki.genexus.com/commwiki/wiki?5879) |
| [Dynamic Transactions that receive parameters](https://wiki.genexus.com/commwiki/wiki?36732) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems First - Formulas](https://wiki.genexus.com/commwiki/wiki?34250) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) | [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593) |

---
