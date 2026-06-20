---
title: "Deploy Server URL property"
source_id: 15042
source_url: https://wiki.genexus.com/commwiki/wiki?15042
genexus_version: "18"
---

# Deploy Server URL property

Indicates the web server to which the application is deployed.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

This property is available when the [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) is set to Yes.

You can find it in the [Knowledge Base Preferences window](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7109,,) for a certain [Environment](https://wiki.genexus.com/commwiki/wiki?7115) (in particular, for a certain Backend generator if the [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) is set to Yes). Remember that it is used for prototyping purposes only; it should not be used to host applications in production that might require another SLA.

GeneXus will deploy the application to the specified server at build time on each run.

The default value depends on the generator and the GeneXus version. More information in: [Servers available for Cloud prototyping](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26157,,).

The web server specified in this URL has to follow some rules; see [Cloud prototyping](https://wiki.genexus.com/commwiki/wiki?15046).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

* https://apps5.genexus.com (up to GeneXus 18 Upgrade 9)
* https://sandbox5.genexus.com (up to GeneXus 18 Upgrade 13)
* https://sandbox5.gxapps.cloud (since GeneXus 18 Upgrade 14)

More information at [Servers available for Cloud prototyping](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26157,,).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041)  
[Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342)  
[Web Root property](https://wiki.genexus.com/commwiki/wiki?9287)


|  |
| --- |
| **Backlinks** |
| [Deploy to cloud property](https://wiki.genexus.com/commwiki/wiki?15041) | [Deploy to cloud: Step by Step](https://wiki.genexus.com/commwiki/wiki?18250) |
| [Deploy to cloud: Step by Step (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58032) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) | [Deploy Virtual Directory property](https://wiki.genexus.com/commwiki/wiki?18342) |
| [IIS Version property](https://wiki.genexus.com/commwiki/wiki?17521) | [Servers available for Cloud prototyping (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?60517) |
| [Servers available for Cloud prototyping (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?60513) |

---
