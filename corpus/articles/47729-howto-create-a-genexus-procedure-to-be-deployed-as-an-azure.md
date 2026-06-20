---
title: "HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function"
source_id: 47729
source_url: https://wiki.genexus.com/commwiki/wiki?47729
genexus_version: "18"
---

# HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function

Some [Azure functions](https://wiki.genexus.com/commwiki/wiki?47430)  or [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) (other than the Http-triggered functions) may require parameters to be executed.  
When the Azure or AWS runtime invokes a function (the function is triggered), it receives information related to the event that happened (e.g: the message that was received from a queue in a Queue Storage or a Service Bus function, or the blob that was stored in a Blob storage).  
This information is needed inside the GeneXus [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) to program the logic of the function.

Therefore, in order to create a GeneXus Procedure that will be deployed as a function, you should consider some aspects regarding the parameters of the Procedure that are explained in this document.

#### [**Notes:**](#Notes%3A)

* This is valid for functions whose trigger type is Blob, Service Bus, Queue, and Timer (all except HTTP)
* The GeneXus Procedures have to be main ([Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = Internal).

### [Install the GeneXusServerlessAPI module](#Install+the+GeneXusServerlessAPI+module)

**1.** First, import the external module called "GeneXusServerlessAPI." into the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). This module contains the definitions of the [SDT](https://wiki.genexus.com/commwiki/wiki?2427)s necessary to be passed as parameters to the function.

`[imagen omitida: wiki id 47807]`

`[imagen omitida: wiki id 53930]`

The [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) can be any of the following:

```
parm(in:&EventMessages,out:&EventMessageResponse); 

parm(in:&RawData,out:&EventMessageResponse); // RawData is a char parameter
```

### [About EventMessage SDT](#About+EventMessage+SDT)

The header of EventMessage allows getting all the information of the event (such as its ID) from the Azure function or AWS Lambda.  
The item EventMessageProperties is a property-value structure, where you can retrieve the body of the message, including its metadata. It's a dynamic structure to support any kind of message, regardless of the trigger type of the function.

`[imagen omitida: wiki id 53876]`

**Note**: If you want to receive the message in a JSON string, use *in:&RawData* character parameter.

### [About EventMessageResponse SDT](#About+EventMessageResponse+SDT)

The EventMessageResponse has the following structure:

`[imagen omitida: wiki id 54146]`

See Error Handling below for more details.

### [Samples](#Samples)

The following is an example of code where the EventMessage is processed.

```
for &EventMessage in &EventMessages.EventMessage  
    &MessageInfo = format(!"Id : %1, Source : %2, Version : %3, Date : %4, Data : %5"
    ,&EventMessage.EventMessageId
    ,&EventMessage.EventMessageSourceType
    ,&EventMessage.EventMessageVersion
    ,&EventMessage.EventMessageDate
    ,&EventMessage.EventMessageData)
    //Process the message properties.
    //This is a dynamic structure (property-value) which depends on the type of message and the provider.
    for &EventMessageProperty in &EventMessage.EventMessageProperties
          &Data +=    format(!"%1:%2 %3 ", &EventMessageProperty.PropertyId, &EventMessageProperty.PropertyValue, "-")
     endfor
endfor
```

### [Deploy](#Deploy)

To deploy the Procedure as a function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) or [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533).

### [Functions Error Handling](#Functions+Error+Handling)

To avoid lost events, error handling is a very important issue to consider. This is for exceptions that require that the function is executed again until the maximum number of retries is reached.

By default, if any system error ocurrs, the function will retry.  
  
In the GeneXus Procedure, if the application fails for any reason that can be controlled by the programmer, he can force the function to be re-run just by indicating HandleFailure  property of &EventMessageResponse output variable to TRUE.

```
If &isError
    &EventMessageResponse.HandleFailure = TRUE
    &EventMessageResponse.ErrorMessage = "There was an error in the process."
 Endif
```

#### 

#### [Azure Error Handling considerations](#Azure+Error+Handling+considerations)

Each type of function has its own management of [retries and error handling](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages?tabs=csharp) in its infrastructure. According to the [MS documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-error-pages?tabs=csharp#app-level-configuration), a retry policy can be defined for all functions in an app using the [host.json file](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json#retry).   
This file is added to the deployment package with basic settings. You have to modify it to your needs and include it as a file if you want.

In this case, the error is thrown to the Azure runtime, so the function can retry all the times it is configured to do so. In the case of Queue Storage or Service Bus, and if none of the retries is successful, the message is sent to a Poison queue or dead letter, respectively.  
In this case, in the monitor of Azure Cloud, you will see the error as an Application Error:

`[imagen omitida: wiki id 47738]`

### [See Also](#See+Also)

[HowTo: Monitor Azure Functions](https://wiki.genexus.com/commwiki/wiki?49260)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547) |
| [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541) | [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) | [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) |
| [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) |
| [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552) | [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550) | [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355) |

---
