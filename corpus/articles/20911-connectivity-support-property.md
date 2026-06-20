---
title: "Connectivity Support property"
source_id: 20911
source_url: https://wiki.genexus.com/commwiki/wiki?20911
genexus_version: "18"
---

# Connectivity Support property

Indicates whether an object is going to be executed online or offline.

### [Values](#Values)

|  |  |
| --- | --- |
| **Inherit** | This value is only available for non-main objects. The value of the property will be inherited from the caller object at runtime. |
| **Offline** | The object is executed completely offline with no automatic communication to the server. |
| **Online** | The object will execute on an online environment communicating with the server via REST services. This is the default value for main objects for mobile applications development. |

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property enables [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262).

It sets whether an object is generated online or offline. When an object is set to execute online, GeneXus will generate REST services in order to enable communication between the device and the web server. On the other hand, if the value is set to offline, native code for devices will be generated to execute every action on the device without invoking a REST service on a web server.  
  
When this property is set to **Offline** in a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770), it means two things:

* A local database will be generated in the device.
* A new GeneXus object appears on the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), under the Main Object: the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).

#### 

#### [Considerations](#Considerations)

Since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) this property is also available for [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s and [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s. This feature makes it easier to call Web Services in an offline application; before, when [HttpClient](https://wiki.genexus.com/commwiki/wiki?6932) was used, it was necessary to perform this kind of calls.

Now, calling a Procedure that is exposed as a REST service from an offline application is as simple as setting the **Connectivity Support property** of that Procedure to Online. Then, every time you call that Procedure from your application, it is going to be called via REST services.

#### [Restrictions](#Restrictions)

* If the Business Component is edited in the layout of some [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), then the **Connectivity Support property** of the Business Component is discarded, and the device uses the Connectivity Support property of the [WW](https://wiki.genexus.com/commwiki/wiki?20840) object instead.
* The **Connectivity Support property** over Procedures, Data Providers, and Business Components work only when these objects are called from [Client Events](https://wiki.genexus.com/commwiki/wiki?24332); otherwise, the called object inherits the **Connectivity Support property** value from the caller object. This means, for example, that if an Online Procedure is called from an Offline Procedure, the Online Procedure is called Offline.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223)  
[HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558)  
[Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237)  
[Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262)


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator resources update](https://wiki.genexus.com/commwiki/wiki?39998) | [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) |
| [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) | [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558) | [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) |
| [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |
| [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) |
| [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400) | [Printer external object](https://wiki.genexus.com/commwiki/wiki?48131) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) |
| [ServerDate function](https://wiki.genexus.com/commwiki/wiki?8490) | [ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491) | [ServerTime function](https://wiki.genexus.com/commwiki/wiki?8492) | [ToJson method](https://wiki.genexus.com/commwiki/wiki?37817) |
| [Use PDF Reports property](https://wiki.genexus.com/commwiki/wiki?42887) |

---
