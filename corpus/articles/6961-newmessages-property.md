---
title: "NewMessages Property"
source_id: 6961
source_url: https://wiki.genexus.com/commwiki/wiki?6961
genexus_version: "18"
---

# NewMessages Property

Indicates whether the messages to be received will be only the new ones or all of them.

### [Syntax](#Syntax)

**&***DataType***.NewMessages**  
  
**Type Returned:**   
Numeric

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | The calls to the *Receive*method will return all the messages in the folder. This is the default value. |
| **1** | The calls to the *Receive* method will return only the unread messages in the current folder. |

### [Description](#Description)

**MAPISession/OutlookSession:** The value of this property will be effective as from the next call to the *ChangeFolder* method.  
  
**POP3Session:** The value of this property will be effective as from the next call to the *Login* method.

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[ChangeFolder Method](https://wiki.genexus.com/commwiki/wiki?6962)  
[Login Method](https://wiki.genexus.com/commwiki/wiki?6963)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)


|  |
| --- |
| **Backlinks** |
| [Count property](https://wiki.genexus.com/commwiki/wiki?7023) | [GetNextUID method](https://wiki.genexus.com/commwiki/wiki?7045) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) |
| [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) |

---
