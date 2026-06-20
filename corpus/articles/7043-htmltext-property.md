---
title: "HTMLText Property"
source_id: 7043
source_url: https://wiki.genexus.com/commwiki/wiki?7043
genexus_version: "18"
---

# HTMLText Property

This property is used to give the message body in HTML format (HyperText Markup Language).

### [Syntax](#Syntax)

**&***DataType***.HTMLText**  
  
**Type Returned:**   
Character

### [Description](#Description)

**MAPISession:** This property is not supported in the MAPISession data type.   
  
**OutlookSession:** Although this property is supported in OutlookSession, it is not possible to handle a message whose contents are at the same time in simple text and in HTLM language. The last contents to be assigned will be considered the final contents. When receiving a message with HTML contents the *Text* property will have the same text as the HTMLText property, but without format (omitting the tags of the HTML language).    
  
**SMTPSession/POP3Session:** It is possible to handle messages with contents both in simple text and HTML language. If a message of this type is sent, the client receiving it will show the HTML contents providing that client is able to show that format. If the client is not able to handle HTML contents, the contents will be shown in simple text.

### [Scope](#Scope)

**Extended Data Types:** [MailMessage](https://wiki.genexus.com/commwiki/wiki?6925)  
**Languages:** .NET, Java, Visual FoxPro (up to GeneXus X Evolution 3), Ruby(up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[MailMessage Data Type](https://wiki.genexus.com/commwiki/wiki?6925)


|  |
| --- |
| **Backlinks** |
| [GetResponse method](https://wiki.genexus.com/commwiki/wiki?7097) | [MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925) |

---
