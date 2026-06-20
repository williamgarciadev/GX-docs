---
title: "Impact Analysis"
source_id: 31023
source_url: https://wiki.genexus.com/commwiki/wiki?31023
genexus_version: "18"
---

# Impact Analysis

When pressing the F5 key, GeneXus examines the impact that the new definitions made in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) will cause the Database. Then, it shows a report called **Impact Analysis** that indicates which additions or structural changes need to be made in the Database. This report also details the SQL Statements that will be executed upon confirmation.

The following image shows an **Impact Analysis** report that informs that a new attribute (CustomerAddress) will have to be added to the CUSTOMER table:

`[imagen omitida: wiki id 31024]`

**Note**: Some symbols will assist you in recognizing certain special situations. For example, a key symbol `[imagen omitida: wiki id 7133]` in the table structure area (right) indicates that the attribute is keys. An exclamation symbol `[imagen omitida: wiki id 7825]` represents a warning.

You can press the “Reorganize” button in order to proceed with the [reorganization](https://wiki.genexus.com/commwiki/wiki?5288), or you can choose to cancel.

The term "Reorganize" refers to making changes to the Database.

When you select to reorganize, GeneXus creates the programs to change the Database and executes them, making the necessary changes. Next, it generates the necessary programs corresponding to the application itself.

In the above image, only one change is shown to be performed to one table, but several changes may be detected and shown to be performed to different tables. Besides, the first time you press the F5 key in a Knowledge Base, the title **"Database** **needs to be reorganized"**is replaced by **"The Database tables will be created"** and the **“Reorganize”** button is replaced by the **"Create"** button.

In some cases, the **Impact Analysis** report may inform that no structural changes need to be made in the Database.

Note that the reorganization script that will be running is saved in ReorganizationScript.txt. This may be useful if a DBA must analyze the script before being executed.


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) |
| [GeneXus for SAP Systems - First Build and Run](https://wiki.genexus.com/commwiki/wiki?34179) | [GeneXus for SAP Systems First Build and Run (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54669) |
| [IAR](https://wiki.genexus.com/commwiki/wiki?18171) | [Impact Database Tables](https://wiki.genexus.com/commwiki/wiki?11088) | [Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847) | [Macroservices and Miniservices systems](https://wiki.genexus.com/commwiki/wiki?55518) |
| [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965) |

---
