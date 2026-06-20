---
title: "QueueMessage Data Type"
source_id: 6914
source_url: https://wiki.genexus.com/commwiki/wiki?6914
genexus_version: "18"
---

# QueueMessage Data Type

The QueueMessage Data Type defines the messages that are sent/received once the connection to the message queue is established (see [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913)).

### [Properties](#Properties)

|  |  |
| --- | --- |
| Text | Is the text of the message sent or received. |
| Priority | Indicates the message priority. |
| MessageID | Allow to set the messageID of the message |
| CorrelationID | Allows to set the CorrelationID of the message |
| Properties | Collection of properties that allows to send custom headers in a message |

**Text**

This is the text contained in the message that is sent or received.

```
&message.text = "This is a message"
```

**Priority**

Indicates the priority of the message. It may be anywhere from 0 to 9.

```
&message.priority = 7 
```

**MessageID**

Indicates the ID of the message (only some message queues allow to set the ID from the client, if it is not allowed this property will be ignored)

```
&message.MessageID = "ID" 
```

**CorrelationID**

Indicates the Correlation ID of the message.

```
&message.CorrelationID = "CorrID" 
```

**Properties**

Collection of properties that allows to send custom headers in a message

```
&message.properties.set(&header_name,&header_value)
&header_value = &message.properties.get(&header_name)
```

### [Complete example of how messages are sent and received](#Complete+example+of+how+messages+are+sent+and+received+)

&queue = Queue Data Type  
&message = QueueMessage Data Type  
&char = Character

**1. Provider settings**

<JMS\_Providers>  
 <Provider>  
   <Name>queueProvider</Name>  
   <User></User>  
   <Password></Password>  
   <Type>Queue</Type>  
   <Factory>com.sun.enterprise.naming.SerialInitContextFactory</Factory>  
   <URL>iiop://myserver:1050</URL>  
   <JNDI\_ID>QueueConnectionFactory</JNDI\_ID>  
   <Queue\_Name>Queue</Queue\_Name>  
 </Provider>  
</JMS\_Providers>

**2.** **Sending a m****essage**

&queue.Provider=queueProvider  
&ret = &queue.Connect()

//

&message.Text = "First message"  
&message.Priority = 7  
&char = &queue.Send(&message)  
//  
&message.Text = "Second Message"  
&message.Priority = 6  
&char = &queue.Send(&message)

**3. Receiving a message**

```
&queue.Provider = queueProvider 
&ret = &queue.Connect() 

for &message in &queue 
      msgbox(&message.text) 
endfor 
&queue.Disconnect()
```

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908)  
**Languages:** Java, .NET  
**Interfaces:** Web


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913) |

---
