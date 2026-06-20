---
title: "ControlValueChanged event"
source_id: 22676
source_url: https://wiki.genexus.com/commwiki/wiki?22676
genexus_version: "18"
---

# ControlValueChanged event

Executes some code when the value of a given input is changed.

### [Syntax](#Syntax)

**Event** *&VarOrAtt***.ControlValueChanged**  
*Event\_code*  
**EndEvent**

**Where:**

*&VarOrAtt*  
   Any variable or attribute that is on a layout. The event will be triggered once the control loses focus or, in some cases, the value has been set.

*Event\_code*The code that will be executed when the event is triggered. The moment depends on the control. For example:

* Edit controls execute the event once it loses focus, not when every key is pressed.
* Wheel controls execute it once the wheel stops spinning, not when the user spins for each value.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | Attribute/Variable |
| **Generators:** | [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [Description](#Description)

The objective of this event is to give constant feedback to the user. It is very useful for giving feedback or updating tightly related data.

**Note**: If the value of the field is changed programmatically (by code), the ControlValueChanged event is not going to be executed (for example, an assignment on another User event).

### [Temporary restrictions](#Temporary+restrictions)

The ControlValueChanged event is not available for the following controls:

#### [Android](#Android)

* Prompts associated with fields

#### [iOS](#iOS)

* Video & Audio fields
* Multi Wheel
* Physical Measures
* Prompts associated with fields

### [Availability](#Availability)

This event is available as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22626,,) in iOS and Android, and as of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35908,,) in Web too.

### [See also](#See+also)

[HowTo: Use ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22678)


|  |
| --- |
| **Backlinks** |
| [Click event](https://wiki.genexus.com/commwiki/wiki?8177) | [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) | [ControlValueChanging event](https://wiki.genexus.com/commwiki/wiki?35768) |
| [HowTo: Use ControlValueChanged event](https://wiki.genexus.com/commwiki/wiki?22678) |
| [Switch control](https://wiki.genexus.com/commwiki/wiki?29973) |

---
