---
title: "Building Azure Serverless from sources (GeneXus 18 Upgrade 7)"
source_id: 56809
source_url: https://wiki.genexus.com/commwiki/wiki?56809
genexus_version: "18"
---

# Building Azure Serverless from sources (GeneXus 18 Upgrade 7)

After having done the [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683) of Azure Serveless, you have to build the sources the following way:

```
dotnet build /p:Configuration=Release <deployment.sln> --output <output_dir> -p:CosmosDBSupport=false -p:TimerSupport=false -p:AzureQueueSupport=false -p:ServiceBusSupport=false -p:HttpSupport=true -p:BlobSupport=false
```

The <deployment.sln> is inside the zip package, under src\build folder.  
  
In the following example, the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) is called "DpuWithoutGAM".

`[imagen omitida: wiki id 55351]`

### [Availability](#Availability)

 This feature is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)
