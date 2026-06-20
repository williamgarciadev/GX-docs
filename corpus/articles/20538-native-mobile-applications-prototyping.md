---
title: "Native Mobile Applications Prototyping"
source_id: 20538
source_url: https://wiki.genexus.com/commwiki/wiki?20538
genexus_version: "18"
---

# Native Mobile Applications Prototyping

Native mobile applications are developed in a Windows environment (where GeneXus runs) but are usually targeted to a different one (iOS, Android, etc.). Many environments, such as Android, provide an emulator that runs in Windows making it possible to run a native mobile application without having an actual device. This is a pretty nice feature but also has the following drawbacks:

* **Lack of resources**   
  Such as calendar, camera, GPS, or third-party applications.  
  If your application requires one of these resources you will not be able to prototype with an emulator. It is recommended to test device-specific features on the device itself instead of the emulator as it may not work as expected, particularly when using these external objects: ClientInformation, Geolocation, Interop, Camera.

* **Performance**  
  Emulators are usually slower than devices to load the application and execute it.
* **What you see may not be what you get**  
  There may be minor but in fact important differences between an emulator and an actual device. It's highly important to test the final application on a physical device.
* **Poor application feeling**  
  Running an application on an emulator provides little “feeling” as you do not actually use it with your hands: shake it, touch it, rotate it, tilt it, etc.  
  It may seem that there is no reason to use an emulator and, if you have an actual device, you may be right. If you don’t, it’s a great friend!

### [See Also](#See+Also)

* [Native Mobile Applications Beta Testing](https://wiki.genexus.com/commwiki/wiki?28890)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
