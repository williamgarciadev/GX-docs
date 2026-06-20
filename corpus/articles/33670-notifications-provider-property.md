---
title: "Notifications Provider property"
source_id: 33670
source_url: https://wiki.genexus.com/commwiki/wiki?33670
genexus_version: "18"
---

# Notifications Provider property

Selects a provider for sending push notifications to applications.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | GeneXus Notifications using RemoteNotification external object (iOS Only and Deprecated). |
| **JPush** | JPush Notifications (China). |
| **OneSignal** | OneSignal Notifications. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

You can find this property in the [Preferences window](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7109,,), for your [Environment](https://wiki.genexus.com/commwiki/wiki?7115) at the Backend Generator level.

### [Values](#Values)

None

Indicates that a [custom notification mechanism](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18150,,) is used. This mechanism is deprecated and remains valid only for Apple applications.

One Signal

When the [OneSignal](http://www.onesignal.com) value is selected as the Notifications Provider, the following properties become available for configuration. These values are required to send push and silent notifications using OneSignal:

* **[OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492)**   
  The application identifier provided by One Signal.
* **[REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493)**  
  The application authorization key provided by One Signal.

This is the recommended option for the whole World, but China.

For more information, read [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147).

JPush

Uses [JPush](http://www.jiguang.cn/push) to send push and silent notifications through the Notification Provider API, using the configured [Jiguang settings](https://wiki.genexus.com/commwiki/wiki?37021).

* **[App Key](https://wiki.genexus.com/commwiki/wiki?36968)**  
  The application identifier provided by JPush.
* **[Master Secret](https://wiki.genexus.com/commwiki/wiki?36969)**  
  Application master secret key provided by JPush to be able to use the REST services.
* **[Channel](https://wiki.genexus.com/commwiki/wiki?36970)**  
  Channel value for the application package, to get sub-channel statistics.
* **[APNs for production](https://wiki.genexus.com/commwiki/wiki?36971)**  
  (iOS only) Indicates if the production APNs certificate will be used or not.
* **[NDK ABI Filters](https://wiki.genexus.com/commwiki/wiki?36972)**  
  (Android only) ABIs that will be included in the Android application package.

This is the recommended option for China.

### [Runtime configuration](#Runtime+configuration)

These properties can be set dynamically at runtime using the [Configuration object](https://wiki.genexus.com/commwiki/wiki?33687). For example:

```
&ConfigurationProperty  = new()
&ConfigurationProperty.PropertyName = !"REST_API_KEY"
&ConfigurationProperty.PropertyValue = !"%oneSignal_Rest_ApiKey%"  
&Configuration.Properties.Add( &ConfigurationProperty )  
&ConfigurationProperty  = new()  
&ConfigurationProperty.PropertyName = !"APP_ID"
&ConfigurationProperty.PropertyValue = !"%appIdOneSignal%"  
&Configuration.Properties.Add( &ConfigurationProperty )
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[HowTo: Receiving and processing a notification message from an external app](https://wiki.genexus.com/commwiki/wiki?33633)  
[HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147)


|  |
| --- |
| **Backlinks** |
| [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545) |
| [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) | [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) |
| [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021) | [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) | [JPush - APNs for production property](https://wiki.genexus.com/commwiki/wiki?36971) |
| [JPush - App Key property](https://wiki.genexus.com/commwiki/wiki?36968) | [JPush - Channel property](https://wiki.genexus.com/commwiki/wiki?36970) | [JPush - Master Secret property](https://wiki.genexus.com/commwiki/wiki?36969) | [JPush - NDK ABI Filters property](https://wiki.genexus.com/commwiki/wiki?36972) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) | [OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492) | [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) |
| [REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) | [Use Huawei Notifications property](https://wiki.genexus.com/commwiki/wiki?47542) |

---
