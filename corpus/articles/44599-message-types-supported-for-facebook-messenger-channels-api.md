---
title: "Message types supported for Facebook Messenger Channels API"
source_id: 44599
source_url: https://wiki.genexus.com/commwiki/wiki?44599
genexus_version: "18"
---

# Message types supported for Facebook Messenger Channels API

This article shows the different message types supported by the Facebook Messenger [Channels API](https://wiki.genexus.com/commwiki/wiki?44072). For specific information on this API, see [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358).

In all the examples, the **GeneXusChannels.Message.SendMessage** API is used.

### [Text Message](#Text+Message)

#### [Sample](#Sample)

```
&Message.Text = !"Hello world" //&Message is GeneXusChannels.Message data type.
GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages) //&ChannelConfiguration is of ChannelConfiguration SDT. &Messages is GeneXus.Common.Messages.
```

### [Grid Message](#Grid+Message)

It's mapped with [Generic Template](https://developers.facebook.com/docs/messenger-platform/reference/template/generic) data type.

#### [Sample](#Sample)

In the [Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) see the *SendMessagesFb* object.

Basically, it does the following:

```
&ChannelConfiguration = GetConfiguration() //Gets the configuration of the channnel.
&Message = GetGOTCharacters()
Do 'SendMessage'

Sub 'SendMessage'
    GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages)
    msg(Format(!"%1 result: %2", &Message.Text, &Messages.ToJson()), status)    
EndSub
```

The *GetGOTCharacters* procedure calls a data provider (*GOTCharacters*) which returns a GeneXusChannels.Message parameter (&GridMessage in the example).

Note that the &Message payload Type is "PayloadTypes.Grid" and Body has to be assigned to the JSON data of the message.

*GetGOTCharacters procedure:*

```
&GridMessage = GOTCharacters()

&Message.Text = !"The winter is here ;)"
&Message.Payload.Type = PayloadTypes.Grid
&Message.Payload.Body = &GridMessage.ToJson()
```

Take a look at the *GOTCharacters* data provider to understand how it should be implemented:

`[imagen omitida: wiki id 44601]`

The following domains are used in the example:

|  |  |
| --- | --- |
| **FacebookGridProperties** | Domain that contains the definition of specific properties for the type of Grid message on Facebook. They are specified to help mapping between the data and the grid. |
| **FacebookGridProperties.Title** | Represents the title of an item (page) of the grid. |
| **FacebookGridProperties.Subtitle** | Represents the subtitle or description of a grid item. |
| **FacebookGridProperties.Image** | Represents the image that can be seen in the grid item. |
| **FacebookGridProperties.Button** | Represents a button that can be added to the grid. |
| **PayloadTypes** | Domain that contains the different message types. |

At runtime, you'll see the following:

`[imagen omitida: wiki id 44600]`

For more information on how to configure the channel, take a look at [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358).

### [Media Message](#Media+Message)

It allows sending images and videos. It maps with [Media Template](https://developers.facebook.com/docs/messenger-platform/reference/template/media) on Facebook.

#### [Sample](#Sample)

In the [Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) see the SendMessagesFb object.

Take a look at this code.

```
&Message = GetGOTAppVideo()
Do 'SendMessage'

Sub 'SendMessage'
    GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages)
    msg(Format(!"%1 result: %2", &Message.Text, &Messages.ToJson()), status)    
EndSub
```

Open the *GetGOTAppVideo* object to understand more in detail how it works:

```
&Message.Text = !"Let me introduce you to the GOT app!"

&MediaMessage = GOTAppVideo()
&Message.Payload.Type = PayloadTypes.Media
&Message.Payload.Body = &MediaMessage.ToJson()
```

### [Web View Message](#Web+View+Message)

It allows rendering a web site to the chat. It maps with [URL button](https://developers.facebook.com/docs/messenger-platform/reference/buttons/url) on Facebook.

#### [Sample](#Sample)

In the [Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) see the SendMessagesFb object.

Take a look at this code.

```
&Message = GetGOTWiki()
Do 'SendMessage'

Sub 'SendMessage'
    GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages)
    msg(Format(!"%1 result: %2", &Message.Text, &Messages.ToJson()), status)    
EndSub
```

Open the GetGOTWiki object to understand more in detail how it works (it calls a data provider that returns the WebViewMessage):

```
&Message.Text = !"This is the wiki of GOT:"

&WebViewMessage = GOTWiki()
&Message.Payload.Type = PayloadTypes.WebView
&Message.Payload.Body = &WebViewMessage.ToJson()
```

The *GOTWiki* data provider is as shown below. Note that the output of the data provider is *WebViewMessage*.

`[imagen omitida: wiki id 44602]`

`[imagen omitida: wiki id 44603]`

The following domains are used in the example:

|  |  |
| --- | --- |
| **FacebookWebViewProperties** | Domain that contains specific properties of the Web View for Facebook. |
| **FacebookHeightRatio** | Domain that contains the different Height Ratio options. |

At runtime:

`[imagen omitida: wiki id 44604]`

### [Quick replies message](#Quick+replies+message)

It allows the user to answer based on quick answers. It maps with [Quick replies](https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies) on Facebook.

#### [Samples](#Samples)

**Example 1**

See at the [Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) the *SendMessagesFb* object.

Take a look at this code.

```
&Message = GetGOTFavorites()
Do 'SendMessage'

Sub 'SendMessage'
    GeneXusChannels.Message.SendMessage(&ChannelConfiguration, &Message, &Messages)
    msg(Format(!"%1 result: %2", &Message.Text, &Messages.ToJson()), status)    
EndSub
```

The *GetGOTFavorites* procedure looks as shown below. It calls a data provider called *GOTFavorites.*

```
&Message.Text = !"Think fast!"

&QuickRepliesMessage = GOTFavorites()
&Message.Payload.Type = PayloadTypes.QuickReplies
&Message.Payload.Body = &QuickRepliesMessage.ToJson()
```

The *GOTFavorites* data provider has an output based on *QuickRepliesMessage* SDT.

`[imagen omitida: wiki id 44605]`

`[imagen omitida: wiki id 44606]`

The following domains are used in the example:

|  |  |
| --- | --- |
| **FacebookQuickRepliesProperties** | Domain that contains the specific properties for Facebook Quick Replies. |
| **FacebookQuickRepliesContentTypes** | Domain that contains the different Content Type options for Quick Replies. |

At runtime:

`[imagen omitida: wiki id 44607]`

**Example 2**

```
&Message.Text = !"Send QuickReplies"

&QuickRepliesMessage.Text = !"¿Are you sure?"

//Yes
&QuickReply = new()
&QuickReply.Text = !"Yes"

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ContentType
&QuickReplyProperty.Value = FacebookQuickRepliesContentTypes.Text
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ImageUrl
&QuickReplyProperty.Value = !"http://pngimg.com/uploads/image.png"
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickRepliesMessage.Replies.Add(&QuickReply)

//No
&QuickReply = new()
&QuickReply.Text = !"No"

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ContentType
&QuickReplyProperty.Value = FacebookQuickRepliesContentTypes.Text
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickRepliesMessage.Replies.Add(&QuickReply)

//Location
&QuickReply = new()
&QuickReply.Text = !"Location"

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ContentType
&QuickReplyProperty.Value = FacebookQuickRepliesContentTypes.Location
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickRepliesMessage.Replies.Add(&QuickReply)

//Phone
&QuickReply = new()
&QuickReply.Text = !"Call"

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ContentType
&QuickReplyProperty.Value = FacebookQuickRepliesContentTypes.PhoneNumber
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickRepliesMessage.Replies.Add(&QuickReply)

//Email
&QuickReply = new()
&QuickReply.Text = !"Email"

&QuickReplyProperty = new()
&QuickReplyProperty.Key = FacebookQuickRepliesProperties.ContentType
&QuickReplyProperty.Value = FacebookQuickRepliesContentTypes.Email
&QuickReply.Properties.Add(&QuickReplyProperty)

&QuickRepliesMessage.Replies.Add(&QuickReply)

&Message.Payload.Type = PayloadTypes.QuickReplies
&Message.Payload.Body = &QuickRepliesMessage.ToJson()
```

### [See Also](#See+Also)

[HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Chatbots sample using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44586) | [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358) |

---
