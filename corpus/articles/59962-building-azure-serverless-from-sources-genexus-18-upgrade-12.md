---
title: "Building Azure Serverless from sources (GeneXus 18 Upgrade 12 or prior)"
source_id: 59962
source_url: https://wiki.genexus.com/commwiki/wiki?59962
genexus_version: "18"
---

# Building Azure Serverless from sources (GeneXus 18 Upgrade 12 or prior)

For  packaging the sources of an Azure Serveless application, follow the instructions on [Packaging .NET sources](https://wiki.genexus.com/commwiki/wiki?54683).

After the packaging has finished, you have to build the sources the following way:

```
dotnet build /p:Configuration=Release <deployment.sln> --output <output_dir> -p:CosmosDBSupport=false -p:TimerSupport=false -p:AzureQueueSupport=false -p:ServiceBusSupport=false -p:HttpSupport=true -p:BlobSupport=false -p:EventGridSupport=false
```

The <deployment.sln> is inside the zip package, under src\build folder.  
  
In the following example, the [Deployment Unit object](https://wiki.genexus.com/commwiki/wiki?38886) is called "DpuWithoutGAM".

`[imagen omitida: wiki id 55351]`
