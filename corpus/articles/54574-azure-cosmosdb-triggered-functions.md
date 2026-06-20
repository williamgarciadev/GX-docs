---
title: "Azure CosmosDB-triggered functions"
source_id: 54574
source_url: https://wiki.genexus.com/commwiki/wiki?54574
genexus_version: "18"
---

# Azure CosmosDB-triggered functions

[Azure functions triggered by CosmosDB insert or update operations](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/serverless-computing-database) can be deployed with the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) using the [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) Target, and setting the [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) to CosmosDB.

This trigger relies on [change feed](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed) streams to monitor your Azure Cosmos DB container for changes. When any changes are made to a container (insert / update), the change feed stream is sent to the trigger, which invokes the Azure Function.

### [Technical issues to consider](#Technical+issues+to+consider)

* The trigger doesn't indicate whether a document was updated or inserted, it just provides the document itself.
* The trigger requires a second container that it uses to store leases over the partitions. Both the container being monitored and the one that contains the leases must be available for the trigger to work.
* If multiple functions are configured to use an Azure Cosmos DB trigger for the same container, each of the functions should use a dedicated lease container or specify a different *LeaseContainerPrefix* for each function.

For more information, check the [Azure Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-cosmosdb-v2-trigger?tabs=python-v2%2Cisolated-process%2Cextensionv4&pivots=programming-language-csharp#usage).

## [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).   
To deploy the function, use the [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) or the MSBuild tasks provided by the Deployment Engine. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351) to have a guide for the deployment.

## [Function Configuration](#Function+Configuration)

To configure the function deployment, you need to have some infrastructure pre-defined, such as:

