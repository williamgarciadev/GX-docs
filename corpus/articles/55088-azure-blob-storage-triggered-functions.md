---
title: "Azure Blob Storage triggered functions"
source_id: 55088
source_url: https://wiki.genexus.com/commwiki/wiki?55088
genexus_version: "18"
---

# Azure Blob Storage triggered functions

When a new or updated blob is detected, the Azure function is triggered.

As stated in the [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cin-process&pivots=programming-language-csharp), several methods exist to execute a function code based on changes to blobs in a storage container. The Azure Blob storage trigger for Azure Functions may be appropriate only for some cases, as detailed in [Working with Blobs](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations?tabs=azure-cli#working-with-blobs). This should only be used when the blob is small.  
  
Besides, Azure's recommendation is to use events to trigger the function. So this solution is based on triggering the Azure Functions on blob containers using an event subscription. For more information see [here](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-csharp#prepare-the-azure-storage-account).

**Important note**: This is a breaking change compared to [GeneXus 18 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?54245).

**Summary**

* [Deployment steps](#Deployment+steps)

+ [Deployment Settings](#Deployment+Settings)
+ [Blob Connection App Settings](#Blob+Connection+App+Settings)
+ [Blob Storage Properties](#Blob+Storage+Properties)
+ [Requirements](#Requirements)

* [Function Inputs](#Function+Inputs)
* [Scope](#Scope)
* [See Also](#See+Also)

## [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).  
To deploy the function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

### [Deployment Settings](#Deployment+Settings)

The [Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) in the deployment unit should be "**Blob**" for this kind of function.

### [Blob Connection App Settings](#Blob+Connection+App+Settings)

At the Blob Connection App Settings section of the deployment dialog, you should set the following:

- **Name**: A name for the Azure cloud application setting containing the connection to the Blob Storage. It can already be defined in the cloud, or not. If not, you can use the deployment to create the app setting if you give a value to it at the following property.

- **Value**: Optionally give a value for the app setting that should contain the connection string of the Blob Storage. The deployment engine will create the app setting using this information.

`[imagen omitida: wiki id 59498]`

Azure Cloud AppSettings:  
  
`[imagen omitida: wiki id 59500]`

### [Blob Storage Properties](#Blob+Storage+Properties)

At the Blob Storage Properties section of the deployment dialog, you should set the Blob Path.  
The Blob Path indicates the Blob storage container and should include a name pattern. It can be a generic pattern like the following (between curly braces):

```
mycontainer/{name}
```

...or it could be a more complex pattern as detailed in the [documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cisolated-process&pivots=programming-language-csharp#filter-on-blob-name).

### [Requirements](#Requirements)

* You require to have a general-purpose v2 storage account
* A blob container
* After having deployed the Azure function you can build an enpoint URL ([reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-csharp#build-the-endpoint-url))  
    
  Search for the **blobs\_extension key** of the Function App:  
    
  `[imagen omitida: wiki id 59742]`  
    
  Create a new endpoint URL for the Blob Storage trigger based on the following example:

  ```
  https://<FUNCTION_APP_NAME>.azurewebsites.net/runtime/webhooks/blobs?functionName=Host.Functions.<FUNCTION_NAME>&code=<BLOB_EXTENSION_KEY>
  ```
* Create the event subscription.  
  An event subscription, powered by Azure Event Grid, raises events based on changes in the subscribed blob container. This event is then sent to the blob extension endpoint for your function ([reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-event-grid-blob-trigger?pivots=programming-language-csharp#create-the-event-subscription)).  
    
  `[imagen omitida: wiki id 59492]`  
    
  Example of Event subscription:  
    
  `[imagen omitida: wiki id 59743]`

## [Function Inputs](#Function+Inputs)

The GeneXus procedure will have a signature as explained in [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

In this case, the EventMessage SDT will contain the following in each of its fields:

* EventMessageId: The invocationId of the Azure Function
* EventMessageSourceType: Blob
* EventMessageVersion: ""
* EventMessageDate: Date and time of execution
* EventMessageData: URI of the file.
* EventMessageProperties: Properties and Metadata of the Blob, including:
  + Uri: The blob's URI for the primary location.
  + name: The name of the file including its extension.

For additional configuration check the [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob?tabs=isolated-process%2Cextensionv5%2Cextensionv3&pivots=programming-language-java#hostjson-settings).

## [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
Note: Java is not supported yet, due to the Java SDK for Azure functions limitation on getting the Blob metadata.

## [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59490) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) |

---
