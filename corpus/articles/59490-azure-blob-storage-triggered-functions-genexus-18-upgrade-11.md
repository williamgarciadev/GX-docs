---
title: "Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)"
source_id: 59490
source_url: https://wiki.genexus.com/commwiki/wiki?59490
genexus_version: "18"
---

# Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)

When a new or updated blob is detected, the Azure function is triggered.

As stated in the [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cin-process&pivots=programming-language-csharp), several methods exist to execute a function code based on changes to blobs in a storage container. The Azure Blob storage trigger for Azure Functions may only be appropriate only for some cases, as detailed in [Working with Blobs](https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations?tabs=azure-cli#working-with-blobs). This should only be used when the blob is small.

**Summary**

* [Deployment steps](#Deployment+steps)

+ [Deployment Settings](#Deployment+Settings)

- [Blob Connection App Settings](#Blob+Connection+App+Settings)
- [Blob Storage Properties](#Blob+Storage+Properties)

* [Function Inputs](#Function+Inputs)
* [Scope](#Scope)
* [Availability](#Availability)
* [See Also](#See+Also)

## [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).  
To deploy the function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

### [Deployment Settings](#Deployment+Settings)

The [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) in the deployment unit should be "**Blob**" for this kind of function.

#### [Blob Connection App Settings](#Blob+Connection+App+Settings)

At the Blob Connection App Settings section of the deployment dialog, you should set the following:

- **Name**: A name for the Azure cloud application setting containing the connection to the Blob Storage. It can already be defined in the cloud, or not. If not, you can use the deployment to create the app setting if you give a value to it at the following property.

- **Value**: Optionally give a value for the app setting that should contain the connection string of the Blob Storage. The deployment engine will create the app setting using this information.

`[imagen omitida: wiki id 55092]`

#### [Blob Storage Properties](#Blob+Storage+Properties)

At the Blob Storage Properties section of the deployment dialog, you should set the Blob Path.  
The Blob Path indicates the Blob storage container and should include a name pattern. It can be a generic pattern like the following (between curly braces):

```
mycontainer/{name}
```

...or it could be a more complex pattern as detailed in the [documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=python-v2%2Cisolated-process&pivots=programming-language-csharp#filter-on-blob-name).

`[imagen omitida: wiki id 55091]`

## [Function Inputs](#Function+Inputs)

The GeneXus procedure will have a signature as explained in [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

In this case, the EventMessage SDT will contain the following in each of its fields:

* EventMessageId: The invocationId of the Azure Function
* EventMessageSourceType: Blob
* EventMessageVersion: ""
* EventMessageDate: Date and time of execution
* EventMessageData: A String containing the file created / updated. If it's a binary file, it will contain the base 64 encoded string.
* EventMessageProperties: Properties and Metadata of the Blob, including:
  + Uri: The blob's URI for the primary location.
  + name: The name of the file including its extension.

For additional configuration check the [Azure documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob?tabs=isolated-process%2Cextensionv5%2Cextensionv3&pivots=programming-language-java#hostjson-settings).

## [Scope](#Scope)

**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604)

## [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

## [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)
