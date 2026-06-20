---
title: "Relative Timer control"
source_id: 42490
source_url: https://wiki.genexus.com/commwiki/wiki?42490
genexus_version: "18"
---

# Relative Timer control

This article describes how to configure a control on the screen to count down to an event that will take place in the future or to express the time elapsed after the start of an event. For example, suppose it is 3 p.m. and an event is programmed for 4 p.m. You need to add a countdown that shows the number of minutes left for the event to begin. Also, if the event is currently taking place, you may want to show, for example, the time elapsed since the beginning of the event.

You can achieve this by defining an attribute or variable based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) and setting its Control Type property = Relative Timer.

You must assign a DateTime value to the attribute/variable, with which the control is initialized when the count is started.

### [**Properties**](#Properties)

|  |  |
| --- | --- |
| **[Format](https://wiki.genexus.com/commwiki/wiki?42530)** | Style with which the time interval will be displayed. |
| **[Units](https://wiki.genexus.com/commwiki/wiki?42251)** | Time units used to display the time interval. |
| **[Most Representative Unit Only](https://wiki.genexus.com/commwiki/wiki?42252)** | Indicates whether only the most significant unit of time should be displayed (truncating). |
| **[Counting Type](https://wiki.genexus.com/commwiki/wiki?42253)** | Sets if the Relative Timer control will make a countdown, count the elapsed time, or both. |
| **[Prefix Text](https://wiki.genexus.com/commwiki/wiki?42254)** | Text that precedes the relative time. |
| **[Suffix Text](https://wiki.genexus.com/commwiki/wiki?42255)** | Text to be displayed after the relative time. |
| **[Maximum Seconds](https://wiki.genexus.com/commwiki/wiki?42256)** | Sets a number of seconds such that when the counter becomes equal to or greater than it, the text set in the Maximum Text property is shown. |
| **[Maximum Text](https://wiki.genexus.com/commwiki/wiki?42257)** | Text to display after the elapse of the interval in seconds set in the Maximum Seconds property, since the start time. |
| **[Minimum Seconds](https://wiki.genexus.com/commwiki/wiki?42258)** | Sets a number of seconds such that when the counter becomes equal to or lower than it, the text set in the Minimum Text property is shown. |
| **[Minimum Text](https://wiki.genexus.com/commwiki/wiki?42259)** | Text to display after the elapse of the interval in seconds set in the Minimum Seconds property. |

### [**Themes**](#Themes)

It applies to the properties of the Attribute theme class.

### [**Events**](#Events)

**TimerStatusChanged**

This event is triggered when any of the following conditions are met:

* When the control starts to be executed.
* Relative time elapsed; that is to say, when the target time is reached, this event will be executed.
* The Maximum Seconds value has been reached.
* The Minimum Seconds value has been reached.

### [**Sample**](#Sample)

Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a variable based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370). Set the variable Control Type property = Relative Timer.

Program the Panel Start event as shown below:

```
Event Start
    &RelativeTimer    = Now()
    &RelativeTimer    = &RelativeTimer.AddMinutes(15) 
EndEvent
```

When executing the application, you will see the following:

`[imagen omitida: wiki id 42753]`

Suppose that once the countdown reaches zero, a text must appear indicating that the event is currently taking place. To achieve this, you have to use the TimerStatusChanged event associated with the control.

Add the third line of code to the Start event, as shown below:

```
Event Start
    &RelativeTimer = Now()
    &RelativeTimer = &RelativeTimer.AddMinutes(15)
    &TimerStarted    = False
EndEvent
```

Program the TimerStatusChanged event associated with the control as shown below:

```
Event &RelativeTimer.TimerStatusChanged
    Composite
        If &TimerStarted = False
          //The control start to be executed
            &TimerStarted = True
        Else
            &RelativeTimer.PrefixText = 'Live Now'
        EndIf
    EndComposite
EndEvent
```

#### [TimerStatusChanged event explanation](#TimerStatusChanged+event+explanation)

This event is executed and &TimerStarted = False. So, you enter the if statement, the counter starts counting, and the value of &TimerStarted is changed to True. When the counter reaches zero, the event will be triggered again, this time entering the else statement. So, the text 'Live Now' is assigned to the control's Prefix Text property.

When executing the application, you will see the following:

`[imagen omitida: wiki id 42813]`

##


|  |
| --- |
| **Backlinks** |
| [Counting Type property](https://wiki.genexus.com/commwiki/wiki?42253) | [Format property (for att/var with Control Type=Relative Timer)](https://wiki.genexus.com/commwiki/wiki?42530) |
| [Maximum Seconds property](https://wiki.genexus.com/commwiki/wiki?42256) | [Maximum Text property](https://wiki.genexus.com/commwiki/wiki?42257) | [Minimum Seconds property](https://wiki.genexus.com/commwiki/wiki?42258) | [Minimum Text property](https://wiki.genexus.com/commwiki/wiki?42259) |
| [Most Representative Unit Only property](https://wiki.genexus.com/commwiki/wiki?42252) | [Prefix Text property](https://wiki.genexus.com/commwiki/wiki?42254) | [Suffix Text property](https://wiki.genexus.com/commwiki/wiki?42255) | [Units property](https://wiki.genexus.com/commwiki/wiki?42251) |

---
