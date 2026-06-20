---
title: "Compilation Mode property"
source_id: 35447
source_url: https://wiki.genexus.com/commwiki/wiki?35447
genexus_version: "18"
---

# Compilation Mode property

This property allows the developer to specify in which mode an Android application should be compiled, simplifying the development-production process by switching its value.

### [Values](#Values)

|  |  |
| --- | --- |
| **Development** | This is the default value. The application is built for development purposes (i.e. it is not distributable). This mode prevents the developer from uploading the application to Google Play store until (s)he considers that it is sufficiently stable to be in production, and allows debugging from Android Studio framework. |
| **Distribution** | The application is built for production (i.e. it is distributable) and must be signed with distribution credentials by setting the Android Application Signing properties (empty by default). This mode allows the developer to upload it to Google Play store and prevents debugging from Android Studio framework. |

### [Description](#Description)

#### [Notes](#Notes)

* This property, for new Knowledge Bases in [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), is available in [Smart Devices Main object](https://wiki.genexus.com/commwiki/wiki?17817).
* If you are migrating your application to [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,) and you have already set the [application signing properties](https://wiki.genexus.com/commwiki/wiki?23328) on your Knowledge Base, both Compilation Mode property and Application Signing properties will remain at [Smart Devices Generator properties](https://wiki.genexus.com/commwiki/wiki?18371,,) in order to make it compatible with GeneXus Server repository.
* It is highly recommended to [obfuscate](https://wiki.genexus.com/commwiki/wiki?33477) the application when it is built in Distribution mode.
* When the developer switches the value of this property must remember that the application is signed with different certificates (debug for Development, custom for Distribution). As consequence, if the application is already installed on the device/emulator and the developer installs the application in a different mode, the installation will fail. This problem is avoided by uninstalling the previous version of the application.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,).

### [Scope](#Scope)

**Objects:** Menu for Smart Devices, Panel for Smart Devices, Work With for Smart Devices  
**Platforms:** Smart Devices(Android)

### [See Also](#See+Also)

[Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328)


|  |
| --- |
| **Backlinks** |
| [Android Application Signing](https://wiki.genexus.com/commwiki/wiki?23328) | [HowTo: Publish an application in Google Play](https://wiki.genexus.com/commwiki/wiki?15948) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Publishing Format property](https://wiki.genexus.com/commwiki/wiki?47457) | [Use Huawei Notifications property](https://wiki.genexus.com/commwiki/wiki?47542) |

---
