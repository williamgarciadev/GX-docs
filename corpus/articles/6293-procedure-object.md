---
title: "Procedure object"
source_id: 6293
source_url: https://wiki.genexus.com/commwiki/wiki?6293
genexus_version: "18"
---

# Procedure object

Defines a program or routine that implements an algorithm, including database access, data updates, and printing.

### [**Description**](#Description)

A **Procedure** object lets you define non-interactive processes for database queries and updates. It also allows you to generate a PDF file to enable list data on screen or printed copies. As its name suggests, the programming style supported is imperative, although it also contains declarative parts (i.e., the Layout).

Each **Procedure** object contains several selectors:

* **[Source](https://wiki.genexus.com/commwiki/wiki?6664):** This is the main section because the code corresponding to the **Procedure logic** is written here. You have to write the code procedurally (imperative). The sequence for the execution is defined by you (including commands to access/update the database, filtering, evaluating whatever you need, printing, etc.). At the end of the code, [Subroutines](https://wiki.genexus.com/commwiki/wiki?24767) may also be defined to be invoked from the code itself.
* **[Layout](https://wiki.genexus.com/commwiki/wiki?5468):** In this section, you can define the **output presentation**. Not every Procedure is meant to have an output. In other words, if the Procedure prints information, you have to design the corresponding output (the information to be printed along with its format) in this section.
* **[Rules](https://wiki.genexus.com/commwiki/wiki?8262):** Only a few rules can be defined in a Procedure object. For example, the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) to declare the parameters received by the object.
* **Conditions:** In this section, you may define conditions that must match the data to be retrieved (general filters). There are other alternatives to define filters.
* **[Variables](https://wiki.genexus.com/commwiki/wiki?3173):** Like most objects, it also has a section for defining variables, which are local to the object.
* **[Help](https://wiki.genexus.com/commwiki/wiki?9924):** A detailed description can be written for the Procedure, to act as online help for the end user at execution time.
* **[Documentation](https://wiki.genexus.com/commwiki/wiki?6685):** A detailed description of the Procedure can be written to document it.

Like most objects, it also has a [Properties Editor](https://wiki.genexus.com/commwiki/wiki?3160) to configure general aspects of the object.

Summing up, a Procedure object allows:

* [Generating a visual output](https://wiki.genexus.com/commwiki/wiki?5489) (typical listings or reports). Here the [Layout](https://wiki.genexus.com/commwiki/wiki?5468) section is mandatory.
* [Updating the database](https://wiki.genexus.com/commwiki/wiki?6826) (insert, update, delete records of the tables, directly with commands or using [Business Components](https://wiki.genexus.com/commwiki/wiki?5846)).
* Solving complex calculations (Consider the alternative of defining [Formulas](https://wiki.genexus.com/commwiki/wiki?25327)).
* Having a non-structured output (although a Procedure object can have a hierarchical output, it is best and easier to achieve with a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836):

```
Airline
{
  AirlineId*
  AirlineName
}
```

Suppose you need to define a [PDF report](https://wiki.genexus.com/commwiki/wiki?13531) to list the airlines a Travel Agency works with.

The Procedure that implements this requirement could have the following Layout (for a complete explanation go to [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468)):

`[imagen omitida: wiki id 5474]`

The logic must be written in the [Source selector](https://wiki.genexus.com/commwiki/wiki?6664), for example, as follows:

```
Header
    Print Pb_Header
End
For each Airline
    Print Pb_Body
Endfor
```

Here the [Header command](https://wiki.genexus.com/commwiki/wiki?7994) indicates the header that each page of the resulting report will have, the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) is used to access the database, and the [Print command](https://wiki.genexus.com/commwiki/wiki?5479) indicates the name of the [Printblock control](https://wiki.genexus.com/commwiki/wiki?1958) (included in the [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468)) to be printed in the output.

### [Note](#Note)

When a Procedure is set to [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), the generated object will have the prefix "a" in its name as follows: aProcedureName (.Net and Java only).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Procedure object presentation and lists definitions](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/lists-and-for-each-command-to-query-the-database-6104762)  
`[imagen omitida: wiki id 20668]` [Updating with procedure-specific commands. Introduction](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/updating-with-procedure-specific-commands-introduction-6104731)


|  |
| --- |
| **Sub Categories** |
| [Category:Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826) | [Category:Static reports](https://wiki.genexus.com/commwiki/wiki?5489) |

---

|  |
| --- |
| **Pages** |
| [Allow user to cancel processing property](https://wiki.genexus.com/commwiki/wiki?7416) | [Application Icon property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7955,Application+Icon+property,) | [Autocenter Objects in (0,0) Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7434,Autocenter+Objects+in+%280%2C0%29+Property,) |
| [BackColorStyle property](https://wiki.genexus.com/commwiki/wiki?8692) | [Beep on messages property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7406,Beep+on+messages+property,) | [Buyer property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7961,Buyer+property,) |
| [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [Cancel caller execution on error property](https://wiki.genexus.com/commwiki/wiki?36669) | [Cancel Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13327,Cancel+Key+Property,) |
| [Code Blocks](https://wiki.genexus.com/commwiki/wiki?7922) | [Commit on Exit property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7942,Commit+on+Exit+property,) | [Commitment property](https://wiki.genexus.com/commwiki/wiki?7951) |
| [Copy table groups property](https://wiki.genexus.com/commwiki/wiki?7973) | [Copyright property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7960,Copyright+property,) | [Customizable Layout property](https://wiki.genexus.com/commwiki/wiki?24473) |
| [Enable Distributed Transactions property](https://wiki.genexus.com/commwiki/wiki?9243) | [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) | [Execute in new LUW property](https://wiki.genexus.com/commwiki/wiki?8008) |
| [Exit Key Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?13328,Exit+Key+Property,) | [Expand dynamic calls property](https://wiki.genexus.com/commwiki/wiki?8569) | [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011) |
| [Fill property](https://wiki.genexus.com/commwiki/wiki?8722) | [Footer command](https://wiki.genexus.com/commwiki/wiki?7967) | [Footer on last page property](https://wiki.genexus.com/commwiki/wiki?7992) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [General Description of Procedures](https://wiki.genexus.com/commwiki/wiki?7927) | [Generate FOR UPDATE clause property](https://wiki.genexus.com/commwiki/wiki?7952) |
| [Generate Object property](https://wiki.genexus.com/commwiki/wiki?7633) | [Generator property](https://wiki.genexus.com/commwiki/wiki?7957) | [Graphic report output property](https://wiki.genexus.com/commwiki/wiki?9245) |
| [Image property](https://wiki.genexus.com/commwiki/wiki?9846) | [Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946) | [Join management property](https://wiki.genexus.com/commwiki/wiki?7966) |
| [Join Type property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8984,Join+Type+property,) | [Layout Metadata Directory property](https://wiki.genexus.com/commwiki/wiki?24561) | [Location property](https://wiki.genexus.com/commwiki/wiki?7956) |
| [NoPrompt rule](https://wiki.genexus.com/commwiki/wiki?6861) | [Print Blocks](https://wiki.genexus.com/commwiki/wiki?7938) | [Print Using DDSs Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7949,Print+Using+DDSs+Property,) |
| [Private object property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7409,Private+object+property,) | [Procedure Layout](https://wiki.genexus.com/commwiki/wiki?5468) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) |
| [Purpose property](https://wiki.genexus.com/commwiki/wiki?9580) | [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) | [Rules in Procedures](https://wiki.genexus.com/commwiki/wiki?8262) |
| [Standard Functions property at Object level](https://wiki.genexus.com/commwiki/wiki?8013) | [Text report output property](https://wiki.genexus.com/commwiki/wiki?10331) | [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) |

---
