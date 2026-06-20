---
title: "HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)"
source_id: 59528
source_url: https://wiki.genexus.com/commwiki/wiki?59528
genexus_version: "18"
---

# HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)

This document explains how to deploy a GeneXus application as [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430).

### [Installing requirements](#Installing+requirements)

Install the requirements in the machine where you will run the deployment —you only need [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

### [Setting up the cloud](#Setting+up+the+cloud)

The basic steps in the Azure portal are the following:

**1.** Create the resources in Azure. See [HowTo: Create an Azure function app](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47419,,)  
**2.** To authenticate, configure a [Service Principal](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47427,,).

### [Modeling in GeneXus](#Modeling+in+GeneXus)

The basic steps in GeneXus are the following:

**1.** Create a [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) and select the objects to deploy.  
  
**2.** Use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) to select the target "Microsoft Azure Functions."   
To deploy the backend services of an app, select thetarget "Microsoft Azure serverless (backend services)." In this case, the Functions are deployed as Http-triggered functions.  
  
**3.** Configure the properties in the property grid.  
  
**4.** Click the deployment button to deploy to Azure.

### [Functions Trigger type](#Functions+Trigger+type)

Azure functions have Trigger Types ([Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) at the Deployment Unit).

`[imagen omitida: wiki id 49354]`

Depending on the trigger type of the functions, you have to consider different aspects when deploying.  
To consider those aspects, you may group the functions that have a trigger other than Http, and those that have Http trigger.

### [Non-Http-triggered functions](#Non-Http-triggered+functions)

For all the functions except those that have http trigger, consider the following to deploy the application.

* Add only one main procedure to the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886).
* Procedures have nothing particular in their logic, except for considering the parameters they receive according to the function trigger.  
  See [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

This is an example of a timer triggered function:

`[imagen omitida: wiki id 47446]`

### [Http-triggered functions](#Http-triggered+functions)

See [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266)

### [Common aspects of functions](#Common+aspects+of+functions)

First, take into account that when the function is published on an existing function app, the function is updated.

### [Function settings](#Function+settings)

Depending on the function, it is preferable to be able to change some settings in the cloud. Those settings are configured at deployment time, and you can set the deployment engine to create an [application setting](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal#settings) in the cloud with the name and value you specify.

For example, for timer functions, you can specify a cron time, or an application setting (to be created in the cloud with the name and value that you wish).

`[imagen omitida: wiki id 47810]`

For the last option, the advantage is that all changes can be made in the cloud (you don't need to deploy again for those changes).

`[imagen omitida: wiki id 49725]`

The same happens with other function types like Queue or Service Bus, where the connection data is defined as an app setting.

### [Global configuration of functions](#Global+configuration+of+functions)

The behavior of all functions within the function app can be configured globally. This is done in the [host.json](https://docs.microsoft.com/en-us/azure/azure-functions/functions-host-json) file. For example, in that file, you can configure the trace level for the app, Health Monitor, etc.  
Azure functions have a default timeout, which can also be changed at the host.json file.  
  
**Important:** The GeneXus user has to manage this file.

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

### [Architecture considerations](#Architecture+considerations)

If the function app uses Image, Audio, Video, or BlobFile data types, you have to configure the [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) because all multimedia must be served from an external URL, such as Microsoft Azure.

For the same reason, it's not supported to use the file system to serve content; that is, to have read/write access to files (such as Blob data type, Excel, or PDF reports).

For solutions using GAM, see [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363).
