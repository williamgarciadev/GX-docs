---
title: "WhatsApp Partner property"
source_id: 45164
source_url: https://wiki.genexus.com/commwiki/wiki?45164
genexus_version: "18"
---

# WhatsApp Partner property

Selects the WhatsApp Partner.

### [Values](#Values)

|  |  |
| --- | --- |
| **Botmaker** | Select Botmaker as the WhatsApp partner. |
| **Twilio** | Select Twilio as the WhatsApp partner. |

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

To integrate with WhatsApp using the [Chatbots Channels API](https://wiki.genexus.com/commwiki/wiki?44072), you have to set the [Enable WhatsApp property](https://wiki.genexus.com/commwiki/wiki?45163) to TRUE. After activating this property, the WhatsApp Partner property becomes available. There, you have to select the partner of your choice (for example, [Twilio](https://wiki.genexus.com/commwiki/wiki?44121)).

Using the information given by this property (and others, depending on the partner selected, for example, [Twilio Token property](https://wiki.genexus.com/commwiki/wiki?45166)), GeneXus generates the **WhatsAppWebhook** procedure under the chatbot's instance module.  
This is the webhook used to configure the chatbot integration. For more details see [HowTo: Integrate Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346).


|  |
| --- |
| **Backlinks** |
| [Botmaker Token property](https://wiki.genexus.com/commwiki/wiki?45993) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Enable WhatsApp property](https://wiki.genexus.com/commwiki/wiki?45163) |
| [HowTo: Integrate Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346) | [HowTo: Set up Botmaker for Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?45899) | [Twilio Token property](https://wiki.genexus.com/commwiki/wiki?45166) |

---
