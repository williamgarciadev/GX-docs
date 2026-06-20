---
title: "Workflow Data Types: Programming best practices"
source_id: 23318
source_url: https://wiki.genexus.com/commwiki/wiki?23318
genexus_version: "18"
---

# Workflow Data Types: Programming best practices

The main purpose of this document is to establish best programming practices when using the [Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240).

The first and main thing to consider is that, when we use any Workflow Data Type exclusively, GeneXus will not commit automatically. This means that Workflow Data Types don´t commit when used, so every time we resort to *Workflow Data Types* for updating, we must commit all changes. It's also very important to consider the [LUW](https://wiki.genexus.com/commwiki/wiki?2424) when we use Workflow Data Types and commit, so that changes are applied correctly in our application.

* In order to ensure data consistency when we program and use Workflow Data Types, we must use the same LUW as the application.  
  For example**:** to perform an action after entering a Transaction, this should not be programmed in the After TRN event, but rather contained in its LUW.

* We should never commit from batch tasks, conditions, multi-instance expression procedures, or event handlers. In such cases, Committing is a responsibility of those using the Workflow Data Types. This will ensure that (in the event of possible flaws) a rollback will be placed, with all actions that have taken place.  
  For example: we use Workflow Data Types to complete a [Workitem](https://wiki.genexus.com/commwiki/wiki?11731). If the Application defined on this Workitem commits, then the actions defined after the "*workitem*.complete()" method (if any) are not defined in the same LUW. This is wrong in most cases.


|  |
| --- |
| **Backlinks** |
| [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |

---
