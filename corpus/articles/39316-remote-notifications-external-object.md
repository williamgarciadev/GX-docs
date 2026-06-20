---
title: "Remote Notifications External Object"
source_id: 39316
source_url: https://wiki.genexus.com/commwiki/wiki?39316
genexus_version: "18"
---

# Remote Notifications External Object

**Deprecated**: Since [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,). Replaced by [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687).

[Push Notifications in Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?19945) are sent using this [External Objects for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17880).

`[imagen omitida: wiki id 32073]`

## 

## [Send Notifications](#Send+Notifications)

If you need to send notification or a list of Notifications, you can use the *Add* and *Send* methods in conjunction. 1

First, you need to create a list of RemoteNotification objects and add them to the Notifications local variable using the Add method. Then use the Send method to deliver the notifications and check the return value (a collection of RemoteNotificationResult objects).

`[imagen omitida: wiki id 32074]``[imagen omitida: wiki id 32075]`

For instance, the following code section loads a list of Notifications which are sent with the Send method; the result is validated.

```
&ErrCode = &Notifications.OpenSession('SampleNotifications')  //Name of Dashboard or SDPanel which enabled notifications.

for each
  &RemoteNotification = new()
  &RemoteNotification.DeviceType = DeviceType
  &RemoteNotification.DeviceToken = DeviceToken.Trim()
  &RemoteNotification.Message = 'Remote Message'
  &RemoteNotification.Badge = '1'
  &Notifications.Add(&RemoteNotification)
endfor

&RemoteNotificationResult = &Notifications.Send()

for &i = 1 to &RemoteNotificationResult.Count
  msg(&RemoteNotificationResult.Item(&i).ErrorDescription, status)
endfor
```

Note: OpenSession and Send methods must be invoked outside the loop that loads the devices on the Notifications collection (i.e. based on **RemoteNotifications external object**).

### [Error Codes](#Error+Codes)

|  |  |
| --- | --- |
| **ErrorCode** | **ErrorDescription** |
| -1 | Unknown device type |
| 0 | Ok |
| 1 | notifications.json not found |
| 2 | Invalid Application ID |

## [Execute an event on the Device](#Execute+an+event+on+the+Device)

Many times sending a Push Notification to invoke the application is not enough, our users expect that an action is executed when they open the received notification.

For example, when you get a Push Notification on the Facebook App that Rachel wants to be Friends with you and you execute the push notification, is not enough to open Facebook App, you expect to open the dialogue to accept or decline Rachel friend proposal.

To do that with GeneXus you need to:

1. Setting the Event Name (as well as their parameters) that will be invoked, on the *Notifications* variable.
2. Define that event on the main object of the app.

### 

### [1. Setting the Event Name](#1.+Setting+the+Event+Name)

This is done using the *Event* node of the *RemoteNotification* SDT.  
There we can indicate which event must be executed and when, as well as including parameters and their values, necessary in this case.

`[imagen omitida: wiki id 32838]`

Domains definitions

* **EventExecution** - Enumerated.  
  - *OnLauchByUser*   
  The event is executed when the user launches the application trough the notification.  
  **-** *OnNotificationArrive*   
  Only available since iOS7 -for iOS 6 or earlier, this value acts the same as OnUserPress.  
  With this value, the event will be executed when the notification arrives at the device, even if the app is inactive. A particular case for this option is when a notification has no message, badge or sound. It's a notification that executes an event and the user does not detect, ie: Get the location of the device remotely or to trigger synchronization of data in case of an offline app. This option is also known as "Silent Notification"
* **PushNotificationPriority** - Enumerated  
  - *High*  
  - *Normal*

**Code sample**

The developer can define on a Web Panel the following event in order to send a notification to all the registered devices.

