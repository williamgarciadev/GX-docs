---
title: "Azure Functions"
source_id: 47430
source_url: https://wiki.genexus.com/commwiki/wiki?47430
genexus_version: "18"
---

# Azure Functions

[Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) is a serverless computing service that allows you to run code without managing infrastructure. It is equivalent to [AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514) and extends the concept of Platform as a Service (PaaS) by abstracting infrastructure details and facilitating auto-scaling.

Key benefits of Azure Functions include:

* Automatic scaling
* Reduction of time to market
* Agile deployment
* Pay-per-use

As stated by Gartner, "Serverless architectures enable developers to focus on what they should be doing –writing code and optimizing application design– making way for business agility and digital experimentation".

### [Scenarios](#Scenarios)

Azure Functions is ideal for scenarios where you want data processing to react to events and pay only for the resources consumed. It is not suitable for long-running batch procedures.

Data processing can be triggered by various events, including:

* Timer triggers (cron jobs)
* Queue triggers
* Service Bus triggers
* HTTP triggers
* CosmosDB triggers
* Blob Storage triggers
* Event Grid triggers

### [Azure Functions in GeneXus](#Azure+Functions+in+GeneXus)

To implement Azure Functions in GeneXus, refer to the following guides:

* [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264)
* [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355)
* [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266)
* [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574)
* [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088)
* [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742)

### [Platform support](#Platform+support)

|  |  |  |
| --- | --- | --- |
|  | **Windows** | **Linux** |
| Net Core 3.1 (In-process execution model) | Yes | Yes |
| Net 5 (Isolated Worker model) | Yes | No |
| Net 6 (Isolated Worker model) | Yes | Yes |
| Net 8 (Isolated Worker model) | Yes | Yes |
| Java 8, 11, 17 | Yes | Yes |

### [Deployment](#Deployment)

To deploy your application to Azure Functions, follow the steps outlined in [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

### [Notes](#Notes)

* This feature is supported for the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47659,,).
* Since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48247,,) you have to define a .NET 5 Function App.
* .NET 6 is supported in [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49616,,).
* [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) is supported for all Trigger Types except HTTP and Blob in [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59446,,).

### [See Also](#See+Also)

[HowTo: Troubleshoot Azure functions](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47434,,)  
[HowTo: Monitor Azure Functions](https://wiki.genexus.com/commwiki/wiki?49260)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) |
| [Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59490) | [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) | [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266) |
| [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264) | [Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59656) | [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) |
| [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) | [HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59528) |
| [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363) | [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355) | [Service Bus and Queue Storage triggered Azure functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59657) | [Tip: Execute Azure functions locally](https://wiki.genexus.com/commwiki/wiki?53877) |
| [Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) | [Trigger type property (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59705) | [Trigger type property (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54594) | [Trigger type property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?59703) |
| [Trigger type property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?59704) |

---
