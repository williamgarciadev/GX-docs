---
title: "EventMessaging API: Send Events using EventGrid Schema"
source_id: 55401
source_url: https://wiki.genexus.com/commwiki/wiki?55401
genexus_version: "18"
---

# EventMessaging API: Send Events using EventGrid Schema

The following example shows how to publish events to [Azure Event Grid](https://wiki.genexus.com/commwiki/wiki?55354) based on EventGrid Schema, using [SendCustomEvents](https://wiki.genexus.com/commwiki/wiki?55337) method.

&EventGridSchema is [EventGridSchema SDT](https://wiki.genexus.com/commwiki/wiki?55344) data type.

```
    &endpoint = !"https://eventgridcloud.eastus-1.eventgrid.azure.net/api/events"
    &accesskey = !"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    &EventRouter = AzureEventGrid.EventGridRouterProvider.Connect(&endpoint,&accesskey,&errorMessages,&IsSuccess)    

    &employee.name = "ernesto"
    &employee.married = true
    &employee.salary = 40000
    &EventGridSchema.data = &employee.ToJson()  
    &EventGridSchema.eventType = !"Example.EventType1"
    &EventGridSchema.subject = !"ExampleEventSubject1"
    &EventGridSchema.dataVersion = "1.0"
    
    &EventGridSchemaCollection.Add(&EventGridSchema)
    
    &EventGridSchema = new()
    &employee = new()
    &employee.name = "agustin"
    &employee.married = true
    &employee.salary = 40050
    &EventGridSchema.data = &employee.ToJson()
    
    &EventGridSchema.eventType = !"Example.EventType2"
    &EventGridSchema.subject = !"ExampleEventSubject2"
    &EventGridSchema.dataVersion = "1.0"
    &EventGridSchemaCollection.Add(&EventGridSchema)
    
    &isOK = &EventRouter.SendCustomEvents(&EventGridSchemaCollection.ToJson(),false,&errorMessages)
```


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
