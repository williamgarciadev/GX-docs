---
title: "AfterValidate Triggering event"
source_id: 8282
source_url: https://wiki.genexus.com/commwiki/wiki?8282
genexus_version: "18"
---

# AfterValidate Triggering event

If you add an AfterValidate [triggering event](https://wiki.genexus.com/commwiki/wiki?6840) to a transaction rule, you will be specifying that you want to execute that rule, for each instance of the [level associated to the rule](https://wiki.genexus.com/commwiki/wiki?23108), immediately before the instance is physically saved (inserted, updated or deleted) in the physical table associated to the level. This triggering event hasn't got implicitly a certain operation (insertion, update, deletion) in the database. The execution is when the user has already confirmed and immediately before writing the involved table.

### [Syntax](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) [ IF *condition* ][ **ON AfterValidate**] ;

Where:

*condition*  
         Is any valid logic condition

### [**Example**](#Example)

Let's suppose the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) isn't an option to number automatically a primary key attribute because the user asks for a particular numeration with a certain criterion (with alphanumeric characters). So, we must solve it by programming a procedure object.

To call the numbering procedure, we must define a rule like the following, in the transaction that requires the particular numeration for its primary key (let's suppose the Flight transaction):

FlightId = NextFlightNumber() if Insert on AfterValidate;

It is not important for us in this moment to know the NextFlightNumber procedure code. If we read this rule defined in the Flight transaction, we know:

1. The procedure is returning a value for the primary key
2. The rule is executed if the user is inserting a flight (because of the if insert condition explicitly added to the rule)
3. Immediately before the first level data is inserted as a record in the FLIGHT physical table, the rule is executed  (because of the triggering event: on AfterValidate and the fact that the only referenced attribute in the rule belongs to the first level transaction).

### [Notes](#Notes)

* This rule definition is appropriate because the procedure call is executed before inserting the record in the table. In other words, the insertion has been confirmed by the user, but it has not yet occurred. So the value returned by the procedure is assigned to the FlightId attribute, at the time of writing the Flight record.

* If no attribute were specified in the rule, the first level is assumed to trigger the rule.

### [**Scope**](#Scope)

**Objects** [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)

### [**Compatibility**](#Compatibility)

The After(Confirm) triggering event is maintained for backward compatibility reasons. We highly recommend using the AfterValidate event instead. For further information see Triggering Events.

### [**See also**](#See+also)

[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[Rule Triggering Events](https://wiki.genexus.com/commwiki/wiki?6840)


|  |
| --- |
| **Backlinks** |
| [After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284) | [After function](https://wiki.genexus.com/commwiki/wiki?8321) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [GetOldValue method](https://wiki.genexus.com/commwiki/wiki?12734) | [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) | [Category:Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840) |

---
