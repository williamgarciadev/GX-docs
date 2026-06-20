---
title: "Authentication Type property"
source_id: 41262
source_url: https://wiki.genexus.com/commwiki/wiki?41262
genexus_version: "18"
---

# Authentication Type property

Authentication type to be used in creating and updating the instance in the provider. The authentication type is determined by the provider. Check the provider's documentation.

### [Values](#Values)

|  |  |
| --- | --- |
| **Basic** | Basic Authentication will be used, so you must configure user and password. |
| **IAM Authentication** | IAM Authentication will be used, so you must configure an API Key. |

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

When the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) is set to Watson, you must choose either the [IAM](https://console.bluemix.net/docs/services/watson/getting-started-iam.html#iam) or the Basic auhentication Type.

IBM cloud uses Identity and Access Management (IAM) authentication, which is the only authentication type supported for newly created services. However, it still supports Basic Authentication for services created prior to the IAM support.

For Basic authentication type, you are given username and password, which should be configured at [User Name property](https://wiki.genexus.com/commwiki/wiki?38932) and [Watson User Password property](https://wiki.genexus.com/commwiki/wiki?38933).

For IAM authentication type, IBM provides you with an API key to be used in configuring the [API Key property](https://wiki.genexus.com/commwiki/wiki?41263).

To apply changes, just save the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) and it will be synchronized automatically to the NLP provider, in addition to updating the <InstanceName>Chatbot.config file. For more information on this file go to [Connecting to the Chatbot Provider](https://wiki.genexus.com/commwiki/wiki?37102#%285%29+Connecting+to+the+Chatbot+Provider').

### [Configuration file](#Configuration+file)

The configuration file used for saving the value of this property is the \*Chatbot.config (the name of the file is the instance name + Chatbot). The file is located in the virtual directory in case of NET, and in the WEB-INF directory of the servlet server in case of Java.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).

### [See Also](#See+Also)

* [Configure IBM Watson services for the Chatbot generator](https://wiki.genexus.com/commwiki/wiki?39748)


|  |
| --- |
| **Backlinks** |
| [API Key property](https://wiki.genexus.com/commwiki/wiki?41263) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096) | [GAM - WeChat Authentication type](https://wiki.genexus.com/commwiki/wiki?45037) | [Region property in Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?41264) |

---
