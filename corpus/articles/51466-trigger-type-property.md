---
title: "Trigger Type property"
source_id: 51466
source_url: https://wiki.genexus.com/commwiki/wiki?51466
genexus_version: "18"
---

# Trigger Type property

Sets the trigger that defines how a function is invoked.

### [Values](#Values)

|  |  |
| --- | --- |
| Timer | The functions to be run are scheduled when to be triggered. |
| Queue | Functions are run when messages are added to the queue. |
| Service Bus | Triggers respond to messages from a Service Bus queue or topic. |
| Http | Functions are invoked with HTTP requests. |
| Event Bridge | Triggers respond to messages from the event bus service. |
| CosmosDB | Triggers respond to CosmosDB inserts / updates. |
| Blob | Triggers respond to Blob Storage changes (insert or update) |
| Event Grid | Triggers respond to Event Grid events. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

For the **.NET Generator**, this property can be found in the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) dialog (Build > Deploy Application) when selecting **"Microsoft Azure Functions"** in the **Target** combo box. The values for this generator are as follows:

|  |  |
| --- | --- |
| 1. Timer | Since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47659,,) |
| 2. Queue | Since GeneXus 17 upgrade 3 |
| 3. Service Bus | Since GeneXus 17 upgrade 3 |
| 4. Http | Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,) |
| 5. CosmosDB | Since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) |
| 6. Blob | Since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| 7. Event Grid | Since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) |

For the **Java Generator**, this property can be found in the **Application Deployment tool** dialog (Build > Deploy Application) when selecting either **"AWS Lambda Functions"** or **"Microsoft Azure Functions"** in the **Target** combo box. The available values for each option are as follows:

AWS Lambda Functions

|  |  |
| --- | --- |
| 1. Timer | Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,) |
| 2. Queue | Since GeneXus 17 Upgrade 11 |
| 3. Event Bridge | Since GeneXus 17 Upgrade 11 |
| 4. Http | Since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) |

Microsoft Azure Functions

|  |  |
| --- | --- |
| 1. Timer | Since [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59446,,) |
| 2. Queue | Since GeneXus 18 upgrade 12 |
| 3. Service Bus | Since GeneXus 18 upgrade 12 |
| 4. CosmosDB | Since GeneXus 18 upgrade 12 |
| 5. Event Grid | Since GeneXus 18 upgrade 12 |

### [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)  
[AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514)


|  |
| --- |
| **Backlinks** |
| [AWS EventBridge triggered functions](https://wiki.genexus.com/commwiki/wiki?51547) | [AWS Queue triggered functions](https://wiki.genexus.com/commwiki/wiki?51541) | [Azure Blob Storage triggered functions](https://wiki.genexus.com/commwiki/wiki?55088) |
| [Azure Blob Storage triggered functions (GeneXus 18 upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59490) | [Azure CosmosDB-triggered functions](https://wiki.genexus.com/commwiki/wiki?54574) | [Azure Event Grid triggered functions](https://wiki.genexus.com/commwiki/wiki?56742) | [Azure HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?49266) |
| [Azure timer triggered functions](https://wiki.genexus.com/commwiki/wiki?49264) | [Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59656) | [Batch Function property](https://wiki.genexus.com/commwiki/wiki?59714) | [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) |
| [HowTo: Deploy as Azure Functions (GeneXus 18 Upgrade 11)](https://wiki.genexus.com/commwiki/wiki?59528) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) | [Lambda HTTP-triggered functions](https://wiki.genexus.com/commwiki/wiki?51552) | [Lambda Timer-triggered functions](https://wiki.genexus.com/commwiki/wiki?51550) |
| [Service Bus and Queue Storage triggered Azure functions](https://wiki.genexus.com/commwiki/wiki?49355) | [Service Bus and Queue Storage triggered Azure functions (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59657) | [Trigger type property (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59705) | [Trigger type property (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54594) |
| [Trigger type property (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?59703) | [Trigger type property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?59704) |

---
