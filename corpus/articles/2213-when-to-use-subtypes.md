---
title: "When to use Subtypes"
source_id: 2213
source_url: https://wiki.genexus.com/commwiki/wiki?2213
genexus_version: "18"
---

# When to use Subtypes

**Rule of thumb: don't use subtypes unless they are needed.**  
  
[GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) uses the [Universal Relation Assumption](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1870,,) (URA), which says that one attribute has the same name everywhere. For example, the Customer's number is CustomerId in the Customer [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) AND in the Invoice Transaction. However, URA can't be used in the following situations:

* More than one relationship in the same [Transaction](https://wiki.genexus.com/commwiki/wiki?1908).

* Self reference.

* Unnecessary integrity constraints.

* Inheritance.

Therefore, in these cases the use of [Subtype Group object](https://wiki.genexus.com/commwiki/wiki?20206) is mandatory.

### [More than one relationship in the same Transaction](#More+than+one+relationship+in+the+same+Transaction)

The canonical example is the Airport/Flight Transactions relationship. The Flight Transaction has two relationships with the Airport Transaction: one that defines which is the Departure airport and another one for the Arrival airport. The model is:

```
Airport
{
  AirportId*
  AirportName
}

Flight
{
  FlightId*
  DepartureAirportId
  DepartureAirportName
  ArrivalAirportId
  ArrivalAirportName
}

Departure Subtype Group
  DepartureAirportId   subtype of AirportId
  DepartureAirportName subtype of AirportName

Arrival Subtype Group
  ArrivalAirportId     subtype of AirportId
  ArrivalAirportName   subtype of AirportName
```

Note that there exists an alternative design that doesn't need the use of subtypes:

```
Airport
{
  AirportId*
  AirportName
}

Flight
{
  FlightId*
  {
      FlightAirportType* (Arrival or Departure)
      AirportId
      AirportName
  }
}
```

This design isn't very common, probably because is a little more difficult to find both airport at the same time.

### [Self reference](#Self+reference)

Consider an old-style Company where each employee has only one boss. In this case the model is as follows:

```
Employee
{
  EmployeeId*
  EmployeeName
  ManagerId
  ManagerName
}

Subtype Group: Manager 
  ManagerId      subtype of   EmployeeId
  ManagerName    subtype of   EmployeeName
```

### [Unnecessary integrity constraints](#Unnecessary+integrity+constraints)

Consider the following online broker model for tracking stocks:

```
Account
{
  AccountId*
  AccountName
}

Stock
{
  StockId*
  StockName
}

Trade
{
  TradeId*
  TradeTime
  AccountId
  AccountName
  StockId
  StockName
  TradeType  (buy or sell)
  TradeQuantity
  TradePrice
}
```

What the Trade Transaction does is to record all the stocks an account has traded. Now suppose you add a 'Watch List' functionality: creating a set of stocks that an account regularly wants to watch (or 'have in the radar', in stock trading slang). At first sight this can be implemented with the following Transaction:

```
BadWatchList 
{
  AccountId*
  AccountName
  StockId*
  StockName
}
```

The problem with this Transaction is that there is an integrity constraint between the Trade base table and that of BadWatchList, meaning that only the stocks in the watch list can be traded by the account. To avoid this unwelcome side effect, the correct Watch List Transaction is:

```
WatchList
{
  AccountId*
  AccountName
  WatchListStockId*
  WatchListStockName
}

Subtype Group: WatchListStock 
  WatchListStockId      subtype of   StockId
  WatchListStockName    subtype of   StockName
```

Probably a more intuitive way of viewing this case is: given an account it's necessary to track two different sets of stocks, those the account has traded and those the account wants to regularly watch. Since these two sets are not related (one can buy stocks that aren't in the watch list or watch stocks that haven't been traded), two different names for stocks are needed (subtypes).

### [Inheritance](#Inheritance)

Suppose it's necessary to store information about People, Students, and Employees. The point is that all Students are People (even though, some high school teachers would disagree with this proposition) and all Employees are People too (no joke here). The best way to model this situation is to define subtypes for Students and Employees:

```
Person
{
  PersonId*
  PersonName
}

Student
{
  StudentId*
  StudentName
  StudentUniversity
}

Subtype Group: Student 
  StudentId      subtype of   PersonId
  StudentName    subtype of   PersonName

Employee
{
  EmployeeId*
  EmployeeName
  EmployeeDateOfHire
}

Subtype Group: Employee 
  EmployeeId      subtype of   PersonId
  EmployeeName    subtype of   PersonName
```

[People And Organizations Knowledge Base](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1834,,) has a good example of this case.  
  
See [Types of Inheritance](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2214,,) for more info on the subject.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Definition of Subtypes](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/definition-of-subtypes-6104723)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Category:Subtype Group object](https://wiki.genexus.com/commwiki/wiki?20206) |

---
