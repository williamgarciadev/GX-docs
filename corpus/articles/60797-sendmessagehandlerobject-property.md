---
title: "SendMessageHandlerObject property"
source_id: 60797
source_url: https://wiki.genexus.com/commwiki/wiki?60797
genexus_version: "18"
---

# SendMessageHandlerObject property

Indicates the Procedure object that handles messages sent from the [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254).

### [Scope](#Scope)

**Controls:** [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The **SendMessageHandlerObject property** of a [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254) allows you to indicate the [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that handles the messages entered by the user in the control.

The Procedure receives the entire message history (make sure the [SendHistoryMessages property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60798,,) of the Chat control is set to True) and returns a response in a variable based on the **MessageUI** SDT.

The Procedure may do, for example, the following:

1. In**GeneXus 18 Upgrade 14 or higher:** Use the Globant Enterprise AI API.
2. In**GeneXus Next:** Use the Globant Enterprise AI API or an [Agent object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59249,,). For more information about it, read [HowTo: Use the Chat Control associated with a Procedure that calls an Agent](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60802,,).

The default value of the **SendMessageHandlerObject property** is **(none)**. If this property is not set to a Procedure name, you must manually handle messages by programming the **Chat.SendMessage** event.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).

### [See Also](#See+Also)

[SendHistoryMessages property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60798,,)  
[HowTo: Use the Chat Control associated with a Procedure that calls an Agent](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?60802,,)
