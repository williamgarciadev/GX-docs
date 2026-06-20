---
title: "When duplicate clause"
source_id: 24843
source_url: https://wiki.genexus.com/commwiki/wiki?24843
genexus_version: "18"
---

# When duplicate clause

Allows to specify the code to be executed when a body of a [For each command](https://wiki.genexus.com/commwiki/wiki?24744) or [New command](https://wiki.genexus.com/commwiki/wiki?6714) is trying to update or create (respectively) a record with a value for a candidate Key (in for each case) and/or primary key (in new case) attribute that has already exists for another record.

It only makes sense in procedures (because it has to do with updates).

### [Syntax](#Syntax)

**When duplicate**

*<CodeWhenDuplicate>*

GeneXus uses the unique index to ensure the uniqueness of that candidate key, as well as the primary index for the primary key. In case it finds duplicates, if this clause is programmed in the For each/New command, it will execute its related code (*<CodeWhenDuplicate>*).

If the clause is not included, and you try to update an attribute that is a candidate key (for each) or assign value to a candidate or primary key (new) and a record with that value already exists, no code will be executed.

About **New command**: most of the times an update of some attributes of that existing record is needed. In these cases a [For each command](https://wiki.genexus.com/commwiki/wiki?24744) is needed. Inside, the attributes to be updated are assigned. Although not so common, other commands can be executed as well. That is:

|  |  |
| --- | --- |
| *<CodeWhenDuplicate>* ::= | [*<AnotherCode>*] |
|  | **For each**       { *<attribute>* = *<expr>*} ...  **endfor** |
|  | [*<AnotherCode>*] |

#### [Note:](#Note%3A)

* **Inside For each**: If another For each command is included into the *<CodeWhenDuplicate>*, and its table has same common attribute with the external For each (that of *<MainCode>)*, this attribute will be considered as instantiated, acting as a filters in the When Duplicate For each.

For more detailed information for each command, see the sintax section in [For each command](https://wiki.genexus.com/commwiki/wiki?24744), and [New command](https://wiki.genexus.com/commwiki/wiki?6714).

### [Example](#Example)

If the CustomerName attribute is a candidate Key (there exists a unique index) in the Customer table, and we are trying to update it for many records accessed by means of a for each:

```
for each Customer

    CustomerName = &customer

when duplicate

    msg( ' The customer ' + &customer + 'already exists')

endfor
```

when there already exists a record with the value contained in &customer, the For each main code is not executed. Instead, the when duplicate code will be executed.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Commands** | [For each command](https://wiki.genexus.com/commwiki/wiki?24744), [Xfor each command](https://wiki.genexus.com/commwiki/wiki?8596), [New command](https://wiki.genexus.com/commwiki/wiki?6714) |
| **Objects** | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |
|  |  |


|  |
| --- |
| **Backlinks** |
| [For each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [New command](https://wiki.genexus.com/commwiki/wiki?6714) |

---
