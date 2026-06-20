---
title: "Kafka Producer and Consumer External Objects (GeneXus 18 Upgrade 11 or prior)"
source_id: 59989
source_url: https://wiki.genexus.com/commwiki/wiki?59989
genexus_version: "18"
---

# Kafka Producer and Consumer External Objects (GeneXus 18 Upgrade 11 or prior)

This document describes the steps to send and receive messages through the Publish-Subscribe API of Apache Kafka using some external objects provided for that specific purpose.

The provided External Objects are used to configure parameters, send and receive the messages. The implementation is based on [Kafka Consumers](https://www.safaribooksonline.com/library/view/kafka-the-definitive/9781491936153/ch04.html#callout_kafka_consumers__reading_data_from_kafka_CO2-1).

### [Steps](#Steps)

* Get a Connection to Apache Kafka
  + See the Appendix for a local installation
* Open a KB with [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?39737,,)
* Download [Kafka API Jars](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40594,,) for Java, [Kafka API Dlls](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40595,,) for .NET Framework or [Kafka API NetCore Dlls](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45797,,) for .NET.
  + Unzip/copy them to the Environment directory. In the case of Java, add them to the classpath too.
* Import [Kafka API External Object and Sample code](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?40596,,)

### [Sample](#Sample)

#### [Consumer](#Consumer)

The consumer can be a daemon that is running all the time waiting for new events. The Consumer method asks the queue or stream for new events and gets a collection of Key-Value.

```
&Consumer.Configuration = "{'bootstrap.servers': 'localhost:9092', 'group.id': 'mi-nuevo-grupo3', 'auto.offset.reset': 'earliest', 'request.timeout.ms': 500}"
&Timeout = 10000
do while (true)
    &ListMessagingResponse.Clear()
    &Consumer.Consume(!"Topic1", &Timeout, &ListMessagingResponse)    //&ListMessagingResponse is a Collection of Key, Value, Topic and Error info.
    PrintResponse(&ListMessagingResponse)
enddo
```

#### Producer

The Producer is asynchronous, which lets to add events to the stream massively. The External Object has a Finish method which waits until all the events are added to the stream.

```
&Producer.Configuration = "{'bootstrap.servers': 'localhost:9092', 'default.topic.config': {'message.timeout.ms': 10000}}"
do while(true)
    &ListMessagingResponse.Clear()
    &Text = GetTextToSend()  // &Text is a string with the message that is sent​.
    &OK = &Producer.ProduceAsync("Topic1", "key_1" ,&Text )
    &ListMessagingResponse = &Producer.Finish(1500)  //Waits up to 1.5 seconds for finishing sending messages. 
    if (&ListMessagingResponse.Count <> 1)
        msg("Some error ocurred", status)    
    endif
    PrintResponse(&ListMessagingResponse)
enddo
```

### [See Also](#See+Also)

* [Queue Data Type](https://wiki.genexus.com/commwiki/wiki?6913)
* [Submit command](https://wiki.genexus.com/commwiki/wiki?15386)

### [Appendix - Tips for testing Kafka](#Appendix+-+Tips+for+testing+Kafka)

1.- Follow the steps of this article  
<https://devops.profitbricks.com/tutorials/install-and-configure-apache-kafka-on-ubuntu-1604-1/>

2.- Configure the file kafka<numberversion>/config/server.properties adding the line:  
advertised.host.name = <ipmachine>

3.- To test from Windows, you can download <http://www.kafkatool.com/>
