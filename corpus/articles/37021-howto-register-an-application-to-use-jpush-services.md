---
title: "HowTo: Register an application to use JPush services"
source_id: 37021
source_url: https://wiki.genexus.com/commwiki/wiki?37021
genexus_version: "18"
---

# HowTo: Register an application to use JPush services

The purpose of this article is to explain the necessary steps to register an application to use JPush services.

To enable the **JPush** [Notification Provider](https://wiki.genexus.com/commwiki/wiki?33670) to send [push notifications](https://wiki.genexus.com/commwiki/wiki?19945), you need to register your application in the [Jiguang Developer Site](https://www.jiguang.cn/accounts/login/form) to get the credentials required to use JPush services.

### [Step 1 - Get certificates](#Step+1+-+Get+certificates)

Get the certificates for each platform deployed.  
Refer to:

* [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451)
* [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) (or try [Google Developer's wizard](https://developers.google.com/mobile/add?platform=android&cntapi=gcm)).

### [Step 2 - Login](#Step+2+-+Login)

Go to [Jiguang Developer Site](https://www.jiguang.cn/accounts/login/form), enter your user credentials and log in.  
`[imagen omitida: wiki id 37022]`

### [Step 3 - Create a new app](#Step+3+-+Create+a+new+app)

Select "Create a new application" option on the dashboard.  
`[imagen omitida: wiki id 37023]`

Enter a name (required) and an icon (optional) for your application.  
`[imagen omitida: wiki id 37024]`

### [Step 4 - Get the credentials](#Step+4+-+Get+the+credentials)

Once the application is created, you already have the credentials needed to integrate the JPush services in your GeneXus-generated application. These credentials will be set through the environment properties [App Key](https://wiki.genexus.com/commwiki/wiki?36968) and [Master Secret](https://wiki.genexus.com/commwiki/wiki?36969).  
`[imagen omitida: wiki id 37025]`

### [Step 5 - Configure platforms](#Step+5+-+Configure+platforms)

Set the platform-specific configurations for
[Android](https://wiki.genexus.com/commwiki/wiki?14453) and
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) in the Application Settings section (check picture above).

[***Android***](https://wiki.genexus.com/commwiki/wiki?14453)  
You just need to set the application package name:  
`[imagen omitida: wiki id 37026]`

[***Apple***](https://wiki.genexus.com/commwiki/wiki?14917)

* Upload Production certificate obtained in Step 1
* Upload Development certificate obtained in Step 1 (optional)
* Set "Certificate" as the Authentication Method

`[imagen omitida: wiki id 37027]`

Once the iOS configuration is set, the application settings will look like the following image:  
`[imagen omitida: wiki id 37028]`

### [Considerations](#Considerations)

The following information is used to contact the provider

```
Notifications host: api.jpush.cn
Devices host: device.jpush.cn
base url: /v3/
protocol: https
Authorization: Basic
```

### [Troubleshooting](#Troubleshooting)

#### [**1. Register Failed with server error**](#1.+Register+Failed+with+server+error)

The following error appears:

```
E/JIGUANG-JCore: [ConnectingHelper] Register Failed with server error - code:1005
W/JIGUANG-JCore: [ConnectingHelper] Local error description: Your appKey and android package name are not matched. Please double check them according to Application you created on Portal.
```

As detailed by the warning, please check the [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814) matches the Jiguang Platform configuration.

#### [**2. no value for onesignal\_app\_id is provided**](#2.+no+value+for+onesignal_app_id+is+provided)

The following error occurs:

```
error: c:\models\sampleKB\Data\mobile\Huawei\TestPushNotifications\src\main\AndroidManifest.xml Error:
error: Attribute meta-data#onesignal_app_id@value at AndroidManifest.xml requires a placeholder substitution but no value for <onesignal_app_id> is provided.
error: c:\models\sampleKB\Data\mobile\Huawei\TestPushNotifications\src\main\AndroidManifest.xml Error:
error: Attribute meta-data#onesignal_google_project_number@value at AndroidManifest.xml requires a placeholder substitution but no value for <onesignal_google_project_number> is provided.
```

When using the [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) to *JPush* and Huawei generation, make sure to turn off the UseHuaweiNotifications property.


|  |
| --- |
| **Backlinks** |
| [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [JPush - App Key property](https://wiki.genexus.com/commwiki/wiki?36968) |
| [JPush - Master Secret property](https://wiki.genexus.com/commwiki/wiki?36969) | [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) |

---
