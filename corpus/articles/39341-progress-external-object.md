---
title: "Progress external object"
source_id: 39341
source_url: https://wiki.genexus.com/commwiki/wiki?39341
genexus_version: "18"
---

# Progress external object

The Progress external object enables you to give a feedback to the end-user about the progress of a batch process that is being executed.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [Class property](#Class+property)

To assign a [Theme-class](https://wiki.genexus.com/commwiki/wiki?6420) to the control.

### [Type property](#Type+property)

The Progress Indicator can be determinate (Type=1) or indeterminate (Type=0). Determinate indicators show the progress of the processing, while indeterminate ones don't inform you about the status during the process. There is an enumerated domain for this purpose (ProgressIndicatorType).

### [Title property](#Title+property)

Main text that is shown on the progress Indicator.

### [Description property](#Description+property)

More information is shown on the progress indicator screen.

### [MaxValue property](#MaxValue+property)

This property is used when the Type is Determinate. This property specifies the value for the task completion.

### [Value property](#Value+property)

When the determinate type is used, this value is the current percentage of the processing task.

## [Methods](#Methods)

### [Show method](#Show+method)

Invokes the progress Indicator screen.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

### [ShowWithTitle method](#ShowWithTitle+method)

Invokes the progress Indicator with a custom title.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | title:[Character(255)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [ShowWithTitleAndDescription](#ShowWithTitleAndDescription)

Invokes the progress indicator with a custom title and description.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | title:[Character(255)](https://wiki.genexus.com/commwiki/wiki?6777), description:[Character(255)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [Hide method](#Hide+method)

Closes the Progress Indicator screen.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

**Smart Devices**  
When a Progress Indicator is shown inside a composite block, an implicit call to the Hide method is automatically added at the end of the event. This is required since the composite block may be canceled by any failing action, and then the Progress must be automatically hidden. Anyway, it is recommended to always add the call to the Hide method to dismiss the Progress where it should be dismissed (according to the application logic).  
Note that this implicit call to the Hide() method is not added when the Progress is shown from generated code (like when shown from an Offline Procedure).

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) |
| **Platforms** | Web(.NET,Java), SmartDevices(Android,iOS) |
| **Connectivity** | Online, Offline |

## [Requirements](#Requirements)

The progress indicator for web applications has the same requirements as the [Server.Socket external object](https://wiki.genexus.com/commwiki/wiki?22442) because they both use [web sockets](http://en.wikipedia.org/wiki/WebSocket). See [Progress Indicator requirements for Web](https://wiki.genexus.com/commwiki/wiki?27740).

## [See also](#See+also)

* [Progress Indicator User Control for Web](https://wiki.genexus.com/commwiki/wiki?31275)
* [Progress Indicator requirements for Web](https://wiki.genexus.com/commwiki/wiki?27740)
* [How To: Use a Progress Indicator in a Web Panel](https://wiki.genexus.com/commwiki/wiki?32779)
* [HowTo: Use a Progress Indicator in a Panel](https://wiki.genexus.com/commwiki/wiki?19338)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
