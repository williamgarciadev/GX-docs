---
title: "Procedure Source"
source_id: 6664
source_url: https://wiki.genexus.com/commwiki/wiki?6664
genexus_version: "18"
---

# Procedure Source

The Procedure Source is the section where the code corresponding to the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) logic is written.

The programming style is procedural (imperative) so the source will be a succession of statements (commands) where the order is important. The order in which they are specified will be the order in which they are executed, with some exceptions.

E.g.: Suppose you need to define a process to increase (by 15%) the salary of all the employees working for more than ten years in the company.

Considering the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836):

```
Employee
{
  EmployeeId*
  EmployeeName
  EmployeeSalary
  EmployeeSeniority
}
```

To solve the need described above, you can define a Procedure object with the **Source** as follows**:**

```
For each Employee
    where EmployeeSeniority >=10
          EmployeeSalary = EmployeeSalary * 1.15
Endfor
```

As you can see, next to the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) a [Base Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23945,,) is specified (Employee). As a base transaction is the name of the transaction whose related physical table you want to navigate, GeneXus will determine to navigate the Employee physical table (which contains all the information of each company employee, including the attributes EmployeeSeniority and EmployeeSalary). Besides, GeneXus will determine to filter those employees whose seniority exceeds 10 years and then, their salary will be updated, raising it by 15 percent.  
  
As in any imperative language, in the Procedure's **Source** the following types of commands are available:

* Control commands to implement conditional execution: If, Do case,
* Repetitive commands: Do while, For in,
* Ways to invoke another object: Call,
* Sentence to break the iterations in a loop: Exit,
* Sentence to leave the program returning to the caller: Return, etc.

...as well as specific commands with the following objectives:

* Print a printblock defined in the [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468): [Print command](https://wiki.genexus.com/commwiki/wiki?5479)
* Access and/or update the database: [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)  (There is no specific update command; within the same command you read attributes values and you can update them, too).
* Create a new record in a table: [New command](https://wiki.genexus.com/commwiki/wiki?6714)
* Delete records: [Delete command](https://wiki.genexus.com/commwiki/wiki?6828)
* Invoke a subroutine: [Do command](https://wiki.genexus.com/commwiki/wiki?8581), etc.

Subroutines can be defined at the end of the **Source** and invoked from the desired place of the code, using the appropriate command (Do).

It is also possible to write to the database using the [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) concept. See [Update the database directly with commands VERSUS using Business Components](https://wiki.genexus.com/commwiki/wiki?2216).

Sometimes Procedures are needed to print data as well. To learn about printing see [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468).

### [See Also](#See+Also)

[Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924)  
[Source Code Editor](https://wiki.genexus.com/commwiki/wiki?3914)


|  |
| --- |
| **Backlinks** |
| [Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215) | [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238) | [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) |
| [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695) | [Business Component InsertOrUpdate method](https://wiki.genexus.com/commwiki/wiki?31697) | [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) |
| [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Business Component Update method](https://wiki.genexus.com/commwiki/wiki?31696) | [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) | [Table of contents:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) |
| [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Do While command](https://wiki.genexus.com/commwiki/wiki?8582) | [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Header command](https://wiki.genexus.com/commwiki/wiki?7994) | [HowTo: Map Application Users to GAM - Adding a secondary attribute referencing the GAMUser](https://wiki.genexus.com/commwiki/wiki?19643) |
| [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441) | [Inline Formulas outside a contextual table](https://wiki.genexus.com/commwiki/wiki?6442) | [Category:Insert - Function...](https://wiki.genexus.com/commwiki/wiki?6877) | [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) |
| [Print command](https://wiki.genexus.com/commwiki/wiki?5479) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) | [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) | [Table of contents:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |
| [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) | [ToJson method](https://wiki.genexus.com/commwiki/wiki?37817) | [Update the database directly with commands VERSUS using Business Components](https://wiki.genexus.com/commwiki/wiki?2216) |

---
