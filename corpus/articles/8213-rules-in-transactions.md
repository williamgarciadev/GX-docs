---
title: "Rules in Transactions"
source_id: 8213
source_url: https://wiki.genexus.com/commwiki/wiki?8213
genexus_version: "18"
---

# Rules in Transactions

Rules play a crucial role in [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, as they allow you to program their behavior (for example: assigning default values, defining controls over the data, etc.).

They are written in a declarative way, which means the order in which they are written is not necessarily the order in which they will be executed.

All Transaction rules can involve attributes of the [Base Table](https://wiki.genexus.com/commwiki/wiki?6347)s associated with the Transaction and most rules can also involve attributes of the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029)s of those base tables, but they must be included in the Transaction's structure.

In addition, many Transaction rules allow involving variables defined within the object, constants, and functions.

The rules defined in Transactions are local. That is, they're only evaluated and executed (if applicable) when executing the Transaction in which they are defined (the Transaction UI or as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)).

Some valid rules for Transactions are:

|  |
| --- |
| [Accept rule](https://wiki.genexus.com/commwiki/wiki?6844) |
| [Add rule](https://wiki.genexus.com/commwiki/wiki?6845) (\*) |
| [Assignment rule](https://wiki.genexus.com/commwiki/wiki?6847) (\*) |
| [Call rule](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6849,,) (\*) |
| [Color rule](https://wiki.genexus.com/commwiki/wiki?8348) (\*) |
| [Default rule](https://wiki.genexus.com/commwiki/wiki?6850) |
| [Equal rule](https://wiki.genexus.com/commwiki/wiki?6855) |
| [Error rule](https://wiki.genexus.com/commwiki/wiki?6852) (\*) |
| [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853) |
| [Msg rule](https://wiki.genexus.com/commwiki/wiki?6854) (\*) |
| [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) (\*) |
| [NoPrompt rule](https://wiki.genexus.com/commwiki/wiki?6861) |
| [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) |
| [Refcall rule](https://wiki.genexus.com/commwiki/wiki?6864) |
| [Refmsg rule](https://wiki.genexus.com/commwiki/wiki?6865) |
| [Serial rule](https://wiki.genexus.com/commwiki/wiki?6866) |
| [Submit rule](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?15405,,) (\*) |
| [Subtract rule](https://wiki.genexus.com/commwiki/wiki?6860) (\*) |
| [Update rule](https://wiki.genexus.com/commwiki/wiki?21430) |

(\*) These are conditional rules and you can define triggering conditions for them.

### [See Also](#See+Also)

[Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868)  
[Triggering context for Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Rules definitions](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/rules-definition-6104751)


|  |
| --- |
| **Backlinks** |
| [After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284) | [After Attribute function](https://wiki.genexus.com/commwiki/wiki?8324) |
| [AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160) | [AfterLevel Event](https://wiki.genexus.com/commwiki/wiki?8285) | [AfterValidate Triggering event](https://wiki.genexus.com/commwiki/wiki?8282) | [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543) |
| [Before Action Triggering events](https://wiki.genexus.com/commwiki/wiki?8283) | [Delete function](https://wiki.genexus.com/commwiki/wiki?8328) | [Error rule](https://wiki.genexus.com/commwiki/wiki?6852) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GeneXus for SAP Systems - First Rules definitions](https://wiki.genexus.com/commwiki/wiki?34181) | [GeneXus for SAP Systems First Rules definitions (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54700) | [Inline Formulas within a contextual table](https://wiki.genexus.com/commwiki/wiki?6426) |
| [Insert - Rule...](https://wiki.genexus.com/commwiki/wiki?13683) | [Insert function](https://wiki.genexus.com/commwiki/wiki?8326) | [Level clause for Transaction rules](https://wiki.genexus.com/commwiki/wiki?8438) | [Msg rule](https://wiki.genexus.com/commwiki/wiki?6854) |
| [Category:Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) | [Transaction Rules Syntax](https://wiki.genexus.com/commwiki/wiki?6868) | [Transaction rules when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?2280) | [Triggering context for Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735) |
| [Category:Triggering events for rules in Transactions](https://wiki.genexus.com/commwiki/wiki?6840) | [Update function](https://wiki.genexus.com/commwiki/wiki?8327) | [View Rules Option](https://wiki.genexus.com/commwiki/wiki?9948) |

---
