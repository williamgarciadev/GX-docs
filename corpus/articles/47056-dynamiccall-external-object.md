---
title: "DynamicCall External Object"
source_id: 47056
source_url: https://wiki.genexus.com/commwiki/wiki?47056
genexus_version: "18"
---

# DynamicCall External Object

Allows setting the call options to a dynamically called object.

|  |  |
| --- | --- |
|  |  |

## [Scenario](#Scenario)

When calling an object, you can configure how the object will be called by setting the object's [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666).

For example:

```
MyPanel.CallOptions.Type = CallType.Popup
MyPanel()
```

However, when the call is dynamic –that is, the object's name is in a variable–, you cannot use this approach. That's where the **DynamicCall** External Object comes in.

## [Methods](#Methods)

### [SetOption](#SetOption)

Sets the specified call option value to the dynamic object.

Parameters:

* ObjectName: Character – The object name for which the call option will be set.
* CallOption: DynamicCallOption, GeneXus.Common – The option to set.
* Value: Varchar – The value to set in the given call option.

Example:

```
&dynObject = "MyPanel"
DynamicCall.SetOption( &dynObject, DynamicCallOption.Type, "Popup" )
Call( &dynObject )
```

## [Domains](#Domains)

### [DynamicCallOption](#DynamicCallOption)

Enumerated domain with the valid call options to set dynamically.

Values:

* [Type](https://wiki.genexus.com/commwiki/wiki?25322)
* [Target](https://wiki.genexus.com/commwiki/wiki?25323)
* [TargetSize](https://wiki.genexus.com/commwiki/wiki?25322)
* TargetHeight
* TargetWidth
* [EnterEffect](https://wiki.genexus.com/commwiki/wiki?20961)
* [ExitEffect](https://wiki.genexus.com/commwiki/wiki?20961)

## [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)


|  |
| --- |
| **Backlinks** |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
