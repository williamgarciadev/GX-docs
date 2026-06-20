---
title: "Building Azure functions from sources"
source_id: 59963
source_url: https://wiki.genexus.com/commwiki/wiki?59963
genexus_version: "18"
---

# Building Azure functions from sources

For packaging the sources of [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430), follow the instructions on [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683).  
Then set the [Package Type property](https://wiki.genexus.com/commwiki/wiki?53373) to "Sources".  
  
`[imagen omitida: wiki id 59964]`

After the packaging has finished, you have to build the sources as shown below (positioned at the src\build directory):

```
dotnet build <Mydeployment>.sln -c release --force -p:DebugType=none --p:OutputPath=<outputh_path> -p:CosmosDBSupport= -p:TimerSupport= -p:AzureQueueSupport= -p:ServiceBusSupport= -p:HttpSupport= -p:BlobSupport= -p:EventGridSupport= -p:IntegratedSecuritySupport=
```

You have to pass the values of CosmosDBSupport, TimerSupport, etc., according to the Azure Function's trigger type.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59630,,)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |

---
