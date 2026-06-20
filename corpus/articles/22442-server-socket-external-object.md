---
title: "Server.Socket external object"
source_id: 22442
source_url: https://wiki.genexus.com/commwiki/wiki?22442
genexus_version: "18"
---

# Server.Socket external object

The purpose of using Sockets is to allow executing actions in real time so that the server sends content to the browser without being solicited by the client, and vice-versa.

Therefore, the user doesn't need to refresh the web browser or the app (the clients) to get the information in real time. For example online chat/messaging systems and monitoring consoles.

To use Sockets in web, you must configure the [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) to "Smooth".

## [Server.Socket API](#Server.Socket+API)

The Server.Socket API consists of the Server.Socket [external object](https://wiki.genexus.com/commwiki/wiki?5670,,) and the NotificationInfo SDT.

### [Server.Socket External Object](#Server.Socket+External+Object)

An external object called Server.Socket exposes all the methods and properties needed for this functionality.

`[imagen omitida: wiki id 46266]`

#### [Server.Socket external object methods](#Server.Socket+external+object+methods)

|  |  |  |
| --- | --- | --- |
| **Method** | **Description** | **Most common use case** |
| Server.Socket.Notify(NotificationInfo sdtNotification): Numeric | Send a notification to the user who originated the action. It is valid during the entire session. | Give feedback to a user when a submitted procedure has finished - if the submit action has been executed from the user's session. |
| Server.Socket.NotifyClient(String clientId, NotificationInfo sdtNotification ): Numeric | Send a notification to a given user. | To implement a chat, only some users will receive the notification. |
| Server.Socket.Broadcast(NotificationInfo sdtNotification) | Send a notification to all connected users. | To send an alert to all users. |
| Server.Socket.NotifyClientText(String clientId, String Message ): Numeric | Send a "raw" message to a specific client. |  |

#### [Server.Socket external object properties](#Server.Socket+external+object+properties)

|  |  |
| --- | --- |
| Server.Socket.ClientId: String | Get the ClientId of the current session. |
| ErrCode | Error Code |
| ErrDescription | Error Message |

#### [Server.Socket methods - Error Codes](#Server.Socket+methods+-+Error+Codes)

|  |  |
| --- | --- |
| 0 | OK |
| 1 | Could not start WebSocket Server |
| 2 | WebSocket Session not found |
| 3 | WebSocket Session is closed or invalid |
| 4 | Message could not be delivered to client |

### [NotificationInfo Structured Data Type](#NotificationInfo+Structured+Data+Type)

The NotificationInfo SDT is provided to specify the notification information that will be sent to the above methods (Notify, NotifyClient, BroadCast) of the Socket.Server external object.

`[imagen omitida: wiki id 32304]`

|  |  |
| --- | --- |
| Id | By identifying the notification, the developer is able to specify which control has to capture it. |
| Object | By specifying this property, the developer can determine which object has to listen to this notification (especially in case of Broadcast) |
| Message | Message of the notification. |

## [Samples](#Samples)

### [Sample: How to send a notification to everyone (Broadcast)](#Sample%3A+How+to+send+a+notification+to+everyone+%28Broadcast%29)

Suppose that you are implementing a messaging system where you need to notify any post made by a user. In this case, we load the NotificationInfo SDT with the data of the post message. Next, we use the Server.Socket external object to broadcast the message.

```
//&NotificationInfo is NotificationInfo SDT data type. &PostId is the identifier of the post.

&NotificationInfo.Id=&PostId.ToString()
//The following is an SDT where data to be notified is loaded. You can send any data because it is sent in json format. First load an SDT with this data.
&commentNotificationInfo.PostId = &PostId
&commentNotificationInfo.PostCommentContent = &PostCommentContent

//Now assign the data to be sent to the NotificationInfo SDT in json format.
&NotificationInfo.Message=&commentNotificationInfo.ToJson()
&socket.Broadcast(&NotificationInfo) //&socket is Server.Socket external object data type
```

### [Sample: How to receive the notification](#Sample%3A+How+to+receive+the+notification)

In the web object that will receive the notification, use the OnMessage event that receives a variable based on the NotificationInfo SDT data type. The notification information will be processed there.

```
Event OnMessage(&NotificationInfo)
for each line
  if (&NotificationInfo.Id=&postid.ToString())
   //processs the notification data
  endif
endfor
Endevent
```

### [Sample: How to send a notification to a specific client](#Sample%3A+How+to+send+a+notification+to+a+specific+client)

Consider a system where only a specific client has to be notified. This client is identified by using the ClientId property of the Server.Socket external object.

Below is the web panel that receives the notification. In the start event, we save the &clientId so we can identify the session afterward.

```
Event Start
    &clientId = &socket.ClientId
   //save the information of the client: RegisteredClientId = &clientId//
Endevent
```

In the procedure that sends the notification, we get the &ClientId (that may have been saved in the database). The Notifyclient method is executed by passing the &ClientId as a parameter, so only that client will receive the message.

```
&ClientId = RegisteredClientId
&NotificationInfo.Id=&cont.ToString()
&NotificationInfo.Message="El mensaje " + &cont.ToString() + "cliente " + &ClientId
&socket.NotifyClient(&ClientId, &NotificationInfo)
```

**Note**: As since GeneXus 15 upgrade 3, you can use the [ClientInformation.Id Property](https://wiki.genexus.com/commwiki/wiki?20198) instead of using &socket.ClientId.

### [As in the previous example, the web panel that receives the message has to implement the OnMessage Event.](#As+in+the+previous+example%2C+the+web+panel+that+receives+the+message+has+to+implement+the+OnMessage+Event.)

```
Event onmessage(&notificationInfo)
    //Do something with the &notificationInfo
endevent
```

**Notes:**

* Remember that the broadcast method should only be executed when the message is public because it is sent to all the browser instances which are subscribed to the notification event.
* The same user event (even if it has different parameters) will be executed on the server only once in a range less than 100ms ([SAC #48220](https://www.genexus.com/developers/websac?es,,,48220))

### [Requirements](#Requirements)

See [Web Notifications and Progress UC requirements](https://wiki.genexus.com/commwiki/wiki?27740)

[Here](http://caniuse.com/#feat=websockets) is a list of Web Browsers that support web sockets. Note that Web Notifications can be received on Smart Device Apps using the [Component Domain](https://wiki.genexus.com/commwiki/wiki?16186), taking into account the OS version indicated in the link. For Smart Devices Applications, you may use it in conjunction with the Client.Socket External Object.

### [Troubleshooting](#Troubleshooting)

* The following line can be added at the end of the gxgral.js file "gx.dbg.enabled = true;" in order to get additional information in the javascript console.
* Warning Message: "Warning: WebNotifications are not supported with "Web User Experience": "Previous versions". You must use Smooth.". Web Notifications are only supported with [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449): "Smooth".

### [See Also](#See+Also)

[Html5 Web Notifications User Control](https://wiki.genexus.com/commwiki/wiki?21082,,)  
[HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527)  
[HowTo: Receiving and processing a notification message from an external app](https://wiki.genexus.com/commwiki/wiki?33633)  
[HowTo: Using WebNotifications for a Specific Client](https://wiki.genexus.com/commwiki/wiki?31559,,)


|  |
| --- |
| **Backlinks** |
| [Client.Socket External Object](https://wiki.genexus.com/commwiki/wiki?41299) | [ClientInformation.Id Property](https://wiki.genexus.com/commwiki/wiki?20198) |
| [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [KB:HowTo : Create a chatbot with human fallback](https://wiki.genexus.com/commwiki/wiki?46255) | [HowTo: Receiving and processing a notification message from an external app](https://wiki.genexus.com/commwiki/wiki?33633) | [HowTo:Develop a messaging web page](https://wiki.genexus.com/commwiki/wiki?22527) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Load Command and Load Method in User Events](https://wiki.genexus.com/commwiki/wiki?22555) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) |
| [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) | [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [Socket API use Sample](https://wiki.genexus.com/commwiki/wiki?41445) | [Web Notifications and Progress UC requirements](https://wiki.genexus.com/commwiki/wiki?27740) |
| [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) |

---
