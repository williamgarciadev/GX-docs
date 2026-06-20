---
title: "Messaging with ActiveMQ and GeneXus"
source_id: 8625
source_url: https://wiki.genexus.com/commwiki/wiki?8625
genexus_version: "18"
---

# Messaging with ActiveMQ and GeneXus

To use ActiveMQ as message broker, in addition to the [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913) documentation, here you have a brief tutorial.

## [Install ActiveMQ 5.1](#Install+ActiveMQ+5.1)

You may download the ActiveMQ from this [link](http://activemq.apache.org/download.html) and installation-related aspects from [here](http://activemq.apache.org/getting-started.html). The installation is merely decompressing a zip![](/commwiki/static/FCKEditor/editor/images/smiley/msn/regular_smile.gif).  
  
The requirement is JDK 1.5 (Java 5) and Windows XP-SP2 or Windows 2000.

### [To lift the service](#To+lift+the+service)

Open an MS-DOS console (Start button > Execute > cmd), go to the installation directory (Ex:"C:\apache-activemq-5.1.0") and enter "bin\activemq" (DO NOT stand on the bin directory, see [note](http://activemq.apache.org/getting-started.html#GettingStarted-StartingActiveMQ)).

You may verify that the service is OK with "http://localhost:8161/admin/index.jsp", which is the administration web console.

### [To stop it](#To+stop+it)

Press Ctrl-C in the same MS-DOS console.

## [Configuration of a GeneXus Java environment](#Configuration+of+a+GeneXus+Java+environment)

To use ActiveMQ, the following files must be referenced in the classpath:

jndi.properties (see further ahead)  
javaee.jar (JavaEE SDK 5.05, obtain from the [Sun](http://java.sun.com/javaee/downloads/index.jsp) site)  
activemq-core-5.1.0.jar (comes with ActiveMQ)  
commons-logging-1.1.jar (comes with ActiveMQ)

#### [File jndi.properties](#File+jndi.properties)

You can see the JNDI support documents in this [link](http://activemq.apache.org/jndi-support.html).  
  
Below is the content of a jndi.properties file where connectionFactoryNames are specified and the Queues defined in the ActiveMQ are recorded.  
In this case, the jndimqtest queue has been recorded, referring to the mqtest queue recorded previously on the administration web console of ActiveMQ.

```
# START SNIPPET: jndi

java.naming.factory.initial = org.apache.activemq.jndi.ActiveMQInitialContextFactory

# use the following property to configure the default connector
java.naming.provider.url = vm://localhost

# use the following property to specify the JNDI name the connection factory
# should appear as. 
connectionFactoryNames = connectionFactory, queueConnectionFactory, topicConnectionFactry

# register some queues in JNDI using the form
# queue.<jndiName> = <physicalName>
queue.jndimqtest = mqtest

# register some topics in JNDI using the form
# topic.<jndiName> = <physicalName>
topic.MyTopic = example.MyTopic

# END SNIPPET: jndi 
```

Should you not want to configure the queue in the activeMQ, then you may call a queue inside dynamicQueues, which is created automatically without using jndi.properties. To do this, enter the following in queueName:

<Queue\_Name>dynamicQueues/jndimqtest</Queue\_Name>

#### [File jms.xml](#File+jms.xml)

As you may have seen in the documentation of [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913), the definition of a Provider to be used in your application is done by creating a jms.xml file like the one shown below.

```
<JMS_Providers> 
 <Provider> 
   <Name>queueProvider</Name> 
   <User></User> 
   <Password></Password> 
   <Type>Queue</Type>
   <Durable></Durable>
   <ClientID></ClientID>
   <SubscriptionName></SubscriptionName>
   <Factory>org.apache.activemq.jndi.ActiveMQInitialContextFactory</Factory> 
   <URL>tcp://localhost:61616</URL> 
   <JNDI_ID>queueConnectionFactory</JNDI_ID> 
   <Queue_Name>jndimqtest</Queue_Name> 
 </Provider> 
</JMS_Providers>
```

### [GeneXus code Sample](#GeneXus+code+Sample)

The following are simple examples of send and receive events.

```
Event 'Send'
    &queue.Provider = 'queueProvider' 
    &ret = &queue.Connect() 
    &message.Text = &texto
    &message.Priority = 7 
    &char = &queue.Send(&message) 
    &queue.Disconnect()
EndEvent  // 'Send'

Event 'Receive'
    &queue.Provider = 'queueProvider' 
    &ret = &queue.Connect() 
    &texto = ''
    for &message in &queue 
        &texto += &message.text + newline() 
    endfor 
    &queue.Disconnect()
EndEvent  // 'Receive'
```

**Note**: The Support for Durable subscriber to Topic JMS was implemented in [GeneXus X Evolution 3 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?29463,,). See [SAC #38859](https://www.genexus.com/developers/websac?es,0,,38859;;</span>).

### [Considerations for Apache Tomcat](#Considerations+for+Apache+Tomcat)

* Place the jms.xml file in the webapp's WEB-INF folder.
* Place the jndi.properties file inside the classes folder.

You may download the xpz and files at: [ActiveMQ Java/Tomcat Sample](https://wiki.genexus.com/commwiki/wiki?40810,,)