```
Event 'RemoteNotification'
    &ErrCode = &Notifications.OpenSession('MySDMainObject')  
    For each 
        &RemoteNotification = new()
        &RemoteNotification.DeviceType = DeviceType
        &RemoteNotification.DeviceToken = DeviceToken.Trim()
        &RemoteNotification.Message = "Look at this new product!"
        &RemoteNotification.Event.Name = 'ViewProduct'             
        &RemoteNotification.Event.Execution = EventExecution.OnLauchByUser
            
        &Parameter.Name = "Product"             
        &Parameter.Value = &ProductId.ToString()
        &RemoteNotification.Event.Parameters.Add(&Parameter)
        
        &Notifications.Add(&RemoteNotification)
    Endfor
    &RemoteNotificationResult = &Notifications.Send()
    for &i = 1 to &RemoteNotificationResult.Count
          msg(&RemoteNotificationResult.Item(&i).ErrorDescription)
    endfor
Endevent
```

In this sample, the **&Parameter** variable is based on RemoteNotification.Event.Parameter SDT.

An alternative to send notifications is through Call or CallActions methods (poor performance for batch sending, use Send method instead).

```
Event 'RemoteNotificationCall' 
  For each 
     &RemoteNotification.Call('MySDMainObject',DeviceType,DeviceToken,"Look at this new product!")
  Endfor 
Endevent
```

```
Event 'RemoteNotificationCallActions'
  For each
    &RemoteNotification.CallActions('MySDMainObject',DeviceType,DeviceToken,"Look at this new product!",&NotificationParameters)
  Endfor
Endevent
```

where **&NotificationParameters** variable is based on *NotificationParameters external object*.

### [2. Define the Event on the Main App](#2.+Define+the+Event+on+the+Main+App)

In order to execute the Event previously defined when the user taps on the notification message, you need to set that event on the Main object app.

#### [**2.1 Define Notification Event on SD Panels / WWSD**](#2.1+Define+Notification+Event+on+SD+Panels+%2F+WWSD)

Define a new [Action](https://wiki.genexus.com/commwiki/wiki?20623) with the exact name of the Event Name field of the *RemoteNotifications* SDT variable.

If the event receives parameters, you need to define variables with the exact name of the Parameters Name field of the *RemoteNotifications*SDT variable.

*Code Sample*  
Continue with the previous example, in this case, the event will be defined as follows:

```
Event 'ViewProduct'
    Composite
        &ProductId = &Product.Trim().ToNumeric()
        WorkWithDevicesProduct.Product.Detail(&ProductId)
    Endcomposite
Endevent
```

#### [**2.2 Define Notification Event on Dashboards**](#2.2+Define+Notification+Event+on+Dashboards)

First, add the notification node:  
`[imagen omitida: wiki id 33763]`

Add an action to the Notification node:  
`[imagen omitida: wiki id 33764]`

This will add an action that is not going to be visible on the dashboard, but you can invoke it from the push notification, putting its name on the Event Name field of the RemoteNotification SDT.

The event of this action will be executed when the push notification is invoked on the device.

## [Set a Badge on the Application icon](#Set+a+Badge+on+the+Application+icon)

Another option when sending a Push Notification is to display a number on the application icon. The badge is the number within a red circle that appears on an application’s home screen icon. The badge is used to denote the number of unread or otherwise unattended-to pieces of content within the app, e.g., unread messages, top news stories or waiting for actions inside the application.

For this scenario, you need to set the value you want to show to the user in the Badge field of the RemoteNotification SDT and send that notification.  
Notice that you need to calculate the number of notifications sent on the server side, tracking the number of notifications sent to each device.

Also, if it is needed to reset this number you can send a push notification with an empty badge.

**NOTE:** Badges only exist in iOS apps.

## [Notes](#Notes)

* WARNING: The event defined in the main app with OnNotificationArrive mode cannot contain any command, function or control that includes UI (such as msg, confirm, etc). Remember that this kind of notifications can arrive with the device locked, with the app running on *background*, and even when the app *not running*. However, this can be done if the app is running on *foreground*(the developer must check it through [Interop.ApplicationState property](https://wiki.genexus.com/commwiki/wiki?23734)).

## [Availability](#Availability)

1Add, Send and SetConfiguration Methods of the Notifications External Object are only available for .NET as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,)
