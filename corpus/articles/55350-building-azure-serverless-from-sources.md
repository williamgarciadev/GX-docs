---
title: "Building Azure Serverless from sources"
source_id: 55350
source_url: https://wiki.genexus.com/commwiki/wiki?55350
genexus_version: "18"
---

# Building Azure Serverless from sources

For packaging the sources of an Azure Serveless application, follow the instructions on [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683).

After the packaging has finished, you have to build the sources as shown below:

```
dotnet build /p:Configuration=Release <deployment.sln> --output <output_dir> -p:CosmosDBSupport=false -p:TimerSupport=false -p:AzureQueueSupport=false -p:ServiceBusSupport=false -p:HttpSupport=true -p:BlobSupport=false -p:EventGridSupport=false -p:IntegratedSecuritySupport=<true/false>
```

Note that if the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) (KB) has [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) enabled, you have to add -p:IntegratedSecuritySupport=true at compilation time.

The <deployment.sln> file is inside the ZIP package, under the src\build folder.  
  
In the following example, the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) is called "DpuWithoutGAM".

`[imagen omitida: wiki id 55351]`


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Building Azure Serverless from sources (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?59962) | [Building Azure Serverless from sources (GeneXus 18 Upgrade 7)](https://wiki.genexus.com/commwiki/wiki?56809) |

---
