---
title: "Subject Property"
source_id: 7037
source_url: https://wiki.genexus.com/commwiki/wiki?7037
genexus_version: "18"
---

# Subject Property

This property gives the subject of the message.

### [Syntax](#Syntax)

**&***DataType***.Subject**  
  
**Type Returned:**   
Character

### [Description](#Description)

**MAPISession:** This property is not supported if the MAPISession data type.   
  
**OutlookSession:** Although this property is supported in OutlookSession, it is not possible to handle a message whose contents are at the same time in simple text and in HTLM language. The last contents to be assigned will be considered the final contents. When receiving a message with HTML contents the *Text* property will have the same text as the HTMLText property, but without format (omitting the HTML tags).    
  
**SMTPSession/POP3Session:** It is possible to handle messages with contents in simple text and HTML language at the same time. If a message of this type is sent, the client receiving it will show the HTML contents provided that client is able to handle that format. If the client is not able to handle the HTML contents, the contents will be shown in simple text.

### [Scope](#Scope)

**Extended Data Types:** [MailMessage](https://wiki.genexus.com/commwiki/wiki?6925)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[MailMessage Data Type](https://wiki.genexus.com/commwiki/wiki?6925)


|  |
| --- |
| **Backlinks** |
| [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) |

---