- [Function App](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#timeout) (see [HowTo: Create an Azure function app](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?47419,,))  
- [CosmosDB account](https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/quickstart-portal)   
- CosmosDB database and container that will be monitored  
- CosmosDB database and container for leasing

## [Deploy using the Application deployment tool inside GeneXus](#Deploy+using+the+Application+deployment+tool+inside+GeneXus)

In the deployment dialog, you have to select:

* Target = Microsoft Azure Functions
* [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) = CosmosDB

`[imagen omitida: wiki id 54596]`

Note that all the settings for connecting to the monitored database container and the lease container are created in the cloud as [app settings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-how-to-use-azure-function-app-settings?tabs=portal).  
You just enter the name of the app setting and the value is not mandatory.  
So, there's no need to redeploy if any of them changes. It is not mandatory to enter the values, as they can be set using infrastructure code or at the Azure portal.

## [MSBuild CreateCloudPackage script](#MSBuild+CreateCloudPackage+script)

In a CI/CD pipeline, you have the possibility of running MSBuild scripts for deployment.

In this case, after having run the basic deployment MSBuild scripts ([CreateDeploy](https://wiki.genexus.com/commwiki/wiki?42073) and [CreatePackage](https://wiki.genexus.com/commwiki/wiki?42073)), you should create the package that will be ready to be uploaded to the cloud.

```
MSBuild.exe  /ToolsVersion:4.0 "C:\<GX>\CreateCloudPackage.msbuild"
/p:TargetId="AZURE_FUNCTIONS"
/p:CreatePackageScript="createpackage.msbuild"
/p:CreatePackageTarget="CreatePackage"
/p:DeployFullPath=<path>
/p:WebSourcePath="C:\Models\TestDeployAzureFunc\NetCoreModel\web"
/p:ProjectName=<ProjectName>
/p:DeploymentUnit=<DeploymentUnit>
/p:GX_PROGRAM_DIR="C:\<GX>"
/p:AZURE_FUNCTIONS_FUNCTION_APP="cosmosdblinuxnet6"
/p:AZURE_FUNCTIONS_RESOURCE_GROUP="cosmoslinuxnet6"
/p:AZURE_FUNCTIONS_SP_APP_ID="000000000000000000000000000"
/p:AZURE_FUNCTIONS_SP_TENANT_ID="00000000000000000000000000"
/p:AZURE_FUNCTIONS_SP_CREDENTIALS="000000000000000000000"
/p:AZURE_FUNCTIONS_TRIGGER_TYPE="cosmosdb"
/p:AZURE_FUNCTIONS_FUNCTION_NAME="TestCosmosDBTrigger"
/p:AZURE_FUNCTIONS_COSMOSDB_CONNECTION="ConnectionString" /p:AZURE_FUNCTIONS_COSMOSDB_CONNECTION_APPSETTINGVALUE="AccountEndpoint=https://gxcosmosdb.documents.azure.com:443/;AccountKey=000000000000000000"
/p:AZURE_FUNCTIONS_COSMOSDB_DATABASE="DBName"
/p:AZURE_FUNCTIONS_COSMOSDB_DATABASE_APPSETTINGVALUE="Test"
/p:AZURE_FUNCTIONS_COSMOSDB_CONTAINER="ContainerName"
/p:AZURE_FUNCTIONS_COSMOSDB_CONTAINER_APPSETTINGVALUE="Writers"
/p:AZURE_FUNCTIONS_COSMOSDB_LEASE_CONTAINER_PREFIX="FullGX"
/p:AZURE_FUNCTIONS_COSMOSDB_LEASE_CONNECTION="LeaseNameConnectionString" /p:AZURE_FUNCTIONS_COSMOSDB_LEASE_CONNECTION_APPSETTINGVALUE="AccountEndpoint=https://gxcosmosdb.documents.azure.com:443/;AccountKey=00000000000000000000" /p:AZURE_FUNCTIONS_COSMOSDB_LEASE_DATABASE="LeaseDataBase"
/p:AZURE_FUNCTIONS_COSMOSDB_LEASE_DATABASE_APPSETTINGVALUE="TestLease"
/p:AZURE_FUNCTIONS_COSMOSDB_LEASE_CONTAINER="LeaseContainer"
/p:AZURE_FUNCTIONS_COSMOSDB_LEASE_CONTAINER_APPSETTINGVALUE="LeaseContainerTest"
/p:DeploySource="C:\Models\TestDeployAzureFunc\NetCoreModel\Deploy\AZURE_FUNCTIONS\<deploy>.zip"
/t:CreatePackage
```

To understand this better, see the [Deployment Targets repository](https://github.com/genexuslabs/deployment-targets) on GitHub, as it is an extensible solution.

## [Considerations](#Considerations)

As explained [here](https://wiki.genexus.com/commwiki/wiki?47729), the GeneXus procedure associated with the function that receives the information returned by Azure (the record(s) updated in the CosmosDB table) may have one of these signatures:

```
1. parm(in:&EventMessages,out:&EventMessageResponse)
2. parm(in:&RawData,out:&EventMessageResponse); // RawData is a char parameter
```

For this particular Function, there's another possible signature:

```
parm(in:&EventMessagesList,out:&EventMessageResponse);
```

`[imagen omitida: wiki id 54604]`

As Azure CosmosDB is a schema-less database and stores JSON, the data can have any structure (it can have nested JSON objects or arrays).

How it will be processed depends on the parameter used to receive the data.

### [Using the signature parm(in:&EventMessages,out:&EventMessageResponse)](#Using+the+signature+parm%28in%3A%26EventMessages%2Cout%3A%26EventMessageResponse%29)

The data loaded in the EventMessageProperty SDT (which is a member of EventMessage), will store the following:

* In the PropertyId: the key of each key-value pair of the JSON object.
* In the PropertyValue: the value converted to a string if it's a string, number, float, or boolean (dates are represented as strings). If it's an array or object, the PropertyValue will have a string with the information flattened.

`[imagen omitida: wiki id 54597]`

### [Using the signature parm(in:&RawData,out:&EventMessageResponse)](#Using+the+signature+parm%28in%3A%26RawData%2Cout%3A%26EventMessageResponse%29)

With the &Rawdata parameter you get in a string the concatenation of all the JSON records updated.

### [Using the signature parm(in:&EventMessagesList,out:&EventMessageResponse)](#Using+the+signature+parm%28in%3A%26EventMessagesList%2Cout%3A%26EventMessageResponse%29)

It's more useful when more than one JSON records are involved.  
You can iterate through the list to process each of the JSON items.

The [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) can be used to load an SDT from that information.  
The SDT can be obtained using the Json Import tool (available through the menu Tools - Application Integration - Json Import).

```
for &EventMessagesListItem in &EventMessagesList.items //&EventMessagesListItem is LongVarchar data type
     &SDTData.fromJson(&EventMessagesListItem)
     //Process information
endfor
```

### [Availability](#Availability)

* For [.NET](https://wiki.genexus.com/commwiki/wiki?38604), this functionality is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).
* For [Java](https://wiki.genexus.com/commwiki/wiki?12258) it is available since [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59446,,).


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) | [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) |

---
