---
title: "Azure HTTP-triggered functions"
source_id: 49266
source_url: https://wiki.genexus.com/commwiki/wiki?49266
genexus_version: "18"
---

# Azure HTTP-triggered functions

They are [Http Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=csharp). The HTTP trigger lets you invoke a function with an HTTP request. You can use an HTTP trigger to build serverless APIs.

**Summary**

* [GeneXus objects that can be deployed as Http Functions](#GeneXus+objects+that+can+be+deployed+as+Http+Functions)

+ [1. Rest services of the KB](#1.+Rest+services+of+the+KB)
+ [2. Mobile Backend services](#2.+Mobile+Backend+services)

* [Function configuration](#Function+configuration)

+ [1. Deploying rest services of the KB as Http Azure functions](#1.+Deploying+rest+services+of+the+KB+as+Http+Azure+functions)
+ [2. Deploying mobile backend services](#2.+Deploying+mobile+backend+services)

* [Availability](#Availability+)
* [See Also](#See+Also)

## [GeneXus objects that can be deployed as Http Functions](#GeneXus+objects+that+can+be+deployed+as+Http+Functions)

### [1. Rest services of the KB](#1.+Rest+services+of+the+KB)

For deploying rest services as Http Azure functions, select the "**Microsoft Azure Functions**" deployment target.

You can add these types of objects to the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886):

* Procedures, Business Components, DataProviders exposed as [Rest services](https://wiki.genexus.com/commwiki/wiki?28213).
* [API object](https://wiki.genexus.com/commwiki/wiki?46151)

### [2. Mobile Backend services](#2.+Mobile+Backend+services)

For deploying the backend services of a mobile app (or Angular) as Http Azure functions, add the main objects of the app to the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) and select the "**Microsoft Azure serverless (backend services)**" deployment target.  
All the objects of the Deployment unit must have [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) set to Yes.  Alternatevely, set to Yes the property at the generator level, and do a rebuild all.

We recommend reading this first: [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

## [Function configuration](#Function+configuration)

### [1. Deploying rest services of the KB as Http Azure functions](#1.+Deploying+rest+services+of+the+KB+as+Http+Azure+functions)

The [Trigger Type property](https://wiki.genexus.com/commwiki/wiki?51466) at the deployment unit should be "Http."

It is optional to deploy in [API Management](https://azure.microsoft.com/en-us/services/api-management/) (APIM) as well.

If you deploy to APIM, first you have to configure the following:

* **APIM service name:** Name of the API Management service instance.
* **APIM resource group:** Azure API Management resource group.
* **API Identification:** API revision identifier. It must be unique in the current API Management service instance.
* **API display name:** Display name of this API.
* **API backend service URL:**Absolute URL of the backend service implementing this API. You should take this value from the settings of the Function App where you deployed the application, concatenated with the value of the Route Prefix property.
* **API path:** Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance.
* **API subscription required (\*):** If true, the API requires a subscription key on requests. When virtualizing your APIs behind an Azure API Management (APIM) service, you may need to provide the subscription key in your calls. Typically, this is done via the header key Ocp-Apim-Subscription-Key. Your subscription key is always linked to an APIM product. See the documentation of Azure about [Subscriptions](https://docs.microsoft.com/en-us/azure/api-management/api-management-subscriptions).
* **API Version:**Describes the Version of the API. If you add a version to a non-versioned API, an Original version will be automatically created and will respond on the default URL. The versioning scheme used is Path based ("Segment"). See [versions in APIM](https://docs.microsoft.com/en-us/azure/api-management/api-management-versions).
* **API Version Set Id:**A resource identifier for the related API Version Set. If an existing API Version Set Id is configured and an API Version display name is not indicated, then the version is updated in that version set.
* **API Version Display Name:**Name of API Version Set.

`[imagen omitida: wiki id 49267]`

**(\*)**In order to get the Subscription Key to consume the API, go through the Subscriptions option as shown below:

`[imagen omitida: wiki id 49514]`

### [2. Deploying mobile backend services](#2.+Deploying+mobile+backend+services)

See [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107).

## [Availability](#Availability+)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,).

The API objects can be deployed to APIM since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,).

## [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Table of contents:Application Deployment tool (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) | [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) | [HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59528) |

---
