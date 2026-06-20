---
title: "Analytics Provider property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54454
source_url: https://wiki.genexus.com/commwiki/wiki?54454
genexus_version: "18"
---

# Analytics Provider property (GeneXus 18 Upgrade 2 or prior)

Sets the Application Analytics Provider.

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

To set the analytics provider for the application, you can choose between [Google Analytics](https://analytics.google.com/analytics/web/) or [Firebase Analytics](https://firebase.google.com/).

Once a supplier has been selected, a new group of properties will be displayed depending on which one has been selected.

If Google Analytics is selected, the properties [Tracker Id property](https://wiki.genexus.com/commwiki/wiki?42119) and [Analytics Dispatch Period property](https://wiki.genexus.com/commwiki/wiki?42128) will be enabled below the GoogleAnalytics properties node.

If Firebase is selected, the properties [Firebase Android File property](https://wiki.genexus.com/commwiki/wiki?48139) and [Firebase Apple File property](https://wiki.genexus.com/commwiki/wiki?48140) will be enabled below the FirebaseAnalytics properties node.

Also, when you select Firebase on **Android,** the information can be sent to [Google Analytics 4 (GA4)](https://support.google.com/analytics/answer/10089681?hl=en). See [SAC #52779](https://www.genexus.com/en/developers/websac?data=52779;;).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Firebase Android File property](https://wiki.genexus.com/commwiki/wiki?48139)  
[Firebase Apple File property](https://wiki.genexus.com/commwiki/wiki?48140)  
[Google Analytics in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?54515)
