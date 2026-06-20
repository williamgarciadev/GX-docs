---
title: "Channels API - Troubleshooting"
source_id: 44609
source_url: https://wiki.genexus.com/commwiki/wiki?44609
genexus_version: "18"
---

# Channels API - Troubleshooting

| Error Code | Description | Help |
| --- | --- | --- |
| **Common Errors** |  |  |
| GXCH1001 | Message Text and Message Body are empty. | If Message.Text and Message.Body are empty, then there is no message to send. The user must specify at least one of the fields. |
| GXCH1002 | Payload Type is Empty. | This error occurs when a Payload Body is specified but not the Payload Type. The user must specify the Payload Type. |
| GXCH1003 | Type is Empty. | If a message of the Media type is being sent, but the Media Type is not specified, it gives this error. The user must specify the Media Type (Image or Video). |
| GXCH1004 | URL is Empty. | If a message of Media type is being sent, but the URL of the content to be sent is not specified, this error is thrown. The user must specify the URL. |
| GXCH1005 | Description is Empty. | When sending a message of type Web View and not specifying the Description, this error is thrown. The user has to specify the Description. |
| GXCH1006 | URL is Empty. | When sending a message of Web View type and not specifying the URL, this error is thrown. The user has to specify the URL. |
| GXCH1007 | Text is Empty. | This error occurs when a value is not assigned to the Text parameter when sending a message of Quick Replies Type. The user must specify something for Text value. |
| GXCH1008 | Text is Empty (Quick Reply Index: {QuickReplyIndex}). | This error tells us that for a specific QuickReply, the Text value is missing. The user must assign a value for the Text. |
| **Facebook & Whatsapp Errors** |  |  |
| GXCH2001 | Access Token not found. | The AccessToken property was not found in the &ChannelConfiguration. This parameter is necessary to be able to send messages using the Facebook page. The user must add this parameter as a property of the Channel (in the ChannelConfiguration SDT). |
| GXCH2002 | The specified value for Access Token is not valid. | The value found for AccessToken is not valid (the property is there, but its value is empty). |
| GXCH2003 | Recipient not found. | In the &ChannelConfiguration the Recipient property was not found. The recipient identifies the recipient of the message, so it needs to be specified. The user must add this parameter as a property of the Channel (in the ChannelConfiguration SDT). |
| GXCH2004 | The specified value for Recipient is not valid. | The value found for Recipient is not valid (the property is there, but its value is empty). |
| GXCH2005 | Title parameter not found. | The Title parameter is not found. This error occurs when sending a grid that does not contain the Title parameter within its parameters, since it is required by the platform. The user must add the Title parameter. |
| GXCH2006 | The specified value for Title is not valid. | The value found for Title is not valid (the property is there, but its value is empty). |
| GXCH3001 | Unsupported Payload Type.{PayloadType} is not supported by Whatsapp. | The type of Payload specified is not supported by Whatsapp. |


|  |
| --- |
| **Backlinks** |
| [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
