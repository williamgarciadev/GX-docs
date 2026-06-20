---
title: "Execution for Android Using the Device"
source_id: 14910
source_url: https://wiki.genexus.com/commwiki/wiki?14910
genexus_version: "18"
---

# Execution for Android Using the Device

[Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24799) can be prototyped directly on the device. In fact, prototyping directly on the device is always more accurate and effective than using the [emulator](https://wiki.genexus.com/commwiki/wiki?18270).

The reasons for this are:

* The emulator lacks resources (calendar, camera, third-party applications for interacting)
* It is easier to handle (interaction is done with manual gestures instead of using the mouse)
* What you see is what you get: the emulator continues to be what it is, i.e. an emulator. What is executed on the device is what will be released in the end.
* Gyroscope, shaker, touch-sensitive: better on the device than in the emulator.
* Faster: the device is quicker (more responsive) than the emulator.

There are different options to prototype the application directly on the device listed below.

### [Prototyping the application on the device connected to PC](#Prototyping+the+application+on+the+device+connected+to+PC)

* Enable USB debugging on the device. [Android - Enable developer options and USB debugging](https://developer.android.com/studio/debug/dev-options?hl=en).
* Before executing the application, connect the device to the PC (its driver must be previously installed).
* If a [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) (e.g. dashboard) was set just press F5; otherwise use "right button/run" option. It will recognize the device as an Android device and will run the application in it (the emulator will not be opened in the PC).

### [Prototyping from QR codes](#Prototyping+from+QR+codes)

* You can scan the application's [QR Code](https://wiki.genexus.com/commwiki/wiki?18095) to install it.
* See [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260) for more information.

### [Download the application to the device (.apk file) and run it](#Download+the+application+to+the+device+%28.apk+file%29+and+run+it)

* Make sure that you have compiled the application before installing it. To compile the application you can make a build/rebuild of the dashboard object or run it (see [Build/Rebuild/Run](https://wiki.genexus.com/commwiki/wiki?5692)).
* Copy the .apk file to the SD card of the device. It is located at: <Knowledge base directory>\<Target Environment directory>\mobile\Android\<Main Startup Object>\bin  
  For example, if the KB was called ControlCar and the main startup object was called DashCar, the .apk file would be at:  
  C:\Models\ControlCar\CsharpModel\mobile\Android\DashCar\bin\DashCar-debug.apk
* These .apk files (which don’t belong to Android's Market) have to be enabled in order to be executed on Android devices. This can be done by enabling this option: **Settings > Applications > Unknown sources**.
* Lastly, copy the .apk file to the SD card of the device, install it with a click and run.

When the application is running, check that the target server of the application is visible from the device for it to work correctly. Typically, it is a public server on the Internet. Its URL is in the [Web Root property](https://wiki.genexus.com/commwiki/wiki?9287) of the web model. The target server is the server where the database is hosted and the place from which the [REST Web Services](https://wiki.genexus.com/commwiki/wiki?14573) will be consumed. In general, when you prototype the application the Web Root property has a value similar to http://localhost/MyKBNameNetEnvironment/, but it can’t be seen from the device. So you must change the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) to use the IP value, for example to the value http://192.168.86.43/MyKBNameNetEnvironment/  where 192.168.86.43 is the IPv4 Address of localhost (you can get it with the command ipconfig /all). Also, make sure the PC is using the same wifi as the device.

### [Use the GeneXus Project Navigator](#Use+the+GeneXus+Project+Navigator)

Set the [Android Execution Type property](https://wiki.genexus.com/commwiki/wiki?55300) to Genexus Project Navigator, download the GeneXus Project Navigator from [here](https://play.google.com/store/apps/details?id=com.genexus.android.navigator&pli=1) and use it in your device.

### [See Also](#See+Also)

* [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270)
* [Prototyping device selection - Android](https://wiki.genexus.com/commwiki/wiki?20441)
* [All about Android prerequisites](https://wiki.genexus.com/commwiki/wiki?14453)
* [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575)


|  |
| --- |
| **Backlinks** |
| [Category:Android platform](https://wiki.genexus.com/commwiki/wiki?14453) | [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270) | [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260) |
| [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) | [Generate Android property](https://wiki.genexus.com/commwiki/wiki?18654) | [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) | [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Prototyping device selection - Android](https://wiki.genexus.com/commwiki/wiki?20441) |

---
