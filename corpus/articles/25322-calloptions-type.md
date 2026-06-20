---
title: "CallOptions Type"
source_id: 25322
source_url: https://wiki.genexus.com/commwiki/wiki?25322
genexus_version: "18"
---

# CallOptions Type

[CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) are used to specify at runtime the transitions, behavior, and position in a call to a particular [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).  
  
The Type gives control over how the call stack is affected when a call is made and also defines what happens to the execution of the event that makes the call to the Panel.

By default the behavior is as follows:

The Panel being called appears, stays in the call stack, and the caller waits for it to return in order to continue the execution of the event.

Using the "call type" you can call a Panel as a Popup, call a Panel contextually (Callout), or call it replacing the current Panel in the stack.

To do this, you need to set the Type property of the CallOptions object, whose values are defined in the **enumerated domain** called **CallType.**

Values:

* Push
* Replace
* Popup
* Callout

The syntax to change the default behavior at runtime is:

```
<object name>.CallOptions.Type = CallType.<call type name>
```

## [Available call types](#Available+call+types)

### [Push](#Push)

This is the default behavior, the called Panel appears in the same space as the caller and the caller waits for its return to continue execution.

### [Replace](#Replace)

The called Panel replaces the caller in the call stack -this will save memory space-. It means that when you call a Panel using this call type, the call terminates the execution of the current event (since the Panel that is executing the event is removed from the stack). A call of this type must be the last line of the caller event.

### [Popup](#Popup)

The size of the popup can be changed with the following parameters from the CallOptions (these parameters only apply when the Type is Popup or Callout):

```
<object name>.CallOptions.TargetSize = CallTargetSize.<Panel Size Type>
```

The values of PanelSizeType can be:

* Default  (Platform Default)
* Small
* Medium
* Large

Also, a custom size can be defined by setting the values for Target Height and Width as follows:

```
CallOptions.TargetHeight = "dips or percentage of the parent height"
CallOptions.TargetWidth = "dips or percentage of the parent width"
```

**NOTE:**[Target](https://wiki.genexus.com/commwiki/wiki?25323) property does not apply when CallType = Popup.

#### [iPhone Support](#iPhone+Support)

As of [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46068,,), the Popup option when using iPhone with iOS 13 or above can have a Small or Medium Target Size (they behave in tha same way, with the popup not covering the whole screen, but allowing to see the application bar of the Panel bellow).

In previous GeneXus versions or older iOS versions, the Popup is always shown with a Large Target Size, covering the entire screen.

### [Callout](#Callout)

 When using this call type, the call can be canceled by touching on any item outside called Panel interface. The call to the Panel is not modal.

#### [Compatibility](#Compatibility)

This call type is fully supported on iPad only.

The Callout Type is not implemented in Android, it behaves like the Popup option in that platform.

Since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,), the Callout option when using iPhone is equivalent to a Popup with Small size in iOS 13 and above. In older GeneXus versions or older iOS versions, it is equivalent to a full-screen Popup.


|  |
| --- |
| **Backlinks** |
| [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) | [CallOptions Target](https://wiki.genexus.com/commwiki/wiki?25323) |
| [DynamicCall External Object](https://wiki.genexus.com/commwiki/wiki?47056) | [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) | [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) |

---
