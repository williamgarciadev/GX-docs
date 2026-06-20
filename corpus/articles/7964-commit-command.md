---
title: "Commit command"
source_id: 7964
source_url: https://wiki.genexus.com/commwiki/wiki?7964
genexus_version: "18"
---

# Commit command

Sets the successful end of a set of database changes.

### [Syntax](#Syntax)

**Commit**

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The Commit command sets the successful end of a set of database changes. The set of database changes between Commit (or [Rollback](https://wiki.genexus.com/commwiki/wiki?7998)) commands is treated as a single unit (called [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963)).  
  
This command assures that the set of changes are all (or none, if any error arises) applied to the Database.

If the [KB](https://wiki.genexus.com/commwiki/wiki?1836) has multiple [Data Stores](https://wiki.genexus.com/commwiki/wiki?7117), the Commit command executes a Commit on every one of them that is active (i.e. where database changes have been performed) at the time the command is executed.

Issuing this command also releases any database locks that have been acquired.

Unless the [Commitment property](https://wiki.genexus.com/commwiki/wiki?7951) has been disabled, GeneXus activates Commitment Control for all [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) and [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) objects. If the [Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,) is set to Yes, it also generates a Commit at the end of each object that updates the database.

The Commit command can be specified anywhere in the program source of [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s. This will force GeneXus to generate a Commit in the source.

When the Commit command is included within a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744), it is always executed just before the EndFor (regardless of where it was included within the For Each sentence).

**Notes:**

* Many DBMSs impose a limit on the number of database changes in a [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963).

Take this into account when designing batch processes that work with a large number of rows. You may need to "break" a big LUW into smaller ones by issuing Commit commands as appropriate.

* Many DBMSs close all open cursors when a Commit is executed.

This is a very important portability issue. You may face this problem in a For Each group that has (or calls an object that has) a Commit command.

* A Commit command in a For Each is always executed just before the EndFor.

No matter where you wrote the Commit command inside a For Each group. If it is executed, an internal flag is set so as to actually perform a Commit to the database just before the EndFor and after performing any Database changes that the For Each may have had.

### [Samples](#Samples)

Given the Invoice [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Invoice
{
  InvoiceId*
  InvoiceDate
  InvoiceAmount
}
```

from which the following table is created in the application database:

```
InvoiceID* 
InvoiceDate
InvoiceAmount
```

suppose you need to perform a Commit each time 10 invoices are deleted.  
  
This could be solved as follows:

```
&i = 0
For each Invoice
    &i = &i + 1
    delete
    If &i = 10
       commit
       &i = 0
    EndIf
EndFor
```

### [See Also](#See+Also)

[Rollback command](https://wiki.genexus.com/commwiki/wiki?7998)  
[Commitment property](https://wiki.genexus.com/commwiki/wiki?7951)  
[Commit on Exit property](https://wiki.genexus.com/commwiki/wiki?7942,,)  
[Confirm Transactions property](https://wiki.genexus.com/commwiki/wiki?7999)


|  |
| --- |
| **Backlinks** |
| [Before Commit, After Commit, Before Rollback and After Rollback Generator properties](https://wiki.genexus.com/commwiki/wiki?8996) | [Business Component Load method](https://wiki.genexus.com/commwiki/wiki?23211) | [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) |
| [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [GAM - Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) |
| [Last Modified Date Time Attribute property](https://wiki.genexus.com/commwiki/wiki?37092) | [Logical Unit of Work (LUW)](https://wiki.genexus.com/commwiki/wiki?7963) | [Rollback command](https://wiki.genexus.com/commwiki/wiki?7998) |

---
