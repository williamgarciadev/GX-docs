---
title: "Apple Maps API property (GeneXus 18 Upgrade 13)"
source_id: 60792
source_url: https://wiki.genexus.com/commwiki/wiki?60792
genexus_version: "18"
---

# Apple Maps API property (GeneXus 18 Upgrade 13)

Displays maps in Apple Maps.

### [Values](#Values)

|  |  |
| --- | --- |
| **Apple Maps** | Default value. Uses Apple Maps. |
| **Google Maps** | Uses Google Maps. Apple Maps API Key property must be set with a Google key. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))

### [Description](#Description)

This property allows you to use another maps provider different from Apple Maps (e.g. Google Maps). When you change its default value, the [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268) will be displayed to set the access key.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Compatibility](#Compatibility)

Make sure to set the [iOS Deployment Target property](https://wiki.genexus.com/commwiki/wiki?47294) to 13 in order to compile with the [Apple Generator](https://wiki.genexus.com/commwiki/wiki?14917) and Google Maps.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?38845,,).

### [See Also](#See+Also)

* [Apple Maps API Key property](https://wiki.genexus.com/commwiki/wiki?39268)
