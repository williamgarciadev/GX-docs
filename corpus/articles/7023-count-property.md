---
title: "Count property"
source_id: 7023
source_url: https://wiki.genexus.com/commwiki/wiki?7023
genexus_version: "18"
---

# Count property

This property returns the following:

- Number of messages to be received, in the case of**MAPISession/OutlookSession/POP3Session**.   
- Number of elements in the collection, in the case of**MailRecipientCollection/StringCollection**. 

#### [Syntax](#Syntax)

**&***DataType***.Count**  
  
**Type Returned:**   
Numeric

### [Description](#Description)

**MAPISession/OutlookSession/POP3Session:** It returns the number of messages which meet the folder opening requirements, and which will therefore be received.  
i.e.: If the folder or the session is opened specifying that only the unread messages will be received (via the *NewMessages* property), it will return the unread messages. But if the folder is opened specifying that all messages will be received, it will return all the messages.  
  
This property is read only, so it cannot be assigned.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Extended data types** | [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996), [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936), [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966), [StringCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6954,,) |
| **Languages** | .NET, Java, Ruby (up to Genexus X Evolution 3), Visual FoxPro (up to Genexus X Evolution 3) |
|  |  |

### [See also](#See+also)

[NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961)  
[Receive method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[StringCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6954,,)


|  |
| --- |
| **Backlinks** |
| [AddItem method](https://wiki.genexus.com/commwiki/wiki?8668) | [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) |
| [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [RemoveItem method](https://wiki.genexus.com/commwiki/wiki?8672) |

---
