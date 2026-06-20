---
title: "Android Execution Type property"
source_id: 55300
source_url: https://wiki.genexus.com/commwiki/wiki?55300
genexus_version: "18"
---

# Android Execution Type property

Specifies how the Android application will be executed.

### [Values](#Values)

|  |  |
| --- | --- |
| **GeneXus Project Navigator** | The application metadata is generated and can be used in the GeneXus Project Navigator installed from the Google Play. |
| **Emulator or Device** | Uses the connected device or active emulator. Otherwise, opens the default emulator. This is the default value. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** Generator

### [Description](#Description)

You can download the GeneXus Project Navigator from [here](https://play.google.com/store/apps/details?id=com.genexus.android.navigator&pli=1).

If the **Android Execution Type** property is set to "GeneXus Project Navigator":

* When performing a Build All, the output shows (in the Android execution section) that there is nothing to compile:

========== Android Compilation started ==========

Nothing to compile

Success: Android Compilation

* When trying to execute a [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) from GeneXus, the output shows (in the Android execution section) the following message:

========== Android Compilation started ==========

Please launch the GeneXus Project Navigator app on your Android device and scan the QR code provided in the Launchpad

Success: Android Execution

Success: Run Panel1

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).


|  |
| --- |
| **Backlinks** |
| [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910) | [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) |

---
