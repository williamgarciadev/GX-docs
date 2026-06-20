---
title: "HowTo: Deploy as Azure Functions"
source_id: 49351
source_url: https://wiki.genexus.com/commwiki/wiki?49351
genexus_version: "18"
---

# HowTo: Deploy as Azure Functions

This document explains how to deploy a GeneXus application as [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430).

**Summary**

* [Installing requirements](#Installing+requirements)
* [Setting up the cloud](#Setting+up+the+cloud)
* [Modeling in GeneXus](#Modeling+in+GeneXus)
* [Functions Trigger type](#Functions+Trigger+type)

+ [Non-HTTP-triggered functions](#Non-HTTP-triggered+functions)
+ [HTTP-triggered functions](#HTTP-triggered+functions)

* [Function execution (all except HTTP)](#Function+execution+%28all+except+HTTP%29)
* [Common aspects of functions](#Common+aspects+of+functions)
* [Function settings](#Function+settings)

+ [Cases where the deployment engine creates the Application Setting](#Cases+where+the+deployment+engine+creates+the+Application+Setting)
+ [Cases where the deployment engine does not create the Application Setting](#Cases+where+the+deployment+engine+does+not+create+the+Application+Setting)

* [Global configuration of functions](#Global+configuration+of+functions)
* [Architecture considerations](#Architecture+considerations)

## [Installing requirements](#Installing+requirements)

Install the requirements in the machine where you will run the deployment —you only need [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

## [Setting up the cloud](#Setting+up+the+cloud)

In the Azure portal, follow the steps below:

1. Create the resources in Azure. See [HowTo: Create an Azure function app](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47419,,).
2. To authenticate, configure a [Service Principal](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47427,,).

## [Modeling in GeneXus](#Modeling+in+GeneXus)

In GeneXus, follow the steps below:

1. Create a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) and select the objects to deploy.
2. Use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) to select the target "Microsoft Azure Functions".  
   To deploy the Backend services of an app, select thetarget "Microsoft Azure serverless (backend services)". In this case, the Functions are deployed as HTTP-triggered functions.
3. Configure the properties in the property grid.
4. Click on the deployment button to deploy to Azure.

## [Functions Trigger type](#Functions+Trigger+type)

Azure functions have Trigger Types ([Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) in the Deployment Unit).

`[imagen omitida: wiki id 49354]`

Depending on the trigger type of the functions, you have to consider different aspects when deploying.

To consider those aspects, you may group the functions that have a trigger other than HTTP and those that have an HTTP trigger.

### [Non-HTTP-triggered functions](#Non-HTTP-triggered+functions)

For all functions except those that have an HTTP trigger, consider the following when deploying the application.

* Add only one main procedure to the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886).
* Procedures have nothing particular in their logic, except for considering the parameters they receive according to the function trigger.  
    
  See [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

This is an example of a timer-triggered function:

`[imagen omitida: wiki id 47446]`

### [HTTP-triggered functions](#HTTP-triggered+functions)

See [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266)

## [Function execution (all except HTTP)](#Function+execution+%28all+except+HTTP%29)

The solution is configured to internally invoke the GeneXus objects that represent Azure Functions using an environment variable of the form:  
GX\_AZURE\_<FUNCTION\_NAME>\_CLASS, where FUNCTION\_NAME is the name of the function.

This environment variable is used to know the mapping between the function and the GeneXus object associated with it.  
  
The value always contains the namespace or package name of the KB, followed by the name of the modularized GeneXus object.

Note that the GeneXus object is prefixed by "a".  
  
Sample:

`[imagen omitida: wiki id 59531]`

If the environment variable is not defined, a file named gxazmappings.json that contains the same information is searched for.

File sample:

```
[
    {
        "FunctionName": "QueueTriggerJava",
        "GXEntrypoint": "com.testazurefunctionsjava.test.testqueue"
    },
    {
        "FunctionName": "testfunction",
        "GXEntrypoint": "com.testazurefunctionsjava.test.queuetriggeredfunction"
    }
]
```

In the case of .NET, this file is generated in addition to the environment variable. In JAVA, only the environment variable is defined.  
  
If neither the environment variable nor the file is found at runtime, this error occurs:  
  
*FunctionConfigurationException: File gxazmappings.json not found. The file is attempted to be read when there is no GX\_AZURE\_<FUNCTIONNAME>\_CLASS environment variable pointing to the GeneXus class associated with the function.*

## [Common aspects of functions](#Common+aspects+of+functions)

First, take into account that when the function is published on an existing function app, the function is updated.

## [Function settings](#Function+settings)

There is great flexibility for deployment in the sense that if you need to change any setting, you do not need to re-deploy.

Depending on the function, it is preferable to be able to change some settings in the cloud. Those settings are configured at deployment time, and you can set the deployment engine to create an [application setting](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#settings) in the cloud with the name and value you specify.  
In other cases, the deployment engine does not define the settings, and it's your responsibility to do it (as part of the infrastructure setup of the function).

### [Cases where the deployment engine creates the Application Setting](#Cases+where+the+deployment+engine+creates+the+Application+Setting)

For example, for timer functions, you can specify a cron time, or an application setting (to be created in the cloud with the name and value that you wish).

`[imagen omitida: wiki id 47810]`

For the last option, the advantage is that all changes can be made in the cloud (you don't need to deploy again for those changes).

`[imagen omitida: wiki id 49725]`

The same happens with other function types like Queue or Service Bus, where the connection data is defined as an app setting.

### [Cases where the deployment engine does not create the Application Setting](#Cases+where+the+deployment+engine+does+not+create+the+Application+Setting)

For those cases where there is no property to specify the App settings and its value, you can also have the flexibility of using App Settings.  
  
For example, in the case of Service Bus or Queue trigger, instead of configuring a fixed value for the queue name, etc., you can configure the Application Setting name between "%" which can then be defined in Azure with a value (you have to define the App Setting in Azure).  
  
This allows you to deploy without leaving fixed values. That is, there is no need to re-deploy just because the function is going to use another Queue or Service Bus, etc.  
  
`[imagen omitida: wiki id 59530]`

## [Global configuration of functions](#Global+configuration+of+functions)

The behavior of all functions within the function app can be configured globally. This is done in the [host.json](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json) file. For example, in that file, you can configure the trace level for the app, Health Monitor, etc.  
Azure functions have a default timeout, which can also be changed in the host.json file.  
  
**Important:** You have to manage manage this file.

* In the case of Java, it can be copied to the <GENEXUS INSTALLATION>\DeploymentTargets\Azure Functions\Templates\Java folder (and replace the existing one).
* In the case of .NET, you can replace the file existing at <GENEXUS INSTALLATION>\ DeploymentTargets\AzureFunctions\AzFunctionFiles\src.

The Application Deployment Tool uploads one with the basic settings, but if you want to use another, you can edit it and add it to the deployment unit (see [Deployment of additional files and directories](https://wiki.genexus.com/commwiki/wiki?32092)).

Sample *host.json* file to generate trace information:

```
{
    "version": "2.0",
    "logging": {
        "fileLoggingMode": "always",
        "logLevel": {
            "default": "Trace",
            "Host.Results": "Trace",
            "Function": "Trace",
            "Host.Aggregator": "Trace"
        },
        "applicationInsights": {
            "samplingExcludedTypes": "Request",
            "samplingSettings": {
                "isEnabled": true
            }
        }
    }
}
```

**Note**: The RoutePrefix property should not be changed at this file directly. In order to customize it use the Route Prefix property of the Deploy dialog properties, or upload the Azure functions to API Management where you can customize the path according to your needs.

## [Architecture considerations](#Architecture+considerations)

If the function app uses Image, Audio, Video, or BlobFile data types, you have to configure the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) because all multimedia must be served from an external URL, such as Microsoft Azure.

For the same reason, it's not supported to use the file system to serve content; that is, to have read/write access to files (such as Blob data type, Excel, or PDF reports).

For solutions using GAM, see [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) |
| [Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59490) | [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) |
| [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266) | [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264) | [Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59656) | [Batch Function property](https://wiki.genexus.com/commwiki/wiki?59714) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59528) |
| [HowTo: Use MSBuild tasks for Azure Functions deployment](https://wiki.genexus.com/commwiki/wiki?59965) | [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355) | [Service Bus and Queue Storage triggered Azure functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59657) | [Tip: Execute Azure functions locally](https://wiki.genexus.com/commwiki/wiki?53877) |

---
