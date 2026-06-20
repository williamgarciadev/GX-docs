---
title: "Chronometer Control"
source_id: 25058
source_url: https://wiki.genexus.com/commwiki/wiki?25058
genexus_version: "18"
---

# Chronometer Control

The Chronometer control gives you the possibility to execute an event after a certain time or simply to show a chronometer on the screen. This could be useful in applications like quizzes (for timing the answers), applications that show something on the screen for a while and hide it automatically, among other functionalities.

**Warning:** As of Android 8.0, Chronometer control could not work properly when it is [invisible](https://wiki.genexus.com/commwiki/wiki?8849). Consider set height of control row with 0 dips in order to achieve the same aim.

## [Using the control](#Using+the+control)

This control can only be applied to Attribute/Variables of numeric type. After dragging the variable to the form, you should set its Control Type property to "Chronometer".

It is valid for both Web and Mobile applications as well.

### [Web Panels](#Web+Panels)

`[imagen omitida: wiki id 29950]`

### [Panels for Smart Devices or WorkWithDevices](#Panels+for+Smart+Devices+or+WorkWithDevices)

`[imagen omitida: wiki id 29951]`

## [Properties](#Properties)

|  |  |
| --- | --- |
| **Tick Interval** | Indicates the frequency in seconds in which the Tick event will be called. |
| **Max Value** | The max value that the chronometer can take. |
| **Max Value Text** | The text associated with the variable when it reaches its max value. |

## [Methods](#Methods)

|  |  |
| --- | --- |
| **Start** | Starts the chronometer. It will start from the value (in seconds) of the attribute/variable associated with the control. |
| **Stop** | Stops the chronometer. |
| **Reset** | Set to 0 the chronometer value. |

## [Events](#Events)

|  |  |
| --- | --- |
| **Tick** | This event will be executed every time the value indicated in the tick interval property is elapsed.  *Note*: The timer needs to be started in order to make the Tick event to execute. When the timer stops, the Tick event will stop its execution. |

## [Example](#Example)

```
Event &Var1.Tick
    &count +=1
    if &count = &Somevalue
       //do something
    endif
EndEvent

Event 'Start'
    &Var1 = 55
    &Var1.MaxValue = 60
    &Var1.Start()
EndEvent
```

## [Scope](#Scope)

**Generators:**[Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

## [See Also](#See+Also)

[SD Chronometer Control - Android Sample](https://wiki.genexus.com/commwiki/wiki?28516,,)


|  |
| --- |
| **Backlinks** |
| [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) |
| [Tick Interval property](https://wiki.genexus.com/commwiki/wiki?42188) |

---
