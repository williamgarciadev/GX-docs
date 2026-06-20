---
title: "Dynamic Transactions that update data"
source_id: 28656
source_url: https://wiki.genexus.com/commwiki/wiki?28656
genexus_version: "18"
---

# Dynamic Transactions that update data

By default, [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) are defined with its [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) = Read Only. Therefore, the data is queried at runtime and the Transaction form doesn't allow updating, inserting, or deleting data.

However, the ability to allow data to be updated is useful in some scenarios.

To define a [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062) that allows data updates, set the following Transaction properties:

* [Data Provider](https://wiki.genexus.com/commwiki/wiki?29597) = True
* [Used To](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data
* [Update Policy](https://wiki.genexus.com/commwiki/wiki?29599) = Updatable

In addition, complete the [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) that is automatically created as a consequence of having set [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True.

Below is an interesting scenario that proposes the use of a Dynamic Transaction that allows data updates. 

Consider a GeneXus [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) for tracking body weight, with the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Person
{
   PersonId*
   PersonName
   GenderId
   GenderName 
}
```

```
Gender
{
   GenderId*
   GenderName
   GenderMembers = count(PersonName)
}
```

```
WeightLog
{
   PersonId*
   WeightLogDate*
   WeightLogKilos
}
```

Now suppose that, with the system already up and running, people want to track not only their weight but also other body measurements (like chest or waist circumference). The database model needs to be redesigned to store this new data. Of course, it's possible to create a new Transaction object for each new measurement to be tracked, but a better (and more extensible) design is to have just one Transaction for any kind of measurement:

```
MeasureLog
{
   PersonId*
   MeasureId*
   MeasureLogDate*
   MeasureLogValue
}
```

Together with a Measure Transaction:

```
Measure
{
   MeasureId*
   MeasureName
}
```

Its [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True, its  [Used To property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data, its [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) = Read Only, and its associated Data Provider is:

`[imagen omitida: wiki id 29649]`

The WeightLog transaction is no longer necessary since all measurements will be stored in the physical table associated with the new MeasureLog transaction. However, the application code still references it as [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) in many places, such as For Each statements. So, instead of removing the WeightLog transaction and modifying it everywhere it is referenced, turn it into a [Dynamic Transaction](https://wiki.genexus.com/commwiki/wiki?28062).

For that purpose, you have to:

1. "Turn on" the WeightLog [Data Provider property](https://wiki.genexus.com/commwiki/wiki?29597) = True
2. Set the WeightLog  [Used to property](https://wiki.genexus.com/commwiki/wiki?29584) = Retrieve Data
3. Complete the Data Provider that was automatically created and named "WeightLog\_DataProvider", as shown in the following image:

`[imagen omitida: wiki id 29650]`

With these definitions, the WeightLog Transaction can still be used in queries exactly as before (no code changes are needed to any For Each statement that references it, and its attributes can be kept in grids, printblocks, etc.). **However, do not forget that if you define a transaction as Dynamic, the associated physical tables will no longer exist. So, before proceeding with this proposal, you have to move the data** (in this case, weights from WeightLog to MeasureLog table).

What about **updates**? The user is used to executing the WeightLog Transaction form so they can use both: the MeasureLog and the WeightLog transactions.

By setting the WeightLog Transaction [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) = Updatable, its Form will allow the user to edit the data; but in which physical table will the updates be stored?

You have to codify the Insert, Update, and Delete events in the WeightLog Transaction Events section to specify their intention. In this example, the logical solution is to store the data in the MeasureLog physical table, using the [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) concept as follows:

```
Event Insert(&Messages)
    &MeasureLog = new()
    &MeasureLog.PersonId        = PersonId
    &MeasureLog.MeasureId       = 1
    &MeasureLog.MeasureLogDate  = WeightLogDate
    &MeasureLog.MeasureLogValue = WeightLogKilos
    &MeasureLog.Insert()
    &Messages = &MeasureLog.GetMessages()
Endevent

Event Update(&Messages)
    &MeasureLog.Load(PersonId, 1, WeightLogDate)
    &MeasureLog.MeasureLogValue = WeightLogKilos
    &MeasureLog.Update()
    &Messages = &MeasureLog.GetMessages()
Endevent

Event Delete(&Messages)
    &MeasureLog.Load(PersonId, 1, WeightLogDate)
    &MeasureLog.Delete()
    &Messages = &MeasureLog.GetMessages()
Endevent
```

Note that after applying the Insert(), Update() and Delete() methods, respectively, to the &MeasureLog business component variable, you obtain the messages and/or errors triggered (in the &Messages collection variable). By setting the &Messages variable as a parameter in each event (as shown), those messages are displayed in the WeightLog Dynamic Transaction in a transparent way, like its own messages.

In this way, the WeightLog Dynamic Transaction can be used **in the same way as before** and no changes to dependent programs are necessary. This also applies if the transaction is used as [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) because it is a Dynamic Transaction that allows updates and the corresponding events to store the data are codified.

### Considerations

Some considerations must be taken into account to use this feature:

* This feature is not available for multi-level dynamic transactions.
* If you are using MySQL, version 5.7.7 or higher is required.
* Informix and SQLite do not support this kind of Transaction.
* To prototype Java applications in the cloud, use [apps6.genexus.com](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26157,,)

###


|  |
| --- |
| **Backlinks** |
| [Automatic data population associated with Transactions - FAQ](https://wiki.genexus.com/commwiki/wiki?31018) | [Table of contents:Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062) |
| [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) | [Update Policy property](https://wiki.genexus.com/commwiki/wiki?29599) |

---
