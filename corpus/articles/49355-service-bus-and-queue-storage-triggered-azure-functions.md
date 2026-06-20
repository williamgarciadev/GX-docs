---
title: "Service Bus and Queue Storage triggered Azure functions"
source_id: 49355
source_url: https://wiki.genexus.com/commwiki/wiki?49355
genexus_version: "18"
---

# Service Bus and Queue Storage triggered Azure functions

[Service Bus triggered](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus-trigger?tabs=csharp) functions and [Queue Storage triggered](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger?tabs=csharp) functions are other types of [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430).

### [Queue Storage](#Queue+Storage)

The Queue storage trigger runs functions as messages are added to Azure Queue storage.  
The [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) at the deployment unit should be "Queue" for this kind of function.

### [Service Bus](#Service+Bus)

The Service Bus trigger is used to respond to messages from a Service Bus queue or topic.  
The Trigger Type property at the deployment unit should be "Service Bus" for this kind of function.

## [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).  
Then, to deploy the function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

## [Function Configuration](#Function+Configuration)

The function's configuration depends on its Trigger type.

## [Samples](#Samples)

In the case of **Service Bus**, it can be "Queue" or "Topic," and it has different configuration settings for each one.

### [Sample for Service Bus Topic:](#Sample+for+Service+Bus+Topic%3A)

###### Trigger Type Service Bus Topic sample

The configurations are created automatically as [app settings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal) in the cloud so they can be managed easily (with no need to re-deploy)

###### 

### [Sample for Service Bus Queue:](#Sample+for+Service+Bus+Queue%3A)

###### Trigger Type Service Bus Queue sample

### [Sample for Queue Trigger Type:](#Sample+for+Queue+Trigger+Type%3A)

In the case of **Queue** Trigger type, the configuration settings are as shown in the following image taken from an example:

###### Trigger Type Queue sample

## [Setting configurations at runtime](#Setting+configurations+at+runtime)

As stated before, the connection configuration is created automatically as [app settings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal) in the cloud so they can be managed easily (with no need to re-deploy).

In the case of the Queue Name or Topic name, if you configure the property surrounded by **%** that name will be taken as an app setting. Then you have to define the app setting in Azure.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

**Note**: For Java, the Azure SDK has some limitations related to obtaining metadata of the message received, such as in the case of Service Bus. In this case, the Invocation Id of the function is returned as the Id of the message. Similarly, the date and time of the execution of the function is taken as the date of the message.


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [Service Bus and Queue Storage triggered Azure functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59657) |

---
