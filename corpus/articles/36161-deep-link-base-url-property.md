---
title: "Deep Link Base URL property"
source_id: 36161
source_url: https://wiki.genexus.com/commwiki/wiki?36161
genexus_version: "18"
---

# Deep Link Base URL property

Indicates which URL should be handled by the application when it accepts deep linking. The property supports multiple sources separated by a semicolon.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

The value to assign to this property should follow this format:

<url> [ ; <url> ] \*

where <url> is the web server domain followed by the virtual directory of the application.

#### [Notes](#Notes)

* Every URL must point to the web-app root, including protocol and port in case it needed.
* URL provided by shorteners are not supported (e.g. goo.gl, bit.ly, ow.ly, etc).
* Allows accessing to every resource that respects the base URL.  
  For example, if the base URL is http://www.mystore.com/, the application is allowed to handle http://www.mystore.com/\*

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

### [See Also](#See+Also)

* [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163)


|  |
| --- |
| **Backlinks** |
| [Deep Link Name property](https://wiki.genexus.com/commwiki/wiki?36162) | [DeepLink external object](https://wiki.genexus.com/commwiki/wiki?36160) | [GAM - WeChat Authentication type](https://wiki.genexus.com/commwiki/wiki?45037) |
| [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
