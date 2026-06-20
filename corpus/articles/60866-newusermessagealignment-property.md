---
title: "NewUserMessageAlignment property"
source_id: 60866
source_url: https://wiki.genexus.com/commwiki/wiki?60866
genexus_version: "18"
---

# NewUserMessageAlignment property

Defines how the new message entered by the user is aligned in the chat.

### [Values](#Values)

|  |  |
| --- | --- |
| Start | Aligns the user’s message at the top of the list. This is the default value. |
| End | Adds the user’s message at the bottom of the list. |

### [Scope](#Scope)

**Controls:** [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Determines how the Chat Control adjusts its scroll position after a new message is sent by the user.

**Start:**  This mode is typically used when the agent’s response is received incrementally, leaving space at the bottom to display the content as it arrives.  
It is usually combined with the property [AutoScroll property](https://wiki.genexus.com/commwiki/wiki?60865)= **Never**.  
**End:** The message is added at the bottom of the list, which is the typical behavior when the response arrives as a complete message (for example, from an agent that doesn’t reply incrementally). It is usually combined with the property [AutoScroll property](https://wiki.genexus.com/commwiki/wiki?60865) = **At scroll end**.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).

### [See Also](#See+Also)

[AutoScroll property](https://wiki.genexus.com/commwiki/wiki?60865)


|  |
| --- |
| **Backlinks** |
| [AutoScroll property](https://wiki.genexus.com/commwiki/wiki?60865) |

---
