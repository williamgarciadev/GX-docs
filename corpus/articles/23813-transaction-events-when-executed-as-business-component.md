---
title: "Transaction events when executed as Business Component"
source_id: 23813
source_url: https://wiki.genexus.com/commwiki/wiki?23813
genexus_version: "18"
---

# Transaction events when executed as Business Component

When you use [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), all [Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042) are ignored except the **Start** event and the **After Trn** event.

If these events include references to objects with user interface, these references are ignored.

You can specify you want to execute one event only when the [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) is executed as Business Component, by preceding it with the qualifier [BC], as the following example shows:

[BC]

Event After Trn  
            .........  
EndEvent

And you can also specify you want to execute both events only when the Transaction is executed as Business Component, like this example shows:

[BC]

{  
     Event After Trn  
                 .........  
     EndEvent

     Event Start  
                 .........  
                 .........  
     EndEvent  
}

Likewise, you have the qualifier [WEB] to indicate that one or both events must be executed only if the Transaction is running in web environment with its web form, and not when it is executed as Business Component.


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |

---
