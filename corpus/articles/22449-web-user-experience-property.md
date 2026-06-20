---
title: "Web User Experience property"
source_id: 22449
source_url: https://wiki.genexus.com/commwiki/wiki?22449
genexus_version: "18"
---

# Web User Experience property

Determines how the Refresh action is performed in web pages when a user-defined event is executed within the page. It also determines how navigation takes place between different web pages.

### [Values](#Values)

|  |  |
| --- | --- |
| **Previous versions compatible** | The mechanism is disabled. |
| **Smooth** | The mechanism is enabled. This is the default value for new KBs. |

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Level:** Version

### [Description](#Description)

This is a version-level and object-level property.

When the Web User experience property is set to "Smooth", the Refresh event is not executed implicitly on every user event exit and the Start event is executed only once. In addition, each web component is independent from the main page where it is contained so the Refresh of a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) does not affect the rest of the page.

The event execution is determined by the rules explained in [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472). Performance of web applications is improved by reducing the round trips to the server.

The Smooth value of the property also allows enabling [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455), where navigating to a web page that is contained in the same [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) as the origin web page does not force a refresh of the whole page in the browser, but only updates the page loaded in the content place holder.

Another benefit of this property is the way the load command is executed within a user event, as explained in [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555). In this case, the load command does not force a refresh of the grid but only adds a new line.

The above options allow you to develop applications with a much better user experience. See [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) as an example.

Important: The value 'Previous Version Compatible' is deprecated since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066). If you use it, you will get the following warning in build time: "The 'Web User Experience' property is configured to be 'PreviousVersionsCompatible'. This execution mode is deprecated and in a future version its support will be removed. The application should be converted to 'Smooth'."

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Converting to Smooth Web UX](https://wiki.genexus.com/commwiki/wiki?22561,,)  
[Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442)  
[User defined event](https://wiki.genexus.com/commwiki/wiki?8044)


|  |
| --- |
| **Backlinks** |
| [CallOptions Target for Web](https://wiki.genexus.com/commwiki/wiki?32382) | [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) |
| [Event execution on the client side since X Evolution 3](https://wiki.genexus.com/commwiki/wiki?22529) | [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [GeneXus 18 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?51080) | [GeneXus 18 Compatibility Section (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53520) |
| [GetString method](https://wiki.genexus.com/commwiki/wiki?8831) | [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) | [Lapse property](https://wiki.genexus.com/commwiki/wiki?17303) | [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) |
| [On session timeout property](https://wiki.genexus.com/commwiki/wiki?17458) | [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) | [Refresh Form command](https://wiki.genexus.com/commwiki/wiki?25287) |
| [Refresh Grid event](https://wiki.genexus.com/commwiki/wiki?8187) | [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578) | [Refresh method for Grid controls (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57357) | [Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579) |
| [Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356) | [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) | [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442) | [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455) |
| [Category:URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523) |

---
