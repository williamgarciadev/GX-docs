---
title: "HowTo: Deploy Angular Frontend applications using serverless backend"
source_id: 49963
source_url: https://wiki.genexus.com/commwiki/wiki?49963
genexus_version: "18"
---

# HowTo: Deploy Angular Frontend applications using serverless backend

When deploying Angular applications, you can choose to deploy the backend services as serverless. You can deploy them as [Azure Functions](https://wiki.genexus.com/commwiki/wiki?49107).

Then, you have to configure the [Cross Origin Resource Sharing - CORS](https://wiki.genexus.com/commwiki/wiki?52092,,).

This configuration has to be done after having deployed your Frontend application (see [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877)).

When using [Azure API Management](https://azure.microsoft.com/en-us/services/api-management/) (APIM) for the backend services deployment, go through the API inbound policies of APIM, on the Azure portal, and configure the CORS Allow Origin policy for the machine where the Angular app is running.

`[imagen omitida: wiki id 49966]`

Example:

```
<cors allow-credentials="true">
  <allowed-origins>
    <origin>http://localhost:62560/</origin>
  </allowed-origins>
  <allowed-methods preflight-result-max-age="300">
     <method>*</method>
  </allowed-methods>
  <allowed-headers>
    <header>*</header>
  </allowed-headers>
  <expose-headers>
    <header>*</header>
  </expose-headers>
</cors>
```

For more information on this topic, read the [Azure documentation](https://docs.microsoft.com/en-us/azure/api-management/api-management-cross-domain-policies#CORS).

If you just deploy to Azure Functions without using APIM, configure the CORS at the Function App CORS setting (located on the left side menu) of the Function App.

`[imagen omitida: wiki id 49728]`


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Deploy to Azure Serverless using API Management](https://wiki.genexus.com/commwiki/wiki?49107) |
| [HowTo: Deploy Frontend applications to a Cloud Provider Object Storage](https://wiki.genexus.com/commwiki/wiki?49877) | [HowTo: Deploy Frontend applications to Docker containers](https://wiki.genexus.com/commwiki/wiki?51104) |

---
