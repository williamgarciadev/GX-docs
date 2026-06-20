---
title: "Queue Data Type"
source_id: 6913
source_url: https://wiki.genexus.com/commwiki/wiki?6913
genexus_version: "18"
---

# Queue Data Type

The Queue data type enables you to establish a connection to a message queue and allows you to send and receive messages to and from the queue. This data type will therefore make it possible to develop applications that require interaction with other applications that are not connected, with all the advantages of this type of programming, such as asynchronic communication and processing.

### [**Description**](#Description)

The Queue data type will allow you to establish a connection to a message queue. Once this connection is established, you will be able to send and receive messages to and from the queue. The messages sent are defined by the [QueueMessage data type](https://wiki.genexus.com/commwiki/wiki?6914), which consists of a text and a priority (see [QueueMessage data type](https://wiki.genexus.com/commwiki/wiki?6914)).

The Queue data type enables you to establish a connection to the two types of existing queues:

* Point to point: a message is sent to the queue and then a client consumes the message (which then no longer exists in the queue). This means that once a message has been sent, a client can then connect to the queue and retrieve the message (if it hasn't been consumed yet).
* Publish / Subscribe: a message is sent to the queue and only the clients that are already connected to the queue will be able to receive the message. If a client connects to the queue after the message has been sent, this client won't receive the message.

### [**Properties**](#Properties)

|  |  |
| --- | --- |
| Provider | Indicates the provider of the queue to be used, defined in the jms.xml file. |
| User | Overwrites the user setup in the provider. |
| Password | Overwrites the password setup in the provider. |
| Browse | Indicates whether the messages will be kept in the queue or if they will be removed from it. |
| errCode | Indicates the error code in case an error happened when a method was executed, returns 0 otherwise |
| errDescription | Indicates the error detail in case an error happened |

**Provider**

Indicates who the provider of the queue to be used is. The name of the provider must have previously been defined in the jms.xml file (see Defining providers). This file must be located in the application directory (DATANNN).

**User**

Overwrites the user setup in the provider.

&queue.user = "myUser"

**Password**

Overwrites the password setup in the provider.

&queue.password = "myPassword"

**Browse**

Indicates whether the messages will be kept in the queue or if they will be removed from it.

The default value is False.

&queue.browse = True

**errCode**

Read only property, Indicates the error code in case an error happened when a method was executed, returns 0 otherwise

Default value 0

&errcode = &queue.errCode

**errDescription**

Read only property, Indicates the error detail in case an error happened

&errDsc = &queue.errDescription

### [**Methods**](#Methods)

|  |  |
| --- | --- |
| Connect | Establishes a connection with the queue defined in Provider. |
| Disconnect | Ends the connection with the queue. |
| Send | Sends a message to the queue. |
| Commit | Commits all the messages that haven't been commited. |
| Rollback | Rollbacks all the messages that haven't been commited. |

**<Boolean> = Connect()**   
  
Establishes a connection with the queue defined in provider. It returns True if the connection was possible and False if it was not possible.  
  
&Boolean = &queue.connect()  
  
**Disconnect**  
  
Ends the connection with the queue.  
  
&queue.disconnect()  
  
**<String> = Send(QueueMessage message)**   
  
Sends a message to the queue. If the message was sent successfully, it returns its ID; otherwise it returns "".  
  
&char = &queue.send(&queueMessage)  
  
**Commit**  
  
Sends all the messages that weren't commited to the queue (if Queue\_AutoCommit = NO. See "Defining Providers").  
  
**Rollback**  
  
Rollbacks all the messages that haven't been sent to the queue (if Queue\_AutoCommit = NO. See "Defining Providers").

### [Processing messages](#Processing+messages+)

To process the messages you must use the "For in" command as follows:  
  
For &message in &queue  
 ... //Work with &message   
EndFor

### [Defining Providers](#Defining+Providers+)

**Defining Providers in Java**   
  
To define a provider it is necessary to create a jms.xml file under the application directory. This file will contain information on different providers. The following is a complete example of a jms.xml file.  
  
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
<Queue\_AutoCommit>YES</Queue\_AutoCommit>  
 </Provider>   
 <Provider>   
    ....   
 </Provider>    
</JMS\_Providers>

|  |  |
| --- | --- |
| <Name> | Provider's name. This name will then be used in GeneXus when connecting to the queue (&queue.Provider = queueProvider). |
| <User> | The user's identification. |
| <Password> | Password of the user specified at <User> |
| <Type> | The type can be either a Queue or a Topic depending on the destination defined in the server. |
| <Factory> | This is the initial context factory class, which is different for every server. For J2EE application servers, it's: com.sun.enterprise.naming.SerialInitContextFactory. For OpenJMS servers, it's: org.exolab.jms.jndi.InitialContextFactory. |
| <URL> | The URL of the server. |
| <JNDI\_ID> | Name of the connection factory previously defined in the server. |
| <Queue\_Name> | Name of the queue (the destination previously defined in the server). |
| <Queue\_AutoCommit> | Indicates if the messages will have to be commited or not. If "NO" is specified, messages will be stored in memory and it will be necessary to make &queue.commit() in order to send them. If "YES" is specified, there is no need to make &queue.commit() because they will be automatically sent every time the &queue.Send() method is invoked. |

For further information, see "Creating queues with J2EE Software Development Kit (SDK) version 1.3.1".  
  
**Defining Providers in .NET**   
  
In .NET the provider must be defined in the client.exe.config file for command line programs or web.config file of the web application. Under AppSetting, you need to add:  
  
<add key="<Queue-ProviderName>" value="<server>\<queue>"/>  
  
Where ProviderName is the name that is going to be set to &queue.provider property, <server> is the name of the server and <queue> is the name of the queue defined in the server. When defining the queue, take into account that you must include the prefix "Queue" in the definition, but that the prefix is not used from GeneXus (only the ProviderName is used): For example:  
  
In client.exe.config:  
  
<add key="Queue-MyFirstQueue" value="paul-xp\myQueue"/>  
  
Then from GX you must use:  
  
&queue.provider = "MyFirstQueue"  
  
In order to define a message queue in .NET you must have previously installed the Messsage Queuing service. After that you will be able to create a Queue. Note that when creating the queue, you can either set it as a transactional queue or not. If transactional is set to NO, the commit and rollback methods of the message queue data type will be disabled and messages will automatically be sent in the "Send" method (so it won't be necessary to commit the messages).

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** Java, .NET, Ruby (up to GeneXus X Evolution 3)  
**Interfaces:** Web


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Kafka Producer and Consumer External Objects](https://wiki.genexus.com/commwiki/wiki?40593) | [Messaging with ActiveMQ and GeneXus](https://wiki.genexus.com/commwiki/wiki?8625) |
| [QueueMessage Data Type](https://wiki.genexus.com/commwiki/wiki?6914) |

---
