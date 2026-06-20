---
title: "Trigger type property (GeneXus 18 Upgrade 7 or prior)"
source_id: 59704
source_url: https://wiki.genexus.com/commwiki/wiki?59704
genexus_version: "18"
---

# Trigger type property (GeneXus 18 Upgrade 7 or prior)

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

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

For the .NET Generator, this property can be found in the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) dialog (Build > Deploy Application) when selecting "Microsoft Azure Functions" in the Target combo box. The values for this generator are as follows:

|  |  |
| --- | --- |
| 1. Timer | Since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47659,,) |
| 2. Queue | Since GeneXus 17 upgrade 3 |
| 3. Service Bus | Since GeneXus 17 upgrade 3 |
| 4. Http | Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,) |
| 5. CosmosDB | Since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) |
| 6. Blob | Since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |

For the Java Generator, this property can be found in the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) dialog (Build > Deploy Application) when selecting "AWS Lambda Functions" in the Target combo box. The values for this generator are as follows:

|  |  |
| --- | --- |
| 1. Timer | Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,) |
| 2. Queue | Since GeneXus 17 Upgrade 11 |
| 3. Event Bridge | Since GeneXus 17 Upgrade 11 |
| 4. Http | Since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) |

### [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)  
[AWS Lambda Functions](https://wiki.genexus.com/commwiki/wiki?51514)
