---
title: "Region property in Conversational Flows Instance"
source_id: 41264
source_url: https://wiki.genexus.com/commwiki/wiki?41264
genexus_version: "18"
---

# Region property in Conversational Flows Instance

Specifies the Watson Assistant region.

### [Values](#Values)

|  |  |
| --- | --- |
| **Dallas** | Uses Dallas region. |
| **Frankfurt** | Uses Frankfurt region. |
| **London** | Uses London region. |
| **Seoul** | Uses Seoul region. |
| **Sydney** | Uses Sydney region. |
| **Tokyo** | Uses Tokyo region. |
| **Washington, DC** | Uses Washington DC region. |

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

When the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) is set to Watson and [Authentication Type property](https://wiki.genexus.com/commwiki/wiki?41262) is set to [IAM](https://console.bluemix.net/docs/services/watson/getting-started-iam.html#iam), you have to configure the API key given by IBM in the [API Key property](https://wiki.genexus.com/commwiki/wiki?41263) and the Region in this property. The Region is the same that you configured in the IBM cloud services contract as the deployment location.

`[imagen omitida: wiki id 41306]`

Select that value in the Region combo box (under the NLP Provider section of the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) properties dialog):

`[imagen omitida: wiki id 45817]`

To apply changes, save the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) and it will be automatically synchronized to the NLP provider, in addition to updating the GXCF\_Chatbots.config file. For more information on this file, go to [Connecting to the Chatbot Provider](https://wiki.genexus.com/commwiki/wiki?37102#%285%29+Connecting+to+the+Chatbot+Provider').

### [Configuration file](#Configuration+file)

The configuration file used for saving the value of this property is GXCF\_Chatbots.config. The file is located in the virtual directory in the case of NET, and in the WEB-INF directory of the servlet server in the case of Java.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

### [See Also](#See+Also)

* [Configure IBM Watson services for the Chatbot generator](https://wiki.genexus.com/commwiki/wiki?39748)


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Configuring GeneXus for using the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?37096) |

---
