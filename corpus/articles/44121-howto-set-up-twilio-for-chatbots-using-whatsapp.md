---
title: "HowTo: Set up Twilio for Chatbots using Whatsapp"
source_id: 44121
source_url: https://wiki.genexus.com/commwiki/wiki?44121
genexus_version: "18"
---

# HowTo: Set up Twilio for Chatbots using Whatsapp

Here you can learn how to setup [Twilio](http://www.twilio.com/) in order to use Whatsapp as a messaging platform for the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102).

Twilio Sandbox for WhatsApp allows you to **prototype** with WhatsApp immediately, without waiting for your Twilio number to be approved for WhatsApp.

### [Step 1 - Creating an account](#Step+1+-+Creating+an+account)

First, create a new account at [Twilio](https://www.twilio.com/try-twilio).

`[imagen omitida: wiki id 44124]`

You'll be asked to verify your email:

`[imagen omitida: wiki id 44134]`

Then, you'll be asked to verify your phone number:

`[imagen omitida: wiki id 44135]`

### [Step 2 - Joining the sandbox](#Step+2+-+Joining+the+sandbox)

You'll have to go through some steps:

`[imagen omitida: wiki id 44206]`

`[imagen omitida: wiki id 44207]`

Here you can skip to dashboard:

`[imagen omitida: wiki id 44208]`

Then go through  "All Product & Services" and select "Programmable Messaging"**.** In a new window that appears, you have to select "WhatsApp" andit asks you if you want to activate the Sandbox.

To activate the sandbox, a page like this one appears:

`[imagen omitida: wiki id 44209]`

Select a number from the available sandbox numbers:

`[imagen omitida: wiki id 54028]`

There's a [learn tutorial](https://www.twilio.com/console/sms/whatsapp/learn) that you can follow easily.

The sandbox is pre-provisioned with a Twilio phone number.  
Send “join <*your sandbox keyword*>” to your Sandbox number in WhatsApp to join your Sandbox.

`[imagen omitida: wiki id 46515]`

After joining, you will receive a message from the sandbox:

`[imagen omitida: wiki id 44125]`

See [here](https://www.twilio.com/docs/sms/whatsapp/api#joining-a-sandbox) for more details.

### [Step 3 - Configuring inbound message webhooks](#Step+3+-+Configuring+inbound+message+webhooks)

When customers send you a WhatsApp message, Twilio sends a webhook to your application.

On the [sandbox page](https://www.twilio.com/console/sms/whatsapp/sandbox) you have to configure the URL that Twilio sends a webhook to for inbound messages.

The Chatbot generator creates a webhook (see [HowTo: Integrate Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346)), under the instance's module.

After building it, configure the URL as follows:

**http://<server>/<baseURL>/<InstanceModule>.****WhatsappWebhook****.aspx (.NET) or http://<server>/<baseURL>/<InstanceModule>.****WhatsappWebhook** **(Java)**

This has to be configured by going through *Programmable Messaging > Settings > Whatsapp sandbox settings*. Note that the computer where the webhook is hosted, has to be visible from Internet:

`[imagen omitida: wiki id 46516]`

### [Step 4 - Configuration Settings](#Step+4+-+Configuration+Settings)

In the [console page](https://www.twilio.com/console), you have the Account SID and an Authorization Token. These credentials are needed to the interaction with Twilio

Account SID - Used to identify yourself in API requests  
Auth Token  - Used to authenticate REST API requests

`[imagen omitida: wiki id 46518]`

The Auth Token is the information needed when you send messages through Twilio. This is the information to be configured in the [WebHook](https://wiki.genexus.com/commwiki/wiki?44346).

**Note:**

If you joined your Sandbox > 24 hours ago, you will need to send a fresh inbound message to your WhatsApp number in order to then send yourself a media message. Otherwise, you'll get the "[ERROR - 63016](https://www.twilio.com/docs/api/errors/63016)  
Failed to send freeform message because you are outside the allowed window. Please use a Template."


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [HowTo: Integrate a new WhatsApp partner into a GeneXus Chatbot](https://wiki.genexus.com/commwiki/wiki?46271) | [HowTo: Integrate Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346) |
| [Twilio Token property](https://wiki.genexus.com/commwiki/wiki?45166) | [WhatsApp Partner property](https://wiki.genexus.com/commwiki/wiki?45164) |

---
