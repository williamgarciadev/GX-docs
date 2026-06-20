---
title: "AzureQueue.MessageQueueProvider external object"
source_id: 51737
source_url: https://wiki.genexus.com/commwiki/wiki?51737
genexus_version: "18"
---

# AzureQueue.MessageQueueProvider external object

The *MessageQueueProvider* is an external object of the[Queue API](https://wiki.genexus.com/commwiki/wiki?51771) located under AzureQueue module.   
It allows establishing a connection to an [Azure Storage Queue](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction).

To send or receive messages from Azure Queue, first you have to establish a connection using the method of this external object. It returns a [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736), which must be used to process the queue (issue and consume messages).  
  
This guarantees that only the Azure Queue dependencies are downloaded to your machine and taken to deployment.

`[imagen omitida: wiki id 55675]`

**Summary**

* [Properties](#Properties)
* [Methods](#Methods)

+ [Connect](#Connect)
+ [Authenticate](#Authenticate+)

* [Events](#Events)
* [Set connection at runtime using environment variables](#Set+connection+at+runtime+using+environment+variables)

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

Static method that allows connecting to Azure Storage Queue using a connection string.

**Return value**  [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)  
**Parameters**   queueName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:VarChar, errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

connectionString should include the authentication information required for your application to access data in an Azure Storage account at runtime.  
It should be extracted from the Azure portal, by going through the storage account -> Access Keys menu option.

### [Authenticate](#Authenticate+)

Static method to authenticate to Azure Storage Queue using passwordless authentication (e.g. [Managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview)).

**Return value**  [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)  
**Parameters**   queueURI:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), queueURL:VarChar, errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

queueURI is an Uri referencing the queue that includes the name of the account, and the name of the queue. This is likely to be similar to "https://{account\_name}.queue.core.windows.net/{queue\_name}".

Applications can use managed identities to obtain Azure AD (Microsoft Entra ID) tokens without having to manage any credentials. As [Azure documents](https://learn.microsoft.com/en-us/dotnet/azure/sdk/authentication/?tabs=command-line#recommended-app-authentication-approach) explain, it is recommended that apps use token-based authentication rather than connection strings when authenticating to Azure resources.

The implementation chains several Token Credential implementations to be tried in order until one succeeds:

* [System-assigned Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview#managed-identity-types).   
  Attempts authentication using a managed identity assigned to the deployment environment. This authentication type works for all Azure-hosted environments that support managed identity.
* [User-assigned Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview#managed-identity-types).  
  The resource ID to authenticate for a user-assigned managed identity must be set in an environment variable named "AZURE\_CLIENT\_ID".
* Service Principal. Enables authentication to Azure Active Directory (Microsoft Entra ID) using a client secret or certificate, or as a user with a username and password. See [here](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential?view=azure-dotnet) for more details.
* Azure CLI credentials  
  Enables authentication to Azure Active Directory using Azure CLI to obtain an access token (for development environments).

## [Events](#Events)

It doesn't have any.

## [Set connection at runtime using environment variables](#Set+connection+at+runtime+using+environment+variables)

Environment variables (encrypted if desired) can be set to indicate connection parameters, instead of passing the values to the methods.

In most cases, it is useful to change the connection at runtime.  
First, the environment variables are read and then the value of the parameter passed to the method is taken into account.  
  
The variables may or may not be encrypted. The encryption key should be indicated in the [Application.key](https://www.genexus.com/en/developers/websac?data=29369) file in the case of the NET generator.  
In Azure, the environment variables are set as [App Settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common?tabs=portal#configure-app-settings).

The enviroment variables for the methods explained in this document are the following:

* QUEUE\_AZUREQUEUE\_QUEUENAME
* QUEUE\_AZUREQUEUE\_CONNECTIONSTRING
* QUEUE\_AZUREQUEUE\_QUEUEURI


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761) |
| [HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781) | [Queue API domains](https://wiki.genexus.com/commwiki/wiki?51928) |

---
