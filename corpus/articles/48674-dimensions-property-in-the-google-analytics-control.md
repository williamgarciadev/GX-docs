---
title: "Dimensions property in the Google Analytics Control"
source_id: 48674
source_url: https://wiki.genexus.com/commwiki/wiki?48674
genexus_version: "18"
---

# Dimensions property in the Google Analytics Control

An SDT containing the dimensions to send on pageviews. Each property in the SDT is a dimension, and the value of the property, the dimension's value.

### [Scope](#Scope)

**Controls:** [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)

### [Description](#Description)

When using the [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847) you can specify an SDT containing a list of dimensions to discriminate further when doing the site analysis.

Each property in the SDT is a *dimension*, and the value of that property is the value you want to record.

From the GeneXus side, create an SDT with Key/Value items (both character datatypes) and assign whatever you want in runtime.  
Make sure to assign the *Dimensions* User Control property to the associated SDT variable.

Check the following associated documentation from the GA4 site:

* [GA4 - Setup Event Parameters](https://developers.google.com/analytics/devguides/collection/ga4/event-parameters)
* [GA4 - Custom dimensions and metrics](https://support.google.com/analytics/answer/10075209)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

Consider the following code snippet:

```
&GADimensions.key_one = !"Some value"
&GADimensions.key_two = !"Some other value"
```

You will be able to analyze the data by the defined dimensions. On the Google Analytics 4 console, the dimensions key and values will be available from the *page\_view* and will expand for each defined property (for this case key\_one and key\_two).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847)


|  |
| --- |
| **Backlinks** |
| [Google Analytics Control](https://wiki.genexus.com/commwiki/wiki?11847) | [Google Analytics Dimensions property (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?55189) |

---
