---
title: "HowTo: Use GAM in Azure serverless architecture"
source_id: 53363
source_url: https://wiki.genexus.com/commwiki/wiki?53363
genexus_version: "18"
---

# HowTo: Use GAM in Azure serverless architecture

When deploying your services (Rest services, API objects, or services of a mobile/Android app) to [Azure serverless](https://wiki.genexus.com/commwiki/wiki?47430), the following has to be considered if the app uses [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)

### [Use Redis to persist the web session](#Use+Redis+to+persist+the+web+session)

Serverless is stateless by default.  
But since GAM uses the web session, it is necessary to use [Azure Cache for Redis](https://azure.microsoft.com/en-us/products/cache/) in such scenarios.

### [How to deploy to Azure serverless and use Redis](#How+to+deploy+to+Azure+serverless+and+use+Redis+)

First,  [define an Azure Cache for Redis service](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-configure) in the cloud. Get the [Access Keys](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-configure#access-keys) because you will need them afterwards.  
At the deployment phase (using the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) inside GeneXus IDE or [MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?51440)), you have to set the required information to indicate the Redis instance and its credentials.

The following image shows the deployment dialog and how to set the properties in the Session State configuration section.

`[imagen omitida: wiki id 53365]`

Using MSBuild directly, the properties are as follows:

```
"AZURE_FUNCTIONS_SESSION_STATE_PROVIDER" - Redis
"AZURE_FUNCTIONS_SESSION_PROVIDER_ADDRESS" 
"AZURE_FUNCTIONS_SESSION_PROVIDER_PASSWORD" 
"AZURE_FUNCTIONS_SESSION_PROVIDER_INSTANCE_NAME"
"AZURE_FUNCTIONS_SESSION_TIMEOUT"
```

For example, for Azure Cache for Redis the configuration could be:

```
"AZURE_FUNCTIONS_SESSION_STATE_PROVIDER" =  Redis
"AZURE_FUNCTIONS_SESSION_PROVIDER_ADDRESS" = sample.redis.cache.windows.net:6380,password=xxxxxxxxxxxxxxxxxxx=,ssl=True,abortConnect=False
"AZURE_FUNCTIONS_SESSION_PROVIDER_INSTANCE_NAME" = sample
"AZURE_FUNCTIONS_SESSION_TIMEOUT"  = 5
```

Note that in this case, you can set the provider Address property with the "Primary Connection string" of the Redis cache. Also, note that in this figure, the instance name is "gxredis".

`[imagen omitida: wiki id 53366]`

#### [Session Timeout](#Session+Timeout+)

The session is renewed with each request; that is, each request resets the time counter to zero and starts again. That is how it happens on the web, where your session expires only due to inactivity after X minutes.

### [Configure GAM settings](#Configure+GAM+settings)

In order to connect to GAM, the services must have a valid [GAM Repository connection](https://wiki.genexus.com/commwiki/wiki?16150).

In the serverless cloud architecture, the GAM connection key is retrieved using an Azure Application Setting (an environment variable in general terms), called **GX\_GAMCONNECTIONKEY**.  
This Application setting is automatically defined by the Deploy Engine through the GAM connection Key property at the deployment dialog, although you can define it yourself in the cloud if you want.

You can see it in the Azure Function configuration settings using the Azure portal.

`[imagen omitida: wiki id 53369]`

Using the Application Deployment tool, you can set the property in the GAM configuration section:

`[imagen omitida: wiki id 53367]`

The connection key can be set using the following MSBuild property:

```
AZURE_SERVERLESS_GAM_CONNECTION_KEY
```

### [Where is the GAM connection key to configure the property for deployment obtained?](#Where+is+the+GAM+connection+key+to+configure+the+property+for+deployment+obtained%3F)

The GAM connection key can be obtained from connection.gam, which contains that key.

**Note**: For the time being, you have to always set the GAM connection key property at the deployment if you have GAM, regardless if you are only packaging the deployment and not uploading it to Azure. That is, even though you will be defining the GX\_GAMCONNECTIONKEY App Setting yourself in the cloud, you have to set a value in the GAM connection key property to make your application connect to GAM.


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) |

---
