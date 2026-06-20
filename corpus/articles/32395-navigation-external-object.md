---
title: "Navigation external object"
source_id: 32395
source_url: https://wiki.genexus.com/commwiki/wiki?32395
genexus_version: "18"
---

# Navigation external object

The Navigation external object allows you to control the visibility and state of targets defined in [CallOptions.Target](https://wiki.genexus.com/commwiki/wiki?25323) (for Native Mobile applications) and [CallOptions.Target for Web](https://wiki.genexus.com/commwiki/wiki?32382).

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [ShowTarget method](#ShowTarget+method)

Displays the area corresponding to the specified target.

**For Web:** The behavior depends on the Mode property of the Navigation Style set up in the class of the Form.

* When the Navigation Style Mode is **Slide**, the target slides into view.
* When the Navigation Style Mode is **Static**, no changes occur because the area corresponding to the target is always visible when an object is loaded on it.
* When the Navigation Style Mode is **Custom**, the Hidden Class property is no longer applied.

**For Native Mobile:**The behavior depends on each Navigation Style implementation. For example, in a Main Menu with Tabs, ShowTarget/HideTarget can show or hide specific tabs. In a Slide Navigation, they open or close the sliding target area.

**Note**: The Mode property does not apply.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [HideTarget method](#HideTarget+method)

Hides the area corresponding to the specified target. It follows the same logic as the ShowTarget method for Web and Mobile.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [ExpandTarget method](#ExpandTarget+method)

The area corresponding to the target specified by the parameter is expanded. The behavior depends on the Mode property of the Navigation Style set up in the Form class.

**For Web:**

* When the Navigation Style Mode is **Slide**, the situation is equivalent to invoking the ShowTarget method. If the target was collapsed, it acquires the dimensions specified in the **Top Target Height**, **Right Target Width**, **Bottom Target Height** or **Left Target Width** property, depending on the target specified.
* When the Navigation Style Mode is **Static**, there are no changes because the area corresponding to the target is always visible when an object is loaded on it.
* When the Navigation Style Mode is **Custom**, the situation is equivalent to invoking the ShowTarget method, and the set up specified in the Collapsed Class property of the theme class associated with the target area is no longer applied.

**For Native Mobile:**

* Expands the target if supported by the current Navigation Style.
* Currently, only the Bottom target in iOS with Slide Navigation supports this method. The goal is to provide generic support for all styles in future versions.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |

### [CollapseTarget method](#CollapseTarget+method)

**For Web:**

Collapses the target according to the Navigation Style Mode set in the Form class.

**For Native Mobile:**

Collapses the target if supported by the Navigation Style. Currently, this is equivalent to hiding the Bottom target in Slide Navigation for iOS.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |

## [Events](#Events)

Navigation events are triggered when targets are shown, hidden, expanded, or collapsed.

These events apply to both Web and Native Mobile environments.  
In iOS, events are currently fired only for the Bottom target in Slide Navigation, but this is a known limitation. In the future, they are expected to be triggered for all supported targets (Left/Right in Slide, Left in Split, Tabs, etc.).

### [TargetShown event](#TargetShown+event+)

Fired after a target is shown using the ShowTarget method.

|  |  |
| --- | --- |
| **Input** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Output** | - |

### [TagetHidden event](#TagetHidden+event)

Fired after a target is hidden using the HideTarget method, or when a Target is hidden automatically.

|  |  |
| --- | --- |
| **Input** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Output** | - |

### [TargetExpanded event](#TargetExpanded+event)

Fired after a target is expanded using the ExpandTarget method.

|  |  |
| --- | --- |
| **Input** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Output** | - |

### [TargetCollapsed event](#TargetCollapsed+event)

Fired after a target is collapsed using the CollapseTarget method.

|  |  |
| --- | --- |
| **Input** | TargetName: [Character(40)](https://wiki.genexus.com/commwiki/wiki?6777) |
| **Output** | - |

## [Notes](#Notes)

* Expand/Collapse methods are available for both Web and Native Mobile environments.
* Navigation events are also available for both environments, with current limitations on iOS (only Bottom in Slide).
* The availability of ShowTarget and HideTarget depends on the Navigation Style. Examples include Right/Bottom for Slide Navigation or tabs in Tabs Navigation (for example: Tab1, Tab2, etc.).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

## [Sample](#Sample)

This is a basic example of using the Navigation external object in GeneXus:

```
Event 'ShowMenu' 
Navigation.ShowTarget('Right') 
EndEvent 

Event Navigation.TargetShown(&Target;) if &Target; = 'Right' 
msg('Menu opened') endif 
EndEvent
```

## [See Also](#See+Also)

[CallOptions Target](https://wiki.genexus.com/commwiki/wiki?25323)  
[CallOptions Target for Web](https://wiki.genexus.com/commwiki/wiki?32382)


|  |
| --- |
| **Backlinks** |
| [CallOptions Target](https://wiki.genexus.com/commwiki/wiki?25323) | [CallOptions Target for Web](https://wiki.genexus.com/commwiki/wiki?32382) |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
