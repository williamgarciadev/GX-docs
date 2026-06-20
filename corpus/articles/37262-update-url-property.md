---
title: "Update URL property"
source_id: 37262
source_url: https://wiki.genexus.com/commwiki/wiki?37262
genexus_version: "18"
---

# Update URL property

Specifies the URL of the Store page where the Application is published, or a link where the APK itself is deployed.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

The **Update URL property** must be set when the application is created. Doing it later will not work because it is not possible to add an install APK permission on an APK that is already built.

When you indicate the APK link (for example, https://apps5.genexus.com/Id85e32a53c32e017634b1c0a1826eaf4f/Panel1.apk), the end user must grant permissions for the application to update itself. So, the update must only be confirmed in the case of changes to the version.

For applications published on Google Play, you must provide a URL like:

https://play.google.com/store/apps/details?id=<package\_name>

Where *<package\_name>* is the one specified in the [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814). For example: https://play.google.com/store/apps/details?id=com.artech.MyKB.MyMainObject

If the application is published, for example, in [Samsung Apps Store](http://www.samsung.com/global/galaxy/apps/galaxy-apps/), or in any other store, this URL must change.

To support multiple stores, you may use the [market URI scheme](https://en.wikipedia.org/wiki/Talk%3AURI_scheme#market:_scheme) (as follows), but always bear in mind that the application must be published on them.

*market://details?id=<your\_app\_package\_name>*

In that case, the device should display a selector at the bottom of the screen indicating the stores installed on the device and where the end user may download a new version of the app.

`[imagen omitida: wiki id 34418]`

The permission generated with the **Update URL property** when using an APK in the URL is the following:

<uses-permission android:name="android.permission.REQUEST\_INSTALL\_PACKAGES" />

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?33798,,).

### [See Also](#See+Also)

[HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223)


|  |
| --- |
| **Backlinks** |
| [HowTo: Version Your Native Mobile Application](https://wiki.genexus.com/commwiki/wiki?17223) |

---
