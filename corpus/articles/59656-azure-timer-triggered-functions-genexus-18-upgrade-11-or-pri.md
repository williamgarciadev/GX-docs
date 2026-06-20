---
title: "Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)"
source_id: 59656
source_url: https://wiki.genexus.com/commwiki/wiki?59656
genexus_version: "18"
---

# Azure timer triggered functions (GeneXus 18 Upgrade 11 or prior)

They are [timed](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp) [functions](https://wiki.genexus.com/commwiki/wiki?47430). One possible scenario is using them to update the merchandise inventory or the redundancies of a DB.

The [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) at the deployment unit should be "Timer" for this kind of functions.

## [Deploy steps](#Deploy+steps)

To start, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).  
To deploy the function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

## [Function configuration: Scheduling the function](#Function+configuration%3A+Scheduling+the+function)

The time can be configured using an [Ncrontab expression](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp#ncrontab-expressions), or a [TimeSpan expression](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-timer?tabs=csharp#timespan).  
  
The GeneXus property to configure the cron Time is:

* *"Schedule Time format"*, whose values are: {"Time value expression","App setting property name and value"}.

If the first option is selected, you have to configure:

* "*Schedule Time value*" property.

Otherwise, configure the [app setting](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings) name and value to be defined in the cloud, through the *"App setting property name"* and *"App setting property value"* properties. The app setting is automatically defined in the cloud by the deploy engine.

`[imagen omitida: wiki id 49265]`

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Availability](#Availability)

This function is available since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47659,,).

### [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)
