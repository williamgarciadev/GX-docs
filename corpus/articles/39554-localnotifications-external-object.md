---
title: "LocalNotifications external object"
source_id: 39554
source_url: https://wiki.genexus.com/commwiki/wiki?39554
genexus_version: "18"
---

# LocalNotifications external object

The LocalNotifications external object enables your app to alert users of scheduled events or alarms in the background, with no servers required.

|  |  |
| --- | --- |
|  |  |

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Properties](#Properties)

It does not have any.

### [Methods](#Methods)

#### [**CreateAlerts method**](#CreateAlerts+method)

Creates a set of local notifications (or alerts) by indicating when each of them will be triggered and the text that will be displayed. It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | alerts:LocalNotificationsInfo |

#### **ListAlerts method**

Lists every local notification (or alert) previously created.

|  |  |
| --- | --- |
| **Return value** | LocalNotificationsInfo |
| **Parameters** | None |

#### **RemoveAlerts method**

Removes a set of local notifications (or alerts), each of them identified by its triggered timestamp and its text. It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | alerts:LocalNotificationsInfo |

#### **RemoveAllAlerts method**

Removes every local notification (or alert) from the device. It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | None |

### Events

It does not have any.

### [LocalNotificationsInfo Structured Data Type](#LocalNotificationsInfo+Structured+Data+Type)

In addition to the LocalNotifications external object, the LocalNotificationsInfo [Structured Data Type object](https://wiki.genexus.com/commwiki/wiki?10021) is used to define the configuration of the Local Notification.

`[imagen omitida: wiki id 54568]`

It is a collection of items, each one containing the following:

* DateTime:[DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)  
  Indicates when the local notification will be triggered. If you do not set this field (you leave it empty), the notification will be triggered instantly.
* Text:[VarChar(128)](https://wiki.genexus.com/commwiki/wiki?6778)  
  Contains the text to be shown to the user as a local notification.
* Event:

  It allows defining an event to be executed when the user interacts with a local notification.

  + Name: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)  
    Name of the event that you want to execute.
  + Parameters:

    Allows you to define parameters in case the event needs them.

    - Item:
      * Name: [VarChar(40)](https://wiki.genexus.com/commwiki/wiki?6778)
      * Value: [VarChar(128)](https://wiki.genexus.com/commwiki/wiki?6778)

You can define as many Local Notifications as you want. A single item on the LocalNotificationsInfo collection is equivalent to one Local Notification.

#### [Sample](#Sample)

Consider a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with its [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True.

The Panel Layout contains a button that is associated with the 'NotificationEvent' event:

```
Event 'NotificationEvent'
 Composite
   &AlertDateTime = Now()
   &AlertDateTime = &AlertDateTime.AddSeconds(10)        
   &LocalNotItem = New() //The notification is created
   &LocalNotItem.DateTime = &AlertDateTime
   &LocalNotItem.Text = !'You have a new notification'
   &LocalNotItem.Event.Name = "EventCallType"   //Name of the event to be called. It must be defined in the Panel.
   &localNotEventsParameters.Name = "callParam" //Variable name defined in the Panel and used in the event to be called.
   &localNotEventsParameters.Value = "PopUp"    //Value assigned to the previous variable name.
   &LocalNotItem.Event.Parameters.Add(&LocalNotEventsParameters)
   &LocalNotInfo.Add(&LocalNotItem)
 EndComposite
Endevent
```

```
Event "EventCallType"
 Composite 
    InfoPanel.CallOptions.Type = &callParam //The &callParam value is "Popup"
    InfoPanel.Call(&callParam)              //The Panel is called with the chosen CallOptions Type as a parameter
 EndComposite
EndEvent
```

When tapping on the Panel button, the 'NotificationEvent' event is executed. This event loads a variable based on the LocalNotificationsInfo SDT. So, the EventCallType event will be executed when indicated (&AlertDateTime was assigned). In this example, the EventCallType event calls a Panel (InfoPanel) with the PopUp mode.

**Note**: Read about [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) and [CallOptions Type](https://wiki.genexus.com/commwiki/wiki?25322).

### [See Also](#See+Also)

[HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294)  
[Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) (servers required)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294) |
| [HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54591) | [LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54527) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
