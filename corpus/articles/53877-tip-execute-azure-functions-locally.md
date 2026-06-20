---
title: "Tip: Execute Azure functions locally"
source_id: 53877
source_url: https://wiki.genexus.com/commwiki/wiki?53877
genexus_version: "18"
---

# Tip: Execute Azure functions locally

You don't need to test [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) in the cloud. Sometimes it may be useful to run them locally to debug any errors. To do so, follow the steps below:

1. Execute the [Azure Functions deployment](https://wiki.genexus.com/commwiki/wiki?49351) with the *Only Package* option. It is not necessary to enter valid settings in the credentials (or have Azure CLI) because the deployment package will not be uploaded to the cloud.  
The deployment output indicates where the package (zip) has been created.  
For example:

*Application successfully Packaged to be uploaded to Azure: C:\models\TestDeployAzureFunc\TestDeployAzureFunc\NetCoreModel\Deploy\AZURE\_FUNCTIONS\TestWindowsQueue\_20230202120948\_testqueue.zip*

2. Unzip the package to a folder.

3. Use [Azure core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Clinux%2Ccsharp%2Cportal%2Cbash) to run your functions locally.

From a cmd, run:

```
func start
```

That starts the Azure functions locally.

### [HTTP Functions](#HTTP+Functions)

The URL of each function is indicated in the output of the command line.  
You can execute HTTP functions using Postman, for example. Also, if it's called using HTTP GET, just use the web browser.  
  
You need a file called  *local.settings.json* in the root directory where you have unzipped the deployment package. If you do not have it, it will be created automatically if you execute "func start" in an interactive mode, just selecting "dotnet (isolated worker model)"

`[imagen omitida: wiki id 59849]`  
  
Otherwise you can create it manually. The file should have the following at least:

```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated"
  },
  "ConnectionStrings": {}
}
```

### [Other functions such as Timer, Queue or Service Bus-triggered functions](#Other+functions+such+as+Timer%2C+Queue+or+Service+Bus-triggered+functions)

For queue or service bus-triggered functions, you need to set the credentials of the queue or service bus to be run locally.  
Otherwise, you'll get the following error when the function starts:

*The 'testqueue' function is in error: Microsoft.Azure.WebJobs.Host: Error indexing method 'Functions.testqueue'. Microsoft.Azure.WebJobs.Extensions.Storage.Queues: Storage account connection string 'AzureWebJobsqueueConnection' does not exist. Make sure that it is a defined App Setting.*

Create a file called *local.settings.json* in the root directory where you have unzipped the deployment package.  
Its contents should be as shown below. Place the connection string of your queue in the *AzureWebJobsqueueConnection* entry*.*

```
{

"IsEncrypted": false,
"Values": {
"FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
"AzureWebJobsqueueConnection": "DefaultEndpointsProtocol=https;AccountName=storagegx;AccountKey=xxxx==;EndpointSuffix=core.windows.net"
}
}
```

For Timer triggered functions, the local.settings.json could be as follows:

```
{

"IsEncrypted": false,
"Values": {
"FUNCTIONS_WORKER_RUNTIME": "dotnet-isolated",
"AzureWebJobsStorage": "<here the connection string of a storage account>"
}
}
```

### [**GAM Applications**](#GAM+Applications)

Using GAM, you have to set the **GX\_GAMCONNECTIONKEY** environment variable (at the command prompt) before executing the Azure function using func start command.  
See [HowTo: Use GAM in Azure serverless architecture](https://wiki.genexus.com/commwiki/wiki?53363)

### [See also](#See+also)

[Test Azure functions locally](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)
