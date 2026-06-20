---
title: "AttachDir Property"
source_id: 6953
source_url: https://wiki.genexus.com/commwiki/wiki?6953
genexus_version: "18"
---

# AttachDir Property

Indicates the directory where the attached files are.

### [Syntax](#Syntax)

**&***DataType***.AttachDir**  
  
**Type Returned:**   
Character

### [Description](#Description)

When using the *Send* method the message will be taken as the base directory for the attached files search (*Attachments* property).   
    
**MAPISession/POP3Session/OutlookSession:** It specifies the directory where the attached files must be saved when the *Receive* method is executed. If this property has an empty string (“”) the attached files will not be saved.    
  
The default value is the empty string (“”).

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966), [SMTPSession](https://wiki.genexus.com/commwiki/wiki?6937)  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [See Also](#See+Also)

[Attachments Property](https://wiki.genexus.com/commwiki/wiki?6952)  
[Receive Method](https://wiki.genexus.com/commwiki/wiki?6964)  
[Send Method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)  
[SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937)


|  |
| --- |
| **Backlinks** |
| [Attachments Property](https://wiki.genexus.com/commwiki/wiki?6952) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) |
| [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [Receive method](https://wiki.genexus.com/commwiki/wiki?6964) | [SMTPSession Data Type](https://wiki.genexus.com/commwiki/wiki?6937) |

---
