---
title: "Notification Settings Panel property"
source_id: 48090
source_url: https://wiki.genexus.com/commwiki/wiki?48090
genexus_version: "18"
---

# Notification Settings Panel property

Specifies the Panel object to show when the system requests the application to open the Notification Settings.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Applications that show notifications to end users may allow configuring which notifications they show so that users can choose the ones they are interested in.

This configuration is usually done in an application panel that can be accessed through some options in the application.

Also, mobile platforms – both Android and iOS – provide system functionality that allows the applications to include this "notifications settings panel" inside the Notifications part of the system configuration.

By setting this property to a Panel object in GeneXus, the notification settings will be included inside the system's notifications settings.

If the application is called MyApplication, the user can access the application's notification settings by going to:

* Settings app > Notifications > MyApplication > MyApplication Notification Settings, in iOS.
* Settings app > Apps & Notifications > Notifications > MyApplication > Advanced > Additional Configuration Options, in Android.

Note that not all OS versions support this feature. Support has been added in iOS 12 and Android 5.0; when running in older OS versions, the property is ignored.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).
