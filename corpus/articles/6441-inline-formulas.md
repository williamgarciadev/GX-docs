---
title: "Inline Formulas"
source_id: 6441
source_url: https://wiki.genexus.com/commwiki/wiki?6441
genexus_version: "18"
---

# Inline Formulas

An Inline [Formula](https://wiki.genexus.com/commwiki/wiki?5861) is a local formula defined within an object code (for example in the middle of a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664), in an object [subroutine](https://wiki.genexus.com/commwiki/wiki?24767), in a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) statement, etc.).

In other words, a formula can be locally assigned to an attribute or variable, as a sentence or statement in the middle of the code, or in a where clause, etc.

### [Syntax](#Syntax)

*<variable>|<attribute>* **=** *<UnconditionalFormula>*} | *<UnconditionalFormula>*

An inline formula (*<UnconditionalFormula>*)*,* can be either [horizontal](https://wiki.genexus.com/commwiki/wiki?5864) or [aggregate](https://wiki.genexus.com/commwiki/wiki?5868).

The main difference regarding [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) is that inline may not consist of several **conditional** expressions, not even a single conditional one. In addition, in any inline formula, variables could be involved in the expression (because the formula does only exists in this local piece of code where the variable is known).

Whereas you really don't know all the places where a global formula is going to be triggered. This is the meaning of "global". It can be used everywhere an attribute of the corresponding base table is allowed)

While [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) always have a table in its context (the table where the formula attribute would be stored if it were not virtual), inline formulas do not have to. For what kind of formulas? Those that don't need context to be evaluated: [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868).

### [Why the context is meaningful?](#Why+the+context+is+meaningful%3F)

Because it will affect the calculation result, allowing to add filtering conditions to the data considered.

### [Example](#Example)

Assume you have a FlightInstance [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to store a real flight from one country/city to another, with a second level, FlighInstanceSeat, to store the passengers of the flight. Suppose a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) needs to know at the beginning if there already are more than 100 seats assigned to passengers in the corresponding table.

```
   &success = Count(FlightInstancePassengerSeatNumber) > 100
```

Here there is no context table for the formula. It is triggered isolated, counting all the records of its base table, FlightInstanceSeat. It will count all the passengers for all the flight instances stored.

On the other hand, if the above code were inside a for each command, such as:

```
   for each FlightInstance
   where Count( FlightInstancePassengerSeatNumber) > 100
      print flightInstanceInfo //FlightInstanceNumber, FlightInstanceDate
   endfor
```

The formula does have a context: the FlightInstance table, the base table of the For each. Thus, not all the passenger seats were going to be counted, but only those corresponding to each FlightInstance record considered in each "for each" iteration. So, only the flights with more than one hundred passengers will be printed in the output.

If you had defined a global formula attribute *FlightInstanceNumberOfPassengers* at FlightInstance transaction level, you could have defined equivalently as follows:

```
   for each FlightInstance
   where FlightInstanceNumberOfPassengers > 100
      print flightInstanceInfo //FlightInstanceNumber, FlightInstanceDate
   endfor
```

Furthermore, if there is a contextual table, all the attributes of its extended table could be used inside the formula, as known. For example, having a variable &fromDate previously loaded:

```
   for each FlightInstance
   where Count( FlightInstancePassengerSeatNumber, FlightDate >= &fromDate) > 100
      ...
   endfor
```

### [Note](#Note)

Inline formulas that are [horizontal](https://wiki.genexus.com/commwiki/wiki?5864) **always have a context table**: at least its own base table. It is exactly the same as horizontal global formulas. Thus, they can not be specified without a context where the attributes could assume value.

For example:

```
   &age = &today.Year() - PassengerBirthDate.Year()
```

this assignment isolated makes no sense. What passenger birth date are you talking about? The situation would be different if this assignment were:

```
for each FlightInstanceSeat
    &age = &today.Year() - PassengerBirthDate.Year()
   ...
endfor
```

Here GeneXus infers the passenger is that of each "for each" iteration, that is, that associated with the for each base table record where you are positioned each time. The "for each" navigates the table that stores the passengers assigned to seats: FlightInstanceSeat. Note in this case the context table, FlightInstanceSeat, is not exactly the base table of the formula, Passenger, but the former contains in its [extended](https://wiki.genexus.com/commwiki/wiki?6029) the latter.

So, inline formulas can be defined according to their context:

* [Within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426)
* [Outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Inline Formulas](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/inline-formulas-6104764)


|  |
| --- |
| **Backlinks** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215) | [Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217) |
| [Data Provider Element](https://wiki.genexus.com/commwiki/wiki?25096) | [Data Provider Element statement](https://wiki.genexus.com/commwiki/wiki?25103) | [Find Formula](https://wiki.genexus.com/commwiki/wiki?6547) | [Category:Formulas](https://wiki.genexus.com/commwiki/wiki?5861) |
| [Toc:Formulas](https://wiki.genexus.com/commwiki/wiki?25327) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems First - Formulas](https://wiki.genexus.com/commwiki/wiki?34250) | [Horizontal Formulas](https://wiki.genexus.com/commwiki/wiki?5864) |
| [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) | [Max, Min Formulas](https://wiki.genexus.com/commwiki/wiki?6502) | [Sum, Count, Average formulas](https://wiki.genexus.com/commwiki/wiki?6500) |
| [TAdd function](https://wiki.genexus.com/commwiki/wiki?8512) | [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) | [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) | [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593) |
| [Upper function](https://wiki.genexus.com/commwiki/wiki?8466) | [Using Read Replicas in GeneXus](https://wiki.genexus.com/commwiki/wiki?54289) | [Val function](https://wiki.genexus.com/commwiki/wiki?8528) |
| [Year function](https://wiki.genexus.com/commwiki/wiki?8380) |

---
