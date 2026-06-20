---
title: "HowTo: Integrate Chatbots using Facebook Messenger"
source_id: 44358
source_url: https://wiki.genexus.com/commwiki/wiki?44358
genexus_version: "18"
---

# HowTo: Integrate Chatbots using Facebook Messenger

This document explains the steps to be followed in order to integrate your chatbot with Facebook Messenger.

### [How does it work?](#How+does+it+work%3F)

Basically, there are three points: the service that will consume the API and send the message, the Facebook Page, and finally the Facebook User.  
The message is going to be sent through the Facebook Page to the Facebook User, so you need to tell which page and to whom the message is directed to.  
To specify the page, the **Page Access Token** is used.  
To specify the user, consider that the user is identified by a [Page-Scoped ID](https://developers.facebook.com/docs/pages/access-tokens). So the user's ID depends on the page they are interacting with.  
You can get the **Page-Scoped ID** (also known as PSID or Recipient ID) through the **webhook**, which will be "listening" to the different events that occur while the user interacts with the chat.

### [Facebook configuration](#Facebook+configuration)

To use Facebook Messenger as a channel, the user needs to do some configuration, as explained in [HowTo: Use Facebook Messenger as a channel](https://wiki.genexus.com/commwiki/wiki?44073).

### [Webhook implementation](#Webhook+implementation)

See at the [Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) the procedure "*FacebookWebhook*". This is an example, where you may note the following:

* *FacebookWebhook* is a main object with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set to HTTP.
* It uses an SDT "ChannelConfiguration" where the information of the channel is stored, including the Page Access Token, the Channel (Channel.FacebookMessenger) and the Recipients ID.

`[imagen omitida: wiki id 44595]`  
  
The code of *FacebookWebhook* looks for the ChannelConfiguration using the *GetWebhookConfiguration* procedure. Note that before running the sample, you have to give a value to the &AccessToken variable (the **Page Access Token**) in the *GetWebhookConfiguration* procedure.

```
&ChannelConfiguration.Channel = Channel.FacebookMessenger
&AccessToken = !"34567899999999999999999999999" //Set a valid value here.
for &ChannelConfigurationProperty in &ChannelConfiguration.Properties
    if &ChannelConfigurationProperty.Key = FacebookProperties.AccessToken
        &ChannelConfigurationProperty.Value = &AccessToken
        return
    endif
endfor

&ChannelConfigurationProperty = new()
&ChannelConfigurationProperty.Key = FacebookProperties.AccessToken
&ChannelConfigurationProperty.Value = &AccessToken
&ChannelConfiguration.Properties.Add(&ChannelConfigurationProperty)
```

Then, in the *FacebookWebhook* procedure, the **Recipient ID** is obtained from the HTTP request, and added to the Channel configuration, calling the *SetUserIdInConfiguration* procedure.

* Next, the message is sent to the chatbot using the *CommonChatbots.SendMessageFromChannel* procedure.
* In the end, the *GeneXusChannels.Message.SendMessage* service is used to send the response to Messenger.  
  The code of *FacebookWebhook* that sends the message to Messenger is as follows. Note that the message payload is set, according to the type of message:

```
       CommonChatbots.SendMessageFromChannel(&FromFacebookMessage.entry.Item(1).messaging.Item(1).message.text, &RecipientId, !"TestChannels", &AnalyzeResponse) (*)
       for &Response in &AnalyzeResponse.GXOutputCollection
           &Message.Text = &Response
           if &AnalyzeResponse.Context.GXSetImageResponse
              &MediaMessage.URL = &AnalyzeResponse.Context.GXResponseImage.ImageURI
              &MediaMessage.Type = MediaTypes.Image
              &Message.Payload.Type = PayloadTypes.Media
              &Message.Payload.Body = &MediaMessage.ToJson()
           endif
       //Send the response using the SendMessage service.
       GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages)
   endfor
```

(\*) Note that you have to set the name of your [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) as the third parameter for the *SendMessageFromChannel* call. In this example, the instance name is "TestChannels."

### [Sending messages to the user](#Sending+messages+to+the+user)

If the user has talked to your page once (and you have their Recipient ID), you can send messages to them (without using the chatbot instance), using the **GeneXusChannels.Message.SendMessage**(&ChannelConfiguration, &Message, &Messages) service.

Take a look at the *SendMessagesFb* object in the [example](https://wiki.genexus.com/commwiki/wiki?44586), where several messages are sent to the user to show the different types of messages that can be sent. The *SendMessagesFb* procedure calls the *GetConfiguration* data provider.

Note that to make this example work, first you must complete the *GetConfiguration* data provider with valid values for the Page Access Token and the Recipient.

```
ChannelConfiguration
{
    Channel = Channel.FacebookMessenger
    Properties
    {
        PropertiesItem
        {
            Key = FacebookProperties.AccessToken
            Value = !"34567899999999999999999999999" //Set a valid value here.
        }
        PropertiesItem
        {
            Key = FacebookProperties.Recipient
            Value = !"11111111111111" //Set a valid value here.
        }
    }
}
```

You can run the *SendMessagesFb* procedure and see how it works:

`[imagen omitida: wiki id 44598]`

### Message Types

You can send all types supported by the Channels API. For more information, see [Message types supported for Facebook Messenger Channels API](https://wiki.genexus.com/commwiki/wiki?44599).

### [Availability](#Availability)

Since [GeneXus 16 upgrade 6](https://wiki.genexus.com/commwiki/wiki?43978,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) |
| [HowTo: Use Facebook Messenger as a channel](https://wiki.genexus.com/commwiki/wiki?44073) | [Message types supported for Facebook Messenger Channels API](https://wiki.genexus.com/commwiki/wiki?44599) |

---
