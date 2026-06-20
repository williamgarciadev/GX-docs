---
title: "AutoScroll property"
source_id: 60865
source_url: https://wiki.genexus.com/commwiki/wiki?60865
genexus_version: "18"
---

# AutoScroll property

Specifies the scroll behavior in the chat.

### [Values](#Values)

|  |  |
| --- | --- |
| Never | Automatic scrolling is disabled. This is the default value. |
| At scroll end | When a message is received incrementally, if the scroll is positioned at the bottom, it remains there to show the new incoming content. |

### [Scope](#Scope)

**Controls:** [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Defines whether the Chat Control should automatically scroll to display new messages as they appear or not.

It can be combined with the [NewUserMessageAlignment property](https://wiki.genexus.com/commwiki/wiki?60866) to define how the chat adjusts its position after a user sends a message:

* When AutoScroll = Never, it is typically combined with NewUserMessageAlignment = Start, to keep space at the bottom for incremental responses.
* When AutoScroll = At scroll end, it is usually combined with NewUserMessageAlignment = End, so new messages appear at the bottom of the list.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).

### [See Also](#See+Also)

[NewUserMessageAlignment property](https://wiki.genexus.com/commwiki/wiki?60866)


|  |
| --- |
| **Backlinks** |
| [NewUserMessageAlignment property](https://wiki.genexus.com/commwiki/wiki?60866) |

---
