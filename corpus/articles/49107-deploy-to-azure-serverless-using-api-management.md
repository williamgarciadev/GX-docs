---
title: "Deploy to Azure Serverless using API Management"
source_id: 49107
source_url: https://wiki.genexus.com/commwiki/wiki?49107
genexus_version: "18"
---

# Deploy to Azure Serverless using API Management

This document explains details about the deployment to [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/) (APIM).

You can deploy to APIM when deploying [Azure Http functions](https://wiki.genexus.com/commwiki/wiki?47430) and when deploying mobile (angular) app services. In both cases, deploying to APIM is optional, although it is recommended.

Before going on with this document, read [Azure Http-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266).

* When deploying mobile app services to an Azure Serverless architecture, you use the "Microsoft Azure Serverless (backend services)" deployment target of the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092).  
  First, note that you have to set the [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) to Yes and [OpenAPI version property](https://wiki.genexus.com/commwiki/wiki?49531,,) to either 2.0 or 3.0, and do a rebuild all in the model, previous to deploying to Azure Serverless.  
  The following error is shown if the property is no set:

  "Error: All the objects of the Deployment unit must have Generate OpenAPI Interface property set to Yes.  Alternatevely, set to Yes the property at the generator level, and do a rebuild all."
* When deploying KB services (Rest services, API Objects) you use the "Microsoft Azure Functions" deployment target.

## [APIM deployment properties](#APIM+deployment+properties)

To deploy to APIM, you need to configure the following deployment properties at the *API Management Settings* of the [deploy dialog](https://wiki.genexus.com/commwiki/wiki?32092) inside GeneXus:

|  |  |
| --- | --- |
| **APIM service name** | Name of the API Management service instance. |
| **APIM resource group** | Azure API Management resource group. |
| **API Identification** | API revision identifier. It must be unique in the current API Management service instance. |
| **API display name** | Display name of this API. |
| **API backend service UR**L | Absolute URL of the backend service implementing this API.  It corresponds to the URL given for the Azure function app.  E.g: https://MyFunctionApp.azurewebsites.net |
| **API path** | Relative URL uniquely identifying this API and all of its resource paths within the API Management service instance.  E.g: travel |
| **API subscription required** | If true, the API requires a subscription key on requests. The recommended value for services being called from mobile clients is False. |

## [Example](#Example)

Consider the following deployment configuration:

`[imagen omitida: wiki id 49959]`

With the above settings, the API can be seen as follows in the [Azure portal](http://portal.azure.com) (going through the API Management service):

`[imagen omitida: wiki id 49960]`

To run the app and use the services just deployed, configure the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) as follows:

**Warning**: You must set [Services URL Mode property](https://wiki.genexus.com/commwiki/wiki?54361) to "Absolute" value.

`[imagen omitida: wiki id 49961]`

Note that the URL is the Gateway URL shown in the Azure portal for the APIM service, followed by the API path you configured on deployment.

Then, at runtime, the /rest suffix in the URL is added automatically by the mobile clients to make the calls, as shown in the figure:

`[imagen omitida: wiki id 49962]`

`[imagen omitida: wiki id 49112]`

## [See also](#See+also)

For angular front end applications which use Azure serverless for deploying their backend, see [HowTo: Deploy Angular Frontend applications using serverless backend](https://wiki.genexus.com/commwiki/wiki?49963).

### [Interesting links](#Interesting+links)

[How to tackle the cold start problem of Azure Function serverless app.](https://itnext.io/how-to-tackle-the-cold-start-problem-of-azure-function-serverless-app-e90030cdb0c7)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Azure Http-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266) |
| [Cloud-native with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51572) |
| [HowTo: Deploy Angular Frontend applications using serverless backend](https://wiki.genexus.com/commwiki/wiki?49963) | [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104) | [HowTo: Deploy static files to Azure Storage in Serverless deploy](https://wiki.genexus.com/commwiki/wiki?50142) |
| [HowTo: MSBuild tasks for Azure serverless deployment](https://wiki.genexus.com/commwiki/wiki?51440) |

---
