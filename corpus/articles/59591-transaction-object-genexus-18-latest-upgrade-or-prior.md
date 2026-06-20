---
title: "Transaction object (GeneXus 18 latest upgrade or prior)"
source_id: 59591
source_url: https://wiki.genexus.com/commwiki/wiki?59591
genexus_version: "18"
---

# Transaction object (GeneXus 18 latest upgrade or prior)

Describes an object or actor of reality, defining the structure of the database, business rules, and the UI for data manipulation.

### [Description](#Description)

Transactions are the first [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) you create in a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), as they allow you to describe objects or actors of reality. By paying attention to the nouns used by the users when describing their reality and needs, you can identify which Transactions you must create (I.e., Customer, Country, etc.).

Each Transaction contains several selectors.

`[imagen omitida: wiki id 48670]`

|  |  |
| --- | --- |
| **[Structure](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,)** | The Transaction structure allows you to define the attributes or fields that describe the object of reality.  The structure may have one Level or several Levels (nested or parallel). The attributes that belong to the same level will be entered, updated, and deleted together. It is necessary to define, among the attributes making up each level, an attribute or set of attributes, acting as a unique identifier (primary key). |
| **[Web Layout](https://wiki.genexus.com/commwiki/wiki?8057)** | GeneXus automatically creates a Web Layout according to the defined structure. This layout will allow users to add, change, and delete data at runtime. |
| **[Rules](https://wiki.genexus.com/commwiki/wiki?8213)** | This section is used to define specific behavior rules for the Transaction. For example, validations for the entered data, etc. |
| **[Events](https://wiki.genexus.com/commwiki/wiki?8042)** | This section allows you to define events with idle code, which are activated in response to certain actions by the user or the system. |
| **[Variables](https://wiki.genexus.com/commwiki/wiki?7375)** | This section allows you to define variables that will be local to the Transaction (temporary, in memory). |
| **[Help](https://wiki.genexus.com/commwiki/wiki?9924)** | Here you can write help texts, which users will be able to refer to during Transaction runtime. |
| **[Documentation](https://wiki.genexus.com/commwiki/wiki?6685)** | Here you can write technical text, in wiki format, to be used as documentation of the system. |
| **[Patterns](https://wiki.genexus.com/commwiki/wiki?2814)** | Here you can apply Patterns to the Transaction. Patterns allow you to empower your applications by easily adding new features! When you apply a pattern, GeneXus creates all the necessary objects to provide the desired behavior without the need to program them.     **Work With for Web.** You can apply the [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) to the Transaction. The Work With Pattern is one of the best-known and most useful patterns in business applications.     **Work With**. You can apply the [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) to the Transaction. In user interfaces, you frequently find a view that shows a list of items and when one of them is selected, that item's detail is displayed. Sometimes this pattern is called Master-DetailTransaction. |

GeneXus analyzes the Transaction structures and generates the necessary programs to create the database (if it doesn't exist), which will be automatically normalized to third normal form, according to the main theories of relational databases. In other words, GeneXus extracts the knowledge from the Transaction structures to define the physical tables to be created or updated in the database. After that, GeneXus also generates programs (forms with several functionalities) to interact with the database previously created.

### [See Also](#See+Also)

[GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866)  
[Transaction Object Limits](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28747,,)  
[GeneXus Knowledge Base Limits](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?10669,,)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Designing the first Transaction](https://training.genexus.com/en/learning/courses/genexus/v18/core/26354/designing-the-first-transaction-6104673)  
`[imagen omitida: wiki id 20668]` [Transactions with more than one level](https://training.genexus.com/en/learning/courses/genexus/v18/core/26354/transactions-with-more-than-one-level-6104683)
