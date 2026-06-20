---
title: "Assignment command for attributes"
source_id: 8215
source_url: https://wiki.genexus.com/commwiki/wiki?8215
genexus_version: "18"
---

# Assignment command for attributes

Assigns a value to an attribute.

### [Syntax](#Syntax)

*att* operator expression  
  
**Where:**  
  
*att*  
     Attribute to be assigned.  
  
*operator*  
     One of the following assignment operators: = , +=, -=, \*=, /=.

e*xpression*  
     Is any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, arithmetic calculations, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the attribute data type definition.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

Attribute assignments imply a database update.

If you need to assign a value to an attribute within the definition of an object, the object section where the assignment can be defined depends on the object (for example it can be done in [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664)s inside a For each command or in [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) Rules).

The assigned value type must match the attribute type. Otherwise, a warning message will be displayed in the navigation report.

### [Which attributes can be updated?](#Which+attributes+can+be+updated%3F)

* Attributes that belong to the Base Table you are navigating.
* Attritubles that can be inferred because they belong to the extended table of the base table you are navigating.

If the update is done inside a For each command, the update is performed when the Endfor command of the associated group is encountered. Despite this, attributes referenced after an assignment and before the associated Endfor, will contain the last assigned value.

### [Samples](#Samples)

```
Flight
{
   FlightId*
   FlightDate
   FlightPrice
   Flight....
   AirlineId
   AirlineName
}

Airline
{
   AirlineId*
   AirlineName
   AirlineDiscountPercentage
}
```

A Procedure is needed to update all the flight prices.

```
For each Flight        //The base table navigated is FLIGHT
    FlightPrice = FlightPrice  * 1.10
Endfor
```

In this example, is FlightPrice, the base table navigated by GeneXus is: FLIGHT.

Since no filters have been defined, all the table records will be navigated. For each flight, its price is updated and in this case, it's increased by 10%.  
  
Remember that in a single For Each command several physical tables can be updated. A For Each command always has a base table that navigates and can update. However, it can also update the entire extended table of that base table.

In the following example, the base table of the For Each command is FLIGHT. As each flight has one airline, the details of the airline associated with each flight could be changed:

```
For each Flight        //The base table navigated isFLIGHT
     FlightPrice = FlightPrice  * 1.10
     AirlineName = ‘Copa Airlines’
     AirlineDiscountPercentage = 20
Endfor
```

**Notes:**

* It is not valid to assign a value to an attribute when the attribute is part of the index used to scan over the base table. An error will be shown in the navigation list.
* It is not valid to assign a value to an attribute that belongs to a [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062). If you do so, the [spc0212 error](https://wiki.genexus.com/commwiki/wiki?6774) will appear.

* Procedures don’t check the consistency of the data we assign. Since databases check the consistency of interrelated data, when the user runs the application and tries to assign an inconsistent value, the database will reject the operation and the inconsistent data will not be saved. However, the program will stop working and this isn’t very user friendly. Therefore, if you use procedures to update the database, it will be your responsibility to assign valid and well related data.
* Redundancy will notbe automatically maintained when updating the database in Procedures. This maintenance is the programmer's responsibility. That is, if a Redundancy depends on the attribute being updated, GeneXus will not search or calculate data to store it in the redundant attribute.

### [See Also](#See+Also)

[Updating the database using Business Components](https://wiki.genexus.com/commwiki/wiki?5846)  
[Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217)  
[Assignment rule](https://wiki.genexus.com/commwiki/wiki?6847)


|  |
| --- |
| **Backlinks** |
| [Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217) | [Assignment rule](https://wiki.genexus.com/commwiki/wiki?6847) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |

---
