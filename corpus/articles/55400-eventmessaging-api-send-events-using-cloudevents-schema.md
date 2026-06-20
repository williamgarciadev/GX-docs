---
title: "EventMessaging API: Send Events using CloudEvents Schema"
source_id: 55400
source_url: https://wiki.genexus.com/commwiki/wiki?55400
genexus_version: "18"
---

# EventMessaging API: Send Events using CloudEvents Schema

The following example shows how to publish an event to [Azure Event Grid](https://wiki.genexus.com/commwiki/wiki?55354) based on CloudEvents Schema, using [SendEvent](https://wiki.genexus.com/commwiki/wiki?55337) method.

&CloudEvent is [CloudEvent SDT](https://wiki.genexus.com/commwiki/wiki?55339).

```
    &endpoint = !"https://eventgridcloud.eastus-1.eventgrid.azure.net/api/events"
    &accesskey = !"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    &EventRouter = AzureEventGrid.EventGridRouterProvider.Connect(&endpoint,&accesskey,&errorMessages,&IsSuccess)

    &CloudEvent = new() 
    &CloudEvent.source = !"GeneXusApp"
    &CloudEvent.type = !"Test"
    &CloudEvent.data = '{'  +\
    '"employee": {'  +\
       '"name":       "Sofia",'   +\
       '"salary":      19000,'  +\
       '"married":    true'  +\
    '}' +\  
    '}'
 
    &isOK = &EventRouter.SendEvent(&CloudEvent,&isBinary,&errorMessages)   
    if not &isOK
        msg(format("Error %1(%2)",&errorMessages.Item(1).Description, &errorMessages.Item(1).Id), status)
    endif
```

The following example shows how to send a collection of events using CloudEvent Schema for the representation of them.  
The method used is [SendEvents](https://wiki.genexus.com/commwiki/wiki?55337).

```
    &CloudEvent = new()
    &CloudEvent.source = !"GeneXusAppTest3"
    &CloudEvent.type = !"Test3"
    &CloudEvent.data = '{'  +\
    '"employee": {'  +\
       '"name":       "maria",'   +\
       '"salary":      59000,'  +\
       '"married":    true'  +\
    '}' +\  
    '}'
    
    &CloudEventCollection.Add(&CloudEvent)
    
    &CloudEvent = new()
    &CloudEvent.source = !"GeneXusAppTest4"
    &CloudEvent.type = !"Test4"
    &CloudEvent.datacontenttype = !"application/json"
    &CloudEvent.data = '{'  +\
    '"employee": {'  +\
       '"name":       "ana",'   +\
       '"salary":      59800,'  +\
       '"married":    false'  +\
    '}' +\  
    '}'
    
    &CloudEventCollection.Add(&CloudEvent)
    &isBinary = false
    &isOK = &EventRouter.SendEvents(&CloudEventCollection,&isBinary,&errorMessages)
```


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
