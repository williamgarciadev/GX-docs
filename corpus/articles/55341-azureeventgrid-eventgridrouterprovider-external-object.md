---
title: "AzureEventGrid.EventGridRouterProvider external object"
source_id: 55341
source_url: https://wiki.genexus.com/commwiki/wiki?55341
genexus_version: "18"
---

# AzureEventGrid.EventGridRouterProvider external object

The *EventGridRouterProvider*external object below the AzureEventGrid module is used to establish a connection to an [Azure Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) using the [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334).

`[imagen omitida: wiki id 55342]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

A static method that allows instantiating an EventRouter. The method returns an EventRouter to publish events to Azure Event Grid.

**Return value:** [EventRouter external object](https://wiki.genexus.com/commwiki/wiki?55337)  
**Parameters:** endpoint:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), accesskey:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

* endpoint indicates the Azure Event Grid Topic or domain endpoint.

`[imagen omitida: wiki id 55343]`

* accesskey is optional. It is found on the left pane of the Event Grid Topic definition.  
  If left empty, the system tries to authenticate using [Azure Active Directory](https://learn.microsoft.com/en-us/azure/event-grid/authentication-overview#authenticate-using-azure-active-directory). That is, if the application is deployed to an Azure host with Managed Identity enabled or a security principal defined, the application will authenticate with that account. For more information, see [Azure Active Directory authentication](https://wiki.genexus.com/commwiki/wiki?55341) in this document.

### [Availability](#Availability)

This external object is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [Azure Active Directory authentication](#Azure+Active+Directory+authentication)

Applications can use managed identities to obtain Azure AD (Microsoft Entra ID) tokens without having to manage any credentials.  
As [Azure documents](https://learn.microsoft.com/en-us/dotnet/azure/sdk/authentication/?tabs=command-line#recommended-app-authentication-approach) explain, it is recommended that apps use token-based authentication rather than connection strings when authenticating to Azure resources.

The implementation of the *connect*method (if no access key is passed) chains several Token Credential implementations to be tried in order until one succeds:

* [System-assigned Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview#managed-identity-types).   
  Attempts authentication using a managed identity that has been assigned to the deployment environment. This authentication type works for all Azure hosted environments that support managed identity.
* [User-assigned Managed Identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview#managed-identity-types).  
  The resource id to authenticate for a user assigned managed identity must be set in an environment variable named "AZURE\_CLIENT\_ID".
* Service Principal. Enables authentication to Azure Active Directory (Microsoft Entra ID) using a client secret or certificate, or as a user with a username and password. See [here](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.environmentcredential?view=azure-dotnet) for more details.
* Azure CLI credentials  
  Enables authentication to Azure Active Directory using Azure CLI to obtain an access token (for development environments).

For configuration details see [Authentication and authorization with Azure Active Directory](https://learn.microsoft.com/en-us/azure/event-grid/authenticate-with-active-directory).

### [See Also](#See+Also)

[Custom Topics in Azure Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/custom-topics).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) |

---
