---
title: "HowTo: Use Facebook Messenger as a channel"
source_id: 44073
source_url: https://wiki.genexus.com/commwiki/wiki?44073
genexus_version: "18"
---

# HowTo: Use Facebook Messenger as a channel

The purpose of this article is to explain the necessary steps to configure an environment with Facebook and then use it through the [Chatbots Channels API](https://wiki.genexus.com/commwiki/wiki?44072).

### [Step 1 - Create a Facebook Page](#Step+1+-+Create+a+Facebook+Page)

To create a page on Facebook, go through [this link](https://www.facebook.com/pages/creation/).

`[imagen omitida: wiki id 44394]`

Continue the configuration process, where you are asked for a profile picture and other information. After the page is created, select the "Add Button" button.

`[imagen omitida: wiki id 44395]`

Next, select the "Send Message" button type:

`[imagen omitida: wiki id 44396]`

In step 2, select "Facebook Messenger."

In this way, the page is configured to send and receive messages.

Finally, select "Send Message" to test the button, so that a drop-down menu with the "Test Button" option is displayed. Clicking on it opens the chat.

`[imagen omitida: wiki id 44397]`

So far, you have configured the page to be able to receive messages through it.

At development time, not publishing the page is recommended (by default it appears published).

### [Step 2 - Create a Facebook application](#Step+2+-+Create+a+Facebook+application)

To create a Facebook APP, click on [this link](https://developers.facebook.com/apps/). There, you have an option to create your app.

`[imagen omitida: wiki id 44074]`

It will open a dialog in which you will be asked for a Display Name and Contact Email.

From the App Dashboard, select "PRODUCTS" and click on the "SET UP" button in the Messenger option.

`[imagen omitida: wiki id 44398]`

Under *Products > Settings* is the "Access Tokens" section. There, click on the "Edit Permissions" button.

`[imagen omitida: wiki id 44075]`

In the window that is opened, select the page you've just created (step 1).  
This action will generate a Page Access Token (which is going to be used later).

`[imagen omitida: wiki id 44076]`

### [Step 3 - Webhook configuration](#Step+3+-+Webhook+configuration)

For Facebook to be able to send messages and events, you need a service as "[Webhook](https://developers.facebook.com/docs/messenger-platform/webhook/)" which receives the requests. According to Facebook's documentation, the Messenger Platform sends events to your webhook to notify your bot when a variety of interactions or events happen, including when a person sends a message. Webhook events are sent by the Messenger Platform as POST requests to your webhook.

You have to program your own webhook, with some considerations.  
  
To configure the Webhook, you need to expose that service, which has to run under HTTPS. To configure the webhook, select the "Subscribe To Events" option:

`[imagen omitida: wiki id 44399]`

In the Events box, it is enough to select: *messages*, *messaging\_postbacks*, *messaging\_options*, *message\_deliveries*, and *message\_reads*.

`[imagen omitida: wiki id 44585]`

In CallbackURL, enter the URL where you exposed the Webhook service. In Verify Token, you have to add any token which will be used later.  
  
`[imagen omitida: wiki id 44078]`

When an event that calls the Webhook is triggered, you can easily obtain the user ID of the user interacting with your page from the Webhook. See [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358).

### [See Also](#See+Also)

[HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) | [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358) |

---
