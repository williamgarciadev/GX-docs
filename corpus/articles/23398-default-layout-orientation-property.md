---
title: "Default Layout Orientation property"
source_id: 23398
source_url: https://wiki.genexus.com/commwiki/wiki?23398
genexus_version: "18"
---

# Default Layout Orientation property

Some SD applications are developed exclusively for a particular orientation and it is important that the screen doesn't rotate when the device does. This behavior should be maintained for every panel, unless explicitly stated.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | It takes the value specified in the property at the platform level. |
| **Landscape** | Each object's "Default Orientation" layout is restricted to Landscape and it cannot rotate unless there is a layout of higher precedence that applies to the platform and specifies Portrait orientation. The "Launch Image" used is specified for Landscape orientation and will not rotate. |
| **Portrait** | Each object's "Default Orientation" layout is restricted to Portrait and it cannot rotate unless there is a layout of higher precedence that applies to the platform and specifies Landscape orientation. The "Launch Image" used is specified for Portrait orientation and will not rotate. |

### [Description](#Description)

For example, an application designed for Portrait view may need some objects with Landscape orientation, to record video or scan barcodes among other things.

For this kind of applications, we have the Default Layout Orientation property which allows us to set our application's orientation, without the need to change the layouts of each object.

This property is found at the following levels:

* Platform, indicating the default orientation for the generated objects in the applications for that platform. At platform level the value "Any" means that there is no predefined orientation (this is the default value).
* Main SD, in the *Application* category, to indicate the orientation of the Main object and the objects invoked from it.

### [Samples](#Samples)

Let's consider an SD Panel in an iOS application with these layouts:

1. Any Platform, Any Mode, Landscape (first layout)
2. iOS, Any Mode, Any Orientation (second layout)
3. iOS, Any Mode, Portrait (third layout)

When the iOS application is :

* Restricted to Landscape orientation, the SD panel uses the first layout because it is the layout of higher precedence.
* Restricted to Portrait orientation, the SD panel uses the third layout.
* Not restricted, the SD panel uses the second layout because it is the layout of higher precedence.

### [Scope](#Scope)

**Platforms:** Smart Devices(Android, IOS)


|  |
| --- |
| **Backlinks** |
| [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) | [KB Platforms](https://wiki.genexus.com/commwiki/wiki?24284) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |
| [Platform Overrides property](https://wiki.genexus.com/commwiki/wiki?40583) |

---
