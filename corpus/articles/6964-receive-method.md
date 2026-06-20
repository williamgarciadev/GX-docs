---
title: "Receive method"
source_id: 6964
source_url: https://wiki.genexus.com/commwiki/wiki?6964
genexus_version: "18"
---

# Receive method

Returns the data of the following email in the current session.

If the email has attached files and a directory was specified in the *AttachDir* property, the attached files are saved on the disk. Otherwise, they are not saved.

### [Syntax](#Syntax)

**&***VarBasedOnExtendedDataType***.Receive(***Message***)**  
  
**Where:**  
*Message*  
    Is a *MailMessage* type parameter.

**Type Returned:**   
Numeric

### [Scope](#Scope)

**Extended Data Types:** [MAPISession](https://wiki.genexus.com/commwiki/wiki?6935), [OutlookSession](https://wiki.genexus.com/commwiki/wiki?6936), [POP3Session](https://wiki.genexus.com/commwiki/wiki?6966)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

**Note**: This method returns an error code, so it is possible to call it as follows: **&**Err **=** **&**DataType**.Receive(***Message***)**

### [See Also](#See+Also)

[AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953)  
[Send method](https://wiki.genexus.com/commwiki/wiki?6965)  
[MailMessage data type](https://wiki.genexus.com/commwiki/wiki?6925)  
[MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935)  
[OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936)  
[POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966)


|  |
| --- |
| **Backlinks** |
| [AttachDir Property](https://wiki.genexus.com/commwiki/wiki?6953) | [ChangeFolder method](https://wiki.genexus.com/commwiki/wiki?6962) | [Count property](https://wiki.genexus.com/commwiki/wiki?7023) |
| [Delete method](https://wiki.genexus.com/commwiki/wiki?6014) | [EditWindow Property](https://wiki.genexus.com/commwiki/wiki?7030) | [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) | [Login method](https://wiki.genexus.com/commwiki/wiki?6963) |
| [Logout method](https://wiki.genexus.com/commwiki/wiki?7080) | [MAPISession Data Type](https://wiki.genexus.com/commwiki/wiki?6935) | [MarksAsRead method](https://wiki.genexus.com/commwiki/wiki?7092) | [NewMessages Property](https://wiki.genexus.com/commwiki/wiki?6961) |
| [OutlookSession Data Type](https://wiki.genexus.com/commwiki/wiki?6936) | [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [POP3Session Data Type](https://wiki.genexus.com/commwiki/wiki?6966) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) |
| [Profile Property](https://wiki.genexus.com/commwiki/wiki?7025) | [Send method](https://wiki.genexus.com/commwiki/wiki?6965) | [Timeout property](https://wiki.genexus.com/commwiki/wiki?7042) |
| [UserName Property](https://wiki.genexus.com/commwiki/wiki?7001) |

---
