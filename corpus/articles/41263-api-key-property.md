---
title: "API Key property"
source_id: 41263
source_url: https://wiki.genexus.com/commwiki/wiki?41263
genexus_version: "18"
---

# API Key property

Specify the Watson Assistant API Key.

### [Scope](#Scope)

**Objects:** Conversational Flows Instance

### [Description](#Description)

When the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) is set to Watson and [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) is set to [IAM](https://console.bluemix.net/docs/services/watson/getting-started-iam.html#iam), you must configure the API key given by IBM, in the API Key property.

At the IBM console, select the service from the Catalog -> Dashboard menu, and copy the API key:

`[imagen omitida: wiki id 41307]`

Then paste it in GeneXus API key property (under the NLP Provider section of the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) properties dialog):

`[imagen omitida: wiki id 41308]`

For more information go to [Configure IBM Watson services for the Chatbot generator](https://wiki.genexus.com/commwiki/wiki?39748).

To apply changes, just save the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) and it will be synchronized automatically to the NLP provider, in addition to updating the <InstanceName>Chatbot.config file. For more information on this file go to [Connecting to the Chatbot Provider](https://wiki.genexus.com/commwiki/wiki?37102#%285%29+Connecting+to+the+Chatbot+Provider').

### [Configuration file](#Configuration+file)

The configuration file used for saving the value of this property is the \*Chatbot.config (the name of the file is the instance name + Chatbot). The file is located in the virtual directory in case of NET, and in the WEB-INF directory of the servlet server in case of Java.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).


|  |
| --- |
| **Backlinks** |
| [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096) | [Region property in Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?41264) |

---
