---
title: "Analytics Provider property (GeneXus 18 or prior)"
source_id: 57765
source_url: https://wiki.genexus.com/commwiki/wiki?57765
genexus_version: "18"
---

# Analytics Provider property (GeneXus 18 or prior)

Application Analytics Provider.

### [Values](#Values)

|  |  |
| --- | --- |
| **Firebase** | The provider is Firebase Analytics. |
| **Google** | The provider is Google Analytics. |
| **None** | Default value. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

To set the analytics provider for the application, you can choose between [Google Analytics](https://analytics.google.com/analytics/web/) or [Firebase Analytic](https://firebase.google.com/).

Once a provider has been selected, a new group of properties will be displayed depending on the chosen one.

If Google Analytics is selected, the [Tracker Id property](https://wiki.genexus.com/commwiki/wiki?42119) and [Analytics Dispatch Period property](https://wiki.genexus.com/commwiki/wiki?42128) will be enabled.

If Firebase is selected, the [Firebase Android File property](https://wiki.genexus.com/commwiki/wiki?48139) and [Firebase Apple File property](https://wiki.genexus.com/commwiki/wiki?48140) will be enabled.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Firebase Android File property](https://wiki.genexus.com/commwiki/wiki?48139)  
[Firebase Apple File property](https://wiki.genexus.com/commwiki/wiki?48140)  
[Google Analytics in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?54515)
