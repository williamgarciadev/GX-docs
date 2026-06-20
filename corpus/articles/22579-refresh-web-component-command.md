---
title: "Refresh Web Component command"
source_id: 22579
source_url: https://wiki.genexus.com/commwiki/wiki?22579
genexus_version: "18"
---

# Refresh Web Component command

Executes a refresh on the web component itself and the web components it contains. This causes the web component to execute the Start, Refresh and Load events.

### [Syntax](#Syntax)

*<web component>***.Refresh**

### [Description](#Description)

This command is very useful when the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to "Smooth" as it allows refreshing only the web components needed, leaving out the others in the web page so as to avoid making a full refresh of the page.

### [Samples](#Samples)

Suppose you need to refresh a web component that is contained in the same web page and in the same level of the web component where an event is triggered.  
  
For example, you have a web page which loads web component A and web component B. Web Component A has the following code:

```
Event "GetBalance"
    &UserBalance = GetUserBalance(&UserId)
    &websession.set("UserBalance",&UserBalance)
EndEvent
```

Web Component B uses &UserBalance to display information in the form. It won't get the information from &UserBalance unless the previous code includes an explicit refresh which causes web component B to reload.

```
Event "GetBalance"
    &UserBalance = GetUserBalance(&UserId)
    &websession.set("UserBalance",&UserBalance)
    WebComponentB.refresh()
EndEvent
```

This causes web component B to execute the Start, Refresh and Load events, so &UserBalance can be read from the web session in the Refresh event.

### [See Also](#See+Also)

[Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472)  
[Event execution on the client side since X Evolution 3](https://wiki.genexus.com/commwiki/wiki?22529)


|  |
| --- |
| **Backlinks** |
| [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) | [Event execution on the client side since X Evolution 3](https://wiki.genexus.com/commwiki/wiki?22529) |
| [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [HowTo: Use Global Events in Web Objects](https://wiki.genexus.com/commwiki/wiki?31167) | [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) | [Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287) |

---
