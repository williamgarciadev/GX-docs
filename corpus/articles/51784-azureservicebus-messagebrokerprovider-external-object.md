---
title: "AzureServiceBus.MessageBrokerProvider external object"
source_id: 51784
source_url: https://wiki.genexus.com/commwiki/wiki?51784
genexus_version: "18"
---

# AzureServiceBus.MessageBrokerProvider external object

The *MessageBrokerProvider* external object under the AzureServiceBus module is used to establish a connection to a [Service Bus](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) (Queue or Topic) using the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782).

`[imagen omitida: wiki id 55678]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

A static method that allows instantiating a MessageBroker using dynamic data. The method connects using a connection string and returns a MessageBroker to be used to send and receive messages from the Service Bus.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queueName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled: True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled: True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queue:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

### [Authenticate](#Authenticate)

A static method for authenticating to a Service Bus Queue that supports Azure Active Directory (Microsoft Entra ID) authentication. No credentials are passed to the method. See [Authenticate using Managed Identities](https://wiki.genexus.com/commwiki/wiki?51784) below in this document.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queueName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), fullyQualifiedNamespace:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled: True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

fullyQualifiedNamespace: The fully qualified Service Bus namespace to connect to. This is likely to be similar to {yournamespace}.servicebus.windows.net

### [Authenticate](#Authenticate)

Authenticate to a Service Bus Topic that supports Azure AD (Microsoft Entra ID) authentication.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), fullyQualifiedNamespace:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled: True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

fullyQualifiedNamespace: The fully qualified Service Bus namespace to connect to. This is likely to be similar to {yournamespace}.servicebus.windows.net

### [Authenticate](#Authenticate)

Authenticate to a Service Bus Queue that supports Azure AD (Microsoft Entra ID) authentication.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queue:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), fullyQualifiedNamespace:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

fullyQualifiedNamespace: The fully qualified Service Bus namespace to connect to. This is likely to be similar to {yournamespace}.servicebus.windows.net

### [Authenticate](#Authenticate+)

Authenticate to a Service Bus Topic that supports Azure AD (Microsoft Entra ID) authentication.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), fullyQualifiedNamespace:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

fullyQualifiedNamespace: The fully qualified Service Bus namespace to connect to. This is likely to be similar to {yournamespace}.servicebus.windows.net

## [Authenticate using Managed Identities](#Authenticate+using+Managed+Identities)

Applications can use managed identities to obtain Azure AD (Microsoft Entra ID) tokens without having to manage any credentials.  
As [Azure documents](https://learn.microsoft.com/en-us/dotnet/azure/sdk/authentication/?tabs=command-line#recommended-app-authentication-approach) explain, it is recommended that apps use token-based authentication rather than connection strings when authenticating to Azure resources.

The implementation of the *Authenticate* methods chains several Token Credential implementations to be tried in order until one succeeds:

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

* MESSAGEBROKER\_AZURESB\_QUEUENAME
* MESSAGEBROKER\_AZURESB\_TOPICNAME
* MESSAGEBROKER\_AZURESB\_SUBSCRIPTION
* MESSAGEBROKER\_AZURESB\_QUEUECONNECTION
* MESSAGEBROKER\_AZURESB\_FULLYQUALIFIEDNAMESPACE

## [See Also](#See+Also)

[Azure Service Bus](https://www.serverless360.com/azure-service-bus).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: BrokerReceiverOptions SDT](https://wiki.genexus.com/commwiki/wiki?51943) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) |
| [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) | [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) |
| [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Schedule a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51982) | [HowTo: Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973) | [Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791) |

---
