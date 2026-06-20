---
title: "Triggering events for rules in Transactions"
source_id: 6840
source_url: https://wiki.genexus.com/commwiki/wiki?6840
genexus_version: "18"
---

# Triggering events for rules in Transactions

The rules you define in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) are usually executed when you expect it. But in some cases, it may be necessary to modify that moment in time.

Most Transaction rules allow you to add a triggering event or moment to them, indicating when each of them must be exactly executed.

### [**Syntax**](#Syntax)

[Any valid Transaction rule](https://wiki.genexus.com/commwiki/wiki?8213) [ IF *condition* ][ **ON** triggering event] ;

**Where:**

*condition*  
Is any valid logic condition

### [Available triggering events](#Available+triggering+events)

The following triggering events are available to be added at the end of most transaction rules:

* [BeforeValidate / BeforeInsert / BeforeUpdate / BeforeDelete / BeforeComplete](https://wiki.genexus.com/commwiki/wiki?8283)
* [AfterValidate](https://wiki.genexus.com/commwiki/wiki?8282)
* [AfterInsert / AfterUpdate / AfterDelete](https://wiki.genexus.com/commwiki/wiki?8284)
* [AfterLevel Level](https://wiki.genexus.com/commwiki/wiki?8285)
* [AfterComplete](https://wiki.genexus.com/commwiki/wiki?8160)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Rule Triggering Events in Transactions](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/rule-triggering-events-in-transactions-6104715)


|  |
| --- |
| **Pages** |
| [After Action Triggering event](https://wiki.genexus.com/commwiki/wiki?8284) | [After Attribute function](https://wiki.genexus.com/commwiki/wiki?8324) | [AfterComplete Triggering event](https://wiki.genexus.com/commwiki/wiki?8160) |
| [AfterLevel Event](https://wiki.genexus.com/commwiki/wiki?8285) | [AfterValidate Triggering event](https://wiki.genexus.com/commwiki/wiki?8282) | [Before Action Triggering events](https://wiki.genexus.com/commwiki/wiki?8283) |
| [Level clause for Transaction rules](https://wiki.genexus.com/commwiki/wiki?8438) |

---
