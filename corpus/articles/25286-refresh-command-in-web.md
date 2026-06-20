---
title: "Refresh command in web"
source_id: 25286
source_url: https://wiki.genexus.com/commwiki/wiki?25286
genexus_version: "18"
---

# Refresh command in web

Refreshes a web page. If [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Compatible, it executes the Start, [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) and Load Event.

### [Syntax](#Syntax)

**Refresh**

### [Description](#Description)

The Refresh command executes a refresh of the web page, and causes to execute the Start, [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) and Load Event when the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Compatible.

In [Smooth](https://wiki.genexus.com/commwiki/wiki?22449) models, the Refresh command causes to execute the [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) and Load Event. In case of executing the Refresh command in a event of a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864), it executes the refresh of the web component and all its descendants. It does not execute the refresh of the parent web components.

In general, the Refresh command is used when [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Smooth. Otherwise, the execution of the page refresh.is automatic

### [Samples](#Samples)

Consider the following example, where a web page contains WEB COMPONENT A, and WEB COMPONENT C. WEB COMPONENT A contains WEB COMPONENT B and the Web User Experience property = Smooth

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | WEB COMPONENT A |  | | --- | | WEB COMPONENT B | | | |  | | --- | | WEB COMPONENT C | |

If the Refresh command is executed on a user event of WEB COMPONENT A; the following is executed:

* UserEvent    Web Component A
* Refresh    Web Component A
* Start    Web Component B (1)
* Refresh    Web Component B
* Load    Web Component B
* Load    WebComponent A

(1) Only if the [Create function](https://wiki.genexus.com/commwiki/wiki?8359) of Web Component B is executed on the Refresh event of Web Component A. Another possibility is that Web Component B is associated to the [Object property](https://wiki.genexus.com/commwiki/wiki?7011) of the web component control in the form of Web Component A.

There are other commands like [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578) and [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579) which allow to refresh more specific parts of the screen.

### [See Also](#See+Also)

[Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472)  
[Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287)


|  |
| --- |
| **Backlinks** |
| [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) | [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069) |
| [Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287) |

---
