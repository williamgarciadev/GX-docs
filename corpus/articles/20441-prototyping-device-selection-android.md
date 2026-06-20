---
title: "Prototyping device selection - Android"
source_id: 20441
source_url: https://wiki.genexus.com/commwiki/wiki?20441
genexus_version: "18"
---

# Prototyping device selection - Android

When you are developing an [Android platform](https://wiki.genexus.com/commwiki/wiki?14453) application you use a device (actual or virtual) to see how it looks and test it. The [run process](https://wiki.genexus.com/commwiki/wiki?5692) checks your machine for connected devices on every run and automatically decides which one to use.

The check sequence is as follows:

* Physical device connected

In order to detect the device connected, the adecquate device driver must be installed. Otherwhise, [the device will be ignored](http://wiki.genexus.com/commwiki/servlet/hwiki?Android+-+FAQ+and+Common+Issues,) by the check sequence and the next sequence step will be executed.

Besides having all functions (GPS, etc.) physical devices provide the fastest prototyping environment.

* [Emulator](https://wiki.genexus.com/commwiki/wiki?18270) already started

If an emulator is already started, it is selected to run the application.

If you want to run your application using your own AVD you must start the emulator with it \_before\_ running.

* The [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270) started with myGXAVD

If none of the above could be used, a new emulator is executed with the default AVD.

### [See Also](#See+Also)

* [Emulation for Android](https://wiki.genexus.com/commwiki/wiki?18270)
* [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910)


|  |
| --- |
| **Backlinks** |
| [Category:Android platform](https://wiki.genexus.com/commwiki/wiki?14453) | [Creating an Android Virtual Device](https://wiki.genexus.com/commwiki/wiki?14462) | [Execution for Android Using the Device](https://wiki.genexus.com/commwiki/wiki?14910) |
| [Execution for Android Using the Device (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56063) |

---
